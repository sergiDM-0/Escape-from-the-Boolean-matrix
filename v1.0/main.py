#!/usr/bin/env python3
"""Proyecto final — relaciones y grafo dirigido (consola)."""

from __future__ import annotations

import sys

import numpy as np

import graph_view
import matrix_io
import matrix_view
import order as order_mod
import relation
import relation_view


def print_matrix(m: np.ndarray) -> None:
    m = np.asarray(m, dtype=bool)
    for row in m:
        print(" ".join("1" if x else "0" for x in row))


def prompt_n() -> int:
    while True:
        try:
            return matrix_io.parse_positive_int(input("Tamaño n de la matriz (entero ≥ 1): "))
        except ValueError as e:
            print(e)


def prompt_mode() -> tuple[str, int | None]:
    print("\nModo de matriz:")
    print("  1) Ingreso manual por teclado (0/1)")
    print("  2) Generación aleatoria")
    while True:
        c = input("Elija 1 o 2: ").strip()
        if c == "1":
            return "manual", None
        if c == "2":
            seed_s = input("Semilla opcional (entero, vacío = aleatorio): ").strip()
            if not seed_s:
                return "random", None
            try:
                return "random", int(seed_s)
            except ValueError:
                print("Semilla inválida; use un entero o deje vacío.")


def load_matrix() -> np.ndarray:
    n = prompt_n()
    mode, seed = prompt_mode()
    if mode == "manual":
        return matrix_io.acquire_matrix("manual", n)
    return matrix_io.acquire_matrix("random", n, random_seed=seed)


def print_all_properties(m: np.ndarray) -> None:
    print("\n--- Propiedades ---")
    print(f"Reflexiva:        {'Sí' if relation.is_reflexive(m) else 'No'}")
    print(f"Irreflexiva:      {'Sí' if relation.is_irreflexive(m) else 'No'}")
    print(f"Simétrica:        {'Sí' if relation.is_symmetric(m) else 'No'}")
    print(f"Asimétrica:       {'Sí' if relation.is_asymmetric(m) else 'No'}")
    print(f"Antisimétrica:    {'Sí' if relation.is_antisymmetric(m) else 'No'}")
    print(f"Transitiva:       {'Sí' if relation.is_transitive(m) else 'No'}")
    ce = relation.transitive_counterexample(m)
    if ce and not relation.is_transitive(m):
        print(f"  ({ce})")
    print(f"Equivalencia:     {'Sí' if relation.is_equivalence(m) else 'No'}")
    print("\n--- Relaciones de orden (definiciones habituales) ---")
    print(f"Orden parcial:    {'Sí' if order_mod.is_partial_order(m) else 'No'}")
    print(f"Orden total:      {'Sí' if order_mod.is_total_order(m) else 'No'}")
    print(f"Orden estricto:   {'Sí' if order_mod.is_strict_order(m) else 'No'}")


def property_menu(m: np.ndarray) -> None:
    opts = [
        ("1", "Reflexiva", relation.is_reflexive),
        ("2", "Irreflexiva", relation.is_irreflexive),
        ("3", "Simétrica", relation.is_symmetric),
        ("4", "Asimétrica", relation.is_asymmetric),
        ("5", "Antisimétrica", relation.is_antisymmetric),
        ("6", "Transitiva", relation.is_transitive),
        ("7", "Equivalencia", relation.is_equivalence),
        ("8", "Orden parcial", order_mod.is_partial_order),
        ("9", "Orden total", order_mod.is_total_order),
        ("10", "Orden estricto", order_mod.is_strict_order),
    ]
    print("\nPropiedad a consultar:")
    for key, name, _ in opts:
        print(f"  {key}) {name}")
    choice = input("Opción: ").strip()
    for key, name, fn in opts:
        if choice == key:
            ok = fn(m)
            print(f"\n{name}: {'Sí' if ok else 'No'}")
            if name == "Transitiva" and not ok:
                ce = relation.transitive_counterexample(m)
                if ce:
                    print(ce)
            return
    print("Opción no reconocida.")


def main_menu(m: np.ndarray) -> str:
    print("\n--- Menú principal ---")
    print("  1) Mostrar matriz MR (0/1)")
    print("  2) Mostrar relación R")
    print("  3) Analizar todas las propiedades y órdenes")
    print("  4) Consultar una propiedad u orden")
    print("  5) Mostrar grafo dirigido (ventana)")
    print("  6) Ingresar otra matriz")
    print("  0) Salir")
    return input("Opción: ").strip()


def run() -> None:
    print("=== Matemáticas discretas — Matriz relacional y grafo ===\n")
    m = load_matrix()
    while True:
        opt = main_menu(m)
        if opt == "0":
            print("Fin.")
            return
        if opt == "1":
            print("\nMatriz MR:")
            print_matrix(m)
            try:
                matrix_view.show_matrix_html(m)
            except Exception as e:  # noqa: BLE001
                print(f"No se pudo mostrar la matriz en HTML: {e}")
        elif opt == "2":
            print("\n" + relation.format_relation_r(m))
            try:
                relation_view.show_relation_html(m)
            except Exception as e:  # noqa: BLE001
                print(f"No se pudo mostrar la relación en HTML: {e}")
        elif opt == "3":
            print_all_properties(m)
        elif opt == "4":
            property_menu(m)
        elif opt == "5":
            try:
                graph_view.show_directed_graph(m)
            except Exception as e:  # noqa: BLE001 — UI/backend varía por SO
                print(f"No se pudo mostrar el grafo: {e}")
        elif opt == "6":
            m = load_matrix()
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nInterrumpido.")
        sys.exit(130)
