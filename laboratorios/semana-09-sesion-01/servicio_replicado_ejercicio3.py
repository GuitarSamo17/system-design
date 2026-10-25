"""Ejercicio 3: decidir, lectura por lectura, si va a la primaria o a la
replica.

Corre las pruebas con:

    pytest test_servicio_replicado_ejercicio3.py

No cambies los nombres de la clase ni de los metodos, y lee siempre a
traves de self.base.leer_de_primaria() o self.base.leer_de_replica():
los tests cuentan en que nodo hiciste cada lectura.
"""

from datos_reservas import ReservaRegistrada


class ServicioDeReservasReplicado:
    def __init__(self, base):
        self.base = base
        self.siguiente_id = 1
        self.ultimo_id_por_estudiante = {}

    def cancha_disponible(self, campus, cancha, fecha, hora):
        # TODO: devuelve True si ninguna reserva ocupa esa cancha, en ese
        # campus, esa fecha y esa hora. Elige de que nodo leer: esta
        # respuesta decide si se acepta una reserva nueva.
        reservas = self.base.leer_de_primaria()
        for reserva in reservas:
            if (reserva.campus == campus and reserva.cancha == cancha and 
                reserva.fecha == fecha and reserva.hora == hora):
                return False
        return True

    def reservar(self, id_estudiante, campus, cancha, fecha, hora):
        if not self.cancha_disponible(campus, cancha, fecha, hora):
            return None
        reserva = ReservaRegistrada(self.siguiente_id, id_estudiante, campus, cancha, fecha, hora)
        self.ultimo_id_por_estudiante[id_estudiante] = self.siguiente_id
        self.siguiente_id = self.siguiente_id + 1
        self.base.escribir(reserva)
        return reserva

    def mis_reservas(self, id_estudiante):
        # TODO: devuelve las reservas de este estudiante. Lee de la replica
        # siempre que puedas, para quitarle carga a la primaria, pero un
        # estudiante que acaba de reservar tiene que ver su reserva aunque
        # la replica todavia no la tenga (leer lo que uno mismo escribio).
        reservas_replica = self.base.leer_de_replica()
        
        max_id_replica = 0
        for r in reservas_replica:
            if r.id_reserva > max_id_replica:
                max_id_replica = r.id_reserva
                
        ultimo_id_mio = self.ultimo_id_por_estudiante.get(id_estudiante, 0)
        
        if ultimo_id_mio > max_id_replica:
            reservas = self.base.leer_de_primaria()
        else:
            reservas = reservas_replica
            
        mis_reservas_lista = []
        for r in reservas:
            if r.id_estudiante == id_estudiante:
                mis_reservas_lista.append(r)
                
        return mis_reservas_lista

    def ocupacion_del_campus(self, campus):
        # TODO: devuelve cuantas reservas tiene el campus. Es el reporte
        # que mira la administracion una vez al dia: elige de que nodo leer.
        reservas = self.base.leer_de_replica()
        total = 0
        for r in reservas:
            if r.campus == campus:
                total += 1
        return total
