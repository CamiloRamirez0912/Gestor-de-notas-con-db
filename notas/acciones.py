import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"{usuario[1]}, vamos a crear una nueva nota")
        titulo = input("Ingresa el titulo de tu nota: ")
        descripcion = input("Ingresa el contenido de tu nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"Se ha guardado correctamente la nota con titulo: {nota.titulo}")  # Cambiado de nota[2] a nota.titulo
        else:
            print("No se pudo guardar la nota.")
            
    def mostrar(self, usuario):
        print(f"{usuario[1]}, tus notas son: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print ("-------------------------------")
            print("Titulo: ", nota[2])
            print("Contenido: ", nota[3])
            print ("-------------------------------\n")
            
    def borrar(self, usuario):
        titulo = input(f"{usuario[1]}, ingresa el titulo de la nota que quieres borrar: ")
        nota = modelo.Nota(usuario[0])
        eliminar = nota.eliminar(titulo)
        if eliminar[0] >= 1:
            print(f"Se ha eliminado la nota con titulo: {titulo}")
        else:
            print("No se pudo borrar la nota.")
