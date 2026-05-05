# Plan v1.2 — Proyecto final Matemáticas Discretas (Relaciones y grafos)

**Versión:** 1.2 (actualizado en este mismo documento; **no** se modifica [Plan v1.0.md](Plan%20v1.0.md))  
**Cambios respecto a v1.0:** Lenguaje fijado en **Python 3**; archivo de dependencias para `pip`; sección de **matrices booleanas**; referencias Web; manual al final.  
**Actualizaciones en v1.2 (stack):** visualización del grafo con **Plotly** (no Matplotlib); **sin cota superior fija** para el orden **n** de la matriz (solo entero **n ≥ 1**; el límite real es memoria **O(n²)** y rendimiento al dibujar o al ingresar datos a mano).

**Fuente de requisitos:** [Proyecto_Final_M.D..pdf](Proyecto_Final_M.D..pdf) (UNIVERSIDAD ECCI).

---

## Lista de trabajo (checklist)

- Crear entorno virtual Python 3.10+ e instalar: `pip install -r dependencias`
- Implementar modelo interno `numpy.ndarray` con `**dtype=bool`** (matriz booleana); parsear teclado 0/1 → `False`/`True` (normativas a,b,c,h)
- Implementar operaciones relacionales y producto booleano según sección “Matrices booleanas” de este documento
- Función que derive y muestre **R** como conjunto de pares `(xᵢ, xⱼ)` donde la celda es verdadera (normativa d)
- Implementar reflexiva, irreflexiva, simétrica, asimétrica, antisimétrica, transitiva y equivalencia (normativa f base)
- Implementar orden parcial, total y estricto; documentar definiciones en informe (normativa f)
- Menú: analizar todas las propiedades o una por una (normativa e)
- Grafo dirigido: **NetworkX** (topología y `spring_layout`) + **Plotly** (`graph_objects`, figura interactiva; p. ej. `fig.show()`) (normativa g)
- Ejecutable con **PyInstaller**; informe, manual y `.zip` de entrega

---

## Dependencias (Python): archivo `dependencias`

Todo el conjunto de paquetes externos del proyecto está listado **únicamente** en el archivo [dependencias](dependencias) (formato compatible con `pip install -r dependencias`). No se omiten dependencias de aplicación: runtime + herramienta de empaquetado.


