# A* CSharp

- Status: Experimental
- Main Language: C#
- Accepting Contributions: Yes

---

## What it does

A* pathfinding implementation with Euclidean heuristic. Finds the shortest path in a weighted graph using g(n) + h(n) priority scoring.

## How to use

```bash
dotnet run
```

Or compile with `csc Program.cs` and run the executable.

## Notes

Uses `PriorityQueue<string, double>` (available in .NET 6+). Includes path reconstruction with per-edge cost breakdown.