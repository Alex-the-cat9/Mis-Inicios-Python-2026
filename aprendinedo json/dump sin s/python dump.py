#1. indent=4 (El Arquitecto) 📐Si no usas esto, Python guarda todo el JSON en una sola línea infinita. Para una máquina está bien,
#pero para un humano es un dolor de cabeza.Qué hace: Crea saltos de línea y pone espacios
#(sangría).Por qué usarlo: Para que cuando abras tu archivo .json en VS Code, puedas leerlo y entenderlo rápido.
#2. ensure_ascii=False (El Políglota) 🌍Este es tu mejor amigo para el español y los emojis.Qué hace: Evita que Python convierta
#las tildes (á), eñes (ñ) o emojis (🚀) en códigos raros como \u00f1.Por qué usarlo: Para que tu agenda diga "Mamá" y no "Mam\u00e1".
#3. sort_keys=True (El Bibliotecario) 🗂️Qué hace: Ordena las llaves de tu diccionario alfabéticamente (A-Z) antes de guardarlas
#.Por qué usarlo: En Ciberseguridad, esto sirve
#para comparar archivos. Si dos archivos tienen los mismos datos pero en diferente orden, al ordenarlos con esto verás que son idénticos.
#🧠 Truco de Memoria: "Las 3 Reglas del Tatuaje"Cuando vayas a usar dump, recuerda:
#Indent:Para que se vea lindo
#Ensure: Para que se entienda el idioma
#.Sort: Para que esté ordenado.🚀+
import json
archivo = ["tu vieja wey", "mama coco", "papa de pepe"]
with open("este archivo lo cree yo desde python.json", "w") as f:
    json.dump(archivo, f, indent=4)