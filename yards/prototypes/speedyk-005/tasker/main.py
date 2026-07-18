"""
Tasker — background task runner using a daemon worker thread.
"""

import inspect
from typing import Callable, Any
from threading import Thread, Event


class Tasker:
    """Background task runner.

    Runs a submitted callable asynchronously using a worker thread.
    
    Warnings:
        The task function should be pure and thread-safe as it runs in a 
        separate thread. Avoid modifying shared state without proper 
        synchronization.
         
    Attributes:
        task (Callable): Function executed when the task is triggered.
        once (bool): If True, the worker stops after the first run.
        running (bool): Indicates if the task is currently running.
        lastest_result (dict[str, Any]): dictionary containing the last execution result.
        _build_event (Event): Threading event used to signal the worker.
        _worker (Thread): The internal thread running the worker loop.
    """
    
    def __init__(self, task: Callable, once: bool = False):
        """
        Initializes the tasker
       
        Args:
           task (Callable): Function executed when the task is triggered.
           once (bool, optional): If True, the worker stops after the first run. Defaults to False.
           
        Raises:
           TypeError: If task is not callable or is a method.
           ValueError: If the task function has incompatible signature.
        """
        if not callable(task):
            raise TypeError(f"Expected callable, got {type(task).__name__}")
            
        self.task = task 
        if inspect.ismethod(self.task):
            raise TypeError("Bound methods are not supported due to potential reference cycles")
        
        # Check if task accepts no arguments
        sig = inspect.signature(task)
        if len(sig.parameters) > 0:
            raise ValueError(f"Task function must accept 0 arguments, but has {len(sig.parameters)}")
        
        self._once = once
                
        self.running = False 
        self.lastest_result: dict | None = None
        
        self._build_event = Event() 
        self._worker = Thread(target=self._worker_loop, daemon=True)
        self._worker.start()
        
    @property
    def once(self):
        """
        Whether to run the task only once and stop the worker after been triggered.
        
        Returns:
            bool: True if the task is set to run only once, False otherwise.
        """
        return self._once
        
    @once.setter
    def once(self, value): 
        """
        Sets whether the task should run only once and stop the worker after being triggered.
        
        Args:
            value (bool): True to run the task only once, False to run it continuously.
        """
        self._once = bool(value)
        if not self._once:
            # Only start if the thread isn't already running
            if not self._worker.is_alive():
                self._worker = Thread(target=self._worker_loop, daemon=True)
                self._worker.start()
        
    def _worker_loop(self) -> None:
        """Worker loop waiting for task notifications.

        The worker blocks until `run()` triggers the event
        
        Raises:
            TypeError: If task result is not a dictionary.
        """
        while True:
            self._build_event.wait()

            self.running = True
            
            res = self.task()
            if not isinstance(res, dict):
                self.running = False
                raise TypeError(f"Task must return a dictionary, got {type(res).__name__}")
                
            self.latest_result = res
            self.running = False
           
            if self._once:
                self._build_event.clear()
                break
              
            self._build_event.clear()
          
    def run(self) -> None:
        """Signal the worker to execute the task.

        Example:
            >>> tasker.run()
            
        Raises:
            ValueError: If the task has already been run once and `once` is set to True.
            RuntimeError: If the worker thread is not alive.
        """
        if self._once and self.lastest_result is not None:
            raise ValueError("The worker has already stopped. Tasker was initialized with 'once=True'.")

        if not self._worker.is_alive():
            raise RuntimeError("Worker thread is no longer alive")
            
        self._build_event.set()
