#vamos a ser hackers eticos jejej
contraseña_del_vecino = 921557
decifrar = 0
while contraseña_del_vecino != decifrar:
    decifrar += 1
print(f"la contraseña del vecino es:{decifrar}")
print("espera el vecino actualizo su contraseña 0_0")
print("eso no es molestia para Alex ")
contraseña_nueva_vecino = "vecino0102039133"
#ahora a lo que eh escuchado posibles nombres que pudo poner:
posibles_nombres = ["nombre_hijo_vecino", "vecino_cloud", "perro_del_vecino", "vecino", "esposa_vecino", "gatovecino"]
decifrar_nueva_contraseña = 0
for nombres in posibles_nombres:
    if nombres in contraseña_nueva_vecino:
        averiguar_digitos = len(contraseña_nueva_vecino) - len(nombres)
        for numero in range(10000000000):
            resolver_si_comienza_con_0 = f"{nombres}{numero:0{averiguar_digitos}}"
            if resolver_si_comienza_con_0 == contraseña_nueva_vecino:
                print(f"la contraseña es:{resolver_si_comienza_con_0}")
                break
print("vieron fue facil y solo me tomo 2 minutos vecino furioso pero no puede con el talento de alex")