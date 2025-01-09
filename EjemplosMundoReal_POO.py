# Ejemplo de un sistema de reservas de boletos de avión usando POO

# Clase Vuelo
class Vuelo:
    def __init__(self, numero_vuelo, destino, capacidad):
        self.numero_vuelo = numero_vuelo
        self.destino = destino
        self.capacidad = capacidad
        self.asientos_disponibles = capacidad

    def reservar_asiento(self):
        if self.asientos_disponibles > 0:
            self.asientos_disponibles -= 1
            return True
        else:
            print(f"No hay asientos disponibles {self.numero_vuelo}.")
            return False

    def cancelar_reserva(self):
        if self.asientos_disponibles < self.capacidad:
            self.asientos_disponibles += 1

# Clase Pasajero
class Pasajero:
    def __init__(self, nombre, id_pasajero):
        self.nombre = nombre
        self.id_pasajero = id_pasajero
        self.boletos_reservados = []

    def reservar_boletos(self, vuelo):
        if vuelo.reservar_asiento():
            self.boletos_reservados.append(vuelo)
            print(f"{self.nombre} ha reservado un asiento en el vuelo {vuelo.numero_vuelo} a {vuelo.destino}.")
        else:
            print(f"Lo siento, {self.nombre}. No se pudo reservar el asiento.")

    def cancelar_reserva(self, vuelo):
        if vuelo in self.boletos_reservados:
            vuelo.cancelar_reserva()
            self.boletos_reservados.remove(vuelo)
            print(f"{self.nombre} ha cancelado la reserva en el vuelo {vuelo.numero_vuelo}.")
        else:
            print(f"{self.nombre} no tiene una reserva en el vuelo {vuelo.numero_vuelo}.")

# Clase Aerolinea
class Aerolinea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def listar_vuelos_disponibles(self):
        print(f"Vuelos disponibles de {self.nombre}:")
        for vuelo in self.vuelos:
            print(f"Vuelo {vuelo.numero_vuelo} a {vuelo.destino} - Asientos disponibles: {vuelo.asientos_disponibles}")

# Ejemplo de uso del sistema de reservas de boletos de avión
if __name__ == "__main__":
    # Crear objetos vuelos
    vuelo1 = Vuelo("AA123", "Nueva York", 3)
    vuelo2 = Vuelo("BA456", "Londres", 2)
    vuelo3 = Vuelo("DL789", "París", 5)

    # Crear pasajero
    pasajero1 = Pasajero("Juan", "P001")

    # Crear aerolínea y agregar vuelos
    aerolinea = Aerolinea("FlyHigh")
    aerolinea.agregar_vuelo(vuelo1)
    aerolinea.agregar_vuelo(vuelo2)
    aerolinea.agregar_vuelo(vuelo3)

    # Lista de vuelos disponibles antes de la reserva
    aerolinea.listar_vuelos_disponibles()

    # El pasajero reserva boletos
    pasajero1.reservar_boletos(vuelo1)
    pasajero1.reservar_boletos(vuelo2)
    
    # Lista de vuelos disponibles después de la reserva
    aerolinea.listar_vuelos_disponibles()

    # Pasajero cancela la reserva y listar los vuelos disponibles de nuevo
    pasajero1.cancelar_reserva(vuelo1)
    aerolinea.listar_vuelos_disponibles()
