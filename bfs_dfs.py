from collections import deque
import time

GRAPH = {
    "A": ["C", "B"], "B": ["D", "E"], "C": ["G", "H"], "D": ["F"],
    "E": ["I", "J"], "F": ["M", "N", "V"], "G": ["O", "P"],
    "H": ["K", "L"], "I": [], "J": [], "K": [], "L": [], "M": [],
    "N": [], "O": ["W"], "P": ["Q", "R"], "Q": ["S"], "R": ["T", "U"],
    "S": [], "T": [], "U": [], "V": [], "W": []
}

START = "A"
GOAL = "W"

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    nodes_expanded = 0
    while queue:
        node, path = queue.popleft()
        nodes_expanded += 1
        if node == goal:
            return path, nodes_expanded
        for neighbour in GRAPH[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))
    return [], nodes_expanded

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        nodes_expanded += 1
        if node == goal:
            return path, nodes_expanded
        for neighbour in GRAPH[node]:
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))
    return [], nodes_expanded

def run_algorithm(algorithm, start, goal):
    times = []
    path = []
    nodes = 0
    for _ in range(3):
        start_time = time.perf_counter()
        path, nodes = algorithm(start, goal)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)
    return path, nodes, times

def display_results(name, path, nodes, times):
    best = min(times)
    average = sum(times) / len(times)
    worst = max(times)
    print()
    print("=" * 50)
    print(f"{name:^50}")
    print("=" * 50)
    print("Path:", " -> ".join(path))
    print(f"Best Time        : {best:.6f} ms")
    print(f"Average Time     : {average:.6f} ms")
    print(f"Worst Time       : {worst:.6f} ms")
    print(f"Nodes Expanded   : {nodes}")
    print("=" * 50)

if __name__ == "__main__":
    print("Graph:", GRAPH)
    print(f"Start: {START}")
    print(f"Goal : {GOAL}")
    bfs_path, bfs_nodes, bfs_times = run_algorithm(bfs, START, GOAL)
    dfs_path, dfs_nodes, dfs_times = run_algorithm(dfs, START, GOAL)
    display_results("BFS RESULTS", bfs_path, bfs_nodes, bfs_times)
    display_results("DFS RESULTS", dfs_path, dfs_nodes, dfs_times)
