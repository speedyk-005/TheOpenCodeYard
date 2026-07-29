/* A* pathfinding implementation in C# with Euclidean heuristic. */

using System;
using System.Collections.Generic;

public class NodePosition {
  public int X, Y;
  public NodePosition(int x, int y) { X = x; Y = y; }
}

public class AStar {
  private Dictionary<string, List<(string, int)>> graph;
  private Dictionary<string, int> bestCase = new Dictionary<string, int>();
  private Dictionary<string, string> comeFrom = new Dictionary<string, string>();
  private Dictionary<string, NodePosition> nodePositions = new Dictionary<string, NodePosition>();

  public AStar(Dictionary<string, List<(string, int)>> graph, Dictionary<string, NodePosition> nodePositions) {
    this.graph = graph;
    this.nodePositions = nodePositions;

    foreach (var (vertex, _) in graph)
      bestCase[vertex] = int.MaxValue;
  }

  private double EuclideanHeuristic(string current, string target, Dictionary<string, NodePosition> positions) {
    int dx = positions[current].X - positions[target].X;
    int dy = positions[current].Y - positions[target].Y;
    return Math.Sqrt(dx * dx + dy * dy);
  }

  public (Dictionary<string, int>, Dictionary<string, string>) PathFind(string start, string target) {
    if (!graph.ContainsKey(start) || !graph.ContainsKey(target)) {
      Console.WriteLine("Error: Start or target vertex not found.");
      return (bestCase, comeFrom);
    }

    var heapq = new PriorityQueue<string, double>();
    bestCase[start] = 0;

    double startHeuristic = EuclideanHeuristic(start, target, nodePositions);
    heapq.Enqueue(start, 0 + startHeuristic);

    while (heapq.Count > 0) {
      if (!heapq.TryDequeue(out string vertex, out double f_cost))
        break;

      int g_cost = bestCase[vertex];

      if (f_cost > g_cost + EuclideanHeuristic(vertex, target, nodePositions))
        continue;

      if (vertex == target)
        break;

      foreach (var neighbor in graph[vertex]) {
        var (adjVertex, adjCost) = (neighbor.Item1, neighbor.Item2);
        int new_gCost = g_cost + adjCost;

        if (new_gCost < bestCase[adjVertex]) {
          bestCase[adjVertex] = new_gCost;
          comeFrom[adjVertex] = vertex;

          double heuristic = EuclideanHeuristic(adjVertex, target, nodePositions);
          double priority = new_gCost + heuristic;
          heapq.Enqueue(adjVertex, priority);
        }
      }
    }
    return (bestCase, comeFrom);
  }
}

public class PathConstructor {
  public static string Construct((Dictionary<string, int>, Dictionary<string, string>) data, string start, string target) {
    var bestCase = data.Item1;
    var comeFrom = data.Item2;
    var path = new List<string> { target };

    if (!comeFrom.ContainsKey(target) && target != start) {
      return $"No path exists from {start} to {target}";
    }

    var curr = target;
    while (curr != start) {
      curr = comeFrom[curr];
      path.Add(curr);
    }

    path.Reverse();
    var report = "The quickest route is: ";
    for (var i = 0; i < path.Count; i++) {
      var vertex = path[i];
      report += $" {vertex}";
      if (i < path.Count - 1) {
        report += $" -({bestCase[path[i + 1]] - bestCase[path[i]]})->";
      }
    }
    report += $", Total cost = {bestCase[target]}";
    return report;
  }
}

public static class Program {
  public static void Main() {
    var nodePositions = new Dictionary<string, NodePosition> {
      {"A", new NodePosition(0, 0)},
      {"B", new NodePosition(1, 1)},
      {"C", new NodePosition(0, -1)},
      {"D", new NodePosition(2, 3)},
      {"E", new NodePosition(3, 1)}
    };

    var graph = new Dictionary<string, List<(string, int)>>{
      {"A", new List<(string, int)>{("B",3), ("C", 5)}},
      {"B", new List<(string, int)>{("A",3), ("D", 4), ("E", 2)}},
      {"C", new List<(string, int)>{("D",6), ("A", 5)}},
      {"D", new List<(string, int)>{("B",4), ("C", 6), ("E", 1)}},
      {"E", new List<(string, int)>{("B",2), ("D", 1)}}
    };

    var start = "A";
    var target = "D";

    var aStar = new AStar(graph, nodePositions);
    var data = aStar.PathFind(start, target);

    var path = PathConstructor.Construct(data, start, target);
    Console.WriteLine(path);
  }
}