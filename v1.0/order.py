"""Órdenes parcial, total y estricto a partir de propiedades básicas."""

from __future__ import annotations

import numpy as np

from relation import (
    is_antisymmetric,
    is_asymmetric,
    is_irreflexive,
    is_reflexive,
    is_transitive,
)


def is_partial_order(m: np.ndarray) -> bool:
    """Reflexiva + antisimétrica + transitiva."""
    return is_reflexive(m) and is_antisymmetric(m) and is_transitive(m)


def is_total_order(m: np.ndarray) -> bool:
    """Orden parcial + comparabilidad: ∀i≠j, M[i,j] ∨ M[j,i]."""
    m = np.asarray(m, dtype=bool)
    if not is_partial_order(m):
        return False
    n = m.shape[0]
    for i in range(n):
        for j in range(n):
            if i != j and not (m[i, j] or m[j, i]):
                return False
    return True


def is_strict_order(m: np.ndarray) -> bool:
    """Irreflexiva + asimétrica + transitiva."""
    return is_irreflexive(m) and is_asymmetric(m) and is_transitive(m)
