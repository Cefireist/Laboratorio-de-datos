import numpy as np
import csv

"""
def generala_tirar():
    tirada = np.random.randint(1,7,5)
    return tirada
print(generala_tirar())

def cuantas_materias(n):
    path = "/home/Estudiante/Escritorio/clases/clase01/cronograma_sugerido.csv"
    with open(path, "rt") as file:
        data = csv.reader(file)
        heads = next(data)
        cuatrimestres = []
        for row in data:
            cuatrimestres.append(row[0])
    print(cuatrimestres)
    return cuatrimestres.count(str(n))

print(cuantas_materias(5))


path = "/home/Estudiante/Escritorio/clases/clase01/datame.txt"
with open(path, "rt") as file:
    for line in file:
        if "estudiante" in line:
            print(line)


path = "/home/Estudiante/Escritorio/clases/clase01/cronograma_sugerido.csv"
with open(path, "rt") as file:
    next(file)
    lista_materias = []
    for line in file:
        datos_linea = line.split(",")
        lista_materias.append(datos_linea[1])
print(lista_materias)

def materias_cuatrimestre(path, n):
    path = "/home/Estudiante/Escritorio/clases/clase01/cronograma_sugerido.csv"
    with open(path, "rt") as file:
        data = csv.DictReader(file)
        for row in data:
            print(row[""], row[""])

"""

def pisar_elemento(M,e):
    A = M.copy()
    index = 0
    for row in A:
        for i in row:
            if i == e:
                A[index,i] = -1
        index += 1
    return A
M = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(pisar_elemento(M, 2))