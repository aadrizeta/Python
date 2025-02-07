numeroUsuario = input("Introduce un numero: ")

numeroInvertido = numeroUsuario[::-1]

if numeroUsuario == numeroInvertido:
    print("El numero es capicua.")
else:
    print("El numero no es capicua.")