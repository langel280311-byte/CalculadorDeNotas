print("===calculador de notas===")
try:
    nombre_estudiante= input("nombre del estudiante: ")
    nombre_materia= input("nombre de lña asignatura: ")


    nota1= float(input("nota 1: "))
    nota2= float(input("nota 2: "))
    nota3= float(input("nota 3: "))

    p=(nota1+nota2+nota3)/3
    
    print("el promedio es: ",p)
except ValueError:
    print()