class alumno():
    def __init__(self,alumno,nota):
        self.alumno = alumno
        self.nota = nota
        print("El alumno se ha creado con éxito")

    def calificacion():
        nota= input("Introduce la nota del alumno: ")
        if nota>= 5 and nota <=10:
            print("El alumno ha aprobado")
        elif 0<= nota <5:
            print("El alumno ha suspendido")
        else:
            print("Esa califiacación no es valida")
