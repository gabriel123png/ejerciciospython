class Curso : 
    def __init__(self):
        self.estudiantes = []
    def inscribir(self,nombre,edad):
        if edad >= 15:
            estudiante = {"nombre": nombre, "edad": edad}
            self.estudiantes.append(estudiante)
            print(f"{nombre} ({edad}años) ha sido inscrito en el curso.")
        else:
            print(f"{nombre} ({edad}años) no cumple con la edad mínima para inscribirse en el curso.")
    def listar_mayores_edad(self):
        return [estudiantes ["nombre"]   for estudiantes in self.estudiantes if estudiantes["edad"] >= 18]

if __name__ == "__main__":
    curso = Curso()
    print("Inscripción de estudiantes:")
    curso.inscribir("sofia", 14)
    curso.inscribir("mateo", 16)
    curso.inscribir("valentina", 18)
    curso.inscribir("andres", 21)
    curso.inscribir("camila", 19)
    print("\nEstudiantes mayores de edad:")
    print(curso.estudiantes)

    print("\nListado de estudiantes mayores de edad:")
    mayores_de_edad = curso.listar_mayores_edad()
    print(mayores_de_edad)