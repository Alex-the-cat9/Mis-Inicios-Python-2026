from typing import Any

# 2. Le decimos que los valores pueden ser CUALQUIER cosa (Any)
reporte_red: dict[str, Any] = {}
reporte_red["servidor"] = "Base de Datos principal"
reporte_red["detalles_ataque"] = {"ip_atacante": "185.220.101.5", "tipo_amenaza": "inyeccion SQL", "nivel_peligro": "critico"}
reporte_red["bloqueado"] = False

# Tu lógica impecable que limpia las alertas
for e, i in reporte_red.items():
    if e == "detalles_ataque":
        for a in i:
            if a == "nivel_peligro":
                # Como usamos Any, Mypy ya te dejará hacer esto sin protestar
                if i[a] == "critico":
                    reporte_red["bloqueado"] = True
                    print("hacker neutralizado")