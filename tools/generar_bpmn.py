#!/usr/bin/env python3
"""Genera los dos fragmentos vectoriales del BPMN del SIGPC.

El proceso se divide mediante un par de eventos intermedios de enlace "A" para
mantener la legibilidad sin alterar la continuidad del flujo.
"""

from __future__ import annotations

from html import escape
from pathlib import Path
import textwrap


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "bpmn"

INK = "#263238"
BLUE = "#006A8E"
BLUE_DARK = "#004E68"
BLUE_LIGHT = "#EAF6FA"
BLUE_LIGHT_2 = "#F4FAFC"
GRAY = "#65757D"
WHITE = "#FFFFFF"
ERROR = "#A33B32"


def _wrap(text: str, width: int) -> list[str]:
    return textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False) or [""]


class SVG:
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            f"<title>{escape(title)}</title>",
            """<defs>
  <marker id="seq-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#263238"/>
  </marker>
  <marker id="msg-arrow" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" orient="auto-start-reverse">
    <path d="M 1 1 L 11 6 L 1 11" fill="none" stroke="#006A8E" stroke-width="1.8"/>
  </marker>
  <filter id="shadow" x="-15%" y="-20%" width="130%" height="145%">
    <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#004E68" flood-opacity="0.15"/>
  </filter>
</defs>""",
            f'<rect width="{width}" height="{height}" fill="{WHITE}"/>',
        ]

    def raw(self, value: str) -> None:
        self.parts.append(value)

    def text(self, x: float, y: float, value: str, size: int = 30, weight: int = 400,
             anchor: str = "middle", color: str = INK, italic: bool = False,
             rotate: float | None = None) -> None:
        transform = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
        style = "italic" if italic else "normal"
        self.parts.append(
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" dominant-baseline="middle" '
            f'font-family="Arial, Liberation Sans, sans-serif" font-size="{size}" font-weight="{weight}" '
            f'font-style="{style}" fill="{color}"{transform}>{escape(value)}</text>'
        )

    def multiline(self, x: float, y: float, value: str, width: int, size: int = 30,
                  weight: int = 500, color: str = INK, line_height: float = 1.15,
                  anchor: str = "middle") -> None:
        lines = _wrap(value, width)
        total = (len(lines) - 1) * size * line_height
        start = y - total / 2
        for i, line in enumerate(lines):
            self.text(x, start + i * size * line_height, line, size=size, weight=weight,
                      anchor=anchor, color=color)

    def rect(self, x: float, y: float, w: float, h: float, fill: str = WHITE,
             stroke: str = INK, sw: float = 3, rx: float = 0, dash: str | None = None,
             shadow: bool = False) -> None:
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        filter_attr = ' filter="url(#shadow)"' if shadow else ""
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{dash_attr}{filter_attr}/>'
        )

    def circle(self, cx: float, cy: float, r: float, fill: str = WHITE,
               stroke: str = INK, sw: float = 4) -> None:
        self.parts.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        )

    def line(self, points: list[tuple[float, float]], dashed: bool = False,
             color: str = INK, sw: float = 4, marker: str | None = "seq-arrow") -> None:
        pts = " ".join(f"{x},{y}" for x, y in points)
        dash = ' stroke-dasharray="18 13"' if dashed else ""
        marker_attr = f' marker-end="url(#{marker})"' if marker else ""
        self.parts.append(
            f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"{dash}{marker_attr}/>'
        )

    def save(self, path: Path) -> None:
        self.parts.append("</svg>")
        path.write_text("\n".join(self.parts), encoding="utf-8")


def title(svg: SVG, text: str, subtitle: str) -> None:
    svg.text(80, 28, text, size=38, weight=700, anchor="start", color=BLUE_DARK)
    svg.text(svg.width - 80, 30, subtitle, size=26, weight=400, anchor="end", color=GRAY)


