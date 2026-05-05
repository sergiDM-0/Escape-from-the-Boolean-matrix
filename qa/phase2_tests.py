"""
QA Phase 2: pruebas de entradas inválidas y generación de HTML.

Ejecución:
  .venv/bin/python qa/phase2_tests.py
"""

from __future__ import annotations

import builtins
import io
import os
from contextlib import redirect_stdout
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
V1 = ROOT / "v1.0"
sys.path.insert(0, str(V1))

import graph_view  # noqa: E402
import matrix_io  # noqa: E402
import matrix_view  # noqa: E402
import relation_view  # noqa: E402


def _fake_inputs(seq: list[str]):
    it = iter(seq)
    return lambda prompt="": next(it)


def test_parse_positive_int_invalids() -> None:
    for raw in ["", "   ", "abc", "1.5"]:
        try:
            matrix_io.parse_positive_int(raw)
            raise AssertionError(f"Expected ValueError for {raw!r}")
        except ValueError:
            pass

    for raw in ["0", "-1", "-999"]:
        try:
            matrix_io.parse_positive_int(raw)
            raise AssertionError(f"Expected ValueError for {raw!r}")
        except ValueError:
            pass

    assert matrix_io.parse_positive_int("1") == 1
    assert matrix_io.parse_positive_int("  25 ") == 25


def test_manual_cell_reprompts_on_invalid_cell() -> None:
    # n=2 → 4 celdas. En la primera celda mete inválidos y luego un '1'.
    # Después del segundo valor responde 'n' para continuar manual.
    inputs = [
        "x",  # inval
        "2",  # inval
        "1",  # ok (0,0)
        "0",  # ok (0,1) -> triggers assist question
        "n",  # continue
        "0",  # ok (1,0)
        "1",  # ok (1,1)
    ]
    orig_input = builtins.input
    buf = io.StringIO()
    builtins.input = _fake_inputs(inputs)
    try:
        with redirect_stdout(buf):
            m = matrix_io.read_matrix_manual(2)
    finally:
        builtins.input = orig_input

    out = buf.getvalue()
    assert "Solo se permiten 0 y 1 en cada celda." in out
    assert m.shape == (2, 2)
    assert (m == np.array([[1, 0], [0, 1]], dtype=bool)).all()


def test_manual_assist_answer_other_than_y_keeps_asking() -> None:
    # n=2: after 2nd value, answer 'maybe' (treated as no), continue.
    inputs = ["1", "1", "maybe", "0", "0"]
    orig_input = builtins.input
    builtins.input = _fake_inputs(inputs)
    try:
        m = matrix_io.read_matrix_manual(2)
    finally:
        builtins.input = orig_input
    assert m.shape == (2, 2)
    assert bool(m[0, 0]) is True and bool(m[0, 1]) is True


def test_html_generation_creates_files() -> None:
    # Evitar abrir navegador en tests.
    import html_export  # noqa: E402

    orig_open = html_export.webbrowser.open
    html_export.webbrowser.open = lambda *args, **kwargs: False
    try:
        m = np.array([[1, 0, 1], [0, 1, 0], [0, 0, 0]], dtype=bool)

        matrix_view.show_matrix_html(m)
        relation_view.show_relation_html(m)
        graph_view.show_directed_graph(m)

        assert (V1 / "matriz_relacional.html").exists()
        assert (V1 / "relacion_R.html").exists()
        assert (V1 / "grafo_dirigido.html").exists()
    finally:
        html_export.webbrowser.open = orig_open


def main() -> None:
    # Limpieza mínima: no borrar HTML del usuario; solo comprobar creación.
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    test_parse_positive_int_invalids()
    test_manual_cell_reprompts_on_invalid_cell()
    test_manual_assist_answer_other_than_y_keeps_asking()
    test_html_generation_creates_files()
    print("OK: QA phase 2 passed")


if __name__ == "__main__":
    main()

