# Plan v1.0 — Proyecto final Matemáticas Discretas (Relaciones y grafos)

**Versión:** 1.0  
**Resumen:** Implementar un programa que lea o genere una matriz relacional binaria n×n, valide entradas, muestre el conjunto de pares R, verifique propiedades (reflexiva, simétrica, transitiva, etc.), clasifique órdenes (parcial/total/estricto), visualice el grafo dirigido y prepare el paquete de entrega académica.

**Fuente de requisitos:** [Proyecto_Final_M.D..pdf](Proyecto_Final_M.D..pdf) (UNIVERSIDAD ECCI).

---

## Lista de trabajo (checklist)

- [ ] Elegir lenguaje y dependencias (ej. Python + networkx/matplotlib); crear estructura de carpetas y punto de entrada main
- [ ] Implementar entrada manual n×n, generación aleatoria, validación cuadrada y solo 0/1 (normativas a,b,c,h)
- [ ] Función que derive y muestre R={(i,j)|MR[i,j]=1} con etiquetas legibles (normativa d)
- [ ] Implementar reflexiva, irreflexiva, simétrica, asimétrica, antisimétrica, transitiva y equivalencia con tests claros (normativa f base)
- [ ] Implementar orden parcial, total y estricto según definiciones del curso; documentar definiciones en informe (normativa f)
- [ ] Menú: analizar todas las propiedades o una por una (normativa e)
- [ ] Renderizar grafo dirigido desde MR en pantalla (normativa g)
- [ ] Redactar informe con portada y referencias, manual de usuario, requirements.txt, ejecutable empaquetado y .zip final

---

## Alcance del software (lo que pide el enunciado)

| Punto PDF | Qué debes construir |
|-----------|---------------------|
| **Intro** | Simulación sobre **relaciones en conjuntos** (matriz MR) y **grafos dirigidos**. Entrada: matriz binaria **n×n**. Salida: propiedades de la relación y grafo. |
| **a** | Modo **entrada manual por teclado** fila a fila o celda a celda (0/1). |
| **b** | **Validar** que la matriz sea **cuadrada** (mismas filas y columnas); si no, mensaje claro y no continuar el análisis. |
| **c** | Modo alternativo: **generación aleatoria** (0/1) con n dado, **o** otro flujo donde el usuario “indique directamente por pantalla” (puede ser el mismo manual + opción generar). |
| **d** | Construir **R = {(i,j) : MR[i,j]=1}** usando etiquetas de elementos (ej. A,B,C… o 1..n) y **mostrar el conjunto de pares** en pantalla. |
| **e** | Menú o flujo que permita: **analizar todas las propiedades de una vez** y/o **consultar una propiedad concreta** (flexible según el PDF). |
| **f** | Salida explícita: **sí/no** (o lista) para reflexiva, irreflexiva, simétrica, asimétrica, antisimétrica, transitiva, **relación de equivalencia**; y si corresponde **orden parcial, total y/o estricto**. |
| **g** | **Grafo dirigido** con aristas i→j cuando MR[i,j]=1; **mostrar en pantalla** (dibujo), no solo lista de aristas. |
| **h** | **Validación robusta**: n entero positivo, solo 0/1 en la matriz, índices válidos, mensajes de error en entradas/salidas interactivas y en funciones puras (contratos claros: tipos y rangos). |

### Definiciones a codificar (alinear con tu clase)

Convención típica: conjunto base **X = {x₁,…,xₙ}**, entrada **MR[i][j]=1** ⇔ **xᵢ R xⱼ**.

- **Reflexiva**: ∀i, MR[i][i]=1. **Irreflexiva**: ∀i, MR[i][i]=0.
- **Simétrica**: MR[i][j]=MR[j][i]. **Asimétrica**: si MR[i][j]=1 con i≠j entonces MR[j][i]=0 (y suele implicar irreflexiva en la diagonal).
- **Antisimétrica**: si i≠j y MR[i][j]=1 y MR[j][i]=1 es imposible (no puede haber simetría fuera de la diagonal salvo ambos 0).
- **Transitiva**: si MR[i][j]=1 y MR[j][k]=1 entonces MR[i][k]=1.
- **Equivalencia**: reflexiva + simétrica + transitiva.
- **Orden parcial** (habitual): reflexiva + antisimétrica + transitiva.
- **Orden total**: orden parcial + **comparabilidad**: ∀i≠j, MR[i][j]=1 **o** MR[j][i]=1 (ajusta si tu profesor usa definición estrictamente distinta).
- **Orden estricto** (habitual): **irreflexiva** + **asimétrica** (o equivalente) + **transitiva**; verifica en apuntes si “estricto” en tu curso exige también que sea subconjunto de un orden parcial no reflexivo.

