"""IRPF 12% SS 5.2%"""

"""def introducirTrabajador():
    # Pedir los datos del trabajador
    nombre = input("Nombre: ")
    sueldo_base = float(input("Sueldo base: "))

salir = False"""
def calcularIRPF(salarioBruto):
    return salarioBruto * 0.12


def calcularSS(salarioBruto):
    return salarioBruto * 0.052


def calcularSueldoNeto(salarioBruto):
    irpf = salarioBruto *0.12
    ss = salarioBruto * 0.052
    return salarioBruto -irpf -ss


print("Introduce el nombre y el salario bruto: ")
nombreTrabajador = input("Nombre: ")
sueldoBaseTrabajador = float(input("Sueldo base: "))

sueldoNeto = calcularSueldoNeto(sueldoBaseTrabajador)

print(f"{nombreTrabajador} cobra: {sueldoNeto}")

