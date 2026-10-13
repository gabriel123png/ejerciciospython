horario = {
    "Lunes": "Matematicas",
    "Martes": "Ingles",
    "Miercoles": "Programacion"
}
dia = input("Ingresa un dia: ").strip().capitalize()
materia = horario.get(dia, "No hay materia registrada para ese dia")
print(materia)
