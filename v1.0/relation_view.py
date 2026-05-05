"""Vista HTML de la relación R como tabla de pares."""

from __future__ import annotations

import numpy as np
import plotly.graph_objects as go

import relation
from html_export import write_and_open_html


def show_relation_html(m: np.ndarray) -> None:
    m = np.asarray(m, dtype=bool)
    pairs = relation.pairs_from_matrix(m)

    if not pairs:
        html = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8"/>
  <title>Relación R</title>
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; margin: 24px; }
    .card { max-width: 720px; padding: 18px; border: 1px solid #ddd; border-radius: 12px; }
    h1 { margin: 0 0 8px; font-size: 20px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Relación R</h1>
    <div>R = ∅</div>
  </div>
</body>
</html>"""
        write_and_open_html(filename="relacion_R.html", html=html)
        return

    a_vals = [a for a, _ in pairs]
    b_vals = [b for _, b in pairs]

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=["Elemento a", "Elemento b"],
                    fill_color=["#1f77b4", "#1f77b4"],
                    font=dict(color="white", size=13),
                    align="center",
                ),
                cells=dict(
                    values=[a_vals, b_vals],
                    fill_color=["#e8f4ff", "#ffffff"],
                    align="center",
                    height=24,
                ),
            )
        ]
    )
    fig.update_layout(
        title=f"Relación R (|R| = {len(pairs)})",
        margin=dict(l=20, r=20, t=60, b=20),
    )

    html = fig.to_html(full_html=True, include_plotlyjs="cdn")
    write_and_open_html(filename="relacion_R.html", html=html)

