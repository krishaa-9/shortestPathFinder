"""Campus map: locations, distances (edges) and coordinates (used by A* and drawing)."""

# Undirected weighted graph as an adjacency list: node -> {neighbor: distance}
graph = {
    "College Gate":  {"Library": 4, "Canteen": 2},
    "Library":       {"College Gate": 4, "Canteen": 5, "Computer Lab": 6},
    "Canteen":       {"College Gate": 2, "Library": 5, "Computer Lab": 3, "Hostel": 11},
    "Computer Lab":  {"Library": 6, "Canteen": 3, "Hostel": 7},
    "Hostel":        {"Canteen": 11, "Computer Lab": 7},
}

# (x, y) positions. Straight-line distance between any two connected places
# is <= the road distance, so the heuristic in A* never overestimates (admissible).
coords = {
    "College Gate": (0, 0),
    "Library":      (3, 2),
    "Canteen":      (2, 0),
    "Computer Lab": (5, 0),
    "Hostel":       (10, -2),
}
