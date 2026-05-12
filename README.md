# Proyecto final — Matemáticas discretas (relaciones y grafos)

Aplicativo en **consola (Python 3)** que trabaja con una **matriz relacional** **n×n** (entradas binarias 0/1 al escribir, almacenadas internamente como **booleanos**), analiza **propiedades** de la relación y de **orden**, y genera **vistas en HTML** (matriz, relación **R** y **grafo dirigido** con flechas).

- **Enunciado del curso:** [Proyecto_Final_M.D..pdf](Proyecto_Final_M.D..pdf)  
- **Código:** carpeta [`v1.0/`](v1.0/)  
- **Documentación técnica (lógica, módulos, grafos):** [Plan v1.4.md](Plan%20v1.4.md)  
- **Pruebas QA:** carpeta [`qa/`](qa/)

---

## 1. Qué necesitas instalado

- **Python 3.10 o superior** (recomendado 3.11+).
- Conexión a Internet **la primera vez** que abras los HTML generados por Plotly si usan Plotly desde CDN (según cómo se exporte la figura).

---

## 2. Estructura útil del repositorio

| Ruta | Contenido |
|------|-----------|
| [`v1.0/main.py`](v1.0/main.py) | Programa principal: menú y flujo |
| [`v1.0/matrix_io.py`](v1.0/matrix_io.py) | Entrada de **n**, matriz manual o aleatoria |
| [`v1.0/relation.py`](v1.0/relation.py) | Propiedades de **R** y formato del conjunto |
| [`v1.0/order.py`](v1.0/order.py) | Orden parcial, total, estricto |
| [`v1.0/matrix_view.py`](v1.0/matrix_view.py) | HTML de la matriz |
| [`v1.0/relation_view.py`](v1.0/relation_view.py) | HTML de la relación |
| [`v1.0/graph_view.py`](v1.0/graph_view.py) | HTML del grafo dirigido |
| [`v1.0/html_export.py`](v1.0/html_export.py) | Guardar/abrir HTML auxiliar |
| [`v1.0/dependencias`](v1.0/dependencias) | Lista para `pip install -r` |
| [`v1.0/README.md`](v1.0/README.md) | Resumen corto de ejecución desde la carpeta `v1.0/` |
| [`qa/TEST_PLAN.md`](qa/TEST_PLAN.md) | Plan de QA: riesgos, casos manuales y comprobaciones recomendadas |
| [`LICENSE`](LICENSE) | Licencia del repositorio |

Los archivos **`matriz_relacional.html`**, **`relacion_R.html`** y **`grafo_dirigido.html`** se crean o sobrescriben dentro de **`v1.0/`** cuando usas las opciones correspondientes del menú.

En la raíz existen además borradores o versiones anteriores del plan técnico (`Plan v1.0.md` … `Plan v1.3.md`); la referencia canónica para la implementación actual es **[Plan v1.4.md](Plan%20v1.4.md)**.

---

## 3. Instalación (entorno virtual en la raíz del proyecto)

El entorno **`.venv`** debe estar en la carpeta **`Matematicas_Discretas_Final`** (no dentro de `v1.0/`).

### macOS / Linux

```bash
cd /ruta/completa/a/Matematicas_Discretas_Final
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r v1.0/dependencias
```

### Windows (PowerShell)

```powershell
cd C:\ruta\completa\a\Matematicas_Discretas_Final
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r v1.0\dependencias
```

Si `pip` no encuentra el archivo, comprueba que estás en la **raíz** del repo y que la ruta sea exactamente `v1.0/dependencias`.

---

## 4. Cómo ejecutar el programa

Con la `.venv` **activada**:

**Opción A — desde la raíz del repo (recomendado):**

```bash
python v1.0/main.py
```

**Opción B — entrando a la carpeta:**

```bash
cd v1.0
python main.py
```

Para salir en cualquier momento puedes usar **Ctrl+C** (interrupción); el programa termina con código de salida adecuado.

---

## 5. Qué ocurre al iniciar (antes del menú principal)

