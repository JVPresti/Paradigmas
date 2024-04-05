class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 0
        self.clientes = []

    def abrirCuenta(self, cliente):
        self.clientes.append(cliente)

    def cerrarCuenta(self, cliente):
        self.clientes.remove(cliente)

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

    def __len__(self):
        return len(self.clientes)

    def __getitem__(self, item):
        return self.clientes[item]

    def __setitem__(self, key, value):
        self.clientes[key] = value

    def __delitem__(self, key):
        del self.clientes[key]

    def __iter__(self):
        return iter(self.clientes)

    def __next__(self):
        return next(self.clientes)
    
    def crearContrasena(self, cliente, contrasena):
        cliente.contrasena = contrasena
    
    def validarContrasena(self, cliente, contrasena):
        if cliente.contrasena == contrasena:
            return True
        else:
            return False
    
    def transferir(self, cuentaOrigen, cuentaDestino, monto):
        if cuentaOrigen.saldo >= monto:
            cuentaOrigen.retirar(monto)
            cuentaDestino.depositar(monto)
        else:
            print("Saldo insuficiente")
        
    def retirar(self, cuenta, monto):
        if cuenta.saldo >= monto:
            cuenta.retirar(monto)
        else:
            print("Saldo insuficiente")
    
    def depositar(self, cuenta, monto):
        self.saldo += monto


    
class Cliente:
    def __init__(self, nombre, apellido, contrasena): 
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena
        self.cuentas = []

    def abrirCuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def cerrarCuenta(self, cuenta):
        self.cuentas.remove(cuenta)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def __repr__(self):
        return f'{self.nombre} {self.apellido}'

    def __len__(self):
        return len(self.cuentas)

    def __getitem__(self, item):
        return self.cuentas[item]

    def __setitem__(self, key, value):
        self.cuentas[key] = value

    def __delitem__(self, key):
        del self.cuentas[key]

    def __iter__(self):
        return iter(self.cuentas)

    def __next__(self):
        return next(self.cuentas)
    
    def crearContrasena(self, contrasena):
        self.contrasena = contrasena