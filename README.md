# Proyecto final — Matemáticas discretas (relaciones y grafos)

Aplicativo para matrices relacionales **n×n**, análisis de propiedades (reflexiva, simétrica, transitiva, equivalencia, órdenes, etc.) y visualización del **grafo dirigido** asociado. Desarrollo previsto en **Python** según [Plan v1.2.md](Plan%20v1.2.md). Enunciado: [Proyecto_Final_M.D..pdf](Proyecto_Final_M.D..pdf).

---

## Requisitos

- **Python 3.10+** instalado en el sistema.
- Archivo **[dependencias](dependencias)** en la raíz del proyecto (lista para `pip`).

## Instalación

En la carpeta del proyecto (recomendado usar entorno virtual):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r dependencias
```

En Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r dependencias
```

## Ejecución (modo desarrollo)

Desde la raíz del proyecto, cuando exista el punto de entrada:

```bash
python main.py
```

(Sustituir `main.py` por el nombre real del archivo principal si difiere.)

## Uso esperado de la aplicación

1. **Tamaño n:** el programa solicita el número de elementos (orden de la matriz). Debe ser un entero positivo acorde al límite que definas (por ejemplo 1–20 para visualización cómoda).
2. **Modo de matriz:** elegir entre **entrada manual** (teclado, fila a fila o celda a celda con **0** o **1**) o **generación aleatoria** con la misma \(n\).
3. **Validación:** si la matriz no es cuadrada o hay caracteres distintos de 0/1, el programa muestra un mensaje de error y pide corregir sin continuar el análisis incorrectamente.
4. **Relación R:** la aplicación lista los pares \((x_i, x_j)\) para los que la entrada booleana es verdadera (equivalente a los “unos” del enunciado).
5. **Análisis:** desde el menú, ejecutar **todas** las comprobaciones de propiedades o **una** propiedad concreta; se muestra **Sí/No** (y opcionalmente un contraejemplo).
6. **Órdenes:** se indica si la relación es orden parcial, total o estricto según las definiciones documentadas en tu informe académico.
7. **Grafo:** al elegir la opción correspondiente, se abre una ventana con el **grafo dirigido**: un nodo por elemento; una flecha de \(i\) a \(j\) si hay **True** en \((i,j)\). Cierra la ventana para volver al menú.

## Generar ejecutable (entrega)

Con PyInstaller (ajusta el nombre del script principal):

```bash
pyinstaller --onefile --windowed main.py
```

La opción `--windowed` evita consola extra si la UI es solo ventanas; si tu aplicación es **solo consola**, omite `--windowed`. Revisa la carpeta `dist/` para el binario y pruébalo en un equipo **sin** el proyecto ni el IDE.

## Problemas frecuentes

- **`pip` no encuentra `dependencias`:** ejecuta el comando desde la carpeta donde está el archivo `dependencias` o usa la ruta completa: `pip install -r /ruta/al/proyecto/dependencias`.
- **Matplotlib no muestra ventana:** en algunos Linux hace falta backend; si ocurre, consulta la documentación de Matplotlib para tu sistema o guarda figura a archivo (`savefig`) como alternativa temporal.
- **Grafo ilegible con n grande:** reduce **n** o amplía figura (`figsize`) y prueba otro layout (`spring_layout`, `kamada_kawai_layout`).

## Documentación técnica

Detalle de **matrices booleanas**, producto booleano, transitividad y referencias: [Plan v1.2.md](Plan%20v1.2.md).

### Referencias útiles

- [Stack Overflow — multiplicación de matrices booleanas en NumPy](https://stackoverflow.com/questions/79106168/best-way-to-calculate-boolean-matrix-multiplication-in-numpy)
- [Notas — cierre transitivo y producto booleano (Waterloo CS466)](https://student.cs.uwaterloo.ca/~cs466/Old_courses/F08/transitiveClosure.pdf)
- [NetworkX — ejemplo dibujo de grafo dirigido](https://networkx.org/documentation/stable/auto_examples/drawing/plot_directed.html)
- [NetworkX — `from_numpy_array`](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_numpy_array.html)
