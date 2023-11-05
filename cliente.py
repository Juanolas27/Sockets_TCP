import clases

HOST = 'localhost'
PORT = 12345

cliente = clases.cliente(HOST, PORT)


while True:

    print('''
        1. Create User
        2. Upload File
        3. Download File
        4. Delete File
        5. Create sub folder
        6. Delete User
    ''')
    pija = False
    cliente.enviadorInformacion(input("Qué quieres que haga (1, 2, 3, 4, 5 or 6): "))
    if cliente.recibidorInformacion() == "1":

        nombre = input("Nombre: ")
        contrasena = input("Contrasena: ")
        email = input("Email: ")
        array = [nombre, contrasena, email]
        for mensaje in array:
            cliente.enviadorInformacion(mensaje)


    cliente.cerradorConexion()


