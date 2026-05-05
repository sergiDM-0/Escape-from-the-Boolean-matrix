"""Visualización del grafo dirigido asociado a la matriz MR."""

from __future__ import annotations

from pathlib import Path
import webbrowser

import networkx as nx
import numpy as np
import plotly.graph_objects as go


def show_directed_graph(m: np.ndarray) -> None:
    """Muestra el digrafo: arista i→j si MR[i,j] es True (Plotly)."""
    m = np.asarray(m, dtype=bool)
    n = m.shape[0]
    if n == 0:
        raise ValueError("Matriz vacía.")

    adj = m.astype(np.uint8, copy=False)
    g = nx.from_numpy_array(adj, create_using=nx.DiGraph)
    # Algunos layouts (como spring_layout) pueden requerir SciPy dependiendo
    # de la versión/condiciones internas de NetworkX. Para no forzar SciPy
    # como dependencia, hacemos fallback a un layout que no lo requiere.
    try:
        pos = nx.spring_layout(g, seed=42, k=2.0 / max(np.sqrt(n), 1e-6))
    except ModuleNotFoundError as e:
        if e.name != "scipy":
            raise
        pos = nx.circular_layout(g)

    xs = [pos[i][0] for i in range(n)]
    ys = [pos[i][1] for i in range(n)]
    node_text = [f"x_{i + 1}" for i in range(n)]

    edge_x: list[float | None] = []
    edge_y: list[float | None] = []
    annotations: list[dict] = []

    # Para cumplir el requisito de grafo dirigido, dibujamos flechas.
    # Nota: muchas aristas pueden hacer la figura más lenta.
    use_arrows = True
    for u, v in g.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        # Acortar el segmento para que la flecha no quede tapada por los nodos.
        dx = x1 - x0
        dy = y1 - y0
        norm = float(np.hypot(dx, dy)) or 1.0
        shrink = 0.05  # fracción del vector para separar de los nodos (más pegado)
        sx = x0 + dx * shrink
        sy = y0 + dy * shrink
        ex = x1 - dx * shrink
        ey = y1 - dy * shrink

        edge_x.extend([sx, ex, None])
        edge_y.extend([sy, ey, None])
        if use_arrows:
            annotations.append(
                dict(
                    ax=sx,
                    ay=sy,
                    x=ex,
                    y=ey,
                    xref="x",
                    yref="y",
                    axref="x",
                    ayref="y",
                    showarrow=True,
                    arrowhead=2,
                    arrowsize=1.15,
                    arrowwidth=2,
                    arrowcolor="#333",
                    opacity=0.9,
                    startstandoff=2,
                    standoff=2,
                )
            )

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1.2, color="#333"),
        hoverinfo="none",
        mode="lines",
        name="aristas",
    )

    node_trace = go.Scatter(
        x=xs,
        y=ys,
        mode="markers+text",
        text=node_text,
        textposition="top center",
        hovertext=node_text,
        hoverinfo="text",
        marker=dict(size=18, color="#c9e4ff", line=dict(width=1.2, color="#222")),
        name="nodos",
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        title="Grafo dirigido de la matriz relacional MR",
        showlegend=False,
        hovermode="closest",
        margin=dict(l=20, r=20, t=60, b=20),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        annotations=annotations,
    )
    # Evitamos depender de la capacidad del entorno para abrir UI.
    # Siempre guardamos un HTML auto-contenido, e intentamos abrirlo sin bloquear.
    out_path = Path(__file__).resolve().parent / "grafo_dirigido.html"
    fig.write_html(out_path)
    try:
        webbrowser.open(out_path.as_uri(), new=2, autoraise=True)
    except Exception:
        # Si el auto-open falla, el usuario puede abrir el HTML manualmente.
        pass
