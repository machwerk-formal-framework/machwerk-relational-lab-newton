"""
Machwerk Relational Lab – TRD Structure
Core relational triple (TRD) implementation
"""

from dataclasses import dataclass
import math


@dataclass
class TRD:
    """
    Relational Triple Structure

    Represents three dynamically coupled quantities.
    No coordinate embedding is assumed.
    """

    a: float
    b: float
    c: float

    def as_tuple(self):
        return (self.a, self.b, self.c)

    def scale(self, factor: float):
        """
        Uniform relational scaling.
        """
        return TRD(self.a * factor, self.b * factor, self.c * factor)

    def swap(self):
        """
        Cyclic permutation of relational entries.
        """
        return TRD(self.b, self.c, self.a)

    def norm(self):
        """
        Structural norm (Euclidean for classical m2 testbed).
        """
        return math.sqrt(self.a**2 + self.b**2 + self.c**2)

    def relational_ratio(self):
        """
        Returns pairwise relational ratios.
        """
        return {
            "a/b": self.a / self.b if self.b != 0 else float("inf"),
            "b/c": self.b / self.c if self.c != 0 else float("inf"),
            "c/a": self.c / self.a if self.a != 0 else float("inf"),
        }

    def invariant_sum(self):
        """
        Simple structural invariant candidate.
        """
        return self.a + self.b + self.c

    def invariant_product(self):
        """
        Multiplicative invariant candidate.
        """
        return self.a * self.b * self.c
