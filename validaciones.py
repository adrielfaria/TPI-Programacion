# Funcion la cual validara que el usuario ingrese solamente letras para los input que asi lo requieran y lo mantendra dentro de un bucle while en caso de ingresar un valor invalido.
def pedir_texto(mensaje: str) -> str:
    while True:
        valor = input(mensaje)
        if valor.replace(' ', '').isalpha():
            return valor.title()
        print("Solo se permiten letras, intentá de nuevo.")

# Funcion la cual validara que el usuario ingrese solamente numeros para los input que asi lo requieran y lo mantendra dentro de un bucle while en caso de ingresar un valor invalido.
def pedir_numero(mensaje: str) -> str:
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return valor
        print("Solo se permiten números enteros, intentá de nuevo.")