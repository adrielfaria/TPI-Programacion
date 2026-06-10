def buscar_pais(paises):
    # Pedir el nombre a buscar y guardar los resultados
    nombre_buscado = input("Ingrese el nombre del país: ").strip().lower()
    encontrados = []

    for pais in paises:
        if nombre_buscado in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron países.")
        return

    print("\nPaíses encontrados:")

    for pais in encontrados:
        print(
            f"{pais['nombre']} | "
            f"Población: {pais['poblacion']} | "
            f"Superficie: {pais['superficie']} | "
            f"Continente: {pais['continente']}"
        )


def agregar_pais(paises):
    # Solicitar datos del país y guardarlos en la lista
    nombre = input("Nombre del país: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Ese país ya existe.")
            return

    poblacion = int(input("Población: "))
    superficie = int(input("Superficie: "))
    continente = input("Continente: ").strip()

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }

    paises.append(nuevo_pais)
    print("País agregado correctamente.")


def actualizar_pais(paises):
    # Buscar el país por nombre y actualizar sus datos
    nombre = input("Ingrese el país a actualizar: ").strip()

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais["poblacion"] = int(input("Nueva población: "))
            pais["superficie"] = int(input("Nueva superficie: "))
            print("País actualizado correctamente.")
            return

    print("País no encontrado.")