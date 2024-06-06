from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")

accion = input("¿Que quieres hacer?: ").lower()
make = acciones.Acciones()

if accion == "registro":
    make.registro()
elif accion == "login":
    make.login()
else:
    print("Acción no reconocida")