Al arrancar verás un título y luego, en orden:

### 5.1 Tamaño **n** de la matriz

Pregunta:

`Tamaño n de la matriz (entero ≥ 1):`

- Debes introducir un **entero mayor o igual que 1**.
- **No** hay un máximo fijo en el código: en la práctica te limita la **memoria** (la matriz ocupa orden **n²**) y el tiempo al usar modo manual o al generar HTML con muchas aristas.

**Entradas rechazadas** (el programa muestra un mensaje y vuelve a preguntar):

- Vacío o solo espacios  
- Texto que no sea un entero (ej. `abc`)  
- Decimales (ej. `3.5`)  
- Cero o negativos (ej. `0`, `-2`)

### 5.2 Modo de obtención de la matriz

Se muestra:

```
Modo de matriz:
  1) Ingreso manual por teclado (0/1)
  2) Generación aleatoria
Elija 1 o 2:
```

- **`1`**: entrada manual **celda por celda** (ver sección 6).
- **`2`**: matriz **aleatoria** booleana.

Si eliges **`2`**, aparece:

`Semilla opcional (entero, vacío = aleatorio):`

- **Enter vacío**: cada ejecución puede dar otra matriz.  
- **Un entero**: se usa como semilla del generador `random` de Python para poder **repetir** la misma matriz aleatoria en otra corrida (útil para depurar o demostrar).

Cuando termina la carga, entras al **menú principal** con la matriz ya guardada en memoria.

---

## 6. Entrada manual (opción 1 del modo matriz)

El programa pide **exactamente n×n valores**, uno por uno, en orden de filas: primero la fila 1 (todas las columnas), luego la fila 2, etc.

Para cada celda verás un mensaje como:

`Valor en posición (fila i, columna j) [faltan k]:`

- **`i`, `j`**: números **1-based** (como en álgebra elemental): fila 1 es la primera fila, columna 1 la primera columna.
- **`k`**: cuántas celdas **quedan por llenar en total** en ese momento (incluye la celda actual).

Solo se aceptan los caracteres **`0`** o **`1`** (sin comillas).  
Si escribes otra cosa (`2`, `x`, vacío…), verás:

`Solo se permiten 0 y 1 en cada celda.`  

y **se repite la misma celda** hasta que sea válido.

### 6.1 Pregunta de ayuda después del **segundo** valor

Cuando ya ingresaste **dos** celdas **y** la matriz tiene más de **una** celda en total (es decir, si **n×n > 2**), aparece exactamente esta pregunta:

`si se canso puedo completarlo por usted y que sera y o n:`

- Respuesta **`y`** (minúscula, tras `.lower()`): el programa **rellena al azar** todas las celdas que **aún faltan** y termina la entrada manual. Las dos primeras celdas que ya escribiste **no** se cambian.
- Cualquier otra respuesta (por ejemplo **`n`**, texto distinto): **no** hay autocompletado; sigues introduciendo celda por celda hasta completar **n×n**.

### 6.2 Casos límite del modo manual

- **`n = 1`**: solo una celda; **no** se hace la pregunta de ayuda (porque no aplica “después del segundo valor” con más celdas pendientes en la misma lógica).
- **`n = 2`**: hay 4 celdas; la pregunta de ayuda aparece **después de la segunda celda** si aún faltan más por llenar.

---

## 7. Menú principal (después de cargar la matriz)

```
--- Menú principal ---
  1) Mostrar matriz MR (0/1)
  2) Mostrar relación R
  3) Analizar todas las propiedades y órdenes
  4) Consultar una propiedad u orden
  5) Mostrar grafo dirigido (ventana)
  6) Ingresar otra matriz
  0) Salir
Opción:
```

### Opción **1** — Mostrar matriz MR

- Imprime en **consola** la matriz en 0/1 (filas separadas por salto de línea, columnas por espacio).
- Genera o sobrescribe **`v1.0/matriz_relacional.html`**: tabla con encabezados de filas/columnas (`x_1`, …, `x_n`) y colores.
- Intenta abrir el archivo en el **navegador**. Si no se abre, ábrelo manualmente desde `v1.0/matriz_relacional.html`.

