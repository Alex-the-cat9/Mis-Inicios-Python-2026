from datetime import datetime, timedelta
hoy = datetime.now()
plazo_pago = hoy + timedelta(days=30)
hace_una_semana = hoy - timedelta(weeks=1)
print(f"Hoy:{hoy:%d-%m-%Y}")
print(f"suscripcion acaba en:{plazo_pago:%d-%m-%Y}")
print(f"hace una semana:{hace_una_semana:%d-%m-%Y}")
