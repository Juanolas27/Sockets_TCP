import clases

HOST = 'localhost'
PORT = 12345
servidor = clases.servidor(HOST,PORT, 10)

while True:
    
    servidor.esperadorConexion()
    data = servidor.recibidorDatos()
    print(data)

    if data == "1":
        servidor.enviadorDatos(data) 
        servidor.enviadorDatos("Nombre")
        nombre = servidor.recibidorDatos()
        servidor.enviadorDatos("Contrasena")
        contrasena = servidor.recibidorDatos()
        servidor.enviadorDatos("Email")
        correo = servidor.recibidorDatos()
        print(nombre, contrasena, correo)
        database = clases.database()
        database.create_user(nombre, contrasena, correo)
    
    if data  ==  "2":
        
        

        pass
    if data  ==  "3":
        pass
    if data  ==  "4":
        pass
    if data  ==  "5":
        pass
    if data  ==  "6":
        pass
    servidor.conn.close()