def pools(svg: SVG, client_h: int, org_y: int, org_h: int, lanes: list[str]) -> None:
    x, w = 60, svg.width - 120
    pool_col, lane_col = 80, 230
    # Cliente como pool de caja negra.
    svg.rect(x, 70, w, client_h, fill="#F7FAFB", stroke=INK, sw=4)
    svg.raw(f'<line x1="{x + pool_col}" y1="70" x2="{x + pool_col}" y2="{70 + client_h}" stroke="{INK}" stroke-width="3"/>')
    svg.text(x + pool_col / 2, 70 + client_h / 2, "Cliente", size=30, weight=700, rotate=-90)
    svg.text(x + pool_col + 35, 70 + client_h / 2, "Pool externo (caja negra): intercambia mensajes con Multitronik",
             size=28, weight=500, anchor="start", color=GRAY)
    # Pool interno y lanes.
    svg.rect(x, org_y, w, org_h, fill=WHITE, stroke=INK, sw=4)
    svg.raw(f'<line x1="{x + pool_col}" y1="{org_y}" x2="{x + pool_col}" y2="{org_y + org_h}" stroke="{INK}" stroke-width="3"/>')
    svg.raw(f'<line x1="{x + pool_col + lane_col}" y1="{org_y}" x2="{x + pool_col + lane_col}" y2="{org_y + org_h}" stroke="{INK}" stroke-width="3"/>')
    svg.text(x + pool_col / 2, org_y + org_h / 2, "Multitronik Solutions S.R.L.", size=30, weight=700, rotate=-90)
    lane_h = org_h / len(lanes)
    for i, lane in enumerate(lanes):
        ly = org_y + i * lane_h
        fill = BLUE_LIGHT_2 if i % 2 == 0 else WHITE
        svg.raw(f'<rect x="{x + pool_col}" y="{ly}" width="{w - pool_col}" height="{lane_h}" fill="{fill}" stroke="none"/>')
        if i:
            svg.raw(f'<line x1="{x + pool_col}" y1="{ly}" x2="{x + w}" y2="{ly}" stroke="{GRAY}" stroke-width="2"/>')
        svg.multiline(x + pool_col + lane_col / 2, ly + lane_h / 2, lane, width=16, size=29, weight=700, color=BLUE_DARK)


def user_icon(svg: SVG, x: float, y: float) -> None:
    svg.circle(x + 21, y + 20, 9, fill=WHITE, stroke=BLUE_DARK, sw=3)
    svg.raw(f'<path d="M {x + 5} {y + 48} Q {x + 21} {y + 31} {x + 37} {y + 48}" fill="none" stroke="{BLUE_DARK}" stroke-width="3"/>')


def service_icon(svg: SVG, x: float, y: float) -> None:
    svg.circle(x + 21, y + 25, 11, fill=WHITE, stroke=BLUE_DARK, sw=3)
    for dx, dy in [(0, -18), (0, 18), (-18, 0), (18, 0), (-13, -13), (13, 13), (-13, 13), (13, -13)]:
        svg.raw(f'<line x1="{x + 21 + dx * .55}" y1="{y + 25 + dy * .55}" x2="{x + 21 + dx}" y2="{y + 25 + dy}" stroke="{BLUE_DARK}" stroke-width="3"/>')


def envelope_icon(svg: SVG, x: float, y: float, filled: bool = False) -> None:
    fill = BLUE_LIGHT if not filled else "#D3EDF5"
    svg.rect(x + 4, y + 8, 38, 27, fill=fill, stroke=BLUE_DARK, sw=2, rx=2)
    svg.raw(f'<path d="M {x + 5} {y + 10} L {x + 23} {y + 25} L {x + 41} {y + 10}" fill="none" stroke="{BLUE_DARK}" stroke-width="2"/>')


def task(svg: SVG, x: float, y: float, label: str, kind: str = "user", w: int = 300, h: int = 120) -> None:
    svg.rect(x, y, w, h, fill=WHITE, stroke=BLUE_DARK, sw=4, rx=20, shadow=True)
    if kind == "user":
        user_icon(svg, x + 8, y + 8)
    elif kind == "service":
        service_icon(svg, x + 8, y + 8)
    elif kind == "send":
        envelope_icon(svg, x + 8, y + 8, filled=True)
    elif kind == "receive":
        envelope_icon(svg, x + 8, y + 8, filled=False)
    svg.multiline(x + w / 2 + 15, y + h / 2 + 2, label, width=18 if w <= 300 else 23,
                  size=29, weight=600)


