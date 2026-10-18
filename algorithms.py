import heapq
import math
import time


def _build_path(previous, goal):
    path, node = [], goal
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    return path


def dijkstra(graph, start, goal):
    """Greedy: always expand the unvisited node with the smallest known distance."""
    t0 = time.perf_counter()
    dist = {n: math.inf for n in graph}
    previous = {n: None for n in graph}
    dist[start] = 0
    pq = [(0, start)]
    visited = set()
    explored = []                       # order in which nodes were expanded

    while pq:
        d, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        explored.append(current)
        if current == goal:
            break
        for neighbor, w in graph[current].items():
            nd = d + w
            if nd < dist[neighbor]:
                dist[neighbor] = nd
                previous[neighbor] = current
                heapq.heappush(pq, (nd, neighbor))

    elapsed = (time.perf_counter() - t0) * 1000
    if dist[goal] == math.inf:
        return {"path": [], "distance": math.inf, "explored": explored, "time_ms": elapsed}
    return {"path": _build_path(previous, goal), "distance": dist[goal],
            "explored": explored, "time_ms": elapsed}


def heuristic(coords, a, b):
    (x1, y1), (x2, y2) = coords[a], coords[b]
    return math.hypot(x1 - x2, y1 - y2)


def astar(graph, coords, start, goal):
    """Like Dijkstra, but orders nodes by f = g + h (h = straight-line estimate to goal)."""
    t0 = time.perf_counter()
    g = {n: math.inf for n in graph}
    previous = {n: None for n in graph}
    g[start] = 0
    pq = [(heuristic(coords, start, goal), start)]
    visited = set()
    explored = []

    while pq:
        _, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        explored.append(current)
        if current == goal:
            break
        for neighbor, w in graph[current].items():
            ng = g[current] + w
            if ng < g[neighbor]:
                g[neighbor] = ng
                previous[neighbor] = current
                f = ng + heuristic(coords, neighbor, goal)
                heapq.heappush(pq, (f, neighbor))

    elapsed = (time.perf_counter() - t0) * 1000
    if g[goal] == math.inf:
        return {"path": [], "distance": math.inf, "explored": explored, "time_ms": elapsed}
    return {"path": _build_path(previous, goal), "distance": g[goal],
            "explored": explored, "time_ms": elapsed}
