import gc

from clases.vehiculos import Vehiculo, Coche, Moto


def mostrar_menu():
    """
    Muestra las opciones disponibles del sistema.
    """

    print("\n========================================")
    print("  🚗 SISTEMA DE GESTIÓN DE VEHÍCULOS 🏍️")
    print("========================================")
    print("1. Registrar coche")
    print("2. Registrar moto")
    print("3. Mostrar flota")
    print("4. Encender/Apagar vehículo")
    print("5. Calcular alquiler")
    print("6. Alquilar vehículo")
    print("7. Devolver vehículo")
    print("8. Ver estadísticas")
    print("9. Dar de baja vehículo")
    print("10. Salir")
    print("========================================")


def solicitar_texto(mensaje):
    """
    Solicita una cadena no vacía.
    """

    texto = input(mensaje).strip()

    if not texto:
        raise ValueError("Este dato no puede estar vacío.")

    return texto


def solicitar_entero(mensaje):
    """
    Solicita un número entero.
    """

    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError(
            "Debe ingresar un número entero."
        )


def solicitar_numero(mensaje):
    """
    Solicita un número decimal o entero.
    """

    try:
        return float(input(mensaje))
    except ValueError:
        raise ValueError(
            "Debe ingresar un valor numérico."
        )


def registrar_coche(flota):
    """
    Solicita los datos y registra un coche.
    """

    print("\n--- REGISTRAR COCHE ---")

    marca = solicitar_texto("Marca: ")
    modelo = solicitar_texto("Modelo: ")
    año = solicitar_entero("Año: ")
    precio_base = solicitar_numero(
        "Precio base por día: $"
    )
    num_puertas = solicitar_entero(
        "Número de puertas: "
    )

    coche = Coche(
        marca,
        modelo,
        año,
        precio_base,
        num_puertas
    )

    flota.append(coche)


def registrar_moto(flota):
    """
    Solicita los datos y registra una moto.
    """

    print("\n--- REGISTRAR MOTO ---")

    marca = solicitar_texto("Marca: ")
    modelo = solicitar_texto("Modelo: ")
    año = solicitar_entero("Año: ")
    precio_base = solicitar_numero(
        "Precio base por hora: $"
    )
    cilindrada = solicitar_entero(
        "Cilindrada en cc: "
    )

    moto = Moto(
        marca,
        modelo,
        año,
        precio_base,
        cilindrada
    )

    flota.append(moto)


def mostrar_flota(flota):
    """
    Muestra todos los vehículos mediante polimorfismo.
    """

    if not flota:
        print("\n⚠️ No hay vehículos registrados.")
        return

    print("\n========== FLOTA REGISTRADA ==========")

    for indice, vehiculo in enumerate(flota, start=1):
        print(f"\nVehículo número {indice}")
        print("--------------------------------------")

        # Polimorfismo:
        # Python decide qué versión de mostrar_info()
        # ejecutar según el tipo real del objeto.
        vehiculo.mostrar_info()

    print("\n======================================")


def seleccionar_vehiculo(flota):
    """
    Solicita y valida el índice de un vehículo.
    """

    if not flota:
        raise ValueError(
            "No hay vehículos registrados en la flota."
        )

    print("\nVehículos disponibles en el sistema:")

    for indice, vehiculo in enumerate(flota, start=1):
        tipo = type(vehiculo).__name__

        print(
            f"{indice}. {vehiculo.marca} "
            f"{vehiculo.modelo} - {tipo}"
        )

    posicion = solicitar_entero(
        "Seleccione el número del vehículo: "
    )

    if posicion < 1 or posicion > len(flota):
        raise IndexError(
            "El índice seleccionado está fuera de rango."
        )

    return posicion - 1


def cambiar_estado_motor(flota):
    """
    Enciende o apaga el vehículo seleccionado.
    """

    posicion = seleccionar_vehiculo(flota)
    vehiculo = flota[posicion]

    if vehiculo.encendido:
        vehiculo.apagar()
    else:
        vehiculo.encender()


