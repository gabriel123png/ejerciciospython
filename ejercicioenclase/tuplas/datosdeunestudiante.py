estudiante = {
    "nombre": "Juan",
    "edad": 18,
    "ciudad": "Bogota"
}
print("Estudiante:", estudiante)

estudiante["curso"] = "Python avanzado"
estudiante.append("edad", 19)  


print("Estudiante actualizado:", estudiante)

# este ejercicio que debemos identificar un error 
#  y el erro es que una tupla no se puede modificar,
#  por lo tanto no se puede agregar un nuevo elemento a la tupla,
#  y tampoco se puede modificar un elemento existente de la tupla.