Si algo falla al generar el HTML, verás un mensaje que empieza por `No se pudo mostrar la matriz en HTML:`.

### Opción **2** — Mostrar relación R

- Imprime en consola algo del estilo `R = { (x_i, x_j), ... }` o `R = ∅` si no hay unos.
- Genera o sobrescribe **`v1.0/relacion_R.html`** (tabla de pares o página simple si **R** está vacío).
- Intenta abrir el navegador; si no, abre el HTML a mano.

### Opción **3** — Todas las propiedades y órdenes

Lista en consola, con **Sí** o **No**:

**Propiedades:** reflexiva, irreflexiva, simétrica, asimétrica, antisimétrica, transitiva, equivalencia.

Si **no** es transitiva, puede mostrarse una línea extra con un **contraejemplo** (tres elementos que rompen la transitividad).

**Órdenes (definiciones habituales programadas):**

- **Orden parcial:** reflexiva **y** antisimétrica **y** transitiva.  
- **Orden total:** orden parcial **y**, para todo **i≠j**, al menos uno de **M[i,j]** o **M[j,i]** es verdadero (comparabilidad).  
- **Orden estricto:** irreflexiva **y** asimétrica **y** transitiva.

*(Si tu curso define “orden total/estricto” distinto, documenta la definición en tu informe académico y compárala con el código en [`v1.0/order.py`](v1.0/order.py).)*

### Opción **4** — Una propiedad u orden

Submenú numérico del 1 al 10. Eliges una sola comprobación y obtienes **Sí/No**. Para transitividad fallida puede imprimirse el mismo tipo de contraejemplo que en la opción 3.

### Opción **5** — Grafo dirigido

- Construye el **digrafo**: hay arista **de i a j** si **MR[i,j]** es verdadero (equivalente a 1 en la matriz impresa).
- Escribe **`v1.0/grafo_dirigido.html`** (Plotly: nodos, segmentos y **flechas** por arista).
- Intenta abrir el navegador.

El texto del menú puede decir **“(ventana)”** por costumbre; en la práctica la salida es un archivo **HTML** que se abre en el **navegador**. Si no se abre solo, abre `v1.0/grafo_dirigido.html` manualmente.

Con **n** o muchas aristas, el archivo puede ser **grande** y el navegador más lento.

### Opción **6** — Otra matriz

Repite todo el flujo inicial: pregunta **n**, modo manual o aleatorio, y sustituye la matriz en memoria.

### Opción **0** — Salir

Termina el programa (`Fin.`).

### Opción no reconocida

Si escribes algo que no sea `0`–`6`, verás `Opción no válida.` y el menú se muestra de nuevo.

---

## 8. Archivos HTML que el programa genera

Todos quedan en **`v1.0/`**:

| Archivo | Cuándo se genera |
|---------|------------------|
| `matriz_relacional.html` | Opción menú **1** |
| `relacion_R.html` | Opción menú **2** |
| `grafo_dirigido.html` | Opción menú **5** |

Cada vez que repites la opción, el archivo se **sobrescribe** con la vista de la matriz actual en memoria.

---

## 9. Cómo interpretar la matriz y la relación R

Se numeran elementos **x₁, x₂, …, xₙ**.

- **MR[i,j] = 1** (o `True` internamente) significa **xᵢ R xⱼ** (el par ordenado pertenece a **R**).
- La diagonal **MR[i,i]** indica si **xᵢ R xᵢ** (reflexividad en ese elemento).

---

## 10. Pruebas automatizadas (QA)

En la carpeta [`qa/`](qa/):

| Script | Propósito |
|--------|-----------|
| [`qa/smoke_tests.py`](qa/smoke_tests.py) | Comprobaciones básicas de propiedades y entrada manual simulada |
| [`qa/phase2_tests.py`](qa/phase2_tests.py) | Entradas inválidas, autocompletado, generación de HTML |

