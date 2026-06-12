from validaciones import pedir_numero   # Se importa la función pedir_numero desde el módulo validaciones


def mostrar_menu():

    print("\n===== GESTIÓN DE PAÍSES =====")
    print("1) Agregar país")
    print("2) Actualizar país")
    print("3) Buscar país")
    print("4) Filtrar países")
    print("5) Ordenar países")
    print("6) Mostrar estadísticas")
    print("0) Salir")

    opcion = pedir_numero("\nSeleccione una opción: ")

    return int(opcion)