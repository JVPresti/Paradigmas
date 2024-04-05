# Sistema bancario utilizando el paradigma de programación orientada a objetos
# Importar la clase Cuenta
import clases

# Crear una cuenta
cliente1= clases.Cliente('Juan', 'Perez', "ejemplo")
cuenta1= clases.Banco(cliente1)
clases.Banco.abrirCuenta(cuenta1, cliente1)

cliente2 = clases.Cliente('Maria', 'Lopez', "ejemplo")
cuenta2 = clases.Banco(cliente2)
clases.Banco.abrirCuenta(cuenta2, cliente2)

print(cuenta1.saldo)
clases.Banco.depositar(cuenta1, 1000, 500)
print(cuenta1.saldo)
