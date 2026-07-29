# Dijkstra

- Status: Experimental
- Main Language: C#
- Accepting Contributions: Yes

---

## What it does

Dijkstra's shortest path algorithm with a list-based priority queue. Finds minimum cost routes in weighted graphs.

## How to use

```bash
dotnet run
```

Or compile with `csc Program.cs` and run.

## Notes

Uses `List.Sort()` as a simple priority queue — O(n log n) per pop vs O(log n) with a proper PQ. Good for understanding the core Dijkstra logic.