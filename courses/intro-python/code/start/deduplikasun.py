"""
Deduplikasun
============
Removi elementus duplikadu di un lista, preservandu orden orijinal.

Objetivus:
- Uza set pa deteta duplikadus
- Uza lista pa preserva orden
- Kompara diferenti abordajens (set vs loop)

Ezemplu:
    Orijinal:  [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    Sen duplikadu: [3, 1, 4, 5, 9, 2, 6]
    Duplikadus atxadu: {1, 3, 5}
"""


def removi_duplikadus(lista: list) -> list:
    """Removi duplikadus preservandu orden orijinal."""
    # TODO 1: Kria un set vaziu pa rastreia elementus já vistu
    # TODO 2: Kria un lista vaziu pa resultadu
    # TODO 3: Uza loop — si elementu ka sta na set, ajunta na resultadu e na set
    pass


def atxa_duplikadus(lista: list) -> set:
    """Retorna set di elementus ki ta aparese más di un vez."""
    # TODO 4: Implementa lójika pa atxa duplikadus
    # Abordajen 1: uza set pa rastreia vistu e duplikadus
    # Abordajen 2: kompara len(lista) ku len(set(lista))
    pass


def main():
    # Testa ku numerus
    numerus = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Orijinal:       {numerus}")

    # TODO 5: Xama removi_duplikadus() e mostra resultadu
    # TODO 6: Xama atxa_duplikadus() e mostra kual é duplikadus

    # Testa ku nomis
    nomis = ["Maria", "João", "Ana", "Maria", "Pedro", "Ana", "Djina"]
    print(f"\nNomis orijinal: {nomis}")

    # TODO 7: Removi duplikadus di nomis e mostra


if __name__ == "__main__":
    main()
