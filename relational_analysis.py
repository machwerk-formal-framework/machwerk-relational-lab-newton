"""
Machwerk Relational Lab – Relational Structural Analysis
"""

from newton_relational import NewtonTwoBody


def test_scaling_invariance():
    """
    Test structural scaling behavior.
    If all masses are scaled by factor k,
    force scales with k^2,
    potential energy scales with k^2.
    """

    m1 = 2.0
    m2 = 3.0
    r = 5.0

    system_original = NewtonTwoBody(m1, m2, r)
    system_scaled = NewtonTwoBody(2*m1, 2*m2, r)

    force_original = system_original.gravitational_force()
    force_scaled = system_scaled.gravitational_force()

    ratio = force_scaled / force_original

    print("Force scaling ratio (expected 4):", ratio)


def test_distance_scaling():
    """
    Test inverse square behavior under distance scaling.
    """

    m1 = 2.0
    m2 = 3.0
    r = 5.0

    system_original = NewtonTwoBody(m1, m2, r)
    system_scaled = NewtonTwoBody(m1, m2, 2*r)

    force_original = system_original.gravitational_force()
    force_scaled = system_scaled.gravitational_force()

    ratio = force_scaled / force_original

    print("Distance scaling ratio (expected 0.25):", ratio)


if __name__ == "__main__":
    test_scaling_invariance()
    test_distance_scaling()
