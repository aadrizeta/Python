irpfEstado = 0
ssEstado = 0
listaTrabajadores= []
listaDeSalarios= []

def introducir_nombre_trabajador():
    nombre = input("Introduce el nombre del trabajador: \n")
    listaTrabajadores.append(nombre)
    return nombre
def introducir_salario():
    salario = float(input("Introduce el salario bruto: \n"))
    listaDeSalarios.append(salario)
    return salario
def calcularSueldoNeto(salarioBruto):
    irpf = salarioBruto *0.12
    global irpfEstado
    irpf = salarioBruto * 0.12
    irpfEstado += irpf
    ss = salarioBruto * 0.052
    global ssEstado
    ss = salarioBruto * 0.052
    ssEstado += ss
    return salarioBruto -irpf -ss

print(f"{introducir_nombre_trabajador()} cobra {calcularSueldoNeto(introducir_salario())}")

continuar = True
while continuar :
    cont = input("¿Desea calcular el sueldo de otro trabajador? (s/n): \n").lower()
    if cont == "s" :
        print(f"{introducir_nombre_trabajador()} cobra {calcularSueldoNeto(introducir_salario())}")
    elif cont == "n":
        print("Gracias por utilizar este programa.")
        print(f"El estado se ha llevado {irpfEstado} en IRPF y {ssEstado} en Cuotas a la seguridad social")
        continuar = False
    else:
        print("Opción incorrecta. Debe escoger s o n.")
