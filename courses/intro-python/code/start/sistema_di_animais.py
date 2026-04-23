"""
Exersísiu: Sistema di Animais
=============================
Konseitu: heransa, polimorfizmu, klasi abstratu

Kria un sistéma ku:
- Klasi abstratu Animal ku métudu abstratu fala()
- Subklasis: Katchor, Gatu, Paságeru
- Funsion polimórfiku konsulta_veterinária()

Uza ABC (Abstract Base Class) di Python.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Klasi abstratu ki representa un animal."""

    def __init__(self, nomi: str, idadi: int, donu: str):
        """
        Inisializa un animal.

        Args:
            nomi: Nomi di animal
            idadi: Idadi na anus
            donu: Nomi di donu di animal
        """
        self.nomi = nomi
        self.idadi = idadi
        self.donu = donu

    @abstractmethod
    def fala(self) -> str:
        """
        Métudu abstratu — kada animal debe implementa si son.

        Returns:
            String ku son di animal
        """
        # TODO: Es métudu já é abstratu — subklasis debe implementa-l
        pass

    def apresenta(self) -> str:
        """Apresenta animal ku si informasons."""
        # TODO: Retorna "Ami é {nomi}, tenhu {idadi} anu(s). Nha donu é {donu}."
        pass


class Katchor(Animal):
    """Klasi ki representa un katchor (cachorro)."""

    # TODO: Implementa métudu fala()
    # Katchor ta fazi: "Woof! Woof!"
    pass


class Gatu(Animal):
    """Klasi ki representa un gatu."""

    # TODO: Implementa métudu fala()
    # Gatu ta fazi: "Miau!"
    pass


class Pasageru(Animal):
    """Klasi ki representa un paságeru (papagaiu kabu-verdianu)."""

    # TODO: Implementa métudu fala()
    # Paságeru ta fazi: "Oi! Oi!"
    pass


def konsulta_veterinaria(animais: list[Animal]) -> None:
    """
    Funsion polimórfiku — trata kada animal sen konxi si tipu.

    Args:
        animais: Lista di animais pa konsulta
    """
    # TODO: Pa kada animal na lista:
    #   1. Mustra apresentason
    #   2. Mustra son ki e ta fazi
    #   3. Mustra un linia separador
    pass


# ============================================================
# Demonstrasion
# ============================================================
if __name__ == "__main__":
    # Kria animais ku nomi kabu-verdianu pa donus
    # TODO: Kria Katchor("Rex", 3, "Nelson")
    # TODO: Kria Gatu("Mimi", 2, "Ivete")
    # TODO: Kria Pasageru("Kiko", 5, "Djina")

    # Lista di animais pa konsulta
    # TODO: animais = [katchor, gatu, pasageru]

    # Konsulta veterinária
    # TODO: konsulta_veterinaria(animais)

    # Tenta kria Animal diretamenti (debe da erru)
    # TODO: try/except pa Animal("Testu", 1, "Ninguém")

    print("Diskumenta es TODO-s pa kompleta exersísiu!")
