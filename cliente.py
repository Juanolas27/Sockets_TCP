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
    recibicion = cliente.recibidorInformacion()
    if recibicion == "received 1":
        print(cliente.recibidorInformacion())
        cliente.enviadorInformacion(input("=> "))
        print(cliente.recibidorInformacion())
        cliente.enviadorInformacion(input("=> "))
        print(cliente.recibidorInformacion())
        cliente.enviadorInformacion(input("=> "))

    elif recibicion == "received 2":
        print(cliente.recibidorInformacion())
        cliente.enviadorInformacion(input("=> "))
        cliente.enviadorArchivo(input("=> "))
    
    elif recibicion == "received 3":
        print(cliente.recibidorInformacion())
        cliente.enviadorInformacion(input("=> "))
        cliente.descargarArchivo(input("Que nombre quieres en el archivo\n=> "))
    
    elif recibicion == "received 4":
        print(cliente.recibidorInformacion())
        cliente.enviadorInformacion(input("=> "))
    
    elif recibicion == "received 5":
        print(cliente.recibidorInformacion())
        cliente.enviadorInformacion(input("=> "))
        cliente.enviadorInformacion(input("=> "))

    elif recibicion == "received 6":
        print(cliente.recibidorInformacion())
        cliente.enviadorInformacion(input("=> "))
    cliente.cerradorConexion()
    
    break


