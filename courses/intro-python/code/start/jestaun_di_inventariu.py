"""
Jestaun di Inventáriu
=====================
Kria un sistema di inventáriu pa un loja ki ta uza listas e disionárius.

Funsionalidadis:
- Ajunta produtu novu (nomi, presi, stoki)
- Removi produtu
- Buska produtu pa nomi
- Mostra tudu produtus
- Kalkula valor total di inventáriu

Objetivus:
- Uza list di dicts pa garda dadus
- Uza list comprehension pa buska
- Uza funsoens pa organiza kódiku
- Uza f-strings pa formata saida

Ezemplu di uzu:
    === Inventáriu di Loja ===
    1. Ajunta produtu
    2. Removi produtu
    3. Buska produtu
    4. Mostra tudu
    5. Valor total
    6. Sai

    Skolhe opsun: 1
    Nomi di produtu: Katchupa
    Presi (ECV): 350
    Stoki: 20
    Produtu 'Katchupa' ajuntadu ku susesu!
"""


def ajunta_produtu(inventariu: list[dict], nomi: str, presi: float, stoki: int):
    """Ajunta un produtu novu na inventáriu."""
    # TODO 1: Kria un disionáriu ku nomi, presi, stoki
    # TODO 2: Ajunta na lista inventariu
    # TODO 3: Mostra mensajen di susesu
    pass


def removi_produtu(inventariu: list[dict], nomi: str):
    """Removi un produtu di inventáriu pa nomi."""
    # TODO 4: Atxa produtu na lista (uza loop o list comprehension)
    # TODO 5: Si atxa, removi e mostra mensajen
    # TODO 6: Si ka atxa, mostra "Produtu ka atxadu"
    pass


def buska_produtu(inventariu: list[dict], nomi: str) -> dict | None:
    """Buska un produtu pa nomi. Retorna dict o None."""
    # TODO 7: Uza loop pa buska produtu ku nomi igual
    # Dika: kompara .lower() pa ignora maiúskulu/minúskulu
    pass


def mostra_tudu(inventariu: list[dict]):
    """Mostra tudu produtus na inventáriu."""
    # TODO 8: Si inventáriu é vaziu, mostra mensajen
    # TODO 9: Si nau, mostra kada produtu formatadu:
    # "  Katchupa — 350.00 ECV — Stoki: 20"
    pass


def valor_total(inventariu: list[dict]) -> float:
    """Kalkula valor total (presi * stoki pa kada produtu)."""
    # TODO 10: Uza sum() ku generator expression
    pass


def main():
    inventariu = []

    while True:
        print("\n=== Inventáriu di Loja ===")
        print("1. Ajunta produtu")
        print("2. Removi produtu")
        print("3. Buska produtu")
        print("4. Mostra tudu")
        print("5. Valor total")
        print("6. Sai")

        opsun = input("\nSkolhe opsun: ")

        # TODO 11: Implementa kada opsun
        # Dika: uza if/elif/else
        if opsun == "6":
            print("Adeus! Té logu!")
            break
        else:
            print("Opsun invólidu. Tenta di novu.")


if __name__ == "__main__":
    main()
