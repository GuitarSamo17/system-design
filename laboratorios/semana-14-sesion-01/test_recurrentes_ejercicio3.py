"""Pruebas del Ejercicio 3: las escriben ustedes, en pareja, una a la vez."""
import pytest

from recurrentes_ejercicio3 import AgendaDeCancha


def test_crea_calendario_por_fecha_y_reutiliza():
    agenda = AgendaDeCancha("cancha-1")
    cal_1 = agenda.calendario("2026-11-10")
    cal_2 = agenda.calendario("2026-11-10")
    assert cal_1 is cal_2
    assert cal_1.cancha == "cancha-1"
    assert cal_1.fecha == "2026-11-10"


def test_reservar_varias_semanas_seguidas():
    agenda = AgendaDeCancha("cancha-1")
    res = agenda.reservar_cada_semana("entreno", "futbol", "2026-11-10", 18, 20, 3)
    assert res == [
        ("2026-11-10", "reservada"),
        ("2026-11-17", "reservada"),
        ("2026-11-24", "reservada"),
    ]
    assert agenda.calendario("2026-11-10").reservas()[0][0] == "entreno-1"
    assert agenda.calendario("2026-11-17").reservas()[0][0] == "entreno-2"
    assert agenda.calendario("2026-11-24").reservas()[0][0] == "entreno-3"


def test_salta_semana_ocupada_y_sigue_con_las_demas():
    agenda = AgendaDeCancha("cancha-1")
    agenda.calendario("2026-11-17").reservar("otra", "ana", 18, 19)
    res = agenda.reservar_cada_semana("entreno", "futbol", "2026-11-10", 18, 20, 3)
    assert res == [
        ("2026-11-10", "reservada"),
        ("2026-11-17", "ocupada"),
        ("2026-11-24", "reservada"),
    ]


def test_reporta_limite_de_horas_en_el_dia():
    agenda = AgendaDeCancha("cancha-1")
    agenda.calendario("2026-11-17").reservar("previa", "futbol", 8, 10)
    res = agenda.reservar_cada_semana("entreno", "futbol", "2026-11-10", 18, 19, 3)
    assert res == [
        ("2026-11-10", "reservada"),
        ("2026-11-17", "limite"),
        ("2026-11-24", "reservada"),
    ]


def test_semanas_fuera_de_rango_lanza_sin_reservar():
    agenda = AgendaDeCancha("cancha-1")
    with pytest.raises(ValueError):
        agenda.reservar_cada_semana("entreno", "futbol", "2026-11-10", 18, 19, 0)
    with pytest.raises(ValueError):
        agenda.reservar_cada_semana("entreno", "futbol", "2026-11-10", 18, 19, 13)
    assert agenda.calendario("2026-11-10").reservas() == []