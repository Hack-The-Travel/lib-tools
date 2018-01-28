# -*- coding: utf-8 -*-
"""
timeless
~~~~~~~~

This module contains some functions from relativity.
"""

from decimal import Decimal

LIGHT_SPEED = Decimal(299792458)  # meters per second


def lorentz_factor(v_obj):
    """Calculates Lorentz factor.

    https://en.wikipedia.org/wiki/Rapidity

    :param v_obj: speed of object, metres per second.
    :return: Lorentz factor.
    """
    v_obj = Decimal(v_obj)
    v_normalized = v_obj/LIGHT_SPEED
    return Decimal(1)/((Decimal(1) - v_normalized*v_normalized).sqrt())

def extra_time(y_factor):
    """Calculates how much the day has increased.

    :param y_factor: Lorentz factor.
    :return: day increased by N seconds.
    """
    day_duraction = Decimal(24*60*60)  # seconds
    return day_duraction*y_factor - day_duraction


def kmh_to_ms(v_kmh):
    """Converts km/h to m/s."""
    return Decimal(v_kmh)*Decimal(1000.0/60.0/60.0)


if __name__ == "__main__":
    AIRPLANES_CRUISE_SPEED = {  # kilometres per hour
        'A318': 828,
        'A319': 828,
        'A320': 840,
        'A330': 871,
        'B738': 838,
    }
    nano = Decimal(10**9)
    for airplane in AIRPLANES_CRUISE_SPEED:
        airplane_speed = kmh_to_ms(AIRPLANES_CRUISE_SPEED[airplane])
        print '{airplane}: {time:0.2f} nanoseconds'.format(
            airplane=airplane,
            time=extra_time(lorentz_factor(airplane_speed))*nano
        )
