"""
Machwerk Relational Lab – Newtonian Two-Body System
Relational formulation using TRD structure
"""

import math
from trd_structure import TRD


G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)


class NewtonTwoBody:
    """
    Relational representation of a classical Newtonian two-body system.
    TRD(m1, m2, r)
    """

    def __init__(self, m1: float, m2: float, r: float):
        if r <= 0:
            raise ValueError("Distance r must be positive.")
        self.trd = TRD(m1, m2, r)

    @property
    def m1(self):
        return self.trd.a

    @property
    def m2(self):
        return self.trd.b

    @property
    def r(self):
        return self.trd.c

    def gravitational_force(self):
        """
        F = G m1 m2 / r^2
        """
        return G * self.m1 * self.m2 / (self.r ** 2)

    def potential_energy(self):
        """
        U = - G m1 m2 / r
        """
        return -G * self.m1 * self.m2 / self.r

    def reduced_mass(self):
        """
        μ = (m1 m2) / (m1 + m2)
        """
        return (self.m1 * self.m2) / (self.m1 + self.m2)

    def circular_orbital_velocity(self):
        """
        v = sqrt(G (m1 + m2) / r)
        """
        return math.sqrt(G * (self.m1 + self.m2) / self.r)

    def total_energy_circular_orbit(self):
        """
        Total energy for circular orbit:
        E = - G m1 m2 / (2 r)
        """
        return -G * self.m1 * self.m2 / (2 * self.r)

    def structural_summary(self):
        """
        Returns key relational quantities.
        """
        return {
            "force": self.gravitational_force(),
            "potential_energy": self.potential_energy(),
            "reduced_mass": self.reduced_mass(),
            "circular_velocity": self.circular_orbital_velocity(),
            "total_energy_circular": self.total_energy_circular_orbit(),
        }
