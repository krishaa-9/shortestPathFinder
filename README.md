# Shortest Path Finder using Dijkstra's and A* Algorithms

DAA implementation project built with Python and Streamlit.

## Features
- Finds the shortest route between campus locations
- Compares Dijkstra and A* (distance, nodes explored, time)
- Visual route display and complexity analysis

## Campus locations
College Gate, Library, Canteen, Computer Lab, Hostel

## How to run
```bash
pip install -r requirements.txt
python main.py          # terminal version
streamlit run app.py    # web app
```

## Project structure
- `graph_data.py` - locations, distances and coordinates
- `algorithms.py` - Dijkstra and A* implementations
- `main.py` - terminal test
- `app.py` - Streamlit interface and DAA analysis

## Complexity
- Time: O((V+E) log V)
- Space: O(V+E)
