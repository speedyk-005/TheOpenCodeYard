/* Dijkstra's shortest path — list-based priority queue. */

using System;
using System.Collections.Generic;

public class Edge {
  public string Target;
  public int Cost;
  public Edge(string target, int cost) {
    Target = target;
    Cost = cost;
  }
}

public class Dijkstra {
  private Dictionary<string, List<Edge>> graph;
  private Dictionary<string, int> bestCase = new Dictionary<string, int>();
  private Dictionary<string, string> comeFrom = new Dictionary<string, string>();

  public Dijkstra(Dictionary<string, List<Edge>> graph) {
    this.graph = graph;
    foreach (string vertex in graph.Keys)
      bestCase[vertex] = int.MaxValue;
  }

  public void PathFind(string start, string target) {
    if (!graph.ContainsKey(start) || !graph.ContainsKey(target)) return;

    var queue = new List<string>();
    bestCase[start] = 0;
    queue.Add(start);

    while (queue.Count > 0) {
      queue.Sort((a, b) => bestCase[a].CompareTo(bestCase[b]));
      string vertex = queue[0];
      queue.RemoveAt(0);

      if (vertex == target) break;

      foreach (Edge edge in graph[vertex]) {
        int newCost = bestCase[vertex] + edge.Cost;
        if (newCost < bestCase[edge.Target]) {
          bestCase[edge.Target] = newCost;
          comeFrom[edge.Target] = vertex;
          if (!queue.Contains(edge.Target)) queue.Add(edge.Target);
        }
      }
    }
  }

  public Dictionary<string, int> GetBestCase() { return bestCase; }
  public Dictionary<string, string> GetComeFrom() { return comeFrom; }
}

public class PathConstructor {
  public static string Construct(Dictionary<string, int> bestCase, Dictionary<string, string> comeFrom, string start, string target) {
    List<string> path = new List<string>();
    path.Add(target);
    string curr = target;
    while (curr != start) {
      if (!comeFrom.ContainsKey(curr)) break;
      curr = comeFrom[curr];
      path.Add(curr);
    }
    path.Reverse();
    return "Path: " + string.Join(" -> ", path.ToArray()) + " Total Cost: " + bestCase[target];
  }
}

public static class Program {
  public static void Main() {
    var graph = new Dictionary<string, List<Edge>>{
      {"A", new List<Edge>{new Edge("B",1), new Edge("C", 1)}},
      {"B", new List<Edge>{new Edge("A",1), new Edge("D", 2)}},
      {"C", new List<Edge>{new Edge("D",3), new Edge("A", 1)}},
      {"D", new List<Edge>{new Edge("B",2), new Edge("C", 3)}}
    };
    var start = "A";
    var target = "D";

    var dijkstra = new Dijkstra(graph);
    dijkstra.PathFind(start, target);

    var path = PathConstructor.Construct(
      dijkstra.GetBestCase(),
      dijkstra.GetComeFrom(),
      start, target
    );
    Console.WriteLine(path);
  }
}