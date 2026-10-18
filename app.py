"""Stage 3 & 4: Streamlit interface + DAA analysis.  Run:  streamlit run app.py"""
import matplotlib.pyplot as plt
import streamlit as st

from algorithms import astar, dijkstra
from graph_data import coords, graph

st.set_page_config(page_title="Shortest Path Finder", layout="wide")
st.title("Shortest Path Finder: Dijkstra vs A*")
st.caption("DAA project: graphs, greedy method, heuristic search, time complexity")

places = list(graph.keys())
c1, c2, c3 = st.columns(3)
start = c1.selectbox("Start location", places, index=0)
goal = c2.selectbox("Destination", places, index=len(places) - 1)
algo = c3.radio("Show route for", ["Dijkstra", "A*"], horizontal=True)


def draw(path):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    drawn = set()
    for a, nbrs in graph.items():
        for b, w in nbrs.items():
            if (b, a) in drawn:
                continue
            drawn.add((a, b))
            (x1, y1), (x2, y2) = coords[a], coords[b]
            ax.plot([x1, x2], [y1, y2], color="lightgray", zorder=1)
            ax.text((x1 + x2) / 2, (y1 + y2) / 2, str(w), fontsize=9,
                    bbox=dict(facecolor="white", edgecolor="none", pad=1))
    for i in range(len(path) - 1):
        (x1, y1), (x2, y2) = coords[path[i]], coords[path[i + 1]]
        ax.plot([x1, x2], [y1, y2], color="crimson", linewidth=3.5, zorder=2)
    for name, (x, y) in coords.items():
        color = "crimson" if name in path else "steelblue"
        ax.scatter(x, y, s=500, color=color, zorder=3)
        ax.text(x, y + 0.45, name, ha="center", fontsize=10, fontweight="bold")
    ax.set_axis_off()
    ax.margins(0.15)
    return fig


if st.button("Find shortest path", type="primary"):
    res_d = dijkstra(graph, start, goal)
    res_a = astar(graph, coords, start, goal)
    chosen = res_d if algo == "Dijkstra" else res_a

    if not chosen["path"]:
        st.error("No path exists between these locations.")
    else:
        left, right = st.columns([2, 1])
        left.pyplot(draw(chosen["path"]))
        right.success(" → ".join(chosen["path"]))
        right.metric("Total distance", chosen["distance"])

        st.subheader("DAA analysis")
        st.table({
            "Algorithm": ["Dijkstra", "A*"],
            "Distance": [res_d["distance"], res_a["distance"]],
            "Nodes explored": [len(res_d["explored"]), len(res_a["explored"])],
            "Time (ms)": [round(res_d["time_ms"], 4), round(res_a["time_ms"], 4)],
            "Explored order": [", ".join(res_d["explored"]), ", ".join(res_a["explored"])],
        })

        st.markdown("""
| | Dijkstra | A* |
|---|---|---|
| Strategy | Greedy (closest node first) | Greedy + heuristic (g + h) |
| Time complexity | O((V+E) log V) | O((V+E) log V) worst case, usually explores fewer nodes |
| Space complexity | O(V+E) | O(V+E) |
| Needs coordinates? | No | Yes (for the heuristic) |
""")
