"""
Exersísiu: Klasi Vetor (Solusion Kompletu)
==========================================
Konseitu: sobrekarga di operador, métudu májiku (dunder methods)

Klasi Vetor 2D ku sobrekarga di operador pa
adison, subtrasion, multiplikason, komparason, e magnitudi.
"""

import math


class Vetor:
    """Klasi ki representa un vetor 2D."""

    def __init__(self, x: float, y: float):
        """
        Inisializa vetor ku koordenadas x e y.

        Args:
            x: Komponenti x di vetor
            y: Komponenti y di vetor
        """
        self.x = x
        self.y = y

    def __add__(self, otru: "Vetor") -> "Vetor":
        """Adison di vetores: v1 + v2"""
        return Vetor(self.x + otru.x, self.y + otru.y)

    def __sub__(self, otru: "Vetor") -> "Vetor":
        """Subtrasion di vetores: v1 - v2"""
        return Vetor(self.x - otru.x, self.y - otru.y)

    def __mul__(self, eskalar: float) -> "Vetor":
        """Multiplikason por eskalar: v * n"""
        return Vetor(self.x * eskalar, self.y * eskalar)

    def __eq__(self, otru: object) -> bool:
        """Komparason di igualdadi: v1 == v2"""
        if not isinstance(otru, Vetor):
            return NotImplemented
        return self.x == otru.x and self.y == otru.y

    def __str__(self) -> str:
        """Reprezentason em string pa uzuáriu."""
        return f"Vetor({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Reprezentason em string pa debugging."""
        return f"Vetor({self.x}, {self.y})"

    def magnitudi(self) -> float:
        """
        Kalkula magnitudi (tamañu) di vetor.

        Fórmula: sqrt(x^2 + y^2)

        Returns:
            Magnitudi di vetor
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)


# ============================================================
# Demonstrasion
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  Operasons ku Vetores 2D")
    print("=" * 50)

    # Kria vetores
    v1 = Vetor(3, 4)
    v2 = Vetor(1, 2)

    print(f"\nv1 = {v1}")
    print(f"v2 = {v2}")

    # Adison di vetores
    v3 = v1 + v2
    print(f"\n--- Adison ---")
    print(f"v1 + v2 = {v3}")

    # Subtrasion di vetores
    v4 = v1 - v2
    print(f"\n--- Subtrasion ---")
    print(f"v1 - v2 = {v4}")

    # Multiplikason por eskalar
    v5 = v1 * 3
    print(f"\n--- Multiplikason ---")
    print(f"v1 * 3 = {v5}")

    # Magnitudi di vetor
    print(f"\n--- Magnitudi ---")
    print(f"|v1| = {v1.magnitudi():.2f}")
    print(f"|v2| = {v2.magnitudi():.2f}")

    # Komparason di vetores
    print(f"\n--- Komparason ---")
    print(f"v1 == v2: {v1 == v2}")
    print(f"Vetor(3, 4) == Vetor(3, 4): {Vetor(3, 4) == Vetor(3, 4)}")
    print(f"Vetor(1, 2) == Vetor(1, 2): {Vetor(1, 2) == Vetor(1, 2)}")

    # Operasons enkadiadu
    print(f"\n--- Operasons Enkadiadu ---")
    rezultadu = (v1 + v2) * 2
    print(f"(v1 + v2) * 2 = {rezultadu}")
    print(f"|(v1 + v2) * 2| = {rezultadu.magnitudi():.2f}")
