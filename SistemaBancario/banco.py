# Sistema bancario utilizando el paradigma de programación orientada a objetos
from Persona import Persona
import random


class Banco(Persona):
    noCuenta = ''
    clave = ''
    saldo = 0

    def __init__(self, titular):
        self.titular = titular
        self.noCuenta = '0'
        self.saldo = 0
        self.clave = '0'

    def nuevaC(self, titular):
        self.titular = titular

        noCuenta4 = random.randint(1000, 9999)
        noCuenta8 = random.randint(1000, 9999)
        noCuenta12 = random.randint(1000, 9999)
        noCuenta16 = random.randint(1000, 9999)
        self.noCuenta = str(noCuenta4)+str(noCuenta8) + \
            str(noCuenta12)+str(noCuenta16)
        self.saldo = 0

        # Generar clave por partes
        clabe3 = random.randint(100, 999)
        clabe6 = random.randint(100, 999)
        clabe17 = random.randint(10000000000, 99999999999)
        clabe18 = random.randint(1, 9)

        self.clave = str(clabe3)+str(clabe6)+str(clabe17)+str(clabe18)
