"""
Smoke tests (sin dependencias extra) para v1.0.

Ejecución:
  .venv/bin/python qa/smoke_tests.py
"""

from __future__ import annotations

import builtins
import sys

import numpy as np

sys.path.insert(0, "v1.0")

import matrix_io  # noqa: E402
import order  # noqa: E402
import relation  # noqa: E402


def test_core_properties() -> None:
    m = np.eye(4, dtype=bool)
    assert relation.is_equivalence(m)
    assert order.is_partial_order(m)

    z = np.zeros((3, 3), dtype=bool)
    assert relation.is_irreflexive(z)
    assert relation.is_symmetric(z)
    assert relation.is_transitive(z)

    bad = np.zeros((3, 3), dtype=bool)
    bad[0, 1] = True
    bad[1, 2] = True
    assert not relation.is_transitive(bad)
    assert relation.transitive_counterexample(bad)

    s = np.zeros((4, 4), dtype=bool)
    for i in range(4):
        for j in range(4):
            if i < j:
                s[i, j] = True
    assert order.is_strict_order(s)


def test_manual_entry_cell_by_cell() -> None:
    # n=2: cuatro celdas. Después del 2do valor responder 'n'.
    inputs = iter(["1", "0", "n", "0", "1"])
    orig_input = builtins.input
    builtins.input = lambda prompt="": next(inputs)
    try:
        m = matrix_io.read_matrix_manual(2)
    finally:
        builtins.input = orig_input

    expected = np.array([[1, 0], [0, 1]], dtype=bool)
    assert (m == expected).all(), (m, expected)


def test_manual_entry_assisted_complete() -> None:
    inputs = iter(["1", "1", "y"])
    orig_input = builtins.input
    builtins.input = lambda prompt="": next(inputs)
    try:
        m = matrix_io.read_matrix_manual(3)
    finally:
        builtins.input = orig_input

    assert m.shape == (3, 3)
    assert bool(m[0, 0]) is True and bool(m[0, 1]) is True


def main() -> None:
    test_core_properties()
    test_manual_entry_cell_by_cell()
    test_manual_entry_assisted_complete()
    print("OK: smoke tests passed")


if __name__ == "__main__":
    main()