def gateway(svg: SVG, cx: float, cy: float, label: str, size: int = 105) -> None:
    h = size / 2
    pts = f"{cx},{cy-h} {cx+h},{cy} {cx},{cy+h} {cx-h},{cy}"
    svg.raw(f'<polygon points="{pts}" fill="#FFF8E7" stroke="{INK}" stroke-width="4" filter="url(#shadow)"/>')
    svg.raw(f'<path d="M {cx-19} {cy-19} L {cx+19} {cy+19} M {cx+19} {cy-19} L {cx-19} {cy+19}" stroke="{INK}" stroke-width="6"/>')
    svg.multiline(cx, cy - h - 42, label, width=20, size=27, weight=700, color=BLUE_DARK)


def start_event(svg: SVG, cx: float, cy: float, label: str) -> None:
    svg.circle(cx, cy, 40, fill=WHITE, stroke=INK, sw=4)
    envelope_icon(svg, cx - 23, cy - 20, filled=False)
    svg.multiline(cx, cy + 78, label, width=18, size=26, weight=600)


def end_event(svg: SVG, cx: float, cy: float, label: str, color: str = INK) -> None:
    svg.circle(cx, cy, 42, fill=WHITE, stroke=color, sw=10)
    svg.multiline(cx, cy + 82, label, width=18, size=26, weight=700, color=color)


def link_event(svg: SVG, cx: float, cy: float, label: str, throwing: bool) -> None:
    svg.circle(cx, cy, 43, fill=WHITE, stroke=BLUE_DARK, sw=4)
    svg.circle(cx, cy, 36, fill=WHITE, stroke=BLUE_DARK, sw=2)
    direction = 1 if throwing else -1
    svg.raw(
        f'<path d="M {cx - 15 * direction} {cy - 15} L {cx + 18 * direction} {cy} '
        f'L {cx - 15 * direction} {cy + 15} z" fill="{BLUE}"/>'
    )
    svg.text(cx, cy + 78, label, size=30, weight=700, color=BLUE_DARK)


def timer_event(svg: SVG, cx: float, cy: float, label: str) -> None:
    svg.circle(cx, cy, 42, fill=WHITE, stroke=INK, sw=4)
    svg.circle(cx, cy, 35, fill=WHITE, stroke=INK, sw=2)
    svg.raw(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-22}" stroke="{INK}" stroke-width="4"/>')
    svg.raw(f'<line x1="{cx}" y1="{cy}" x2="{cx+18}" y2="{cy+10}" stroke="{INK}" stroke-width="4"/>')
    svg.multiline(cx, cy + 80, label, width=18, size=25, weight=600)


def seq(svg: SVG, points: list[tuple[float, float]], label: str | None = None,
        label_at: tuple[float, float] | None = None) -> None:
    svg.line(points, dashed=False, color=INK, sw=4, marker="seq-arrow")
    if label and label_at:
        svg.text(label_at[0], label_at[1], label, size=25, weight=700, color=BLUE_DARK)


def msg(svg: SVG, points: list[tuple[float, float]], label: str, label_at: tuple[float, float]) -> None:
    # El pequeño círculo abierto señala el origen del flujo de mensaje.
    x0, y0 = points[0]
    svg.circle(x0, y0, 7, fill=WHITE, stroke=BLUE, sw=3)
    svg.line(points, dashed=True, color=BLUE, sw=4, marker="msg-arrow")
    svg.text(label_at[0], label_at[1], label, size=24, weight=600, color=BLUE)