Para criterios de aceptación, riesgos y **pruebas manuales** recomendadas, consulta además [`qa/TEST_PLAN.md`](qa/TEST_PLAN.md).

Ejecución (raíz del repo, con `.venv` activada):

```bash
python qa/smoke_tests.py
python qa/phase2_tests.py
```

---

## 11. Empaquetado con PyInstaller (entrega tipo ejecutable)

Desde la raíz, con `.venv` activada:

```bash
cd v1.0
pyinstaller --onefile main.py
```

El ejecutable suele quedar en `v1.0/dist/`. **Prueba el binario en una máquina sin el proyecto**. Si Plotly no embebiera bien los recursos, puede hacer falta algo como `--collect-all plotly` (consulta la documentación actual de PyInstaller para tu versión).

Este repositorio **no** incluye el ejecutable ya construido; debes generarlo antes de la entrega si la asignatura lo exige.

---

## 12. Problemas frecuentes

- **`pip install -r` falla:** revisa que estés en la raíz del repo y uses `v1.0/dependencias`.  
- **Los HTML no se abren solos:** ábrelos manualmente desde `v1.0/` con doble clic o “Abrir con navegador”.  
- **Error `No module named 'scipy'` al graficar:** el código intenta `spring_layout`; si falta SciPy, usa `circular_layout` como respaldo (ver [`v1.0/graph_view.py`](v1.0/graph_view.py)).  
- **Grafo lento o HTML enorme:** reduce **n** o usa matrices más dispersas.  
- **Matriz manual muy larga:** usa opción aleatoria o la pregunta de completado con **`y`** tras dos valores.

---

## 13. Documentación técnica detallada

Para **cómo están implementadas** las funciones, el producto booleano, la transitividad y el pipeline del grafo Plotly, lee **[Plan v1.4.md](Plan%20v1.4.md)**.

### Inventario técnico (todo lo que interviene en el código)