Implementa cada chequeo en **funciones pequeñas** que devuelvan booleano + opcionalmente **contraejemplo** (par de índices) para depuración y para el manual.

## Stack técnico recomendado (el PDF permite cualquier lenguaje)

**Opción A – Python 3** (rápida para validación y visualización): `numpy` opcional para multiplicación booleana (transitividad vía MR²≤MR elemento a elemento), **`networkx` + `matplotlib`** para dibujar el digrafo en ventana o guardar PNG. Empaquetado: **PyInstaller** para ejecutable.

**Opción B – JavaScript/HTML**: interfaz web, canvas o librería de grafos (p. ej. vis.js, cytoscape.js) para el punto **g** sin instalador.

**Opción C – Java/C#**: Swing/WPF + librería de grafos o dibujo manual.

El plan detallado asume **Python** por balance entre tiempo y el requisito de **grafo en pantalla**; puedes sustituir solo la capa de UI.

## Arquitectura sugerida

```mermaid
flowchart TD
  input[Entrada n y modo manual o aleatorio]
  validate[Validar n y matriz cuadrada binaria]
  pairs[Extraer y mostrar R]
  menu[Menu propiedades: todas o una]
  props[Modulo propiedades relacionales]
  order[Modulo orden parcial total estricto]
  graph[Render grafo dirigido]
  input --> validate --> pairs --> menu
  menu --> props --> order
  pairs --> graph
```

- **`matrix_io.py`**: lectura teclado, generación aleatoria, validaciones (**a,b,c,h**).
- **`relation.py`**: `pairs_from_matrix`, cada propiedad (**d,e,f** base matemática).
- **`order.py`**: composición de reflexiva/antisimétrica/transitiva + total + estricto (**f**).
- **`graph_view.py`**: nodos 1..n o etiquetas, aristas desde MR (**g**).
- **`main.py`**: menú consola o ventana simple (**e**).

**Transitividad eficiente**: para cada (i,j,k) comprobar la implicación, O(n³), suficiente para n razonable en un proyecto académico; o producto booleano MR·MR y comparar con MR.

## Entrega documental (sección “EN LA ENTREGA…” del PDF)

Incluir en el **.zip/.rar**:

1. **Documento general** (Word/PDF): portada con integrantes, materia, profesor (Germán Salas Ojeda), descripción del problema, diseño, capturas, **referencias/bibliografía** (punto i del PDF).
2. **Código fuente** completo + dependencias (`requirements.txt` o equivalente).
3. **Aplicación funcional**: ejecutable generado (PyInstaller u otro) **probar en PC limpio** sin IDE.
4. **Manual de usuario**: cómo ingresar matriz, menú de propiedades, cómo ver el grafo, mensajes de error comunes.

Checklist operativo: **probar casos** conocidos (matriz identidad → reflexiva simétrica transitiva; relación vacía → irreflexiva simétrica transitiva vacía; orden lineal 1<2<3 en representación habitual).

## Riesgos y acuerdos con el profesor

- Definiciones de **“asimétrica”** vs **“antisimétrica”** y de **orden total/estricto** pueden variar ligeramente entre textos: incluye en el documento las definiciones que usa tu código.
- Si **n** es muy grande, el dibujo del grafo se satura; opcional: límite máximo de n con mensaje o layout automático.

## Orden de trabajo sugerido

1. Implementar validación de matriz y extracción de **R** (**a–d,h**).
2. Implementar todas las propiedades booleanas + equivalencia (**f** parcial).
3. Implementar clasificación de órdenes (**f** restante).
4. Menú interactivo (**e**).
5. Visualización del grafo (**g**).
6. Pruebas manuales y documentación + empaquetado ejecutable.
