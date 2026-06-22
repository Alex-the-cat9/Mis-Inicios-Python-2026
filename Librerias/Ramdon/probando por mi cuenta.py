from random import choices
alumnos = {}
alumnos["Gabriel"] = 15
alumnos["Alex"] = 10
alumnos["Pepe"] = 20
alumnos["Pepito"] = 12
alumnos["Alexis"] = 10
Reprobados:list[str] = []
for e,i in alumnos.items():
    if i < 15:
        print(f"alumno:{e} esta reprobado")
        Reprobados.append(e)

    else:
        print(f"alumno:{e} esta aprovado")
print("Como hoy estoy de buenas aremos un sorteo para ver que reprovado se va a los aprovados")
Alunmo_suertudo = choices(Reprobados, k=1)[0]
print(f"felicidades:{Alunmo_suertudo} es su dia de suerte esta aprovado")