| Paquete         | Rol en el proyecto                                                                                                                                                                                                                                                                                        |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **numpy**       | Matriz relacional como `ndarray` `**dtype=bool`**; producto matricial booleano para transitividad / composición; validación vectorizada.                                                                                                                                                                  |
| **networkx**    | Construir `**DiGraph`** desde la matriz de adyacencia booleana; calcular posiciones (p. ej. `spring_layout`). API: `nx.from_numpy_array(..., create_using=nx.DiGraph)` ([documentación NetworkX](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_numpy_array.html)). |
| **plotly**      | Visualización interactiva del digrafo (`graph_objects`, `fig.show()`; suele abrirse el navegador). **No** usar Matplotlib en la implementación alineada a este plan. [Plotly Python](https://plotly.com/python/).                                                                                         |
| **pyinstaller** | Generar **ejecutable** para la entrega (“aplicación funcional” del PDF).                                                                                                                                                                                                                                  |


**Estándar del lenguaje:** Python **3.10 o superior** (recomendado 3.11–3.12) para compatibilidad con NumPy 2.x y herramientas actuales.

---

## Matrices booleanas frente a entradas 0 y 1

### Distinción conceptual

- En **matemáticas discretas**, una **matriz relacional** sobre un conjunto finito es una matriz cuyas entradas son valores de verdad: **verdadero** si el par está en la relación, **falso** si no.
- Los símbolos **0 y 1** en el enunciado son la forma **habitual de escribir** esos valores en papel o por teclado; **no** es obligatorio que el programa las trate como enteros en las operaciones internas.

### Modelo recomendado en código

1. **Entrada humana:** el usuario puede seguir introduciendo **0** y **1** (normativa del PDF). El programa **valida** que solo existan esos símbolos y los **convierte** al tipo booleano del lenguaje.
2. **Representación interna:** `M: np.ndarray` con `**dtype=np.bool`** (o `dtype=bool`). Así, reflexividad, simetría, etc. se expresan con operadores lógicos `**&**`, `**|**`, `**~**`, y comparaciones `**==**`, sin ambigüedad aritmética.
3. **Conjunto R:** R = (i,j) \mid M[i,j] = \text{True}, mostrado con etiquetas de nodos (por ejemplo `1..n` o `A,B,C,...`).

### Producto (multiplicación) de matrices booleanas

La composición de relaciones corresponde al **producto booleano**: para matrices A, B booleanas n\times n,


C_{ij} = \bigvee_{k=1}^{n} (A_{ik} \land B_{kj})


En **NumPy**, `np.matmul(A, B)` con `**A` y `B` de tipo `bool`** usa multiplicación como **AND** y suma acumulada como **OR**, lo cual coincide con el producto booleano estándar (véase discusión en [Stack Overflow: boolean matrix multiplication in NumPy](https://stackoverflow.com/questions/79106168/best-way-to-calculate-boolean-matrix-multiplication-in-numpy)).

**Transitividad:** la relación es transitiva si, para todo i,j,k, M_{ij} \land M_{jk} \Rightarrow M_{ik}. Equivalentemente, si M^2 (producto booleano de M consigo misma) es **implicada** entrada a entrada por M: donde (M^2)*{ij} es verdadero, M*{ij} debe ser verdadero:

`(M @ M) <= M` (comparación elemento a elemento en booleanos), o comprobación en triple bucle O(n^3) equivalente.

Referencia teórica sobre **multiplicación booleana** y **cierre transitivo** en grafos: [notas tipo Waterloo — transitive closure y producto booleano](https://student.cs.uwaterloo.ca/~cs466/Old_courses/F08/transitiveClosure.pdf) (relación entre existencia de caminos y potencias / productos en el semiring booleano).

### Por qué no “solo enteros 0/1” en el núcleo

- Con enteros, `+` y `*` son aritméticos: podrían aparecer **2, 3, …** en productos si no se reclampa a 0/1 tras cada operación, lo que **no** es el álgebra booleana de relaciones.
- Trabajar en `**bool`** deja explícito que solo importan **∧** y **∨**, alineado con la definición de matriz de una relación.

---

## Alcance del software (normativas del PDF)


| Punto PDF | Qué debes construir                                                                                                                       |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Intro** | Simulación: relación (MR booleana) + grafo dirigido; entrada n\times n.                                                                   |
| **a**     | Entrada manual por teclado (filas/celdas); aceptar **0/1** y almacenar como **bool**.                                                     |
| **b**     | Validar matriz **cuadrada**; si falla, mensaje claro y no analizar.                                                                       |
| **c**     | Generación **aleatoria** booleana o entrada manual (usuario “indica por pantalla”).                                                       |
| **d**     | Mostrar **R** a partir de las posiciones **True** en la matriz.                                                                           |
| **e**     | Menú: todas las propiedades **o** una a una.                                                                                              |
| **f**     | Salida sí/no: reflexiva, irreflexiva, simétrica, asimétrica, antisimétrica, transitiva, equivalencia; órdenes parcial / total / estricto. |
| **g**     | Grafo dirigido **dibujado** en pantalla (no solo lista de aristas).                                                                       |
| **h**     | Validar n (entero **≥ 1**, sin tope fijo en código), forma de matriz, símbolos de entrada y argumentos de funciones.                         |


### Definiciones a codificar (alinear con tu clase)

Misma lógica que v1.0, interpretando M_{ij}=1 del PDF como `**M[i,j] is True`**.

- **Reflexiva / irreflexiva:** diagonal toda **True** / toda **False**.
- **Simétrica:** `M == M.T`.
- **Asimétrica:** para i \neq j, no puede darse **True** en (i,j) y (j,i) a la vez; suele ir con diagonal **False**.
- **Antisimétrica:** si i \neq j y ambos **True**, entonces no antisimétrica (salvo convención del texto; la habitual es: nunca **True** simétricos fuera de la diagonal).
- **Transitiva:** ver sección de producto booleano arriba.
- **Equivalencia:** reflexiva + simétrica + transitiva.
- **Orden parcial (habitual):** reflexiva + antisimétrica + transitiva.
- **Orden total:** orden parcial + comparabilidad para todo par i \neq j.
- **Orden estricto (habitual):** irreflexiva + asimétrica + transitiva (confirmar en apuntes del curso).

---

## Arquitectura sugerida (módulos)

```mermaid
flowchart TD
  input[Entrada n y modo manual o aleatorio]
  validate[Validar n y matriz cuadrada bool]
  pairs[Extraer y mostrar R]
  menu[Menu propiedades: todas o una]
  props[Modulo propiedades sobre ndarray bool]
  order[Modulo orden parcial total estricto]
  graph[NetworkX layout plus Plotly Figure]
  input --> validate --> pairs --> menu
  menu --> props --> order
  pairs --> graph
```



- `**matrix_io.py`:** lectura 0/1 → `bool`/`np.bool_`, aleatorio, validaciones; **n** solo validado como entero **≥ 1** (sin tope máximo en código).
- `**relation.py`:** extracción de pares, cada propiedad, producto booleano auxiliar.
- `**order.py`:** composición de órdenes.
- `**graph_view.py`:** `from_numpy_array` → `DiGraph` → layout NX → construir figura **Plotly** (trazas + opcional flechas por arista).
- `**main.py`:** menú consola (o GUI opcional más adelante).

---

## Entrega documental (PDF del proyecto)

Incluir en el **.zip/.rar**: documento general con portada (integrantes, materia, profesor Germán Salas Ojeda, referencias), código fuente, archivo **[dependencias](dependencias)**, ejecutable probado en máquina sin IDE, manual de usuario (este README puede servir de base).

---

## Riesgos

- Definiciones de orden **total** / **estricto**: documentar las que usa el código.
- **n** muy grande: matriz **n×n** consume mucha RAM; el grafo en Plotly puede volverse lento o ilegible; la entrada manual es impracticable. No se impone tope en código: la responsabilidad es del usuario o de advertencias en el manual (no sustituyen un máximo obligatorio).
- **PyInstaller** con Plotly puede exigir empaquetar recursos del paquete (p. ej. `--collect-all plotly`); probar el ejecutable en un PC limpio.

---

## Orden de trabajo sugerido

1. Entorno + `pip install -r dependencias`.
2. I/O y validación con `**dtype=bool`**.
3. Propiedades + producto booleano para transitividad.
4. Órdenes y menú.
5. Grafo: NetworkX + Plotly.
6. PyInstaller + pruebas + informe.

---

## Manual de uso (README)

### Requisitos

- **Python 3.10+** instalado en el sistema.
- Copia del proyecto con el archivo **[dependencias](dependencias)** en la raíz.

### Instalación

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

### Ejecución (modo desarrollo)

Desde la raíz del proyecto, una vez implementado el punto de entrada:

```bash
python main.py
```

(Sustituir `main.py` por el nombre real del archivo principal si difiere.)

### Uso esperado de la aplicación

1. **Tamaño n:** el programa solicita el orden de la matriz: cualquier entero **n ≥ 1** (sin tope fijo en código). Para uso cómodo en consola y en el visor del grafo, conviene **n** moderado; valores grandes están limitados solo por memoria y tiempo.
2. **Modo de matriz:** elegir entre **entrada manual** (teclado, fila a fila o celda a celda con **0** o **1**) o **generación aleatoria** con la misma n.
3. **Validación:** si la matriz no es cuadrada o hay caracteres distintos de 0/1, el programa muestra un mensaje de error y pide corregir sin continuar el análisis incorrectamente.
4. **Relación R:** la aplicación lista los pares (x_i, x_j) para los que la entrada booleana es verdadera (equivalente a los “unos” del enunciado).
5. **Análisis:** desde el menú, ejecutar **todas** las comprobaciones de propiedades o **una** propiedad concreta; se muestra **Sí/No** (y opcionalmente un contraejemplo).
6. **Órdenes:** se indica si la relación es orden parcial, total o estricto según las definiciones documentadas en tu informe académico.
7. **Grafo:** al elegir la opción correspondiente, se abre la vista interactiva de **Plotly** (habitualmente en el **navegador**) con el **grafo dirigido**: un nodo por elemento; aristas según **True** en (i,j), con indicación de dirección según implementación (trazas + anotaciones). Cierra la pestaña o la ventana del visor y vuelve a la consola.

### Generar ejecutable (entrega)

Con PyInstaller (ajusta el nombre del script principal):

```bash
pyinstaller --onefile --windowed main.py
```

La opción `--windowed` evita consola extra si la UI es solo ventanas; si tu aplicación es **solo consola** y Plotly abre el navegador, suele bastar sin `--windowed`. Revisa la carpeta `dist/` y prueba el binario en un equipo **sin** el proyecto ni el IDE; si falla Plotly empaquetado, prueba `--collect-all plotly`.

### Problemas frecuentes

- `**pip` no encuentra `dependencias`:** ejecuta el comando desde la carpeta donde está el archivo `dependencias` o usa la ruta completa: `pip install -r /ruta/al/proyecto/dependencias`.
- **Plotly no abre el navegador:** revisa `plotly.io.renderers` y la documentación de Plotly para tu SO; asegúrate de tener navegador predeterminado.
- **Grafo ilegible con n grande:** reduce **n** o ajusta layout en NetworkX (`spring_layout`, `kamada_kawai_layout`) y parámetros de traza Plotly (tamaño de nodo, longitud de arista).

---

**Referencias Web citadas en este plan**

- [Stack Overflow — multiplicación de matrices booleanas en NumPy](https://stackoverflow.com/questions/79106168/best-way-to-calculate-boolean-matrix-multiplication-in-numpy)  
- [Notas — cierre transitivo y producto booleano (Waterloo CS466)](https://student.cs.uwaterloo.ca/~cs466/Old_courses/F08/transitiveClosure.pdf)  
- [Plotly — Python graphing library](https://plotly.com/python/)  
- [NetworkX — `from_numpy_array`](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_numpy_array.html)