| Área | Qué se usa | Dónde (principalmente) |
|------|-------------|-------------------------|
| **Python 3** | Sintaxis, consola, `if`/`for`/`while`, f-strings, `try`/`except`/`finally` | Todo `v1.0/*.py`, `qa/*.py` |
| **`from __future__ import annotations`** | Anotaciones de tipos pospuestas | Todos los `.py` del proyecto |
| **`pathlib.Path`** | Rutas a HTML, `unlink`, `write_text`, `exists`, `resolve`, `parent`, `as_uri` | [`v1.0/main.py`](v1.0/main.py), [`v1.0/html_export.py`](v1.0/html_export.py), [`v1.0/graph_view.py`](v1.0/graph_view.py), [`qa/phase2_tests.py`](qa/phase2_tests.py) |
| **`sys`** | `sys.path.insert`, `sys.exit(130)` tras `KeyboardInterrupt` | [`v1.0/main.py`](v1.0/main.py), `qa/*.py` |
| **`builtins.input` / `print`** | Menú, prompts, matriz manual | [`v1.0/main.py`](v1.0/main.py), [`v1.0/matrix_io.py`](v1.0/matrix_io.py) |
| **`random`** | `seed`, `choice` (matriz aleatoria y autocompletado) | [`v1.0/matrix_io.py`](v1.0/matrix_io.py) |
| **`typing.Literal`** | Modo de matriz acotado a cadenas `"manual"` o `"random"` en `acquire_matrix` | [`v1.0/matrix_io.py`](v1.0/matrix_io.py) |
| **`Exception` / `ValueError` / `KeyboardInterrupt` / `ModuleNotFoundError`** | Validación de entrada, salida limpia; en el grafo, ausencia opcional de SciPy (`graph_view`) | [`v1.0/main.py`](v1.0/main.py), [`v1.0/matrix_io.py`](v1.0/matrix_io.py), [`v1.0/graph_view.py`](v1.0/graph_view.py) |
| **`webbrowser`** | Abrir HTML en el navegador (`open`, `as_uri`) | [`v1.0/html_export.py`](v1.0/html_export.py), [`v1.0/graph_view.py`](v1.0/graph_view.py); parche en pruebas |
| **Pruebas (stdlib)** | `io.StringIO`, `contextlib.redirect_stdout`, `os.environ.setdefault`, sustitución de `builtins.input` | [`qa/phase2_tests.py`](qa/phase2_tests.py), [`qa/smoke_tests.py`](qa/smoke_tests.py) |
| **HTML estático** | `<!doctype html>`, `<meta charset="utf-8">`, CSS en línea (relación vacía **R = ∅**) | [`v1.0/relation_view.py`](v1.0/relation_view.py) |
| **NumPy** | `ndarray` `dtype=bool`, `zeros`, `eye`, `asarray`, `diag`, transpuesta `.T`, operadores booleanos elemento a elemento (`&`, OR con barra vertical de Python, `~`), `all`, `any`, `matmul`, `astype`, `hypot`, `sqrt`, `shape` | [`v1.0/relation.py`](v1.0/relation.py), [`v1.0/matrix_io.py`](v1.0/matrix_io.py), [`v1.0/order.py`](v1.0/order.py), vistas, `main`, `qa` |
| **NetworkX** | `DiGraph`, `from_numpy_array`, `.edges()`, `spring_layout`, `circular_layout` | [`v1.0/graph_view.py`](v1.0/graph_view.py) |
| **Plotly** | `graph_objects.Figure`, `Table`, `Scatter`, `to_html(full_html=..., include_plotlyjs="cdn")`, `write_html`, `update_layout`, anotaciones con `showarrow` | [`v1.0/matrix_view.py`](v1.0/matrix_view.py), [`v1.0/relation_view.py`](v1.0/relation_view.py), [`v1.0/graph_view.py`](v1.0/graph_view.py) |
| **SciPy** | *No* está en `dependencias`; solo aparece si NetworkX intenta usarlo en `spring_layout` | [`v1.0/graph_view.py`](v1.0/graph_view.py) |
| **PyInstaller** | Empaquetado opcional del ejecutable | README §11, [`v1.0/dependencias`](v1.0/dependencias) |
| **Matemática (lógica en código)** | Matriz relacional 0/1, propiedades de **R**, producto booleano **M²**, orden parcial/total/estricto, digrafo desde MR | [`v1.0/relation.py`](v1.0/relation.py), [`v1.0/order.py`](v1.0/order.py) |
| **Enunciado y plan (repo)** | PDF del curso; documentación de implementación | [`Proyecto_Final_M.D..pdf`](Proyecto_Final_M.D..pdf), [`Plan v1.4.md`](Plan%20v1.4.md) |
| **Scripts QA** | Comprobaciones manuales con `assert` (sin framework de test externo) | [`qa/smoke_tests.py`](qa/smoke_tests.py), [`qa/phase2_tests.py`](qa/phase2_tests.py) |

Los paquetes declarados en [`v1.0/dependencias`](v1.0/dependencias) son: **numpy**, **networkx**, **plotly**, **pyinstaller** (con rangos de versión allí indicados).

### API por archivo (funciones y puntos de entrada)

Listado de **def** a nivel de módulo en `v1.0/` y en `qa/`, en el orden en que suelen leerse los módulos. No hay `__all__`: en Python todo lo de nivel superior es importable; lo marcado como “interno” en QA es por convención de nombre (`_`).

#### [`v1.0/main.py`](v1.0/main.py)

| Función | Rol breve |
|---------|-----------|
| `cleanup_generated_html()` | Borra los tres HTML generados en la carpeta del script al salir o al interrumpir. |
| `print_matrix(m)` | Imprime la matriz en consola como `0`/`1` separados por espacios. |
| `prompt_n()` | Bucle hasta obtener un entero **n** ≥ 1 válido (`matrix_io.parse_positive_int`). |
| `prompt_mode()` | Devuelve `("manual", None)` o `("random", semilla_o_None)` según menú 1/2. |
| `load_matrix()` | Pide **n** y modo, devuelve `np.ndarray` bool cuadrado (`matrix_io.acquire_matrix`). |
| `print_all_properties(m)` | Opción menú 3: propiedades de **R**, equivalencia y órdenes. |
| `property_menu(m)` | Opción menú 4: submenú de una sola propiedad u orden. |
| `main_menu(m)` | Muestra menú principal y devuelve la cadena de opción. |
| `run()` | Bucle del programa: menú, ramas 0–6, limpieza HTML en `finally`. |

