import  socket
import mysql.connector
from cryptography.fernet import Fernet

class servidor:

    def __init__(self,  HOST, PORT, nConexiones):
        self.sk   = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.bind((HOST, PORT))
        self.sk.listen(nConexiones)
        self.conn = None
        self.addr = None


    def esperadorConexion(self):
        self.conn, self.addr = self.sk.accept()


    def recibidorDatos(self):
        datos = self.conn.recv(1024)
        return datos.decode('utf-8')
  

    def enviadorDatos(self, data):
        self.conn.send(("received %s" % data).encode('utf-8'))


    def cerradorConexion(self):
        self.sk.close()



class cliente:

    def __init__(self, HOST, PORT):
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.connect((HOST, PORT))
        print("Connected to %s:%d" % (HOST, PORT))


    def enviadorInformacion(self, data):
        self.sk.send(data.encode('utf-8'))


    def recibidorInformacion(self):
        data = self.sk.recv(1024)
        return data.decode('utf-8')


    def cerradorConexion(self):
        self.sk.close()



class database:
    def __init__(self):
        self.conection = mysql.connector.connect(host = "localhost", user = "root", password = "david", db = "users")
    
    def cargar_clave():
        return open("clave.key","rb").read()

    def create_user(self, username, password, email):
        self.username = username
        self.contraseña = Fernet(clave).encrypt(password.encode())
        self.email = email
        clave = Fernet.generate_key()
        with open("clave.key", "wb") as archivo_clave:
            archivo_clave.write(self.username + ":" + clave)
        pointer = self.conection.cursor()
        pointer.execute("USE users")
        pointer.execute("INSERT INTO users (nombre, contraseña, token, email) VALUES (%s, %s, %s, %s)")%(self.username, self.contraseña, clave, self.email)


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