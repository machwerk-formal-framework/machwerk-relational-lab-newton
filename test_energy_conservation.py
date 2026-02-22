"""
Machwerk Relational Lab – Energy Consistency Test
"""

from newton_relational import NewtonTwoBody


def test_circular_orbit_energy():
    """
    Test whether circular orbit energy relation holds:
    E = - G m1 m2 / (2 r)
    """

    # Example: Earth–Sun system (approximate values)
    m_sun = 1.989e30       # kg
    m_earth = 5.972e24     # kg
    r = 1.496e11           # m (1 AU)

    system = NewtonTwoBody(m_sun, m_earth, r)

    potential = system.potential_energy()
    total_energy = system.total_energy_circular_orbit()

    # For circular orbit: E_total = U / 2
    assert abs(total_energy - potential / 2) < 1e-5 * abs(potential)

    print("Energy consistency test passed.")


if __name__ == "__main__":
    test_circular_orbit_energy()
