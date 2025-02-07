"""
Agua: 0.50€
Refresco: 0.75€
zumo: 0.95€
"""
import decimal
valoresMonedas = [0.05, 0.10, 0.20, 0.50, 1, 2]
reservaMonedas = [20, 20, 20, 20, 20, 20]
stockMaquina = [3, 3, 3]



menu = True

def comprobarStock(prodcto, stock):
    if stock != 0:
        return True
    else:
        print(f"No hay stock disponible de {prodcto}")
        return False


def despedida():
    print("Gracias por su compra. Espero que tenga un buen día.")


def continuar():
    ok = True
    while ok:
        respuesta = input("¿Desea comprar otro producto? (s/n): \n").lower()
        if respuesta == "s":
            return False
        elif respuesta == "n":
            return True
        else:
            print("Opción no válida. Vuelva a intentarlo.")



def menuMaquina():
    opcion = int(input("Bienvenido a la máquina expendedora. \nSeleccione el producto que desee:\n1.Agua: 0.50€\n2.Refresco: 0.75€\n3.Zumo: 0.95€\n4.Salir\n"))
    return opcion

def introducirMonedas(producto, precio):
    saldo = 0
    print(f"El precio de {producto} es {precio}€")
    while saldo < precio:
        try:
            monedaIntroducida = float(input(
                f"Saldo actual: {round(saldo, 2)}€\nIntroduzca el valor de moneda (0.05, 0.10, 0.20, 0.50, 1, 2): \n"))
            if monedaIntroducida in valoresMonedas:
                saldo = round(saldo + monedaIntroducida, 2)
                indice = valoresMonedas.index(monedaIntroducida)
                reservaMonedas[indice] += 1
            else:
                print("Moneda no válida.")
        except ValueError:
            print("Por favor, introduzca un valor numérico válido.")
    print(f"Que disfrute su {producto}")
    print(f"Saldo introducido: {saldo}")
    cambio = round(saldo - precio, 2)
    if cambio != 0:
        calcularCambio(cambio)
    else:
        print("Saldo exacto")


def calcularCambio(cambio):
    cambio = round(cambio, 2)
    print(f"Su cambio es: {cambio}€")
    monedasCambio = []

    for i in reversed(valoresMonedas):
        while cambio >= i:
            monedasCambio.append(i)
            cambio = round(cambio - i, 2)
    for moneda in monedasCambio:
        print(f"Moneda de {moneda}€")


while menu:
    try:
        opcion = menuMaquina()
        if opcion == 1:
            if comprobarStock("Agua", stockMaquina[0]):
                stockMaquina[0] -= 1
                introducirMonedas("Agua", 0.50)
                if continuar():
                    despedida()
                    menu = False
        elif opcion == 2:
            stockMaquina[1] -= 1
            introducirMonedas("Refresco", 0.75)
            if continuar():
                despedida()
                menu = False
        elif opcion == 3:
            stockMaquina[2] -= 1
            introducirMonedas("Zumo", 0.95)
            if continuar():
                despedida()
                menu = False
        elif opcion == 4:
            despedida()
            menu = False
        else:
            print("Opción incorrecta. Intente nuevamente.")
    except ValueError:
        print("Por favor, introduzca un valor numérico válido.")


