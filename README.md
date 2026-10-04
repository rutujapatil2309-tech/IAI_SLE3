# SLE-3: Architectural Design Using Full C4 Model

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Student:** Rutuja Patil  
**System:** Graph Search System using BFS and DFS  
**Previous work:** SLE-2 BFS vs DFS performance comparison

## 1. System Title & Short Description

The **Graph Search System** is a Python-based search system continued from SLE-2. It represents a graph using an adjacency list and searches from start node **A** to goal node **W**. The system implements both **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. It records the path, nodes expanded, and execution time for three runs of each algorithm. SLE-3 documents this system using all four levels of the C4 architecture model.

## 2. C4 Model

C4 means **Context, Container, Component, and Code**. This repository presents the same Graph Search System at four levels, from the complete system view to its main functions.

---

## Level 1 — Context Diagram

~~~mermaid
flowchart LR
    U[User / Student] -->|Graph, start, goal, method| S[Graph Search System]
    S -->|BFS/DFS path, nodes expanded, timing| U
~~~

### Explanation

The User/Student runs the Graph Search System and provides or selects the search configuration. The system executes BFS or DFS on the graph and returns the search path, nodes expanded, and timing information. No external database or external service is required.

---

## Level 2 — Container Diagram

~~~mermaid
flowchart LR
    U[User / Student] --> I[Input & Configuration]
    I --> G[Graph Data]
    I --> E[Search Engine]
    G --> E
    E --> M[Performance Measurement]
    E --> O[Output / Result Display]
    M --> O
    O --> U
~~~

### Containers

| Container | Responsibility |
|---|---|
| **Input & Configuration** | Defines the graph-search configuration, including START, GOAL, and algorithm execution. |
| **Graph Data** | Stores the graph as the GRAPH adjacency-list dictionary. |
| **Search Engine** | Executes BFS and DFS and returns the path and number of expanded nodes. |
| **Performance Measurement** | Runs each algorithm three times and measures execution time using time.perf_counter(). |
| **Output / Result Display** | Displays paths, run times, best/average/worst time, and nodes expanded. |

The container view uses five boxes, which stays within the guideline's recommended 4–7 containers.

---

## Level 3 — Component Diagram

The **Search Engine** is the main container selected for the component-level view.

~~~mermaid
flowchart TB
    R[run_algorithm()]
    B[bfs()]
    D[dfs()]
    V[Visited Tracking]
    F[Frontier: Queue / Stack]
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

### Component Responsibilities

- **bfs()** — performs breadth-first graph search using a queue.
- **dfs()** — performs depth-first graph search using a stack.
- **Frontier** — stores nodes waiting to be explored.
- **Visited Tracking** — prevents repeated processing of vertices.
- **Goal Test** — checks whether the current node is W.
- **Path Tracking** — maintains the path from A to the current node.
- **run_algorithm()** — executes a selected algorithm three times and records timings.

Only the Search Engine is expanded into components, as required by the SLE-3 guideline.

---

## Level 4 — Code Level Overview

The code-level view contains only the main functions and data elements.

| Code element | Responsibility |
|---|---|
| GRAPH | Stores the graph as an adjacency list. |
| START | Defines the starting vertex (A). |
| GOAL | Defines the goal vertex (W). |
| bfs(start, goal) | Performs breadth-first search. |
| dfs(start, goal) | Performs depth-first search. |
| run_algorithm(...) | Runs an algorithm three times and measures execution time. |
| display_results(...) | Displays search and performance results. |

There are no custom classes in the SLE-2 implementation; the architecture therefore maps the actual functions and data structures instead of inventing classes.

---

## 3. Search Flow

~~~text
Graph + Start(A) + Goal(W)
            |
            v
     Select/Run Algorithm
          /       \
        BFS       DFS
        |          |
     Queue       Stack
        |          |
        +----+-----+
             |
       Visited Tracking
             |
          Goal Test
             |
       Path + Nodes
             |
    Performance Measurement
             |
        Result Display
~~~

For the supplied SLE-2 graph, both BFS and DFS can reach the goal W through:

~~~text
A -> C -> G -> O -> W
~~~

The exact timing values are machine-dependent and should be taken from the actual program output/profile rather than assumed.

---

## 4. Design Decisions

1. **Adjacency list:** The existing SLE-2 graph is represented as a Python dictionary of neighboring vertices.
2. **Separate BFS and DFS:** Keeping the algorithms in separate functions makes their behavior and performance easy to compare.
3. **Visited tracking:** A visited set prevents unnecessary repeated processing.
4. **Three timing runs:** The existing SLE-2 implementation executes each algorithm three times and reports best, average, and worst execution time.
5. **Simple C4 structure:** Only the Search Engine is expanded at Component level so the architecture remains readable and follows the SLE-3 guideline.

---

## 5. AI Contribution Note

AI assistance was used to help organize the SLE-3 repository documentation, C4 architecture structure, Mermaid diagrams, and README content. The student remains responsible for checking the architecture against the actual SLE-2 source code and understanding/explaining the design.

See AI_CONTRIBUTION_LOG.md for the detailed contribution record.

---

## 6. Repository Structure

~~~text
IAI_SLE3/
├── README.md
├── AI_CONTRIBUTION_LOG.md
├── .gitignore
├── bfs_dfs.py
└── docs/
    ├── architecture.md
    └── C4_MODEL.md
~~~

### Source

bfs_dfs.py is the SLE-2 BFS/DFS implementation used as the basis for this SLE-3 architecture.

### Documentation

- README.md — complete project and C4 overview.
- docs/C4_MODEL.md — focused four-level C4 documentation.
- docs/architecture.md — architecture notes and code mapping.
- AI_CONTRIBUTION_LOG.md — AI assistance and student verification record.

---

## 7. Running the System

Requirements:

- Python 3
- Standard-library modules used by the program (collections and time)

Run:

~~~bash
python bfs_dfs.py
~~~

The program displays BFS and DFS paths, execution times for three runs, best/average/worst timing, and nodes expanded.

---

## 8. SLE-3 Submission Checklist

- [x] System connected to SLE-2
- [x] Level 1 — Context Diagram
- [x] Level 2 — Container Diagram
- [x] Level 3 — Component Diagram for one main container
- [x] Level 4 — Code Level Overview
- [x] Design Decisions
- [x] AI Contribution Note
- [x] README
- [x] AI Contribution Log

For the final Word/PDF submission, export the diagrams clearly and include PRN, name, division, date, and the required short explanations according to the faculty guideline.

## Author

**Rutuja Patil**
