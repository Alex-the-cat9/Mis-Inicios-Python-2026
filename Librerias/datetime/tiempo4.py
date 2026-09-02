from datetime import datetime
fecha_limite = datetime(2026, 2, 8)
fecha = datetime.now()
def ver(fecha_hoy, fecha2):
    if fecha_hoy > fecha2:
        return "el plazo ya expiro"
    else:
        return "todavia queda tiempo"
print(ver(fecha, fecha_limite))
print(ver(fecha, fecha_limite.replace(year=2030)))
