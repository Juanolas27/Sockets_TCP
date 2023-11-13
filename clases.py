import socket
import mysql.connector
from cryptography.fernet import Fernet
import os

class servidor:

    def __init__(self,  HOST, PORT, nConexiones):
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.bind((HOST, PORT))
        self.sk.listen(nConexiones)


    def esperadorConexion(self):
        self.conn, self.addr = self.sk.accept()


    def recibidorDatos(self):
        return self.conn.recv(1024).decode('utf-8')

    def recibidorArchivo(self, NombreUsuario):
        file_name = self.conn.recv(1024).decode('utf-8')
        file_size = self.conn.recv(1024).decode('utf-8')
        print(file_size)
        with open("C:\Escritorio\Clase\Servidor\TCP\{}\{}".format(NombreUsuario, file_name), 'wb') as file:
            data = self.conn.recv(1024)
            
            while data:
                file.write(data)
                data = self.conn.recv(1024)
    
    def enviarArchivo(self, rutaArchivo):
        with open (rutaArchivo, "rb") as file:
            data = file.read(1024)
            while data:
                self.conn.send(data)
                data = file.read(1024)


    def enviadorDatos(self, data):
        self.conn.sendall(("received %s" % data).encode('utf-8'))
    
    def borrarArchivo(self, ruta):
        if os.path.exists(ruta):
            os.remove(ruta)
        else:
            print("The file doesn't exist")


    def cerradorConexion(self):
        self.conn.close()



class cliente:

    def __init__(self, HOST, PORT):
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.connect((HOST, PORT))
        print("Connected to %s:%d" % (HOST, PORT))


    def enviadorInformacion(self, data):
        self.sk.sendall(data.encode('utf-8'))



    def  enviadorArchivo(self, rutaArchivo):
        file = open(rutaArchivo, "rb")
        file_size = os.path.getsize(rutaArchivo)
        file_name = input("Nombre del archivo => ")
        self.sk.send(file_name.encode('utf-8'))
        self.sk.send(str(file_size).encode('utf-8'))
        file_data = file.read(1024)

        while file_data:
            self.sk.send(file_data)
            file_data = file.read(1024)
        
        file.close()


    def recibidorInformacion(self):
        return self.sk.recv(1024).decode('utf-8')


    def cerradorConexion(self):
        self.sk.close()
    

    def descargarArchivo(self, NombreArchivo):
        ruta_guardado = input("Donde quieres que se guarde el archivo, escribe la ruta completa => ")

        with open("{}\{}".format(ruta_guardado, NombreArchivo), "wb") as f:
            data = self.sk.recv(1024)

            while data:
                f.write(data)
                data = self.sk.recv(1024)




class database:
    def __init__(self):
        self.conection = mysql.connector.connect(host = "localhost", user = "root", password = "david", db = "users")
    
    def cargar_clave():
        return open("clave.key","rb").read()

    def create_user(self, username, password, email):
        self.username = username
        clave = Fernet.generate_key()
        self.contraseña = Fernet(clave).encrypt(password.encode())
        self.email = email
        with open("clave.key", "a") as archivo_clave:
            archivo_clave.write(self.username + ":" + clave.decode("utf-8")+"\n")
        pointer = self.conection.cursor()
        pointer.execute("USE users")
        query1 = ("INSERT INTO usuarios (nombre, contraseña, email) VALUES (%s, %s, %s)")
        query2 = (self.username, self.contraseña, self.email)
        pointer.execute(query1, query2)
        self.conection.commit()
        os.mkdir(username)

    def forgot_password(self, username):
        with open("clave.key", "r") as fichero:
            for linea in fichero.readlines():
                if username in linea:
                    key = linea.split(":")[1]
        f = Fernet(key)
        pointer = self.connection.cursor()
        pointer.execute("USE users")
        pointer.execute("SELECT contraseña FROM users WHERE nombre = '%s'" % username)
        pass_encrypt = pointer.fetchall()[0]
        print(f.decrypt(pass_encrypt))