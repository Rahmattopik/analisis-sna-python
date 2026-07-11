import networkx as nx
import pandas as pd


def load_graph(file_path):
    """
    Membaca dataset edge list dan membuat graph
    """

    G = nx.read_edgelist(
        file_path,
        nodetype=int,
        create_using=nx.Graph()
    )

    return G


def graph_info(G):
    """
    Informasi dasar graf
    """

    info = {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "graph_type": "Undirected",
        "weighted": "Tidak"
    }

    return info


def adjacency_matrix(G, size=5):
    """
    Membuat adjacency matrix dari 5 node pertama
    """

    nodes = list(G.nodes())[:size]

    matrix = nx.to_pandas_adjacency(
        G,
        nodelist=nodes,
        dtype=int
    )

    return matrix


def get_nodes(G):
    """
    Mengambil semua node
    """

    return list(G.nodes())


def get_edges(G):
    """
    Mengambil semua edge
    """

    return list(G.edges())


def degree_list(G):
    """
    Menampilkan degree setiap node
    """

    degree = dict(G.degree())

    df = pd.DataFrame(
        degree.items(),
        columns=["Node", "Degree"]
    )

    df = df.sort_values(
        by="Degree",
        ascending=False
    )

    return df


def graph_summary(G):
    """
    Ringkasan graf
    """

    summary = {
        "Jumlah Node": G.number_of_nodes(),
        "Jumlah Edge": G.number_of_edges(),
        "Node Terbesar": max(dict(G.degree()), key=dict(G.degree()).get),
        "Degree Maksimum": max(dict(G.degree()).values())
    }

    return summary