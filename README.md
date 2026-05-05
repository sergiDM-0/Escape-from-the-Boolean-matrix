# Proyecto final — Matemáticas discretas (relaciones y grafos)

Aplicativo para matrices relacionales **n×n**, análisis de propiedades (reflexiva, simétrica, transitiva, equivalencia, órdenes, etc.) y visualización del **grafo dirigido** asociado. Desarrollo previsto en **Python** según [Plan v1.2.md](Plan%20v1.2.md). Enunciado: [Proyecto_Final_M.D..pdf](Proyecto_Final_M.D..pdf).

---

## Requisitos

- **Python 3.10+** instalado en el sistema.
- Archivo **[v1.0/dependencias](v1.0/dependencias)** (lista para `pip`).

## Instalación

El entorno virtual **`.venv`** debe crearse en la **raíz del repositorio** (no dentro de `v1.0/`):

```bash
cd /ruta/a/Matematicas_Discretas_Final
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r v1.0/dependencias
```

En Windows (PowerShell):

```powershell
cd C:\ruta\a\Matematicas_Discretas_Final
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r v1.0\dependencias
```

## Ejecución (modo desarrollo)

Con la `.venv` activada, desde la raíz del proyecto:

```bash
python v1.0/main.py
```

O bien:

```bash
cd v1.0
python main.py
```

## Uso esperado de la aplicación

1. **Tamaño n:** el programa solicita el número de elementos (orden de la matriz). Debe ser un entero positivo acorde al límite que definas (por ejemplo 1–20 para visualización cómoda).
2. **Modo de matriz:** elegir entre **entrada manual** (teclado, fila a fila o celda a celda con **0** o **1**) o **generación aleatoria** con la misma \(n\).
3. **Validación:** si la matriz no es cuadrada o hay caracteres distintos de 0/1, el programa muestra un mensaje de error y pide corregir sin continuar el análisis incorrectamente.
4. **Relación R:** la aplicación lista los pares \((x_i, x_j)\) para los que la entrada booleana es verdadera (equivalente a los “unos” del enunciado).
5. **Análisis:** desde el menú, ejecutar **todas** las comprobaciones de propiedades o **una** propiedad concreta; se muestra **Sí/No** (y opcionalmente un contraejemplo).
6. **Órdenes:** se indica si la relación es orden parcial, total o estricto según las definiciones documentadas en tu informe académico.
7. **Grafo:** al elegir la opción correspondiente, se genera un HTML interactivo con el **grafo dirigido** (con flechas). Si el navegador no se abre automáticamente, abre manualmente `v1.0/grafo_dirigido.html`.

## Generar ejecutable (entrega)

Con PyInstaller (desde la raíz, con `.venv` activada):

```bash
cd v1.0
pyinstaller --onefile main.py
```

La opción `--windowed` evita consola extra si la UI es solo ventanas; si tu aplicación es **solo consola**, omite `--windowed`. Revisa la carpeta `dist/` para el binario y pruébalo en un equipo **sin** el proyecto ni el IDE.

## Problemas frecuentes

- **`pip` no encuentra `dependencias`:** usa la ruta desde la raíz del repo: `pip install -r v1.0/dependencias`.
- **El grafo no se abre:** abre manualmente `v1.0/grafo_dirigido.html`.
- **Grafo ilegible con n grande:** reduce **n** o usa matriz aleatoria con n moderado (el HTML con muchas aristas se vuelve pesado).

## Documentación técnica

Detalle de **matrices booleanas**, producto booleano, transitividad y referencias: [Plan v1.2.md](Plan%20v1.2.md).

### Referencias útiles

- [Stack Overflow — multiplicación de matrices booleanas en NumPy](https://stackoverflow.com/questions/79106168/best-way-to-calculate-boolean-matrix-multiplication-in-numpy)
- [Notas — cierre transitivo y producto booleano (Waterloo CS466)](https://student.cs.uwaterloo.ca/~cs466/Old_courses/F08/transitiveClosure.pdf)
- [NetworkX — ejemplo dibujo de grafo dirigido](https://networkx.org/documentation/stable/auto_examples/drawing/plot_directed.html)
- [NetworkX — `from_numpy_array`](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_numpy_array.html)
