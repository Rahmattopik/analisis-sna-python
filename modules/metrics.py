import networkx as nx


def network_metrics(G):
    """
    Menghitung metrik global jaringan
    """

    # Density
    density = nx.density(G)

    # Clustering Coefficient
    clustering = nx.average_clustering(G)

    # Jika graf tidak connected, gunakan komponen terbesar
    if nx.is_connected(G):

        diameter = nx.diameter(G)

        average_path = nx.average_shortest_path_length(G)

    else:

        largest_component = max(
            nx.connected_components(G),
            key=len
        )

        H = G.subgraph(largest_component).copy()

        diameter = nx.diameter(H)

        average_path = nx.average_shortest_path_length(H)

    return {
        "density": round(density, 6),
        "diameter": diameter,
        "average_path": round(average_path, 4),
        "clustering": round(clustering, 6)
    }


def is_connected_graph(G):
    """
    Mengecek apakah graf terhubung
    """

    return nx.is_connected(G)


def connected_components_count(G):
    """
    Menghitung jumlah komponen
    """

    return nx.number_connected_components(G)


def largest_component_size(G):
    """
    Menghitung ukuran komponen terbesar
    """

    largest = max(
        nx.connected_components(G),
        key=len
    )

    return len(largest)


def graph_statistics(G):
    """
    Statistik tambahan graf
    """

    stats = {
        "Jumlah Node": G.number_of_nodes(),
        "Jumlah Edge": G.number_of_edges(),
        "Density": round(nx.density(G), 6),
        "Connected": nx.is_connected(G),
        "Jumlah Komponen": nx.number_connected_components(G),
        "Average Degree": round(
            sum(dict(G.degree()).values()) /
            G.number_of_nodes(),
            2
        )
    }

    return stats