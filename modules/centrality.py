import networkx as nx
import pandas as pd


def top10_table(data):
    """
    Mengubah dictionary menjadi tabel HTML Top 10
    """

    df = pd.DataFrame(
        data.items(),
        columns=["Node", "Nilai"]
    )

    df = df.sort_values(
        by="Nilai",
        ascending=False
    ).head(10)

    df["Nilai"] = df["Nilai"].round(5)

    return df.to_html(
        classes="table table-striped table-bordered",
        index=False
    )


def centrality_analysis(G):
    """
    Menghitung seluruh centrality
    """

    print("Menghitung Degree Centrality...")
    degree = nx.degree_centrality(G)

    print("Menghitung Betweenness Centrality...")
    betweenness = nx.betweenness_centrality(G)

    print("Menghitung Closeness Centrality...")
    closeness = nx.closeness_centrality(G)

    print("Menghitung Eigenvector Centrality...")
    eigenvector = nx.eigenvector_centrality(
        G,
        max_iter=1000
    )

    return {
        "degree": top10_table(degree),
        "betweenness": top10_table(betweenness),
        "closeness": top10_table(closeness),
        "eigenvector": top10_table(eigenvector)
    }


def get_best_degree(G):

    degree = nx.degree_centrality(G)

    node = max(degree, key=degree.get)

    return node, degree[node]


def get_best_betweenness(G):

    data = nx.betweenness_centrality(G)

    node = max(data, key=data.get)

    return node, data[node]


def get_best_closeness(G):

    data = nx.closeness_centrality(G)

    node = max(data, key=data.get)

    return node, data[node]


def get_best_eigenvector(G):

    data = nx.eigenvector_centrality(
        G,
        max_iter=1000
    )

    node = max(data, key=data.get)

    return node, data[node]