**Punto de entrada:** `if __name__ == "__main__"` llama a `run()`; ante `KeyboardInterrupt` imprime mensaje, ejecuta `cleanup_generated_html()` y `sys.exit(130)`.

#### [`v1.0/matrix_io.py`](v1.0/matrix_io.py)

| Función | Rol breve |
|---------|-----------|
| `parse_positive_int(text)` | Valida texto → entero ≥ 1 o `ValueError`. |
| `ensure_square_bool_matrix(m)` | Comprueba matriz 2D cuadrada; devuelve copia `bool` o `ValueError`. |
| `row_from_tokens(tokens)` | Convierte una lista de tokens `0`/`1` en un `ndarray` bool de forma `(1, n)` (helper del módulo; el flujo manual actual no la llama). |
| `read_matrix_manual(n)` | Entrada celda a celda, mensaje de ayuda tras la segunda celda si aplica. |
| `random_matrix(n, *, seed=None)` | Matriz **n×n** aleatoria `bool`; opcionalmente fija `random.seed`. |
| `acquire_matrix(mode, n, *, random_seed=None)` | `mode` ∈ `Literal["manual","random"]`; devuelve matriz cuadrada bool validada. |

#### [`v1.0/relation.py`](v1.0/relation.py)

| Función | Rol breve |
|---------|-----------|
| `node_label(i)` | Índice 0-based → cadena `x_{i+1}` (subíndice en consola como `x_1`, etc.). |
| `pairs_from_matrix(m)` | Lista de pares `(x_i, x_j)` donde `m[i,j]` es verdadero. |
| `format_relation_r(m)` | Cadena `R = { ... }` o `R = ∅`. |
| `is_reflexive(m)` | Diagonal toda verdadera. |
| `is_irreflexive(m)` | Diagonal toda falsa. |
| `is_symmetric(m)` | **M** igual a **M** transpuesta. |
| `is_asymmetric(m)` | Ningún par simétrico fuera de la diagonal; implica irreflexiva. |
| `is_antisymmetric(m)` | No hay **i≠j** con **M[i,j]** y **M[j,i]** simultáneos. |
| `boolean_square(m)` | Producto booleano **M∘M** vía `np.matmul(m, m)`. |
| `is_transitive(m)` | **M²** implica **M** entrada a entrada. |
| `is_equivalence(m)` | Reflexiva ∧ simétrica ∧ transitiva. |
| `transitive_counterexample(m)` | Primer contraejemplo textual para transitividad, o `None`. |

#### [`v1.0/order.py`](v1.0/order.py)

| Función | Rol breve |
|---------|-----------|
| `is_partial_order(m)` | Reflexiva ∧ antisimétrica ∧ transitiva. |
| `is_total_order(m)` | Orden parcial ∧ comparabilidad para todo **i≠j**. |
| `is_strict_order(m)` | Irreflexiva ∧ asimétrica ∧ transitiva. |

#### [`v1.0/html_export.py`](v1.0/html_export.py)

| Función | Rol breve |
|---------|-----------|
| `write_and_open_html(*, filename, html)` | Escribe UTF-8 en `v1.0/<filename>`, intenta `webbrowser.open`, devuelve `Path`. |

#### [`v1.0/matrix_view.py`](v1.0/matrix_view.py)

| Función | Rol breve |
|---------|-----------|
| `show_matrix_html(m)` | `go.Table` + `to_html(..., include_plotlyjs="cdn")` → `matriz_relacional.html`. |

#### [`v1.0/relation_view.py`](v1.0/relation_view.py)

