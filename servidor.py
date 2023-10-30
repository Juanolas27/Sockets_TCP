import clases

HOST = 'localhost'
PORT = 12345
servidor = clases.servidor(HOST,PORT, 10)

while True:
    servidor.esperadorConexion()
    data = servidor.recibidorDatos()
    if data == 1:
        username = input("Nombre del usuario: ")
        password = input("Contraseña: ")
        email = input("Email: ")
        database = clases.database
        database.create_user(username, password, email)
