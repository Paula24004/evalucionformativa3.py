#Autor: Paula Leiva
#seccion 001D

import os

# Definición de la colección de cargos
cargos = ["CEO", "Desarrollador", "Analista de datos"]
trabajadores = []

# Función para verificar si una cadena contiene solo letras
def contiene_solo_letras(cadena):
    return cadena.replace(" ", "").isalpha()

# Función para verificar si el cargo es válido
def es_cargo_valido(cargo):
    return cargo.upper() in [c.upper() for c in cargos]

# Función para validar el formato del sueldo
def validar_sueldo(sueldo):
    sueldo_sin_signo = sueldo.replace("$", "").replace(".", "")
    return sueldo_sin_signo.isdigit()

# Registrar trabajador
while True:
    nombre = input("Ingrese el nombre del trabajador: ")
    while not contiene_solo_letras(nombre):
        print("Nombre inválido. El nombre no puede contener números.")
        nombre = input("Ingrese el nombre del trabajador: ")

    apellido = input("Ingrese el apellido del trabajador: ")
    while not contiene_solo_letras(apellido):
        print("Apellido inválido. El apellido no puede contener números.")
        apellido = input("Ingrese el apellido del trabajador: ")

    print("Cargos disponibles:")
    for i, cargo in enumerate(cargos, 1):
        print(f"{i}. {cargo}")

    cargo_index = input("Seleccione el número correspondiente al cargo del trabajador: ")
    while not cargo_index.isdigit() or int(cargo_index) not in range(1, len(cargos) + 1):
        print("Seleccione un número válido.")
        cargo_index = input("Seleccione el número correspondiente al cargo del trabajador: ")

    cargo = cargos[int(cargo_index) - 1]

    sueldo_bruto = input("Ingrese el sueldo bruto del trabajador con $ y puntos: ")
    while not validar_sueldo(sueldo_bruto):
        print("Sueldo inválido. El formato correcto es $X.XXX.XXX.")
        sueldo_bruto = input("Ingrese el sueldo bruto del trabajador con $ y puntos: ")

    sueldo_bruto = float(sueldo_bruto.replace("$", "").replace(".", ""))
    desc_salud = 0.07 * sueldo_bruto
    desc_afp = 0.12 * sueldo_bruto
    liquido_pagar = sueldo_bruto - desc_salud - desc_afp
    trabajadores.append({'Nombre': nombre, 'Apellido': apellido, 'Cargo': cargo, 'Sueldo Bruto': sueldo_bruto,
                         'Descuento Salud': desc_salud, 'Descuento AFP': desc_afp, 'Líquido a pagar': liquido_pagar})
    continuar = input("¿Desea registrar otro trabajador? (s/n): ")
    if continuar.lower() != 's':
        break

# Preguntar al usuario si desea imprimir la planilla
imprimir_planilla = input("¿Desea imprimir la planilla de sueldos? (s/n): ").lower()
if imprimir_planilla == 's':
    imprimir_todos = input("¿Desea imprimir la planilla para todos los trabajadores o solo para un cargo específico? (todos/cargo): ").lower()
    if imprimir_todos == 'todos':
        print("Planilla de sueldos para todos los trabajadores:")
        for trabajador in trabajadores:
            print("Nombre:", trabajador['Nombre'], trabajador['Apellido'])
            print("Cargo:", trabajador['Cargo'])
            print("Sueldo Bruto: ${:,.2f}".format(trabajador['Sueldo Bruto']))
            print("Descuento Salud: ${:,.2f}".format(trabajador['Descuento Salud']))
            print("Descuento AFP: ${:,.2f}".format(trabajador['Descuento AFP']))
            print("Líquido a pagar: ${:,.2f}".format(trabajador['Líquido a pagar']))
            print("-----------------------------")
    else:
        print("Cargos disponibles:")
        for i, cargo in enumerate(cargos, 1):
            print(f"{i}. {cargo}")

        cargo_index = input("Seleccione el número correspondiente al cargo para imprimir la planilla: ")
        while not cargo_index.isdigit() or int(cargo_index) not in range(1, len(cargos) + 1):
            print("Seleccione un número válido.")
            cargo_index = input("Seleccione el número correspondiente al cargo para imprimir la planilla: ")

        cargo_seleccionado = cargos[int(cargo_index) - 1]

        print(f"Planilla de sueldos para el cargo {cargo_seleccionado}:")
        for trabajador in trabajadores:
            if trabajador['Cargo'] == cargo_seleccionado:
                print("Nombre:", trabajador['Nombre'], trabajador['Apellido'])
                print("Cargo:", trabajador['Cargo'])
                print("Sueldo Bruto: ${:,.2f}".format(trabajador['Sueldo Bruto']))
                print("Descuento Salud: ${:,.2f}".format(trabajador['Descuento Salud']))
                print("Descuento AFP: ${:,.2f}".format(trabajador['Descuento AFP']))
                print("Líquido a pagar: ${:,.2f}".format(trabajador['Líquido a pagar']))
                print("-----------------------------")

print("Se ha generado la planilla de sueldos correctamente.")