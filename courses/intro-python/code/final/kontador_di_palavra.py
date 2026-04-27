"""
Kontador di Palavra
===================
Konta frekuensia di kada palavra nun tekstu.
"""


def konta_palavras(tekstu: str) -> dict[str, int]:
    """Konta frekuensia di kada palavra na tekstu."""
    palavras = tekstu.lower().split()
    frekuensia = {}
    for palavra in palavras:
        palavra = palavra.strip(".,!?;:")
        frekuensia[palavra] = frekuensia.get(palavra, 0) + 1
    return frekuensia


def mostra_top_n(frekuensia: dict[str, int], n: int = 5):
    """Mostra top N palavras más komun."""
    ordenadu = sorted(frekuensia.items(), key=lambda x: x[1], reverse=True)
    print(f"Top {n} palavras más komun:")
    for palavra, konta in ordenadu[:n]:
        print(f"  {palavra:<12}: {konta}")


def main():
    tekstu = (
        "Python é un linguajen di programasun sabi. "
        "Nôs ta aprendi Python pamodi Python ta djuda nôs "
        "pa kria programa inkrível. Ku Python nôs ta podi "
        "fazi kualker kuza ki nôs ta imajina."
    )

    print(f"Tekstu: {tekstu}\n")

    frekuensia = konta_palavras(tekstu)
    mostra_top_n(frekuensia, 5)

    print(f"\nTotal di palavras únikuj: {len(frekuensia)}")
    print(f"Total di palavras: {sum(frekuensia.values())}")


if __name__ == "__main__":
    main()
