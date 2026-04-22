#🛡️ EL RETO: "EL RASTREADOR DE IPs MALIGNAS"
#Tu Misión:
#Tienes esta lista de IPs: ips = ["192.168.1.1", "10.0.0.1", "666.666.666.1", "172.16.0.1"].
#Crea un bucle for que recorra la lista.
#Llama a tu variable temporal sospechoso.
#Dentro del bucle, usa un if:
#Si el sospechoso es exactamente "666.666.666.1", imprime: "💀 IP MALIGNA DETECTADA: [sospechoso]".
#Si no, imprime: "🟢 IP [sospechoso] verificada".
#El código se ve así para completar:
ips = ["192.168.1.1", "10.0.0.1", "666.666.666.1", "172.16.0.1"]

for sospechoso in ips:
    if "666.666.666.1" in sospechoso:
        print("IP MALIGNA DETECTADA:",{sospechoso})
    else:
        print("IP:",{sospechoso}, "vereficada")
#Alex:lo logre easy