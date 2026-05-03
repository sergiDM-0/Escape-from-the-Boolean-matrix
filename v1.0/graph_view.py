"""Visualización del grafo dirigido asociado a la matriz MR."""

from __future__ import annotations

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def show_directed_graph(m: np.ndarray) -> None:
    """Abre una ventana con el digrafo: arista i→j si MR[i,j] es True."""
    m = np.asarray(m, dtype=bool)
    n = m.shape[0]
    if n == 0:
        raise ValueError("Matriz vacía.")
    adj = m.astype(np.uint8)
    g = nx.from_numpy_array(adj, create_using=nx.DiGraph)
    pos = nx.spring_layout(g, seed=42, k=2.0 / max(np.sqrt(n), 1e-6))
    _, ax = plt.subplots(figsize=(8, 6))
    nx.draw_networkx_nodes(
        g,
        pos,
        ax=ax,
        node_color="#c9e4ff",
        edgecolors="#222",
        linewidths=1.2,
        node_size=800,
    )
    labels = {i: f"x_{i + 1}" for i in range(n)}
    nx.draw_networkx_labels(g, pos, labels=labels, ax=ax, font_size=10)
    nx.draw_networkx_edges(
        g,
        pos,
        ax=ax,
        edge_color="#333",
        arrows=True,
        arrowstyle="-|>",
        arrowsize=16,
        connectionstyle="arc3,rad=0.08",
        width=1.2,
    )
    ax.set_axis_off()
    ax.set_title("Grafo dirigido de la matriz relacional MR")
    plt.tight_layout()
    plt.show()
