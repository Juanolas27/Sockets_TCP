import  socket

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
        print(datos.decode('utf-8'))
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