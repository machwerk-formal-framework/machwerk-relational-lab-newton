"""
Machwerk Relational Lab – Structural Perturbation Analysis
"""

from newton_relational import NewtonTwoBody


def perturb_distance(m1, m2, r, delta):
    """
    Computes change in potential energy under small relational perturbation of r.
    """

    system_original = NewtonTwoBody(m1, m2, r)
    system_perturbed = NewtonTwoBody(m1, m2, r + delta)

    U_original = system_original.potential_energy()
    U_perturbed = system_perturbed.potential_energy()

    dU = U_perturbed - U_original

    print("Original potential energy:", U_original)
    print("Perturbed potential energy:", U_perturbed)
    print("Energy difference dU:", dU)


def numerical_gradient(m1, m2, r, delta):
    """
    Numerical approximation of dU/dr.
    """

    system_original = NewtonTwoBody(m1, m2, r)
    system_perturbed = NewtonTwoBody(m1, m2, r + delta)

    U_original = system_original.potential_energy()
    U_perturbed = system_perturbed.potential_energy()

    gradient = (U_perturbed - U_original) / delta

    print("Numerical dU/dr:", gradient)


if __name__ == "__main__":
    m1 = 5.0
    m2 = 3.0
    r = 10.0
    delta = 0.001

    perturb_distance(m1, m2, r, delta)
    numerical_gradient(m1, m2, r, delta)
