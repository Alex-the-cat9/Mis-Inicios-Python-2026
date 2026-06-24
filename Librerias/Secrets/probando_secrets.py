from secrets import choice

# Una lista gigante con muchas opciones
opciones = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

# Le decimos a Python: "Elige 16 caracteres al azar de esa lista gigante y júntalos"
password_segura = "-".join(choice(opciones) for _ in range(16))
print(password_segura)