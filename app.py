from flask import Flask, render_template

# Import module
from modules.graph import load_graph, graph_info, adjacency_matrix
from modules.centrality import centrality_analysis
from modules.metrics import network_metrics
from modules.community import detect_communities
from modules.simulation import simulate_information
from modules.visualisasi import create_network_plot

app = Flask(__name__)

# ===================================
# Load Dataset
# ===================================
#DATASET = "email-Eu-core.txt.gz"
# Jika file berada di folder dataset gunakan:
DATASET = "dataset/email-Eu-core.txt.gz"

print("Membaca dataset...")
G = load_graph(DATASET)

print("Menghitung informasi graf...")
info = graph_info(G)

print("Membuat adjacency matrix...")
matrix = adjacency_matrix(G)

print("Menghitung centrality...")
centrality = centrality_analysis(G)

print("Menghitung network metrics...")
metrics = network_metrics(G)

print("Deteksi komunitas...")
communities = detect_communities(G)

print("Simulasi penyebaran informasi...")
simulation = simulate_information(G)

print("Membuat visualisasi...")
graph_html = create_network_plot(G)

print("Selesai.")


@app.route("/")
def index():

    return render_template(
        "index.html",

        info=info,

        matrix=matrix.to_html(
            classes="table table-bordered table-striped",
            index=True
        ),

        degree=centrality["degree"],

        betweenness=centrality["betweenness"],

        closeness=centrality["closeness"],

        eigenvector=centrality["eigenvector"],

        metrics=metrics,

        communities=communities,

        simulation=simulation,

        graph_html=graph_html
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )