from datetime import datetime


class Vehiculo:
    """
    Clase base que representa un vehículo general.
    """

    # Atributo de clase
    _contador_vehiculos = 0

    def __init__(self, marca, modelo, año, precio_base):
        """
        Constructor de la clase Vehiculo.
        """

        if not self.validar_año(año):
            raise ValueError("El año del vehículo no es válido.")

        if not self.validar_precio(precio_base):
            raise ValueError("El precio base debe ser un número positivo.")

        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_base = precio_base

        # Atributos protegidos
        self._encendido = False
        self._disponible = True

        # Evita que el contador disminuya más de una vez
        self._dado_de_baja = False

        Vehiculo._contador_vehiculos += 1

        print(
            f"🚗 Vehículo registrado: "
            f"{self.marca} {self.modelo} ({self.año})"
        )

    def __del__(self):
        """
        Destructor de la clase Vehiculo.
        """

        # Se utiliza getattr porque el destructor también puede ejecutarse
        # cuando el constructor no terminó correctamente.
        if (
            hasattr(self, "marca")
            and hasattr(self, "modelo")
            and not getattr(self, "_dado_de_baja", True)
        ):
            print(
                f"🗑️ {self.marca} {self.modelo} "
                f"ha sido dado de baja."
            )

            if Vehiculo._contador_vehiculos > 0:
                Vehiculo._contador_vehiculos -= 1

            self._dado_de_baja = True

    @property
    def encendido(self):
        """
        Propiedad de solo lectura que devuelve el estado del motor.
        """
        return self._encendido

    @property
    def disponible(self):
        """
        Propiedad de solo lectura que devuelve la disponibilidad.
        """
        return self._disponible

    def encender(self):
        """
        Enciende el motor del vehículo.
        """

        if self._encendido:
            print(
                f"⚠️ {self.marca} {self.modelo}: "
                f"El motor ya estaba encendido."
            )
        else:
            self._encendido = True
            print(
                f"🔑 {self.marca} {self.modelo}: "
                f"Motor encendido."
            )

    def apagar(self):
        """
        Apaga el motor del vehículo.
        """

        if not self._encendido:
            print(
                f"⚠️ {self.marca} {self.modelo}: "
                f"El motor ya estaba apagado."
            )
        else:
            self._encendido = False
            print(
                f"🔒 {self.marca} {self.modelo}: "
                f"Motor apagado."
            )

    def calcular_alquiler(self, tiempo):
        """
        Método que será redefinido por las clases derivadas.
        """

        raise NotImplementedError(
            "El método calcular_alquiler() debe redefinirse "
            "en las clases derivadas."
        )

    def mostrar_info(self):
        """
        Muestra la información común del vehículo.
        """

        estado_motor = (
            "Encendido" if self._encendido else "Apagado"
        )

        estado_disponibilidad = (
            "Disponible" if self._disponible else "Alquilado"
        )

        print(f" Marca: {self.marca}")
        print(f" Modelo: {self.modelo}")
        print(f" Año: {self.año}")
        print(f" Precio base: ${self.precio_base:.2f}")
        print(f" Motor: {estado_motor}")
        print(f" Disponibilidad: {estado_disponibilidad}")

    def alquilar(self):
        """
        Marca el vehículo como no disponible.
        """

        if not self._disponible:
            raise ValueError(
                f"{self.marca} {self.modelo} ya está alquilado."
            )

        self._disponible = False

        print(
            f"✅ {self.marca} {self.modelo} "
            f"ha sido alquilado."
        )

    def devolver(self):
        """
        Marca el vehículo como disponible.
        """

        if self._disponible:
            raise ValueError(
                f"{self.marca} {self.modelo} "
                f"no estaba alquilado."
            )

        self._disponible = True

        print(
            f"↩️ {self.marca} {self.modelo} "
            f"ha sido devuelto."
        )

    @classmethod
    def total_vehiculos(cls):
        """
        Devuelve el número total de vehículos activos.
        """

        return Vehiculo._contador_vehiculos

    @classmethod
    def crear_desde_diccionario(cls, datos):
        """
        Crea un vehículo usando los datos de un diccionario.
        """

        claves_requeridas = {
            "marca",
            "modelo",
            "año",
            "precio_base"
        }

        if not claves_requeridas.issubset(datos):
            raise ValueError(
                "El diccionario no contiene todas las claves requeridas."
            )

        return cls(
            datos["marca"],
            datos["modelo"],
            datos["año"],
            datos["precio_base"]
        )

    @staticmethod
    def validar_año(año):
        """
        Valida que el año esté entre 1901 y el año actual.
        """

        año_actual = datetime.now().year

        return (
            isinstance(año, int)
            and 1900 < año <= año_actual
        )

    @staticmethod
    def validar_precio(precio):
        """
        Valida que el precio sea numérico y positivo.
        """

        return (
            isinstance(precio, (int, float))
            and not isinstance(precio, bool)
            and precio > 0
        )


