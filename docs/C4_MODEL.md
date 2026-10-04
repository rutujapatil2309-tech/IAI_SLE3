# Full C4 Model — Graph Search System

## C4 Level 1 — Context

~~~mermaid
flowchart LR
    U[User / Student] -->|Run search| S[Graph Search System]
    S -->|Path, nodes expanded, timing| U
~~~

The Graph Search System is the main system and the User/Student is the external actor. No external service or database is required by the current implementation.

## C4 Level 2 — Container

~~~mermaid
flowchart LR
    U[User / Student] --> I[Input & Configuration]
    I --> G[Graph Data]
    I --> E[Search Engine]
    G --> E
    E --> T[Performance Measurement]
    E --> O[Output / Result Display]
    T --> O
    O --> U
~~~

Containers:
- Input & Configuration
- Graph Data
- Search Engine
- Performance Measurement
- Output / Result Display

## C4 Level 3 — Component

The selected container is Search Engine.

~~~mermaid
flowchart TB
    R[run_algorithm()]
    B[bfs()]
    D[dfs()]
    F[Frontier]
    V[Visited Tracking]
    G[Goal Test]
    P[Path Tracking]

    R --> B
    R --> D
    B --> F
    D --> F
    B --> V
    D --> V
    B --> G
    D --> G
    B --> P
    D --> P
~~~

Components:
- bfs() — queue-based breadth-first search.
- dfs() — stack-based depth-first search.
- Frontier — queue for BFS and stack for DFS.
- Visited Tracking — records processed vertices.
- Goal Test — checks whether the current node is W.
- Path Tracking — maintains the current path.
- run_algorithm() — executes the selected search and measures timing.

## C4 Level 4 — Code

The implementation does not define custom classes. Main code elements:

~~~text
GRAPH
START
GOAL
bfs(start, goal)
dfs(start, goal)
run_algorithm(algorithm, start, goal)
display_results(name, path, nodes, times)
~~~

| Code element | Responsibility |
|---|---|
| GRAPH | Adjacency-list graph |
| START / GOAL | Search endpoints A and W |
| bfs() | Breadth-first search |
| dfs() | Depth-first search |
| run_algorithm() | Three-run timing measurement |
| display_results() | Result and metric display |

## Design Decision

The architecture continues the existing SLE-2 BFS/DFS system. The Search Engine is the only container expanded at Component level, keeping the C4 model within the SLE-3 guideline's simple and readable structure.
