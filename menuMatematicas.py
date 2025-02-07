
def calcularBisiesto():
    year = int(input("Introduce año: \n"))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} es un año bisiesto.")
    else:
        print(f"{year} no es un año bisiesto.")

def calcularNumeroPrimo():
    numero = int(input("Introduce un número: \n"))
    if numero <= 1:
        print("No es un número primo.")
    else:
        for i in range(2, numero):
            if numero % i == 0:
                print("No es un número primo.")
                return False
        print(f"{numero} Es es un número primo.")
        return True
def calcularNumeroPar():
    numero = int(input("Introduce un número: \n"))
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

ok = True
while ok:
    print("Elige una opción: ")
    print("1. Calcular numero primo")
    print("2. Calcular numero par")
    print("3. Calcular año bisiesto")
    print("4. Salir")
    opcion = int(input("Opcion: "))
    if opcion > 4 or opcion <= 0:
        print("Opción incorrecta.")
    elif opcion == 1:
        calcularNumeroPrimo()
    elif opcion == 2:
        calcularNumeroPar()
    elif opcion == 3:
        calcularBisiesto()
    elif opcion == 4 :
        print("Gracias por utilizar el programa.")
        ok = False