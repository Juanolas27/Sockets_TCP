import clases

HOST = 'localhost'
PORT = 12345
servidor = clases.servidor(HOST,PORT, 10)

while True:
    servidor.esperadorConexion()
    data = servidor.recibidorDatos()
    if data == "1":
        database = clases.database()
        database.create_user(input("Nombre del usuario: "), input("Contraseña: "), input("Email: "))
    servidor.conn.close()