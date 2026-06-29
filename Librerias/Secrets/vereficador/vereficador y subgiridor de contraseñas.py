from IA_porcentaje_de_hackeo import IA_porcentaje_de_hackeo
from generar_token import generar_token
print("-------Bienvenido----------")
print("para entrar pon tu correo electronico gmail")
def pedir_correo(correo):
    if "@" not in correo or "gmail.com" not in correo:
        raise ValueError("A-10")
while True:
    gmail = input("Pon tu gmail: ").strip()
    try:
        pedir_correo(gmail)
    except ValueError as a10:
        if str(a10) == "A-10":
            print("asegurese de poner bien su gmail")
            continue
        else:
            print("asegurese de poner bien su gamil")
    else:
        print("se le envio un vereficador si usted es el propietario")
        break
nombre = input("ahora ponga su nombre de usuario: ").strip()
while True:
    print("si eligue maxima su token sera casi imposible de hackear si eligue media sera tambien casi imposible y la baja lo eligue usted")
    token = input("como quieres tu token de seguridad [maxima] [media] [baja]: ").lower()
    if "maxima" in token or "media" in token or "baja" in token:
        token_user = generar_token(token)
        print(f"su token es:{token_user}")
        user = input("le gustaria pasar a una prueba de porcentaje si es hackeable o no?[si] [no]: ").lower()
        if user == "si":
            porcentaje, razon = IA_porcentaje_de_hackeo(token_user)
            print(f"el porcentaje fue un:{porcentaje}% y sus razones son:")
            for i in razon:
                print(i)
            ver = input("desea descargar un archivo .txt para que no se olvide de su token?[si] [no]: ").lower()
            if ver == "si":
                with open("TOKEN.txt", "w", encoding="utf-8") as archivo:
                    archivo.write("SU TOKEN ES:")
                    archivo.write(token_user)
                    archivo.write("NO SE OLVIDE QUE SU TOKEN ES UNICO Y SI LO PIERDE CONTACTESE CON EL SOPORTE GRACIAS")
            print("------gracias---------")
            print("disfrute de nuestras cosas que ofrecemos")
            break
        else:
            ver = input("desea descargar un archivo .txt para que no se olvide de su token?[si] [no]: ").lower()
            if ver == "si":
                    with open("TOKEN.txt", "w", encoding="utf-8") as archivo:
                        archivo.write("SU TOKEN ES:")
                        archivo.write(token_user)
                        archivo.write("NO SE OLVIDE QUE SU TOKEN ES UNICO Y SI LO PIERDE CONTACTESE CON EL SOPORTE GRACIAS")
            print("disfrute de nuestras cosas que ofrecemos")
            break
    else:
        continue

            




    