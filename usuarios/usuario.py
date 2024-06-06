import usuarios.conexion as conexion
import datetime
import hashlib

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        password_cifrada = cifrado.hexdigest()
        
        sql = "INSERT INTO usuarios (nombre, apellido, email, password, fecha) VALUES (%s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, password_cifrada, fecha)
        
        try:
            cursor.execute(sql, usuario)
            database.commit()
            if cursor.rowcount >= 1:
                result = [cursor.rowcount, self]
            else:
                result = [0, self]
        except:
            result = [0, self]
        
        return result
    
    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        password_cifrada = cifrado.hexdigest()
        usuario = (self.email, password_cifrada)
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        return result
