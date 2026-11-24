"""Pruebas del Ejercicio 1. Empieza vacio: cada prueba se escribe antes
del codigo que la hace pasar, una a la vez, en el orden de la lista de
penalizaciones_ejercicio1.py.
"""
from penalizaciones_ejercicio1 import HistorialDePenalizaciones, puntos_por_cancelar

def test_cancelar_con_mas_de_un_dia_no_penaliza():

    assert puntos_por_cancelar(2000) == 0

def test_cancelar_el_mismo_dia_penaliza():

    assert puntos_por_cancelar(600) == 1

def test_cancelar_a_ultima_hora_penalizar():

    assert puntos_por_cancelar(30) == 2

def test_casos_frontera():

    assert puntos_por_cancelar(1440) == 0
    assert puntos_por_cancelar(120) == 1

def test_estudiante_con_tres_puntos_nloqueado():

    historial = HistorialDePenalizaciones()

    historial.cancelar('Ana', 600)

    assert historial.esta_bloqueado('Ana') == False

    historial.cancelar('Ana', 10)

    assert historial.esta_bloqueado('Ana') == True

def test_estudiante_nuevo_ver_bloqueado():

    historial = HistorialDePenalizaciones()

    assert historial.esta_bloqueado('Pedro') == False

# Hay mas pruebas que debemos ir creando para confirmar la calidad del comportamiento de la funcionalidad
def test_no_presentarse_bloquea():
    historial = HistorialDePenalizaciones()
    historial.no_se_presento('Luis')
    assert historial.esta_bloqueado('Luis') is True


def test_penalizaciones_de_uno_no_bloquean_a_otro():
    historial = HistorialDePenalizaciones()
    historial.no_se_presento('Ana')
    assert historial.esta_bloqueado('Ana') is True
    assert historial.esta_bloqueado('Beto') is False