| Función | Rol breve |
|---------|-----------|
| `show_relation_html(m)` | Si **R** vacío, HTML estático; si no, `go.Table` → `relacion_R.html`. |

#### [`v1.0/graph_view.py`](v1.0/graph_view.py)

| Función | Rol breve |
|---------|-----------|
| `show_directed_graph(m)` | Digrafo con NetworkX + trazas Plotly + anotaciones con flechas → `grafo_dirigido.html` (`write_html` + intento de abrir navegador). |

#### [`qa/smoke_tests.py`](qa/smoke_tests.py)

| Símbolo | Rol breve |
|---------|-----------|
| `test_core_properties()` | Matrices fijas: equivalencia, transitividad, orden estricto, etc. |
| `test_manual_entry_cell_by_cell()` | Simula `input` para matriz manual 2×2. |
| `test_manual_entry_assisted_complete()` | Simula autocompletado con respuesta `y` en 3×3. |
| `main()` | Ejecuta las pruebas anteriores e imprime éxito. |

**Punto de entrada:** `if __name__ == "__main__"` → `main()`.

#### [`qa/phase2_tests.py`](qa/phase2_tests.py)

| Símbolo | Rol breve |
|---------|-----------|
| `ROOT`, `V1` | Rutas absolutas a la raíz del repo y a `v1.0/` (para comprobar existencia de HTML). |
| `_fake_inputs(seq)` | Fábrica de `input` que devuelve valores de `seq` en orden (uso interno del test). |
| `test_parse_positive_int_invalids()` | Entradas inválidas a `parse_positive_int`. |
| `test_manual_cell_reprompts_on_invalid_cell()` | Reintentos de celda + pregunta de ayuda `n`. |
| `test_manual_assist_answer_other_than_y_keeps_asking()` | Respuesta distinta de `y` tras la ayuda. |
| `test_html_generation_creates_files()` | Genera los tres HTML con `webbrowser.open` mockeado. |
| `main()` | Fija `PYTHONIOENCODING` si hace falta y lanza todas las pruebas. |

**Punto de entrada:** `if __name__ == "__main__"` → `main()`.

---

### Referencias útiles (implementación, matrices booleanas y apoyo)

#### Matrices booleanas, producto booleano y transitividad

