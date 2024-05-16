import random
import time
import os

import Persona
import Banco


#!Archivos

def createTxt():

    # Obtener direccion actual del main
    dirActual = os.path.dirname(os.path.realpath(__file__))

    # Moverse a la carpeta registros y juntarla a la ruta de dirActual
    dirReg = os.path.join(dirActual, "logsBanco")

    if not os.path.exists(dirReg):
        os.makedirs(dirReg)

    # Construimos la ruta
    docName = os.path.join(dirReg, perso1.name + '.txt')

    # Copiamos los datos personales
    tName = perso1.name + '\n'
    tApp = perso1.app + '\n'
    tApm = perso1.apm + '\n'
    tPas = perso1.password + '\n'
    tMail = perso1.mail + '\n'
    tPhone = perso1.phone + '\n'
    tCuenta = bancoB.noCuenta + '\n'
    tClave = bancoB.clave + '\n'
    tSaldo = str(bancoB.saldo) + '\n'

    with open(docName, 'w') as doc:
        doc.write(tName)
        doc.write(tPas)

        doc.write(tCuenta)
        doc.write(tClave)
        doc.write(tSaldo)

        doc.write(tApp)
        doc.write(tApm)
        doc.write(tMail)
        doc.write(tPhone)


def readTxt(name):
    dirActual = os.path.dirname(os.path.realpath(__file__))

    # Moverse a la carpeta registros y juntarla a la ruta de dirActual
    dirReg = os.path.join(dirActual, "logsBanco")
    dirReg = os.path.join(dirReg, name)

    if os.path.exists(dirReg):
        tName = ""
        tApm = ""
        tPas = ""
        tMail = ""
        tPhone = ""
        tCuenta = ""
        tClave = ""
        tSaldo = ""

        with open(dirReg, 'r') as doc:
            tName = doc.readline().strip()
            tPas = doc.readline().strip()

            tCuenta = doc.readline().strip()
            tClave = doc.readline().strip()
            tSaldo = doc.readline().strip()

            tApp = doc.readline().strip()
            tApm = doc.readline().strip()
            tMail = doc.readline().strip()
            tPhone = doc.readline().strip()

        return tCuenta, tClave, tSaldo, tName, tPas, tApp, tApm, tMail, tPhone
    else:
        print("Archivo no encontrado")


#!Metodos


def registrar():
    op = 0

    while op != 1:
        os.system('cls')
        print("Ingrese sus datos personales\n")

        tname = input("Nombre(s): ")
        tapp = input("\nApellido paterno: ")
        tapm = input("\nApellido Materno: ")
        os.system('cls')

        print("\nIngrese la fecha de nacimiento\n")
        tday = input("Dia: ")
        tmonth = input("\nMes: ")  # metodo de validacion para solo numeros
        tyear = input("\nAno: ")

        os.system('cls')
        tmail = input("\nEmail: ")
        pas = input("\nContrasena: ")
        phone = input("\nNumero de Telefono: ")

        # Pega los datos en una variable temporal
        perso1 = Persona.Persona(tname, tapp, tapm, tday, tmonth, tyear)
        perso1.__count_init__(tmail, pas, phone)

        os.system("cls")
        print("\nVerifique sus datos\n")
        print("Nombre: ", perso1.name, end=("\n"))
        print("Apellido paterno: ", perso1.app, end=("\n"))
        print("Apellido Materno: ", perso1.apm)

        print("\nFecha de nacimiento: \n")
        print("Dia: ", perso1.day, "\tMes: ",
              perso1.month, "\tAño: ", perso1.year)

        print("\nCorreo: ", perso1.mail, "\tContrasena: ",
              perso1.password, "\tPhone Number", perso1.phone)

        print("\nDesea continuar?\n")
        op = int(input("1.-Continuar\t2.-Cancelar\n"))

    print("Datos guardados!\n")
    return perso1


def saldo():
    os.system("cls")
    print("Saldo actual: ")
    print(bancoB.saldo)
    os.system("pause")


def depositar():
    os.system("cls")
    op = 1
    dep = 0
    while op != 0:
        print("\tDepositar\n")
        print("Para salir escriba -1")
        print("1.-Realizar deposito\n")
        dep = int(input("Seleccione una opcion: "))
        if dep == -1:
            print("Operacion cancelada")
            op = 0
            os.system("pause")
        else:
            dep = int(input("Cuanto desea depositar: "))
            op = int(input("\nEsta seguro?\n1.-Continuar\t2.-Cancelar\n"))

            if op == 1:
                print("Cargando...")
                temp = int(bancoB.saldo)
                bancoB.saldo = temp + dep
                time.sleep(2)
                createTxt()
                print("Operacion realizada con exito!")
                op = 0
                os.system("pause")

            elif op == -1:
                print("Operacion cancelada")
                op = 0
                os.system("pause")


def retirar():
    os.system("cls")
    op = 1
    ret = 0
    while op != 0:
        print("\tRetirar\n")
        print("Para salir escriba -1\n")
        print("1.-Retirar\n")
        ret = int(input("Seleccione una opcion: "))
        if ret == -1:
            print("Operacion cancelada")
            op = 0
            os.system("pause")
        else:
            ret = int(input("Cuanto desea retirar: "))
            while ret > bancoB.saldo:
                print("Saldo insuficiente\n")
                ret = int(input("Cuanto desea retirar: "))
            op = int(input("\nEsta seguro?\n1.-Continuar\t2.-Cancelar\n"))
            if op == 1:
                print("Cargando...")
                temp = (bancoB.saldo)
                bancoB.saldo = temp - ret
                time.sleep(2)
                createTxt()
                print("Operacion realizada con exito!\n")
                op = 0
                os.system("pause")

            elif op == -1:
                print("Operacion cancelada\n")
                op = 0
                os.system("pause")

#!LogIn

op = 1
perso1 = Persona.Persona("", "", "", "", "", "")
bancoB = Banco.Banco(perso1)

while op != 0:
    os.system("cls")
    print("\t---Bienvenido a BancoPapuPro---\n")
    print("1.-Iniciar sesion\t\t2.-Registrarse")
    op = int(input("Seleccione una opcion: "))

    if op == 1:
        sName = input("\nIngrese su nombre: ")
        sDoc = sName + '.txt'
        sPas = input("\nIngrese su contrasena: ")

        bancoB.noCuenta, bancoB.clave, bancoB.saldo, perso1.name, perso1.pasword, perso1.app, perso1.apm, perso1.mail, perso1.phone = readTxt(
            sDoc)

        if sName == perso1.name and sPas == perso1.pasword:
            print("Inicio exitoso\n")
            op = 0
        else:
            print("Datos incorrectos\n")

        os.system("pause")

    if op == 2:
        perso1 = registrar()
        bancoB.nuevaC(perso1)
        createTxt()

        print("Su informacion bancaria: \n")
        print("clave: ", bancoB.clave, "\tcuenta: ",
              bancoB.noCuenta, "\tsaldo: ", bancoB.saldo)

        os.system("pause")


#! Main


op = 1
while op != 0:
    os.system("cls")
    print("Bienvenido ", perso1.name)
    print("Que desea realizar hoy?\n")
    op = int(input(
        "1.-Ver saldo\t2.-Depositar\t3.-Retirar\t0.-Salir\nSelecciona una opcion: "))
    if op == 1:
        saldo()
    elif op == 2:
        depositar()
    elif op == 3:
        retirar()
    elif op == 0:
        print("\nHasta luego...\n")

print("Gracias por usar BancoPapuPro!\n")