class Coche(Vehiculo):
    """
    Clase derivada que representa un coche.
    """

    def __init__(
        self,
        marca,
        modelo,
        año,
        precio_base,
        num_puertas
    ):
        if (
            not isinstance(num_puertas, int)
            or isinstance(num_puertas, bool)
            or num_puertas <= 0
        ):
            raise ValueError(
                "El número de puertas debe ser un entero positivo."
            )

        # Reutilización del constructor de Vehiculo
        super().__init__(
            marca,
            modelo,
            año,
            precio_base
        )

        self.num_puertas = num_puertas

    def calcular_alquiler(self, dias):
        """
        Calcula el alquiler del coche por días.
        """

        if not self.disponible:
            raise ValueError(
                "No se puede calcular el alquiler porque "
                "el coche no está disponible."
            )

        if (
            not isinstance(dias, (int, float))
            or isinstance(dias, bool)
            or dias <= 0
        ):
            raise ValueError(
                "La cantidad de días debe ser positiva."
            )

        costo = (
            self.precio_base * dias
            + self.num_puertas * 10
        )

        return costo

    def mostrar_info(self):
        """
        Extiende la información de la clase Vehiculo.
        """

        print(" Tipo: Coche")

        # Reutilización del método de la clase base
        super().mostrar_info()

        print(f" Puertas: {self.num_puertas}")

    def abrir_maletero(self):
        """
        Método propio de la clase Coche.
        """

        print(
            f"🧳 {self.marca} {self.modelo}: "
            f"Maletero abierto."
        )


class Moto(Vehiculo):
    """
    Clase derivada que representa una moto.
    """

    def __init__(
        self,
        marca,
        modelo,
        año,
        precio_base,
        cilindrada
    ):
        if (
            not isinstance(cilindrada, int)
            or isinstance(cilindrada, bool)
            or cilindrada <= 0
        ):
            raise ValueError(
                "La cilindrada debe ser un entero positivo."
            )

        # Reutilización del constructor de Vehiculo
        super().__init__(
            marca,
            modelo,
            año,
            precio_base
        )

        self.cilindrada = cilindrada

    def calcular_alquiler(self, horas):
        """
        Calcula el alquiler de la moto por horas.
        """

        if not self.disponible:
            raise ValueError(
                "No se puede calcular el alquiler porque "
                "la moto no está disponible."
            )

        if (
            not isinstance(horas, (int, float))
            or isinstance(horas, bool)
            or horas <= 0
        ):
            raise ValueError(
                "La cantidad de horas debe ser positiva."
            )

        costo = (
            self.precio_base * horas
            + self.cilindrada * 0.5
        )

        return costo

    def mostrar_info(self):
        """
        Extiende la información de la clase Vehiculo.
        """

        print(" Tipo: Moto")

        # Reutilización del método de la clase base
        super().mostrar_info()

        print(f" Cilindrada: {self.cilindrada} cc")

    def hacer_caballito(self):
        """
        Método propio de la clase Moto.
        """

        print(
            f"🏍️ {self.marca} {self.modelo}: "
            f"¡Haciendo caballito!"
        )