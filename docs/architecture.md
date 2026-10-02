# SLE-3 Architecture Notes

## Level 1 — Context
The primary actor is the user/student running the Graph Search System. The user supplies or selects graph-search configuration and receives the result. No external service or separate database is assumed.

## Level 2 — Containers
- **Command-line interface:** handles configuration and output.
- **Search engine:** executes the chosen traversal.
- **Graph data:** an in-memory adjacency list.

## Level 3 — Components
- Configuration: graph, start vertex, goal vertex, algorithm choice.
- BFS: queue-based breadth-first traversal.
- DFS: stack-based depth-first traversal.
- Visited tracker: prevents repeated processing.
- Result handling: reports outcome and counters if the program provides them.

## Level 4 — Code mapping
| Code element | Architectural role |
|---|---|
| GRAPH | In-memory adjacency list |
| START / GOAL | Search configuration |
| bfs() | BFS traversal |
| dfs() | DFS traversal |
| queue / stack | Frontier structures |
| visited | Visited tracking |

## Verify before submission
Check whether the actual program uses fixed constants or interactive input, and whether it returns a path, traversal order, counters, or another result. Update this document to match the source exactly.
