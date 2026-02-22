"""
Machwerk Relational Lab – Relational Orbit Energy Scan
"""

from newton_relational import NewtonTwoBody


def energy_scan(m1, m2, r_min, r_max, steps):
    """
    Scans total circular orbit energy over a range of distances.
    """

    dr = (r_max - r_min) / steps
    results = []

    for i in range(steps + 1):
        r = r_min + i * dr
        system = NewtonTwoBody(m1, m2, r)
        E = system.total_energy_circular_orbit()
        results.append((r, E))

    return results


if __name__ == "__main__":
    m1 = 5.0
    m2 = 3.0

    data = energy_scan(m1, m2, r_min=5.0, r_max=20.0, steps=10)

    for r, E in data:
        print(f"r = {r:.2f}, E_total = {E:.6e}")
