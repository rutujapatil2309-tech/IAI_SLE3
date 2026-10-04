# SLE-3 Architecture Notes

## System

**Graph Search System using BFS and DFS**

This SLE-3 project continues the SLE-2 system. The implementation uses a Python adjacency-list graph and searches from A to W using BFS and DFS.

## Level 1 — Context

~~~mermaid
flowchart LR
    U[User / Student] -->|Search configuration| S[Graph Search System]
    S -->|Path + performance result| U
~~~

The user runs the Graph Search System and receives the result of the selected graph search operation.

## Level 2 — Containers

~~~mermaid
flowchart LR
    U[User] --> I[Input & Configuration]
    I --> G[Graph Data]
    I --> E[Search Engine]
    G --> E
    E --> M[Performance Measurement]
    E --> O[Output / Result Display]
    M --> O
    O --> U
~~~

### Container responsibilities

1. **Input & Configuration** — defines START, GOAL, and the search execution.
2. **Graph Data** — stores the GRAPH adjacency list.
3. **Search Engine** — runs BFS and DFS.
4. **Performance Measurement** — measures three runs using time.perf_counter().
5. **Output / Result Display** — prints path, timing statistics, and nodes expanded.

## Level 3 — Components inside Search Engine

~~~mermaid
flowchart TB
    R[run_algorithm()]
    B[bfs()]
    D[dfs()]
    F[Frontier: Queue / Stack]
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

Only one main container is expanded at this level, following the SLE-3 guideline.

## Level 4 — Code

| Element | Role |
|---|---|
| GRAPH | Adjacency-list graph |
| START | Start vertex A |
| GOAL | Goal vertex W |
| bfs() | Breadth-first search |
| dfs() | Depth-first search |
| run_algorithm() | Three-run timing measurement |
| display_results() | Result and metric display |

## Design decisions

- The architecture continues the existing SLE-2 Graph Search System rather than introducing a new system.
- BFS and DFS remain separate because their frontier behavior is different.
- The adjacency-list representation is retained from SLE-2.
- Component-level detail is limited to the Search Engine to keep the diagram simple and readable.

## Verification

All architecture names should remain synchronized with bfs_dfs.py. Performance values should be taken from an actual run and should not be invented in the architecture document.
