# Sistema de Gestión de Vehículos

## Descripción

Sistema desarrollado en Python para administrar una flota de vehículos de una agencia de alquiler. Permite registrar coches y motos, gestionar alquileres, controlar el estado de los vehículos y consultar estadísticas de la flota.

El proyecto fue desarrollado aplicando conceptos de Programación Orientada a Objetos (POO), como herencia, polimorfismo, encapsulamiento, reutilización de código mediante `super()`, métodos de clase, métodos estáticos y manejo de excepciones.

---

## Estructura del Proyecto

```text
vehiculos_simulator/
│
├── main.py
└── clases/
    └── vehiculos.py
```

### Archivos

- **main.py:** contiene el menú interactivo y la lógica principal del programa.
- **vehiculos.py:** contiene las clases `Vehiculo`, `Coche` y `Moto`.

---

## Funcionalidades

- Registrar coches y motos.
- Mostrar la información de todos los vehículos.
- Encender y apagar vehículos.
- Calcular el costo de alquiler.
- Alquilar y devolver vehículos.
- Consultar estadísticas de la flota.
- Dar de baja vehículos.
- Validar datos ingresados por el usuario.

---

## Clases Implementadas

### Vehiculo

Clase base que contiene la información común de todos los vehículos:

- Marca
- Modelo
- Año
- Precio base
- Estado del motor
- Disponibilidad

Métodos principales:

- `encender()`
- `apagar()`
- `mostrar_info()`
- `alquilar()`
- `devolver()`

### Coche

Hereda de `Vehiculo`.

Atributo adicional:

```python
num_puertas
```

Cálculo de alquiler:

```python
precio_base * dias + (num_puertas * 10)
```

### Moto

Hereda de `Vehiculo`.

Atributo adicional:

```python
cilindrada
```

Cálculo de alquiler:

```python
precio_base * horas + (cilindrada * 0.5)
```

---

## Conceptos de POO Aplicados

- Herencia
- Polimorfismo
- Encapsulamiento
- Redefinición de métodos
- Métodos de clase (`@classmethod`)
- Métodos estáticos (`@staticmethod`)
- Propiedades (`@property`)
- Manejo de excepciones (`try/except`)

## Menú Principal

```text
1. Registrar coche
2. Registrar moto
3. Mostrar flota
4. Encender/Apagar vehículo
5. Calcular alquiler
6. Alquilar vehículo
7. Devolver vehículo
8. Ver estadísticas
9. Dar de baja vehículo
10. Salir
```

---
