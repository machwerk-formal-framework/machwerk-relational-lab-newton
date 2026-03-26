# MACHWERK Relational Lab: Newton

A computational lab for understanding **relational mechanics**—not a physics simulator.

## The Why

You don't need coordinates or time parameters to describe physical systems. You need **relations**. Instead of solving differential equations, you define **structural properties** and test their consistency. This lab shows how.

---

## What Is TRD?

**TRD = Temporal Relational Determinacy**

A system of three coupled quantities:

TRD(m1, m2, r)  # masses and distance → everything else derives from this

**Key idea:** Once you define the TRD, all physical quantities (force, energy, velocity) are **structurally determined**. No ODEs. No integration. No time stepping.

---

## Repository Contents

### Core Files

**`trd_structure.py`** — The relational triple

- `relational_ratio()` — How quantities relate to each other
- `invariant_sum()`, `invariant_product()` — Structural invariants
- `scale()` — How structure transforms under scaling
- `norm()` — Structural magnitude

**`newton_relational.py`** — Relational two-body mechanics

- `gravitational_force()` 
- `potential_energy()`
- `reduced_mass()`
- `circular_orbital_velocity()`
- `total_energy_circular_orbit()`

All derived directly from TRD(m1, m2, r). No external equations.

### Tests & Analysis

**`relational_analysis.py`** — Structural invariance tests

- Verify that force scales as k² when masses scale by k
- Verify inverse-square behavior under distance scaling

**`test_energy_conservation.py`** — Admissibility check

- Energy relation must hold: E = U/2 for circular orbits
- This test verifies the system remains **closed and consistent**

**`relational_orbit_scan.py`** — Parameter space explorer

- Scans energy across distance ranges
- Shows how relational quantities behave

**`structural_perturbation.py`** — Sensitivity analysis

- Apply small perturbations to the TRD
- Detect where the structure becomes unstable
- Find boundaries where reconstruction fails

---

## How This Differs From Classical Mechanics Code

| Classical Approach | Relational Approach |
|---|---|
| Solve: F = ma | Define: TRD(m1, m2, r) |
| Integrate over time | Compute structural properties |
| Output: trajectories x(t), v(t) | Output: invariants, constraints, admissibility |
| Time is primitive | Time emerges (or isn't needed) |
| Coordinates needed | Pure relations only |

---

## Running the Lab

python3 newton_relational.py          # See how TRD works
python3 relational_analysis.py        # Test structural consistency
python3 test_energy_conservation.py   # Verify energy admissibility
python3 relational_orbit_scan.py      # Explore parameter behavior
python3 structural_perturbation.py    # Find stability boundaries

---

## Understanding The Code

### Example: Why No ODEs?

Traditional approach:

# Newton: F = ma, solve a = d²x/dt²
# Requires: numerical integration, time stepping

Relational approach:

system = NewtonTwoBody(m1=5.0, m2=3.0, r=10.0)
F = system.gravitational_force()  # Direct computation from TRD

The force is **structurally determined** by the TRD triple. Nothing to integrate.

### Example: Structural Invariants

From `relational_analysis.py`:

# Original system
force_original = system_original.gravitational_force()

# Scaled masses (k=2)
force_scaled = system_scaled.gravitational_force()

# Ratio should be k² = 4
ratio = force_scaled / force_original  # = 4.0

This isn't a numerical coincidence. It's a **structural property** baked into how relations work.

### Example: Admissibility

From `test_energy_conservation.py`:

# For a valid circular orbit, energy must satisfy: E = U/2
assert abs(total_energy - potential / 2) < tolerance

If this test fails, the system **leaves m₂** (the valid domain) and becomes non-reconstructible. The structure breaks.

---

## Connection to MACHWERK Formal Core

This lab is a **computational implementation** of the formal framework:

- **U-space (𝒰)** → TRD: irreducible relational structure
- **Projection (Π)** → `structural_summary()`: measurable quantities
- **Valid domain (m₂)** → `test_energy_conservation()`: where physics works
- **Schwarzgrenze (Σ)** → `structural_perturbation()`: stability boundaries
- **Non-reconstructible (Δ₀)** → `float("inf")`: system breakdown

---

## For Programmers

Think of TRD as a **constraint system** with no time:

- Define constraints (the TRD triple)
- Query properties (force, energy, etc.)
- Test invariants (do they scale correctly?)
- Find boundaries (where does it break?)

This pattern applies to any relational system: networks, information theory, economics, biology.

---

## Next Steps

This Newton example teaches the **pattern**. Future labs will apply it to:

- Chemistry (atomic systems as TRDs)
- Information theory (sender-receiver-channel)
- Network dynamics
- Relational economics

---

## Reference

**Formal definitions:**
MACHWERK Relational Physics Framework
https://github.com/machwerk-formal-framework/machwerk-relational-physics

**Book:**
*MACHWERK — Formal Conditions of Physical Describability*
ISBN: 979-8-24410-846-0 (February 2026)
DOI: https://doi.org/10.5281/zenodo.18478523

This lab is the **Python implementation** of those formal definitions.
