from typing import Any

# Creamos la función (la alarma automatizada)
def procesar_seguridad(reporte: dict[str, Any]) -> None:
    for e, i in reporte.items():
        if e == "detalles_ataque":
            for a in i:
                if a == "nivel_peligro" and i[a] == "critico":
                    reporte["bloqueado"] = True
                    print("🚨 [ALERTA] ¡Hacker neutralizado automáticamente!")