- [Wikipedia — matriz lógica / booleana (*logical matrix*)](https://en.wikipedia.org/wiki/Logical_matrix) (enlace con la idea de matriz 0/1 y composición de relaciones).  
- [Wikipedia — matriz de adyacencia (incluye grafos dirigidos)](https://en.wikipedia.org/wiki/Adjacency_matrix) (MR como matriz de un digrafo).  
- [Stack Overflow — multiplicación booleana en NumPy](https://stackoverflow.com/questions/79106168/best-way-to-calculate-boolean-matrix-multiplication-in-numpy) (relacionado con `np.matmul` sobre `bool` en [`v1.0/relation.py`](v1.0/relation.py)).  
- [Waterloo — transitividad y cierre transitivo / producto booleano (PDF)](https://student.cs.uwaterloo.ca/~cs466/Old_courses/F08/transitiveClosure.pdf)  
- [NumPy — `matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) y [tipos escalares / booleanos](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool).  
- [NumPy — indexación y formas de array](https://numpy.org/doc/stable/user/basics.indexing.html) (filas/columnas 0-based en código vs etiquetas **x₁…xₙ** en salida).

#### Biblioteca estándar de Python (lo que importa el proyecto)

- [`pathlib`](https://docs.python.org/3/library/pathlib.html) · [`sys`](https://docs.python.org/3/library/sys.html) · [`random`](https://docs.python.org/3/library/random.html) · [`typing.Literal`](https://docs.python.org/3/library/typing.html#typing.Literal) · [`webbrowser`](https://docs.python.org/3/library/webbrowser.html) · [`builtins`](https://docs.python.org/3/library/builtins.html) (sustitución de `input` en pruebas) · [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO) · [`contextlib.redirect_stdout`](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout) · [`os.environ`](https://docs.python.org/3/library/os.html#os.environ) · [Excepciones integradas](https://docs.python.org/3/library/exceptions.html) (`ValueError`, `KeyboardInterrupt`, `ModuleNotFoundError`).  
- [PEP 563 — *Postponed Evaluation of Annotations*](https://peps.python.org/pep-0563/) (`from __future__ import annotations`).  
- [**Entorno virtual `venv`**](https://docs.python.org/3/library/venv.html) y [**pip (guía de usuario)**](https://pip.pypa.io/en/stable/user_guide/) — alineados con las secciones 3–4 de este README (no son `import` en el código, pero sí herramientas usadas para ejecutar el proyecto).

#### NetworkX, grafos dirigidos y layouts

- [`networkx.from_numpy_array`](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_numpy_array.html) · [`DiGraph`](https://networkx.org/documentation/stable/reference/classes/digraph.html) · [Dibujo — `spring_layout`, `circular_layout`](https://networkx.org/documentation/stable/reference/drawing.html) (uso en [`v1.0/graph_view.py`](v1.0/graph_view.py)).

#### Plotly y HTML generado

- [Plotly Python — `graph_objects`](https://plotly.com/python/graph-objects/) · [Tablas (`go.Table`)](https://plotly.com/python/table/) · [`Figure.to_html`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_html) (incluye `include_plotlyjs="cdn"` en tablas) · [`Figure.write_html`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.write_html) (grafo).  
- [Anotaciones y flechas](https://plotly.com/python/text-and-annotations/) (`showarrow`, cabeza de flecha en aristas).  
- [MDN — HTML básico y `meta charset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides) (referencia para el HTML manual de [`v1.0/relation_view.py`](v1.0/relation_view.py)).

#### SciPy (opcional, solo si NetworkX lo pide)

- [SciPy — documentación](https://docs.scipy.org/doc/scipy/) (instalación opcional para algunos caminos de `spring_layout`).  
- [Foro Scientific Python](https://discuss.scientific-python.org/).

#### PyInstaller

- [Manual de PyInstaller](https://pyinstaller.org/en/stable/) (sección 11 del README; flags como `--collect-all plotly`).

#### Teoría: relaciones, órdenes y grafos

- [**Mathematics Stack Exchange — relaciones**](https://math.stackexchange.com/questions/tagged/relations) · [**grafos**](https://math.stackexchange.com/questions/tagged/graph-theory) · [**relaciones de orden**](https://math.stackexchange.com/questions/tagged/order-theory) (definiciones y contraejemplos).  
- [Wikipedia — relación binaria](https://en.wikipedia.org/wiki/Binary_relation) (reflexiva, simétrica, transitiva, etc.).  
- [Wikipedia — orden parcial](https://en.wikipedia.org/wiki/Partially_ordered_set) (contrastar con [`v1.0/order.py`](v1.0/order.py)).

#### Foros y comunidades (preguntas concretas, errores de entorno, versiones)

- [**Discuss Python**](https://discuss.python.org/) — `venv`, `pip`, versiones de Python.  
- [**Stack Overflow — `python`**](https://stackoverflow.com/questions/tagged/python) — consola, `pathlib`, `webbrowser`, `random`.  
- [**Stack Overflow — `numpy`**](https://stackoverflow.com/questions/tagged/numpy) — matrices `bool`, `matmul`, indexación.  
- [**Stack Overflow — búsqueda «numpy boolean matrix»**](https://stackoverflow.com/search?q=numpy+boolean+matrix) — producto booleano, máscaras y tipos.  
- [**Stack Overflow — `networkx`**](https://stackoverflow.com/questions/tagged/networkx) — digrafos, adyacencia, layouts, *“No module named scipy”*.  
- [**Discusiones NetworkX (GitHub)**](https://github.com/networkx/networkx/discussions).  
- [**Comunidad Plotly (Python)**](https://community.plotly.com/c/python/6) — HTML, tablas, flechas, rendimiento.  
- [**Discusiones PyInstaller (GitHub)**](https://github.com/pyinstaller/pyinstaller/discussions).
