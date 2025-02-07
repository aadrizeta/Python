import random as r

numero =r.randint(1, 100)
acertado = False

def introducirNumero():
    return int(input("Introduce un numero entre 1 y 100: "))

n = introducirNumero()
while not acertado:
    if n < numero:
        print("El número es mayor")
        n= introducirNumero()
    elif n > numero:
        print("El número es menor")
        n = introducirNumero()
    else:
        print("Has acertado")
        acertado = True



