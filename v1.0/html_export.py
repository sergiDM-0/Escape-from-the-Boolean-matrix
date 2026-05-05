"""Exporta vistas a HTML y (si es posible) abre el navegador."""

from __future__ import annotations

from pathlib import Path
import webbrowser


def write_and_open_html(*, filename: str, html: str) -> Path:
    out_path = Path(__file__).resolve().parent / filename
    out_path.write_text(html, encoding="utf-8")
    try:
        webbrowser.open(out_path.as_uri(), new=2, autoraise=True)
    except Exception:
        pass
    return out_path

