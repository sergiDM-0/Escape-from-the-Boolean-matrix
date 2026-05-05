# QA / Test Plan (v1.0)

Este directorio contiene material de pruebas para el proyecto en su estado actual.

## Objetivo

- Detectar fallos por **entradas inválidas** del usuario.
- Asegurar que las propiedades y órdenes se calculen correctamente en casos clásicos.
- Verificar que las salidas HTML se generen (matriz, relación, grafo) sin romper el flujo.

## Riesgos principales

- **n grande**: consumo de RAM O(n²); ingreso manual inviable; HTML del grafo pesado si hay muchas aristas.
- **Plotly + navegador**: el auto-open puede fallar; el archivo HTML debe quedar generado siempre.
- **Layouts de NetworkX**: `spring_layout` puede intentar usar SciPy; debe existir fallback sin SciPy.

## Pruebas recomendadas (manuales)

### A. Validación de entradas

- `n = 0` → rechaza
- `n = -3` → rechaza
- `n = abc` → rechaza
- valores de celda distintos de 0/1 (ej. `2`, `-1`, `x`) → rechaza y repregunta

### B. Ingreso manual iterado

- En `n=2`, ingresar: `1,0, n, 0,1` → matriz identidad.
- En `n=3`, ingresar dos celdas y luego `y` a la pregunta “si se canso…” → completa aleatorio y finaliza.

### C. Propiedades (casos canónicos)

- Identidad (diagonal 1, resto 0) → equivalencia (sí), orden parcial (sí)
- Vacía (todo 0) → irreflexiva (sí), simétrica (sí), transitiva (sí)
- No transitiva: (1,2) y (2,3) pero no (1,3) → transitiva (no) + contraejemplo
- Estricto (i<j) → estricto (sí)

### D. HTML

- Opción (1) genera `v1.0/matriz_relacional.html`
- Opción (2) genera `v1.0/relacion_R.html`
- Opción (5) genera `v1.0/grafo_dirigido.html` con flechas visibles

## Pruebas automáticas sugeridas

Actualmente se usan scripts de “smoke tests” (asserts) sin dependencias extra.

### Fase 2 (automatizada)

- Validación `n` inválido (vacío, texto, decimales, 0, negativos)
- Entrada manual: repregunta ante valores no 0/1
- Entrada manual: respuesta distinta de `y` no autocompleta
- Generación HTML: se crean `matriz_relacional.html`, `relacion_R.html`, `grafo_dirigido.html` aunque el navegador no se abra