def diagram_1(path: Path) -> None:
    svg = SVG(5200, 1700, "BPMN SIGPC — Admisión y alta del proyecto")
    title(svg, "BPMN — Gestión integral de un proyecto de software", "Fragmento 1 de 2 · Admisión y alta")
    pools(svg, client_h=170, org_y=300, org_h=1200,
          lanes=["Comercial", "SIGPC (sistema)", "Dirección"])

    start_event(svg, 390, 500, "Solicitud recibida")
    task(svg, 510, 440, "Relevar requisitos", "user")
    task(svg, 880, 840, "Validar datos obligatorios", "service")
    gateway(svg, 1280, 900, "¿Datos completos?")
    task(svg, 1370, 330, "Pedir información faltante", "send")
    task(svg, 1730, 330, "Recibir datos adicionales", "receive")
    task(svg, 1450, 520, "Preparar propuesta", "user")
    task(svg, 1900, 1240, "Evaluar propuesta", "user")
    gateway(svg, 2290, 1300, "¿Aprobada internamente?")
    task(svg, 2180, 510, "Ajustar alcance y costo", "user")
    task(svg, 2590, 440, "Enviar propuesta", "send")
    task(svg, 2960, 440, "Recibir respuesta", "receive")
    gateway(svg, 3360, 500, "Respuesta del cliente")
    task(svg, 3500, 330, "Registrar rechazo", "user")
    end_event(svg, 3930, 390, "Propuesta rechazada", ERROR)
    task(svg, 3500, 520, "Ajustar propuesta", "user")
    task(svg, 3650, 840, "Crear proyecto aprobado", "service")
    task(svg, 4050, 840, "Notificar responsables", "service")
    link_event(svg, 4580, 900, "Enlace A", throwing=True)

    seq(svg, [(430, 500), (510, 500)])
    seq(svg, [(810, 500), (840, 500), (840, 900), (880, 900)])
    seq(svg, [(1180, 900), (1227, 900)])
    seq(svg, [(1280, 847), (1280, 390), (1370, 390)], "No", (1308, 720))
    seq(svg, [(1670, 390), (1730, 390)])
    seq(svg, [(2030, 390), (2070, 390), (2070, 735), (1030, 735), (1030, 840)])
    seq(svg, [(1333, 900), (1390, 900), (1390, 580), (1450, 580)], "Sí", (1365, 865))
    seq(svg, [(1750, 580), (1810, 580), (1810, 1300), (1900, 1300)])
    seq(svg, [(2200, 1300), (2237, 1300)])
    seq(svg, [(2290, 1247), (2290, 630)], "No", (2318, 1030))
    seq(svg, [(2180, 570), (2100, 570), (2100, 1170), (2050, 1170), (2050, 1240)])
    seq(svg, [(2343, 1300), (2500, 1300), (2500, 500), (2590, 500)], "Sí", (2475, 1265))
    seq(svg, [(2890, 500), (2960, 500)])
    seq(svg, [(3260, 500), (3307, 500)])
    seq(svg, [(3360, 447), (3360, 390), (3500, 390)], "Rechaza", (3425, 355))
    seq(svg, [(3800, 390), (3888, 390)])
    seq(svg, [(3413, 500), (3450, 500), (3450, 580), (3500, 580)], "Pide cambios", (3480, 480))
    seq(svg, [(3650, 640), (3650, 690), (2140, 690), (2140, 1170), (2050, 1170), (2050, 1240)])
    seq(svg, [(3360, 553), (3360, 900), (3650, 900)], "Acepta", (3395, 735))
    seq(svg, [(3950, 900), (4050, 900)])
    seq(svg, [(4350, 900), (4537, 900)])

    msg(svg, [(390, 240), (390, 460)], "Solicitud y requisitos", (560, 272))
    msg(svg, [(1520, 330), (1520, 240)], "Pedido de datos", (1660, 270))
    msg(svg, [(1880, 240), (1880, 330)], "Información adicional", (2060, 270))
    msg(svg, [(2740, 440), (2740, 240)], "Propuesta", (2830, 270))
    msg(svg, [(3110, 240), (3110, 440)], "Aceptación, cambios o rechazo", (3370, 270))

    svg.text(60, 1570,
             "Flujo continuo: secuencia interna · Flujo discontinuo: mensaje · Rombo con X: decisión exclusiva · Enlace A: continuidad en el fragmento 2",
             size=27, weight=500, anchor="start", color=GRAY)
    svg.text(5140, 1640, "Elaboración propia · BPMN 2.0", size=24, weight=500, anchor="end", color=GRAY)
    svg.save(path)


