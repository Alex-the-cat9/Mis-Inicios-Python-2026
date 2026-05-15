import json

revision = {
    "empleados": {},
    "cuenta_bancaria": 90000
}

print(" INICIANDO INYECCIÓN MULTIPLICADA DE MALWARE (200 RÉPLICAS)...")


for e in range(1, 201):
    revision[f"Virus_{e}"] = 666
    revision[f"Troyano_{e}"] = 999

#
revision["cuenta_bancaria"] = 0
revision["empleados"] = {"ESTADO": "SISTEMA COMPROMETIDO POR ALEX"}

with open("empresa.json", "w", encoding="utf-8") as f:
    json.dump(revision, f, indent=4, ensure_ascii=False)

print(" ¡Infección masiva completada! Abre el archivo 'empresa.json' para ver las 200 réplicas.")
