"""Entrada y validación de la matriz relacional (booleana internamente)."""

from __future__ import annotations

import random
from typing import Literal

import numpy as np

MAX_N = 40


def parse_positive_int(text: str, *, max_value: int = MAX_N) -> int:
    text = text.strip()
    if not text:
        raise ValueError("Entrada vacía.")
    try:
        n = int(text)
    except ValueError as exc:
        raise ValueError("Debe ser un número entero.") from exc
    if n < 1:
        raise ValueError("n debe ser al menos 1.")
    if n > max_value:
        raise ValueError(f"n no puede ser mayor que {max_value}.")
    return n


def ensure_square_bool_matrix(m: np.ndarray) -> np.ndarray:
    """Devuelve copia bool cuadrada o lanza ValueError."""
    m = np.asarray(m)
    if m.ndim != 2:
        raise ValueError("La matriz debe ser bidimensional.")
    if m.shape[0] != m.shape[1]:
        raise ValueError("La matriz relacional debe ser cuadrada (mismo número de filas y columnas).")
    return m.astype(bool, copy=True)


def row_from_tokens(tokens: list[str]) -> np.ndarray:
    """Una fila de n valores 0 o 1 -> ndarray bool (1, n)."""
    row: list[bool] = []
    for t in tokens:
        t = t.strip()
        if t not in ("0", "1"):
            raise ValueError("Solo se permiten 0 y 1 en cada celda.")
        row.append(t == "1")
    return np.array([row], dtype=bool)


def read_matrix_manual(n: int) -> np.ndarray:
    print(f"Ingrese la matriz {n}×{n}, una fila por línea.")
    print("Cada fila: {n} valores separados por espacio (solo 0 o 1).".format(n=n))
    rows: list[np.ndarray] = []
    for i in range(n):
        while True:
            line = input(f"Fila {i + 1}/{n}: ").strip()
            if not line:
                print("Línea vacía; reintente.")
                continue
            tokens = line.split()
            if len(tokens) != n:
                print(f"Se esperaban {n} valores; obtuvo {len(tokens)}. Reintente.")
                continue
            try:
                rows.append(row_from_tokens(tokens))
            except ValueError as e:
                print(e)
                continue
            break
    return np.vstack(rows)


def random_matrix(n: int, *, seed: int | None = None) -> np.ndarray:
    if seed is not None:
        random.seed(seed)
    data = [[random.choice((False, True)) for _ in range(n)] for _ in range(n)]
    return np.array(data, dtype=bool)


def acquire_matrix(
    mode: Literal["manual", "random"],
    n: int,
    *,
    random_seed: int | None = None,
) -> np.ndarray:
    if mode == "manual":
        return ensure_square_bool_matrix(read_matrix_manual(n))
    return ensure_square_bool_matrix(random_matrix(n, seed=random_seed))
