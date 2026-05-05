"""Entrada y validación de la matriz relacional (booleana internamente)."""

from __future__ import annotations

import random
from typing import Literal

import numpy as np

def parse_positive_int(text: str) -> int:
    text = text.strip()
    if not text:
        raise ValueError("Entrada vacía.")
    try:
        n = int(text)
    except ValueError as exc:
        raise ValueError("Debe ser un número entero.") from exc
    if n < 1:
        raise ValueError("n debe ser al menos 1.")
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
    print(f"Ingrese la matriz {n}×{n} celda por celda (solo 0 o 1).")
    print("Se pedirá cada posición (fila, columna).")

    m = np.zeros((n, n), dtype=bool)
    total = n * n
    filled = 0
    asked_assist = False

    for i in range(n):
        for j in range(n):
            remaining = total - filled
            prompt = f"Valor en posición (fila {i + 1}, columna {j + 1}) [faltan {remaining}]: "

            while True:
                raw = input(prompt).strip()
                if raw not in ("0", "1"):
                    print("Solo se permiten 0 y 1 en cada celda.")
                    continue
                m[i, j] = raw == "1"
                filled += 1
                break

            if filled == 2 and not asked_assist and total > 2:
                asked_assist = True
                ans = input("si se canso puedo completarlo por usted y que sera y o n: ").strip().lower()
                if ans == "y":
                    for ii in range(i, n):
                        jj_start = j + 1 if ii == i else 0
                        for jj in range(jj_start, n):
                            m[ii, jj] = random.choice((False, True))
                    return m

    return m


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
