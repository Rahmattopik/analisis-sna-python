import networkx as nx
import plotly.graph_objects as go


def create_network_plot(G, max_nodes=300):
    """
    Membuat visualisasi jaringan menggunakan Plotly.
    Agar ringan di browser hanya menampilkan sebagian node.
    """

    # Ambil sebagian node
    nodes = list(G.nodes())[:max_nodes]

    H = G.subgraph(nodes)

    # Layout
    pos = nx.spring_layout(H, seed=42)

    # Edge
    edge_x = []
    edge_y = []

    for edge in H.edges():

        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]

        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        hoverinfo="none",
        line=dict(
            width=0.5,
            color="#888"
        )
    )

    # Node
    node_x = []
    node_y = []
    node_text = []
    node_color = []

    degree = dict(H.degree())

    for node in H.nodes():

        x, y = pos[node]

        node_x.append(x)
        node_y.append(y)

        node_text.append(
            f"Node : {node}<br>Degree : {degree[node]}"
        )

        node_color.append(degree[node])

    node_trace = go.Scatter(

        x=node_x,
        y=node_y,

        mode="markers",

        hoverinfo="text",

        text=node_text,

        marker=dict(

            size=8,

            color=node_color,

            colorscale="Viridis",

            colorbar=dict(
                title="Degree"
            ),

            line=dict(
                width=1,
                color="black"
            )

        )

    )

    fig = go.Figure(
        data=[edge_trace, node_trace]
    )

    fig.update_layout(

        title="Visualisasi Jejaring Sosial",

        showlegend=False,

        hovermode="closest",

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),

        xaxis=dict(
            showgrid=False,
            zeroline=False,
            visible=False
        ),

        yaxis=dict(
            showgrid=False,
            zeroline=False,
            visible=False
        ),

        height=700

    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs="cdn"
    )


def save_network_image(G):

    """
    Menyimpan visualisasi menggunakan matplotlib
    """

    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 10))

    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx(
        G,
        pos,
        with_labels=False,
        node_size=20,
        edge_color="gray"
    )

    plt.savefig(
        "static/network.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()