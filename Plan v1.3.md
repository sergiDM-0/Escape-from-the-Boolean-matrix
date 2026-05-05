# Plan v1.3 — Estado actual del proyecto (v1.0)

Este documento describe **únicamente** lo que el proyecto hace **en este instante** (la fase actual de código en `v1.0/`). No contempla fases pasadas.

**Enunciado:** [Proyecto_Final_M.D..pdf](Proyecto_Final_M.D..pdf)

---

## Qué hace el proyecto hoy

El proyecto implementa un aplicativo en consola que:

- **Lee o genera** una matriz relacional booleana **n×n**.
  - Entrada manual por teclado con **0/1** (se convierte internamente a `bool`).
  - Generación aleatoria booleana con **semilla opcional**.
- **Muestra la relación \(R\)** en forma de conjunto de pares \((x_i, x_j)\) donde la matriz es verdadera.
- **Evalúa propiedades** de la relación:
  - Reflexiva
  - Irreflexiva
  - Simétrica
  - Asimétrica
  - Antisimétrica
  - Transitiva (usando producto booleano `M @ M` sobre `dtype=bool`)
  - Equivalencia (reflexiva + simétrica + transitiva)
- **Clasifica relaciones de orden** (definiciones habituales):
  - Orden parcial
  - Orden total
  - Orden estricto
- **Genera un grafo dirigido** desde la matriz y lo “presenta en pantalla” mediante un **HTML interactivo** (Plotly), incluyendo **flechas** para dirección.

---

## Restricciones y validaciones actuales

- **n**: se valida como **entero \(n ≥ 1\)** (sin tope fijo).
  - Nota práctica: el límite real es memoria/tiempo, porque la matriz es **O(n²)**.
- **Entrada manual**: cada celda debe ser **0 o 1**; cada fila debe contener exactamente **n** valores.
- **Matriz**: debe ser **cuadrada** para analizar propiedades.

---

## Interfaz (menú en consola)

El programa (`v1.0/main.py`) expone este menú:

- **1)** Mostrar matriz MR (0/1)
- **2)** Mostrar relación R
- **3)** Analizar todas las propiedades y órdenes
- **4)** Consultar una propiedad u orden (una sola)
- **5)** Mostrar grafo dirigido (genera/abre `grafo_dirigido.html`)
- **6)** Ingresar otra matriz
- **0)** Salir

Cuando la transitividad falla, el sistema puede imprimir un **contraejemplo** (un triple \(i,j,k\)) para explicar por qué.

---

## Visualización del grafo dirigido (Plotly)

Archivo: [`v1.0/graph_view.py`](v1.0/graph_view.py)

- Se construye un `DiGraph` a partir de la matriz booleana.
- Se calcula un layout (intenta `spring_layout`; si faltara SciPy, hace fallback a `circular_layout`).
- Se genera un archivo **auto-contenido**:
  - `v1.0/grafo_dirigido.html`
- Se intenta abrir el HTML automáticamente con el navegador; si no se abre, se puede abrir manualmente.
- Las aristas incluyen **punta de flecha** (dirección) usando anotaciones de Plotly.

---

## Estructura del código (módulos actuales)

Código principal (fase actual) en la carpeta [`v1.0/`](v1.0/):

- [`v1.0/main.py`](v1.0/main.py): flujo principal y menú.
- [`v1.0/matrix_io.py`](v1.0/matrix_io.py): lectura/generación/validación de la matriz.
- [`v1.0/relation.py`](v1.0/relation.py): propiedades de relaciones y formato de \(R\).
- [`v1.0/order.py`](v1.0/order.py): orden parcial, total y estricto.
- [`v1.0/graph_view.py`](v1.0/graph_view.py): export HTML interactivo del grafo dirigido.

---

## Dependencias (fase actual)

Archivo: [`v1.0/dependencias`](v1.0/dependencias)

- `numpy` (matrices booleanas y producto booleano)
- `networkx` (estructura de grafo + layout)
- `plotly` (HTML interactivo con flechas)
- `pyinstaller` (empaquetado a ejecutable)

---

## Documentación y manual de uso (README)

Manual principal: [`README.md`](README.md)

Puntos clave del uso hoy:

- Crear y activar una **única** `.venv` en la raíz del repositorio.
- Instalar dependencias desde `v1.0/dependencias`.
- Ejecutar el programa con `python v1.0/main.py` (o `cd v1.0 && python main.py`).
- Para el grafo: abrir `v1.0/grafo_dirigido.html` si el navegador no se abre solo.

---

## Checklist de verificación (fase actual)

- [ ] Corre `python v1.0/main.py` y permite ingresar matriz manual y aleatoria.
- [ ] Opción (2) muestra \(R\) correctamente.
- [ ] Opción (3) lista propiedades y órdenes con Sí/No.
- [ ] Opción (5) genera `v1.0/grafo_dirigido.html` y las aristas muestran **dirección** (flechas).
- [ ] Validaciones: rechaza `n` no entero / `n<1` / filas con longitud distinta / valores distintos de 0/1.

