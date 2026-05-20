"""
Kontador di Palavra
===================
Konta frekuensia di kada palavra nun tekstu.

Funsionalidadis:
- Le un tekstu (string)
- Separa na palavras (split)
- Konta quantu vez kada palavra ta aparese
- Mostra top 5 palavras más komun

Objetivus:
- Uza string methods (.split(), .lower(), .strip())
- Uza disionáriu pa konta frekuensia
- Uza .get() pa evita KeyError
- Uza sorted() ku key parameter

Ezemplu di saida:
    Tekstu: "nôs ta studu Python pamodi Python é sabi e Python ta djuda nôs"

    Frekuensia di palavra:
      python   : 3
      nôs      : 2
      ta       : 2
      studu    : 1
      ...
"""


def konta_palavras(tekstu: str) -> dict[str, int]:
    """Konta frekuensia di kada palavra na tekstu."""
    # TODO 1: Konverti tekstu pa minúskulu ku .lower()
    # TODO 2: Separa na palavras ku .split()
    # TODO 3: Kria disionáriu vaziu pa frekuensia
    # TODO 4: Uza loop pa konta kada palavra
    # Dika: uza frekuensia[palavra] = frekuensia.get(palavra, 0) + 1
    pass


def mostra_top_n(frekuensia: dict[str, int], n: int = 5):
    """Mostra top N palavras más komun."""
    # TODO 5: Ordena disionáriu pa valor (frekuensia) di máximu pa mínimu
    # Dika: uza sorted(frekuensia.items(), key=lambda x: x[1], reverse=True)
    # TODO 6: Mostra apenas top N
    pass


def main():
    tekstu = (
        "Python é un linguajen di programasun sabi. "
        "Nôs ta prende Python pamodi Python ta djuda nôs "
        "pa kria programa inkrível. Ku Python nôs ta podi "
        "fazi kualker kuza ki nôs ta imajina."
    )

    print(f"Tekstu: {tekstu}\n")

    # TODO 7: Xama konta_palavras() e mostra_top_n()
    pass


if __name__ == "__main__":
    main()
