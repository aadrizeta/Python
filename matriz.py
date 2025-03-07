def crearMatriz(n):
    tabla = [[1 if i % 2 == 0 else 0 for i in range(n)] for j in range(n)]
    for fila in tabla:
        print(fila)
def crearMatrizDiagonal(n):
    tabla = [[1 if i + j == n - 1 else 0 for i in range(n)] for j in range(n)]
    for fila in tabla:
        print(fila)

def crearMatrizNoCuadrada(n, m):
    tabla = [[1 if i % 2 == 0 else 0 for i in range(n)] for j in range(m)]
    for fila in tabla:
        print(fila)

def capturarValores():
    valor = int(input("Introduzca un valor: \n"))
    return valor

def crearMatrizPorTeclado():
    matriz = [[capturarValores() for i in range(4)] for j in range(4)]
    for fila in matriz:
        print(fila)

crearMatrizPorTeclado()