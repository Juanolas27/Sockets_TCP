import clases

HOST = 'localhost'
PORT = 12345
servidor = clases.servidor(HOST,PORT, 10)

while True:
    servidor.esperadorConexion()
    data = servidor.recibidorDatos()
    if data == "1":
        servidor.enviadorDatos(data) 
        print(data)
        data = servidor.recibidorDatos()
        nombre = data[0]
        contrasena = data[1]
        correo = data[2]
        print(data, nombre, contrasena, correo)
        database = clases.database()
        database.create_user(nombre, contrasena, correo)
    servidor.conn.close()