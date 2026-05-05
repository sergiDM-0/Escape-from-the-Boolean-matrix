"""Vista HTML de la matriz MR con encabezados y color."""

from __future__ import annotations

import numpy as np
import plotly.graph_objects as go

from html_export import write_and_open_html


def show_matrix_html(m: np.ndarray) -> None:
    m = np.asarray(m, dtype=bool)
    n = m.shape[0]

    labels = [f"x_{i + 1}" for i in range(n)]
    data_int = m.astype(int)

    # Construcción de tabla: primera fila = encabezados de columnas, primera columna = encabezados de filas
    header = [""] + labels

    # Valores por columna (Plotly Table trabaja por columnas)
    col0 = labels
    cols: list[list[str]] = [col0]
    for j in range(n):
        cols.append([str(int(v)) for v in data_int[:, j]])

    # Colores: encabezado azul, columna índice celeste, celdas según 0/1
    header_fill = ["#1f77b4"] * (n + 1)
    header_font = ["white"] * (n + 1)

    # fill_color requiere lista por columna
    index_col_fill = ["#e8f4ff"] * n
    cell_fills: list[list[str]] = [index_col_fill]
    for j in range(n):
        cell_fills.append(["#ffffff" if v == 0 else "#c9e4ff" for v in data_int[:, j]])

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=header,
                    fill_color=header_fill,
                    font=dict(color=header_font, size=13),
                    align="center",
                ),
                cells=dict(
                    values=cols,
                    fill_color=cell_fills,
                    font=dict(color="#111", size=12),
                    align="center",
                    height=24,
                ),
            )
        ]
    )

    fig.update_layout(
        title=f"Matriz relacional MR ({n}×{n})",
        margin=dict(l=20, r=20, t=60, b=20),
    )

    html = fig.to_html(full_html=True, include_plotlyjs="cdn")
    write_and_open_html(filename="matriz_relacional.html", html=html)

