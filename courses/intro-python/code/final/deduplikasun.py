"""
Deduplikasun
============
Removi elementus duplikadu di un lista, preservandu orden orijinal.
"""


def removi_duplikadus(lista: list) -> list:
    """Removi duplikadus preservandu orden orijinal."""
    vistu = set()
    resultadu = []
    for elementu in lista:
        if elementu not in vistu:
            vistu.add(elementu)
            resultadu.append(elementu)
    return resultadu


def atxa_duplikadus(lista: list) -> set:
    """Retorna set di elementus ki ta aparese más di un vez."""
    vistu = set()
    duplikadus = set()
    for elementu in lista:
        if elementu in vistu:
            duplikadus.add(elementu)
        vistu.add(elementu)
    return duplikadus


def main():
    numerus = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Orijinal:       {numerus}")
    print(f"Sen duplikadu:  {removi_duplikadus(numerus)}")
    print(f"Duplikadus:     {atxa_duplikadus(numerus)}")

    nomis = ["Maria", "João", "Ana", "Maria", "Pedro", "Ana", "Djina"]
    print(f"\nNomis orijinal: {nomis}")
    print(f"Sen duplikadu:  {removi_duplikadus(nomis)}")
    print(f"Duplikadus:     {atxa_duplikadus(nomis)}")


if __name__ == "__main__":
    main()
