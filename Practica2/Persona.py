# Clase Persona, esta clase tiene como atributos el nombre, apellido paterno, apellido materno, correo, contraseña, telefono y fecha de nacimiento
class Persona:

    name = ""
    app = ""
    apm = ""
    mail = ""
    password = ""
    phone = ""
    day = 0
    month = 0
    year = 0

    def __init__(self, nombre, app, apm, day, month, year):
        self.name = nombre
        self.app = app
        self.apm = apm

        self.day = day
        self.month = month
        self.year = year

    def __count_init__(self, mail, pasword, phone):
        self.mail = mail
        self.password = pasword
        self.phone = phone
