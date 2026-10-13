notas = {
    "Matematicas": 8.5,
    "Ingles": 7.0,
    "Programacion": 9.2
}
total_notas = 0
for nota in notas.values():
    total_notas += nota
promedio = total_notas / len(notas)
print("Promedio del estudiante:", promedio)