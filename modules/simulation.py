import networkx as nx
import pandas as pd
import random


def simulate_information(G, probability=0.3, max_iteration=10):
    """
    Simulasi penyebaran informasi menggunakan model SI.
    """

    # Node awal dengan Degree Centrality tertinggi
    degree = nx.degree_centrality(G)
    source = max(degree, key=degree.get)

    infected = set([source])

    history = []

    history.append({
        "Iterasi": 0,
        "Node Baru": source,
        "Total Terinfeksi": len(infected)
    })

    for i in range(1, max_iteration + 1):

        new_infected = set()

        for node in infected:

            for neighbor in G.neighbors(node):

                if neighbor not in infected:

                    if random.random() <= probability:
                        new_infected.add(neighbor)

        infected.update(new_infected)

        history.append({
            "Iterasi": i,
            "Node Baru": len(new_infected),
            "Total Terinfeksi": len(infected)
        })

        if len(infected) == G.number_of_nodes():
            break

    df = pd.DataFrame(history)

    html = f"""
    <div class="alert alert-info">

    <h5>Simulasi Penyebaran Informasi</h5>

    <p><b>Node Awal :</b> {source}</p>

    <p><b>Probabilitas Penyebaran :</b> {probability}</p>

    <p><b>Total Node Terinfeksi :</b> {len(infected)}</p>

    </div>

    {df.to_html(
        classes='table table-bordered table-striped',
        index=False
    )}
    """

    return html


def information_speed(G):

    degree = nx.degree_centrality(G)

    node = max(degree, key=degree.get)

    return {
        "node_awal": node,
        "degree": round(degree[node], 5)
    }


def simulate_from_node(
        G,
        source,
        probability=0.3,
        max_iteration=10):

    infected = set([source])

    result = []

    for i in range(max_iteration):

        new = set()

        for node in infected:

            for n in G.neighbors(node):

                if n not in infected:

                    if random.random() <= probability:
                        new.add(n)

        infected.update(new)

        result.append(len(infected))

    return result