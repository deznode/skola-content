"""
Jestaun di Inventáriu
=====================
Sistema di inventáriu pa un loja ki ta uza listas e disionárius.
"""


def ajunta_produtu(inventariu: list[dict], nomi: str, presi: float, stoki: int):
    """Ajunta un produtu novu na inventáriu."""
    produtu = {"nomi": nomi, "presi": presi, "stoki": stoki}
    inventariu.append(produtu)
    print(f"Produtu '{nomi}' ajuntadu ku susesu!")


def removi_produtu(inventariu: list[dict], nomi: str):
    """Removi un produtu di inventáriu pa nomi."""
    for produtu in inventariu:
        if produtu["nomi"].lower() == nomi.lower():
            inventariu.remove(produtu)
            print(f"Produtu '{nomi}' removidu.")
            return
    print(f"Produtu '{nomi}' ka atxadu.")


def buska_produtu(inventariu: list[dict], nomi: str) -> dict | None:
    """Buska un produtu pa nomi. Retorna dict o None."""
    for produtu in inventariu:
        if produtu["nomi"].lower() == nomi.lower():
            return produtu
    return None


def mostra_tudu(inventariu: list[dict]):
    """Mostra tudu produtus na inventáriu."""
    if not inventariu:
        print("Inventáriu ta vaziu.")
        return
    print(f"\n{'Produtu':<20} {'Presi (ECV)':>12} {'Stoki':>8}")
    print("-" * 42)
    for p in inventariu:
        print(f"  {p['nomi']:<18} {p['presi']:>10.2f}   {p['stoki']:>6}")


def valor_total(inventariu: list[dict]) -> float:
    """Kalkula valor total (presi * stoki pa kada produtu)."""
    return sum(p["presi"] * p["stoki"] for p in inventariu)


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

        if opsun == "1":
            nomi = input("Nomi di produtu: ")
            presi = float(input("Presi (ECV): "))
            stoki = int(input("Stoki: "))
            ajunta_produtu(inventariu, nomi, presi, stoki)

        elif opsun == "2":
            nomi = input("Nomi di produtu pa removi: ")
            removi_produtu(inventariu, nomi)

        elif opsun == "3":
            nomi = input("Nomi di produtu pa buska: ")
            produtu = buska_produtu(inventariu, nomi)
            if produtu:
                print(f"  {produtu['nomi']} — {produtu['presi']:.2f} ECV — Stoki: {produtu['stoki']}")
            else:
                print(f"Produtu '{nomi}' ka atxadu.")

        elif opsun == "4":
            mostra_tudu(inventariu)

        elif opsun == "5":
            total = valor_total(inventariu)
            print(f"Valor total di inventáriu: {total:.2f} ECV")

        elif opsun == "6":
            print("Adeus! Té logu!")
            break

        else:
            print("Opsun invólidu. Tenta di novu.")


if __name__ == "__main__":
    main()
