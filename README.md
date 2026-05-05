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

Los archivos **`matriz_relacional.html`**, **`relacion_R.html`** y **`grafo_dirigido.html`** se crean o sobrescriben dentro de **`v1.0/`** cuando usas las opciones correspondientes del menú.

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

### Referencias útiles (implementación)

- [Stack Overflow — multiplicación booleana en NumPy](https://stackoverflow.com/questions/79106168/best-way-to-calculate-boolean-matrix-multiplication-in-numpy)  
- [Waterloo — transitividad y producto booleano (PDF)](https://student.cs.uwaterloo.ca/~cs466/Old_courses/F08/transitiveClosure.pdf)  
- [NetworkX — `from_numpy_array`](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_numpy_array.html)  
- [Plotly — Python](https://plotly.com/python/)
