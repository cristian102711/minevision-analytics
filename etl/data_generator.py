"""
Generador de datos para MineVision Analytics.
"""

# Importamos librerías de Python
import random
from datetime import datetime

# Importamos las constantes del proyecto
from etl.constants import (
    TRUCKS,
    EXCAVATORS,
    OPERATORS,
    MATERIALS,
    ORIGINS,
    DESTINATIONS,
    SHIFTS,
    MIN_TONS,
    MAX_TONS,
    MIN_FUEL,
    MAX_FUEL,
    MIN_SPEED,
    MAX_SPEED,
    MIN_ENGINE_TEMPERATURE,
    MAX_ENGINE_TEMPERATURE,
)


def generate_trip():
    """
    Genera un viaje minero simulado.
    """

    trip = {
        "trip_id": "TRIP-000001",
    }

    return trip


if __name__ == "__main__":
    trip = generate_trip()
    print(trip)