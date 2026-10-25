# Shortest Path Finder using Dijkstra's and A* Algorithms

A DAA (Design and Analysis of Algorithms) implementation project built with Python and Streamlit. It finds the shortest route between locations on a college campus and compares two algorithms: **Dijkstra** and **A\***.

## Features
- Finds the shortest route between any two campus locations
- Implements Dijkstra's algorithm (greedy method)
- Implements A* algorithm (heuristic search)
- Compares both: total distance, nodes explored, execution time
- Visual map with the route highlighted
- Shows time and space complexity

## Campus locations
College Gate, Library, Canteen, Computer Lab, Hostel

## Technologies used
- Python 3.9 or higher
- Streamlit (web interface)
- Matplotlib (drawing the map)
- heapq (priority queue)

## Project structure
```
ShortestPathFinder/
├── graph_data.py      # locations, distances and coordinates
├── algorithms.py      # Dijkstra and A* implementations
├── main.py            # terminal version (test both algorithms)
├── app.py             # Streamlit web app + DAA analysis
├── requirements.txt   # libraries to install
└── README.md
```

## Setup and run (step by step)

### Step 1: Install the requirements
- Install [Python](https://www.python.org/downloads/) (tick "Add Python to PATH" during installation)
- Install [VS Code](https://code.visualstudio.com/) and the Python extension

### Step 2: Get the project
```bash
git clone https://github.com/krishaa-9/shortestPathFinder.git
cd shortestPathFinder
```
Or download the ZIP from GitHub (Code -> Download ZIP), extract it and open the folder in VS Code.

### Step 3: Install the libraries
Open the terminal in the project folder and run:
```bash
pip install -r requirements.txt
```

### Step 4: Run the terminal version
```bash
python main.py
```
On Windows, if this does not work, use `py main.py`.

Expected output:
```
--- Dijkstra ---
Shortest Path: College Gate -> Canteen -> Computer Lab -> Hostel
Total Distance: 12
Nodes explored: 5
--- A* ---
Shortest Path: College Gate -> Canteen -> Computer Lab -> Hostel
Total Distance: 12
Nodes explored: 4
```

### Step 5: Run the web app
```bash
streamlit run app.py
```
The app opens in your browser at `http://localhost:8501`.

### Step 6: Use the app
1. Choose a **start location**
2. Choose a **destination**
3. Select **Dijkstra** or **A\*** to display the route
4. Click **Find shortest path**
5. View the map, total distance and DAA analysis table

To stop the app, press `Ctrl + C` in the terminal.

## How it works

| Concept | Meaning in this project |
|---|---|
| Graph | Campus locations and their connections |
| Vertex (node) | A location, such as the Library |
| Edge | A connection between two locations |
| Weight | Distance of a connection |
| Greedy method | Dijkstra always expands the closest unvisited node |
| Heuristic | A* uses straight-line distance to the goal as an estimate |
| Priority queue | Picks the node with the lowest cost first |

## Complexity analysis

| | Dijkstra | A* |
|---|---|---|
| Time | O((V+E) log V) | O((V+E) log V) worst case, usually explores fewer nodes |
| Space | O(V+E) | O(V+E) |
| Needs coordinates | No | Yes (for the heuristic) |

V = number of vertices, E = number of edges.

## Customising the map
Edit `graph_data.py` to add locations or change distances. Keep the coordinates consistent with the distances: the straight-line distance between two connected places must never be greater than the road distance, otherwise A* may not return the shortest path.

## Output
## Output

<img src="https://github.com/user-attachments/assets/c03834f1-2f14-440a-9c62-b0d783776aae" width="700" alt="Shortest Path Finder Output 1">

<img src="https://github.com/user-attachments/assets/e35a2b5b-9646-422c-8125-54cddd0200f3" width="700" alt="Shortest Path Finder Output 2">

<img src="https://github.com/user-attachments/assets/9304dcd8-d793-4694-93ba-5dc38aaa7a7f" width="700" alt="Shortest Path Finder Output 3">

## Author
Krisha

