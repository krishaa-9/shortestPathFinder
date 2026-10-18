"""Stage 1 & 2: test both algorithms in the terminal."""
from graph_data import graph, coords
from algorithms import dijkstra, astar

start, goal = "College Gate", "Hostel"

for name, result in [("Dijkstra", dijkstra(graph, start, goal)),
                     ("A*", astar(graph, coords, start, goal))]:
    print(f"--- {name} ---")
    if result["path"]:
        print("Shortest Path:", " -> ".join(result["path"]))
        print("Total Distance:", result["distance"])
        print("Nodes explored:", len(result["explored"]))
        print(f"Time: {result['time_ms']:.4f} ms")
    else:
        print("No path exists between these locations.")