def diagram_2(path: Path) -> None:
    svg = SVG(6300, 2500, "BPMN SIGPC — Ejecución, aceptación y cierre")
    title(svg, "BPMN — Gestión integral de un proyecto de software", "Fragmento 2 de 2 · Ejecución y cierre")
    pools(svg, client_h=170, org_y=300, org_h=2000,
          lanes=["SIGPC (sistema)", "Tecnología / Desarrollo", "Soporte", "Finanzas", "Dirección"])

    link_event(svg, 390, 500, "Enlace A", throwing=False)
    task(svg, 520, 840, "Planificar tareas e hitos", "user")
    task(svg, 900, 840, "Ejecutar tareas y registrar horas", "user")
    task(svg, 1290, 840, "Probar solución", "user")
    gateway(svg, 1680, 900, "¿Pruebas superadas?")
    task(svg, 1770, 1030, "Corregir defectos", "user")
    task(svg, 2050, 440, "Publicar entrega y notificar", "service")
    task(svg, 2450, 1240, "Recibir validación del cliente", "receive")
    gateway(svg, 2850, 1300, "¿Entrega aceptada?")
    task(svg, 3000, 1240, "Registrar incidencia", "user")
    task(svg, 3400, 840, "Corregir entrega", "user")
    task(svg, 3100, 440, "Cerrar tareas e hito", "service")
    task(svg, 3550, 1640, "Emitir factura", "user")
    task(svg, 3950, 440, "Actualizar hito facturado", "service")
    task(svg, 4350, 1640, "Verificar y registrar pago", "receive")
    gateway(svg, 4760, 1700, "¿Pago acreditado?")
    task(svg, 4910, 1640, "Enviar recordatorio", "send")
    timer_event(svg, 5370, 1700, "Esperar vencimiento")
    task(svg, 5050, 440, "Cerrar proyecto y consolidar métricas", "service", w=350)
    task(svg, 5540, 2040, "Revisar indicadores", "user")
    end_event(svg, 6070, 2100, "Proyecto cerrado")

    seq(svg, [(433, 500), (470, 500), (470, 900), (520, 900)])
    seq(svg, [(820, 900), (900, 900)])
    seq(svg, [(1200, 900), (1290, 900)])
    seq(svg, [(1590, 900), (1627, 900)])
    seq(svg, [(1680, 953), (1680, 1090), (1770, 1090)], "No", (1710, 1020))
    seq(svg, [(2070, 1090), (2120, 1090), (2120, 1180), (1440, 1180), (1440, 960)])
    seq(svg, [(1733, 900), (1950, 900), (1950, 500), (2050, 500)], "Sí", (1815, 865))
    seq(svg, [(2350, 500), (2390, 500), (2390, 1300), (2450, 1300)])
    seq(svg, [(2750, 1300), (2797, 1300)])
    seq(svg, [(2903, 1300), (3000, 1300)], "No", (2950, 1265))
    seq(svg, [(3300, 1300), (3340, 1300), (3340, 900), (3400, 900)])
    seq(svg, [(3700, 900), (3750, 900), (3750, 1190), (1440, 1190), (1440, 960)])
    seq(svg, [(2850, 1247), (2850, 500), (3100, 500)], "Sí", (2885, 820))
    seq(svg, [(3400, 500), (3480, 500), (3480, 1700), (3550, 1700)])
    seq(svg, [(3850, 1700), (3900, 1700), (3900, 500), (3950, 500)])
    seq(svg, [(4250, 500), (4300, 500), (4300, 1700), (4350, 1700)])
    seq(svg, [(4650, 1700), (4707, 1700)])
    seq(svg, [(4813, 1700), (4910, 1700)], "No", (4860, 1665))
    seq(svg, [(5210, 1700), (5328, 1700)])
    seq(svg, [(5370, 1658), (5370, 1540), (4500, 1540), (4500, 1640)])
    seq(svg, [(4760, 1647), (4760, 500), (5050, 500)], "Sí", (4795, 1180))
    seq(svg, [(5400, 500), (5460, 500), (5460, 2100), (5540, 2100)])
    seq(svg, [(5840, 2100), (6028, 2100)])

    msg(svg, [(2200, 440), (2200, 240)], "Entrega disponible", (2360, 270))
    msg(svg, [(2600, 240), (2600, 1240)], "Aceptación u observaciones", (2820, 270))
    msg(svg, [(3700, 1640), (3700, 240)], "Factura", (3780, 270))
    msg(svg, [(4500, 240), (4500, 1640)], "Pago", (4560, 270))
    msg(svg, [(5060, 1640), (5060, 240)], "Recordatorio", (5170, 270))

    svg.text(60, 2370,
             "Flujo continuo: secuencia interna · Flujo discontinuo: mensaje · Los ciclos modelan corrección, reentrega y seguimiento de pago",
             size=27, weight=500, anchor="start", color=GRAY)
    svg.text(6240, 2440, "Elaboración propia · BPMN 2.0", size=24, weight=500, anchor="end", color=GRAY)
    svg.save(path)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    diagram_1(OUT / "bpmn_01_admision_alta.svg")
    diagram_2(OUT / "bpmn_02_ejecucion_cierre.svg")
    print("Diagramas BPMN generados en", OUT)


if __name__ == "__main__":
    main()

