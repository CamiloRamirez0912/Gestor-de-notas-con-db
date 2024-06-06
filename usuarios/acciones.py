import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("Ingresando al sistema de registro")
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu contraseña: ")
        
        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"Te has registrado con el email {registro[1].email}")
        else:
            print("No te registraste correctamente")
        
    def login(self):
        print("Ingresando al sistema de login")
        try:
            email = input("Ingresa tu email: ")
            password = input("Ingresa tu contraseña: ")

            usuario = modelo.Usuario("","", email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el dia {login[5]}")
                if self.proximasAcciones(login):
                    return
        except Exception as e:
            print(f"El correo o contraseña son incorrectos. Error: {e}")
            
    def proximasAcciones(self, usuario):
        while True:
            print("""
            Opciones disponibles:
            Opcion 1: Crear nota.
            Opcion 2: Mostrar notas.
            Opcion 3: Eliminar nota.
            Opcion 4: Salir.  
            """)
            accion = input("Ingresa la accion que deseas realizar: ").lower()
            make = notas.acciones.Acciones()
            
            if accion == "crear":
                make.crear(usuario)
            elif accion == "mostrar":
                make.mostrar(usuario)
            elif accion == "eliminar":
                make.borrar(usuario)
            elif accion == "salir":
                print(f"Nos vemos pronto, {usuario[1]}")
                return True
            else:
                print("Acción no reconocida, por favor intenta de nuevo.")