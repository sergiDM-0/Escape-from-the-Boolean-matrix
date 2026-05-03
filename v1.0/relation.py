"""Propiedades de relaciones sobre matriz booleana MR[i,j] <=> x_i R x_j."""

from __future__ import annotations

import numpy as np


def node_label(i: int) -> str:
    """Índice 0-based -> etiqueta x_1, x_2, ..."""
    return f"x_{i + 1}"


def pairs_from_matrix(m: np.ndarray) -> list[tuple[str, str]]:
    m = np.asarray(m, dtype=bool)
    n = m.shape[0]
    out: list[tuple[str, str]] = []
    for i in range(n):
        for j in range(n):
            if m[i, j]:
                out.append((node_label(i), node_label(j)))
    return out


def format_relation_r(m: np.ndarray) -> str:
    pairs = pairs_from_matrix(m)
    if not pairs:
        return "R = ∅"
    inner = ", ".join(f"({a}, {b})" for a, b in pairs)
    return f"R = {{ {inner} }}"


def is_reflexive(m: np.ndarray) -> bool:
    m = np.asarray(m, dtype=bool)
    return bool(np.all(np.diag(m)))


def is_irreflexive(m: np.ndarray) -> bool:
    m = np.asarray(m, dtype=bool)
    return bool(np.all(~np.diag(m)))


def is_symmetric(m: np.ndarray) -> bool:
    m = np.asarray(m, dtype=bool)
    return bool(np.all(m == m.T))


def is_asymmetric(m: np.ndarray) -> bool:
    """∀i,j: M[i,j] => ¬M[j,i] (implica irreflexiva)."""
    m = np.asarray(m, dtype=bool)
    return not np.any(m & m.T)


def is_antisymmetric(m: np.ndarray) -> bool:
    """i≠j y M[i,j] y M[j,i] no puede ocurrir."""
    m = np.asarray(m, dtype=bool)
    n = m.shape[0]
    for i in range(n):
        for j in range(n):
            if i != j and m[i, j] and m[j, i]:
                return False
    return True


def boolean_square(m: np.ndarray) -> np.ndarray:
    """Producto booleano M∘M (usando matmul sobre bool)."""
    m = np.asarray(m, dtype=bool)
    return np.matmul(m, m)


def is_transitive(m: np.ndarray) -> bool:
    """M²[i,j] => M[i,j] para todo i,j (producto booleano)."""
    m = np.asarray(m, dtype=bool)
    m2 = boolean_square(m)
    return bool(np.all(~m2 | m))


def is_equivalence(m: np.ndarray) -> bool:
    return is_reflexive(m) and is_symmetric(m) and is_transitive(m)


def transitive_counterexample(m: np.ndarray) -> str | None:
    """Primer (i,j,k) que rompe transitividad, o None."""
    m = np.asarray(m, dtype=bool)
    n = m.shape[0]
    for i in range(n):
        for j in range(n):
            if not m[i, j]:
                continue
            for k in range(n):
                if m[j, k] and not m[i, k]:
                    return (
                        f"Falla transitividad: {node_label(i)} R {node_label(j)}, "
                        f"{node_label(j)} R {node_label(k)}, pero no {node_label(i)} R {node_label(k)}."
                    )
    return None
