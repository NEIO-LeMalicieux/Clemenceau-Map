from flask import Flask, render_template, request

app = Flask(__name__)

rooms = {
    "A1": {"x": 120, "y": 240},
    "A2": {"x": 200, "y": 240},
    "B1": {"x": 350, "y": 400},
    "B2": {"x": 450, "y": 400},
}

paths = {
    "Entrance": ["HallwayA"],
    "HallwayA": ["A1", "A2", "Stairs"],
    "Stairs": ["B1", "B2"],
}

def find_path(graph, start, end):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.append(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


@app.route("/", methods=["GET", "POST"])
def index():
    selected_room = None
    path = None
    return render_template(index.html)

app.run(debug=True)