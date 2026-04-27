"""
Exersísiu: Sistema di Animais (Solusion Kompletu)
==================================================
Konseitu: heransa, polimorfizmu, klasi abstratu

Sistéma ku klasi abstratu Animal, subklasis konkretu,
e funsion polimórfiku pa konsulta veterinária.
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
        pass

    def apresenta(self) -> str:
        """Apresenta animal ku si informasons."""
        return f"Ami é {self.nomi}, tenhu {self.idadi} anu(s). Nha donu é {self.donu}."


class Katchor(Animal):
    """Klasi ki representa un katchor (cachorro)."""

    def fala(self) -> str:
        """Katchor ta fazi son."""
        return "Woof! Woof!"


class Gatu(Animal):
    """Klasi ki representa un gatu."""

    def fala(self) -> str:
        """Gatu ta fazi son."""
        return "Miau!"


class Pasageru(Animal):
    """Klasi ki representa un paságeru (papagaiu kabu-verdianu)."""

    def fala(self) -> str:
        """Paságeru ta fazi son."""
        return "Oi! Oi!"


def konsulta_veterinaria(animais: list[Animal]) -> None:
    """
    Funsion polimórfiku — trata kada animal sen konxi si tipu.

    Args:
        animais: Lista di animais pa konsulta
    """
    for animal in animais:
        print(animal.apresenta())
        print(f"  Son: {animal.fala()}")
        print("-" * 40)


# ============================================================
# Demonstrasion
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  Konsulta Veterinária na Praia")
    print("=" * 50)

    # Kria animais ku nomi kabu-verdianu pa donus
    katchor = Katchor("Rex", 3, "Nelson")
    gatu = Gatu("Mimi", 2, "Ivete")
    pasageru = Pasageru("Kiko", 5, "Djina")

    # Lista di animais pa konsulta
    animais = [katchor, gatu, pasageru]

    # Konsulta veterinária — polimorfizmu na asion
    print("\nAnimais na sala di espera:\n")
    konsulta_veterinaria(animais)

    # Más un animal — Carla si katchor
    print("\nKarla txiga ku si katchor:")
    katchor_karla = Katchor("Bobi", 1, "Carla")
    print(katchor_karla.apresenta())
    print(f"  Son: {katchor_karla.fala()}")

    # Tenta kria Animal diretamenti (debe da erru)
    print("\n--- Tenta kria Animal diretamenti ---")
    try:
        animal = Animal("Testu", 1, "Ninguém")
    except TypeError as e:
        print(f"Erru: Ka pode kria Animal diretamenti!")
        print(f"  Detálhi: {e}")
