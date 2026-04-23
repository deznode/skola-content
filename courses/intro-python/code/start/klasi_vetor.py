"""
Exersísiu: Klasi Vetor
======================
Konseitu: sobrekarga di operador, métudu májiku (dunder methods)

Kria un klasi Vetor 2D ku:
- Adison di vetores (+)
- Subtrasion di vetores (-)
- Multiplikason por eskalar (*)
- Komparason di igualdadi (==)
- Reprezentason em string
- Kálkulu di magnitudi

Uza métudu májiku di Python pa sobrekarga di operador.
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
        """
        Adison di vetores: v1 + v2

        Args:
            otru: Otru vetor pa adisiona

        Returns:
            Novu Vetor ku soma
        """
        # TODO: Retorna novu Vetor ku soma di komponenti x e y
        pass

    def __sub__(self, otru: "Vetor") -> "Vetor":
        """
        Subtrasion di vetores: v1 - v2

        Args:
            otru: Otru vetor pa subtrai

        Returns:
            Novu Vetor ku diferensa
        """
        # TODO: Retorna novu Vetor ku diferensa di komponenti x e y
        pass

    def __mul__(self, eskalar: float) -> "Vetor":
        """
        Multiplikason por eskalar: v * n

        Args:
            eskalar: Valor eskalar pa multiplika

        Returns:
            Novu Vetor multiplikadu
        """
        # TODO: Retorna novu Vetor ku kada komponenti multiplikadu por eskalar
        pass

    def __eq__(self, otru: object) -> bool:
        """
        Komparason di igualdadi: v1 == v2

        Args:
            otru: Obijetu pa kompara

        Returns:
            True si vetores é igual
        """
        # TODO: Verifica si otru é instánsia di Vetor
        # TODO: Kompara komponenti x e y
        pass

    def __str__(self) -> str:
        """Reprezentason em string pa uzuáriu."""
        # TODO: Retorna "Vetor(x, y)"
        pass

    def __repr__(self) -> str:
        """Reprezentason em string pa debugging."""
        # TODO: Retorna "Vetor(x, y)" — mesmu formatu ki __str__
        pass

    def magnitudi(self) -> float:
        """
        Kalkula magnitudi (tamañu) di vetor.

        Fórmula: sqrt(x² + y²)

        Returns:
            Magnitudi di vetor
        """
        # TODO: Uza math.sqrt pa kalkula magnitudi
        pass


# ============================================================
# Demonstrasion
# ============================================================
if __name__ == "__main__":
    # Kria vetores
    # TODO: v1 = Vetor(3, 4)
    # TODO: v2 = Vetor(1, 2)

    # Mustra vetores
    # TODO: print(f"v1 = {v1}")
    # TODO: print(f"v2 = {v2}")

    # Adison
    # TODO: v3 = v1 + v2
    # TODO: print(f"v1 + v2 = {v3}")

    # Subtrasion
    # TODO: v4 = v1 - v2
    # TODO: print(f"v1 - v2 = {v4}")

    # Multiplikason por eskalar
    # TODO: v5 = v1 * 3
    # TODO: print(f"v1 * 3 = {v5}")

    # Magnitudi
    # TODO: print(f"|v1| = {v1.magnitudi():.2f}")

    # Komparason
    # TODO: print(f"v1 == v2: {v1 == v2}")
    # TODO: print(f"Vetor(3, 4) == Vetor(3, 4): {Vetor(3, 4) == Vetor(3, 4)}")

    print("Diskumenta es TODO-s pa kompleta exersísiu!")