def calcular_alquiler(flota):
    """
    Calcula el costo mediante polimorfismo.
    """

    posicion = seleccionar_vehiculo(flota)
    vehiculo = flota[posicion]

    if not vehiculo.disponible:
        raise ValueError(
            "No se puede calcular el alquiler porque "
            "el vehículo no está disponible."
        )

    if isinstance(vehiculo, Coche):
        tiempo = solicitar_numero(
            "Ingrese la cantidad de días: "
        )
        unidad = "día(s)"

    elif isinstance(vehiculo, Moto):
        tiempo = solicitar_numero(
            "Ingrese la cantidad de horas: "
        )
        unidad = "hora(s)"

    else:
        raise TypeError(
            "El tipo de vehículo no es reconocido."
        )

    # Polimorfismo:
    # El mismo método ejecuta una fórmula diferente
    # dependiendo de si el objeto es Coche o Moto.
    costo = vehiculo.calcular_alquiler(tiempo)

    print("\n========== CÁLCULO DE ALQUILER ==========")
    print(
        f"Vehículo: {vehiculo.marca} "
        f"{vehiculo.modelo}"
    )
    print(f"Tiempo: {tiempo:g} {unidad}")
    print(f"Costo total: ${costo:.2f}")
    print("=========================================")


def alquilar_vehiculo(flota):
    """
    Alquila el vehículo seleccionado.
    """

    posicion = seleccionar_vehiculo(flota)
    vehiculo = flota[posicion]

    vehiculo.alquilar()


def devolver_vehiculo(flota):
    """
    Devuelve el vehículo seleccionado.
    """

    posicion = seleccionar_vehiculo(flota)
    vehiculo = flota[posicion]

    vehiculo.devolver()


def ver_estadisticas(flota):
    """
    Muestra las estadísticas actuales de la flota.
    """

    total = Vehiculo.total_vehiculos()

    encendidos = sum(
        1 for vehiculo in flota
        if vehiculo.encendido
    )

    coches = sum(
        1 for vehiculo in flota
        if isinstance(vehiculo, Coche)
    )

    motos = sum(
        1 for vehiculo in flota
        if isinstance(vehiculo, Moto)
    )

    disponibles = sum(
        1 for vehiculo in flota
        if vehiculo.disponible
    )

    alquilados = sum(
        1 for vehiculo in flota
        if not vehiculo.disponible
    )

    print("\n========== ESTADÍSTICAS ==========")
    print(f"Total de vehículos: {total}")
    print(f"Vehículos encendidos: {encendidos}")
    print(f"Coches registrados: {coches}")
    print(f"Motos registradas: {motos}")
    print(f"Vehículos disponibles: {disponibles}")
    print(f"Vehículos alquilados: {alquilados}")
    print("==================================")


def dar_de_baja(flota):
    """
    Elimina un vehículo de la flota.
    """

    posicion = seleccionar_vehiculo(flota)
    vehiculo = flota[posicion]

    marca = vehiculo.marca
    modelo = vehiculo.modelo

    # Se elimina el objeto de la lista.
    del flota[posicion]

    # Se elimina la referencia local.
    del vehiculo

    # Fuerza la recolección de basura para ejecutar
    # el destructor durante la demostración.
    gc.collect()

    print(
        f"✅ {marca} {modelo} fue eliminado de la flota."
    )


def limpiar_flota(flota):
    """
    Elimina todos los vehículos al cerrar el programa.
    """

    while flota:
        vehiculo = flota.pop()
        del vehiculo

    gc.collect()


def main():
    """
    Función principal del programa.
    """

    flota = []

    while True:
        mostrar_menu()

        try:
            opcion = solicitar_entero(
                "Seleccione una opción: "
            )

            if opcion == 1:
                registrar_coche(flota)

            elif opcion == 2:
                registrar_moto(flota)

            elif opcion == 3:
                mostrar_flota(flota)

            elif opcion == 4:
                cambiar_estado_motor(flota)

            elif opcion == 5:
                calcular_alquiler(flota)

            elif opcion == 6:
                alquilar_vehiculo(flota)

            elif opcion == 7:
                devolver_vehiculo(flota)

            elif opcion == 8:
                ver_estadisticas(flota)

            elif opcion == 9:
                dar_de_baja(flota)

            elif opcion == 10:
                print("\nCerrando el sistema...")

                limpiar_flota(flota)

                print(
                    "👋 Gracias por utilizar el sistema "
                    "de gestión de vehículos."
                )
                break

            else:
                print(
                    "\n⚠️ Opción no válida. "
                    "Seleccione una opción del 1 al 10."
                )

        except ValueError as error:
            print(f"\n❌ Error: {error}")

        except IndexError as error:
            print(f"\n❌ Error: {error}")

        except TypeError as error:
            print(f"\n❌ Error: {error}")

        except Exception as error:
            print(
                f"\n❌ Ocurrió un error inesperado: {error}"
            )


if __name__ == "__main__":
    main()