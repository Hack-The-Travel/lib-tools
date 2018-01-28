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


if __name__ == "__main__":
    nano = Decimal(10**9)
    print "A318: {0:0.2f} nanoseconds".format(extra_time(lorentz_factor(230))*nano)
    print "A319: {0:0.2f} nanoseconds".format(extra_time(lorentz_factor(230))*nano)
    print "A320: {0:0.2f} nanoseconds".format(extra_time(lorentz_factor(233.333))*nano)
    print "A320: {0:0.2f} nanoseconds".format(extra_time(lorentz_factor(241.944))*nano)
    print "B738: {0:0.2f} nanoseconds".format(extra_time(lorentz_factor(232.778))*nano)
