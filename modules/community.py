import community as community_louvain
import pandas as pd
import networkx as nx


def detect_communities(G):
    """
    Deteksi komunitas menggunakan algoritma Louvain
    """

    # Louvain hanya untuk graph tak berarah
    partition = community_louvain.best_partition(G)

    # Membuat DataFrame
    df = pd.DataFrame(
        partition.items(),
        columns=["Node", "Community"]
    )

    df = df.sort_values(
        by=["Community", "Node"]
    )

    # Hitung jumlah anggota setiap komunitas
    summary = (
        df.groupby("Community")
        .size()
        .reset_index(name="Jumlah Node")
        .sort_values(
            by="Jumlah Node",
            ascending=False
        )
    )

    jumlah_komunitas = summary.shape[0]

    komunitas_terbesar = summary.iloc[0]["Community"]

    anggota_terbesar = summary.iloc[0]["Jumlah Node"]

    html = f"""
    <div class="alert alert-success">
        <h5>Hasil Deteksi Komunitas</h5>

        <p><b>Jumlah Komunitas :</b> {jumlah_komunitas}</p>

        <p><b>Komunitas Terbesar :</b> {komunitas_terbesar}</p>

        <p><b>Jumlah Anggota :</b> {anggota_terbesar}</p>
    </div>

    <h5>Daftar Komunitas</h5>

    {summary.to_html(
        classes='table table-bordered table-striped',
        index=False
    )}
    """

    return html


def get_partition(G):
    """
    Mengembalikan hasil partition Louvain
    """

    return community_louvain.best_partition(G)


def community_sizes(G):
    """
    Menghitung ukuran setiap komunitas
    """

    partition = community_louvain.best_partition(G)

    df = pd.DataFrame(
        partition.items(),
        columns=["Node", "Community"]
    )

    result = (
        df.groupby("Community")
        .size()
        .reset_index(name="Jumlah Node")
    )

    return result


def modularity_score(G):
    """
    Menghitung nilai modularity
    """

    partition = community_louvain.best_partition(G)

    score = community_louvain.modularity(
        partition,
        G
    )

    return round(score, 5)