# v1.0 — Matriz relacional y grafo

## Entorno virtual (una sola `.venv` en la raíz del repo)

Crea y activa **`.venv`** en la carpeta **`Matematicas_Discretas_Final`** (padre de `v1.0`), instala dependencias y ejecuta:

```bash
cd /ruta/a/Matematicas_Discretas_Final
python3 -m venv .venv
source .venv/bin/activate
pip install -r v1.0/dependencias
cd v1.0
python main.py
```

Desde la raíz sin cambiar de carpeta:

```bash
source .venv/bin/activate
python v1.0/main.py
```

## Contenido

| Archivo         | Descripción                                           |
| --------------- | ----------------------------------------------------- |
| `main.py`       | Menú interactivo                                      |
| `matrix_io.py`  | Entrada manual (0/1) o matriz aleatoria, validación   |
| `relation.py`   | Propiedades de la relación (bool / NumPy)             |
| `order.py`      | Orden parcial, total y estricto                       |
| `graph_view.py` | Grafo dirigido con NetworkX + Plotly (HTML)           |
| `dependencias`  | Paquetes pip (instalar con `-r v1.0/dependencias` desde la raíz) |
