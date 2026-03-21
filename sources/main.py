from flask import Flask, render_template, request
import tkinter as tk
from PIL import Image, ImageTk

app = Flask(__name__)

salles = [

# COULOIR BAS (administration / CDI)
{"id":"48","type":"salle","escalier_proche":"K","x":70,"y":92},
{"id":"49","type":"salle","escalier_proche":"K","x":65,"y":92},
{"id":"50","type":"salle","escalier_proche":"K","x":60,"y":92},d 
{"id":"51","type":"salle","escalier_proche":"K","x":55,"y":92},
{"id":"52","type":"salle","escalier_proche":"K","x":50,"y":92},
{"id":"53","type":"salle","escalier_proche":"A","x":45,"y":92},
{"id":"54","type":"salle","escalier_proche":"A","x":40,"y":92},
{"id":"55","type":"salle","escalier_proche":"A","x":35,"y":92},
{"id":"56","type":"salle","escalier_proche":"A","x":30,"y":92},
{"id":"57","type":"salle","escalier_proche":"A","x":25,"y":92},

{"id":"100","type":"salle","escalier_proche":"A","x":25,"y":95},
{"id":"148","type":"salle","escalier_proche":"A","x":27,"y":95},
{"id":"149","type":"salle","escalier_proche":"A","x":29,"y":95},

# BLOC GAUCHE BAS
{"id":"101","type":"salle","escalier_proche":"A","x":12,"y":88},
{"id":"102","type":"salle","escalier_proche":"A","x":12,"y":85},
{"id":"103","type":"salle","escalier_proche":"A","x":12,"y":82},

{"id":"104","type":"salle","escalier_proche":"B","x":12,"y":78},
{"id":"105","type":"salle","escalier_proche":"B","x":12,"y":75},
{"id":"106","type":"salle","escalier_proche":"B","x":12,"y":72},

# BLOC GAUCHE MILIEU
{"id":"7","type":"salle","escalier_proche":"C","x":12,"y":63},
{"id":"8","type":"salle","escalier_proche":"C","x":12,"y":60},
{"id":"9","type":"salle","escalier_proche":"C","x":12,"y":57},
{"id":"10","type":"salle","escalier_proche":"D","x":12,"y":54},

{"id":"107","type":"salle","escalier_proche":"C","x":16,"y":63},
{"id":"108","type":"salle","escalier_proche":"C","x":16,"y":60},
{"id":"109","type":"salle","escalier_proche":"D","x":16,"y":57},

{"id":"110","type":"salle","escalier_proche":"D","x":18,"y":52},
{"id":"111","type":"salle","escalier_proche":"D","x":18,"y":50},
{"id":"112","type":"salle","escalier_proche":"D","x":18,"y":48},
{"id":"113","type":"salle","escalier_proche":"D","x":18,"y":46},

{"id":"210","type":"salle","escalier_proche":"D","x":16,"y":52},
{"id":"211","type":"salle","escalier_proche":"D","x":16,"y":50},
{"id":"212","type":"salle","escalier_proche":"D","x":16,"y":48},
{"id":"213","type":"salle","escalier_proche":"E","x":16,"y":46},

# BLOC HAUT GAUCHE
{"id":"14","type":"salle","escalier_proche":"E","x":20,"y":42},
{"id":"15","type":"salle","escalier_proche":"E","x":20,"y":38},
{"id":"16","type":"salle","escalier_proche":"E","x":20,"y":34},
{"id":"17","type":"salle","escalier_proche":"E","x":20,"y":30},
{"id":"18","type":"salle","escalier_proche":"E","x":25,"y":30},
{"id":"116","type":"salle","escalier_proche":"E","x":23,"y":30},

# COULOIR PALMIERS
{"id":"20","type":"salle","escalier_proche":"D","x":35,"y":38},
{"id":"21","type":"salle","escalier_proche":"D","x":37,"y":38},
{"id":"22","type":"salle","escalier_proche":"D","x":39,"y":38},
{"id":"23","type":"salle","escalier_proche":"G","x":41,"y":38},
{"id":"24","type":"salle","escalier_proche":"G","x":43,"y":38},
{"id":"25","type":"salle","escalier_proche":"G","x":45,"y":38},
{"id":"26","type":"salle","escalier_proche":"G","x":47,"y":38},

{"id":"125","type":"salle","escalier_proche":"E","x":45,"y":25},
{"id":"126","type":"salle","escalier_proche":"E","x":50,"y":25},

# BLOC DROIT HAUT
{"id":"30","type":"salle","escalier_proche":"F","x":88,"y":8},
{"id":"31","type":"salle","escalier_proche":"F","x":88,"y":12},

{"id":"130","type":"salle","escalier_proche":"F","x":92,"y":8},
{"id":"131","type":"salle","escalier_proche":"F","x":92,"y":12},
{"id":"132","type":"salle","escalier_proche":"F","x":92,"y":15},

{"id":"133","type":"salle","escalier_proche":"G","x":92,"y":25},
{"id":"134","type":"salle","escalier_proche":"G","x":92,"y":28},
{"id":"135","type":"salle","escalier_proche":"G","x":92,"y":31},

{"id":"136","type":"salle","escalier_proche":"H","x":92,"y":34},
{"id":"137","type":"salle","escalier_proche":"H","x":92,"y":37},

# BLOC DROIT MILIEU
{"id":"138","type":"salle","escalier_proche":"H","x":92,"y":42},
{"id":"139","type":"salle","escalier_proche":"H","x":92,"y":45},

{"id":"140","type":"salle","escalier_proche":"I","x":92,"y":50},
{"id":"141","type":"salle","escalier_proche":"I","x":92,"y":53},

# BLOC DROIT BAS
{"id":"40","type":"salle","escalier_proche":"J","x":85,"y":70},
{"id":"41","type":"salle","escalier_proche":"J","x":85,"y":73},
{"id":"42","type":"salle","escalier_proche":"J","x":85,"y":76},
{"id":"43","type":"salle","escalier_proche":"J","x":85,"y":79},

{"id":"142","type":"salle","escalier_proche":"J","x":90,"y":76},
{"id":"143","type":"salle","escalier_proche":"J","x":90,"y":79},

{"id":"44","type":"salle","escalier_proche":"K","x":85,"y":85},
{"id":"45","type":"salle","escalier_proche":"K","x":85,"y":88},
{"id":"46","type":"salle","escalier_proche":"K","x":85,"y":91},
{"id":"47","type":"salle","escalier_proche":"K","x":85,"y":94},

{"id":"144","type":"salle","escalier_proche":"K","x":90,"y":85},
{"id":"145","type":"salle","escalier_proche":"K","x":90,"y":88},
{"id":"146","type":"salle","escalier_proche":"K","x":90,"y":91},

# BLOC AMPHI / CAFET
{"id":"151","type":"salle","escalier_proche":"I","x":45,"y":55},
{"id":"152","type":"salle","escalier_proche":"I","x":47,"y":55},
{"id":"153","type":"salle","escalier_proche":"I","x":49,"y":55},
{"id":"154","type":"salle","escalier_proche":"I","x":51,"y":55},

{"id":"251","type":"salle","escalier_proche":"I","x":45,"y":52},
{"id":"252","type":"salle","escalier_proche":"I","x":47,"y":52},
{"id":"253","type":"salle","escalier_proche":"I","x":49,"y":52},
{"id":"254","type":"salle","escalier_proche":"I","x":51,"y":52},

]
paths = [
# ESCALIERS
{"id":"A","type":"escalier","x":10,"y":90},
{"id":"B","type":"escalier","x":10,"y":75},
{"id":"C","type":"escalier","x":10,"y":60},
{"id":"D","type":"escalier","x":10,"y":45},
{"id":"E","type":"escalier","x":10,"y":25},

{"id":"F","type":"escalier","x":90,"y":10},
{"id":"G","type":"escalier","x":90,"y":25},
{"id":"H","type":"escalier","x":90,"y":40},
{"id":"I","type":"escalier","x":90,"y":55},
{"id":"J","type":"escalier","x":90,"y":75},
{"id":"K","type":"escalier","x":90,"y":90},
]

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
    return render_template("index.html")

app.run(debug=True)