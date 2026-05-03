#Tienes esta lista: ips_entrantes = ["192.168.1.1", "10.0.0.5", "192.168.1.100", "0.0.0.0"].
#Crea un diccionario vacío llamado cortafuegos.
#Recorre la lista con un for.
#Lógica de Senior:
#Si la IP empieza con "192", asígnale el valor "LOCAL".
#Si la IP es "0.0.0.0", asígnale el valor "NULA".
#Para cualquier otra, asígnale el valor "EXTERNA".
ips_entrantes = ["192.168.1.1", "10.0.0.5", "192.168.1.100", "0.0.0.0"]
cortafuegos = {

}
for i in ips_entrantes:
    if "192" in i:
        cortafuegos[i] = "LOCAL"#me isiste una broma aqui supongo pense que era cambiar directo de la lista ip_entrantes
    elif "0.0.0.0" in i:#pero no para hacer eso es ips_entrantes[numero] y me di cuenta que era para corta fuegos porque
        cortafuegos[i] = "NULA"#los diccionarios cortafuegos[i] se agregan oh se cambian con [letras] mientras que
    else:#las listas con [numeros]
        cortafuegos[i] = "EXTERNA"
#Alex:EASY
print(cortafuegos)