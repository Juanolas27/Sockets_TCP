import clases

HOST = 'localhost'
PORT = 12345
servidor = clases.servidor(HOST,PORT, 10)

while True:
    servidor.esperadorConexion()
    servidor.enviadorDatos(servidor.recibidorDatos())