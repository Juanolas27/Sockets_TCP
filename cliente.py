import clases

HOST = 'localhost'
PORT = 12345

cliente = clases.cliente(HOST, PORT)

cliente.enviadorInformacion("Mamame la pinga")

data = cliente.recibidorInformacion()
print(data)
cliente.cerradorConexion()
