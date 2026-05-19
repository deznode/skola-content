"""
Kontador di Palavra (Ficheru)
=============================
Konta frekuensia di palavras lidu di un ficheru di tekstu.

Diferensa di ezersísiu anterior: gosi ta le di ficheru, nau di string.

Funsionalidadis:
- Le tekstu di un ficheru
- Konta frekuensia di kada palavra
- Mostra top 10 palabras
- Skrebi rezultadu na ficheru novu

Objetivus:
- Uza file I/O ku with statement
- Kombina disionárius ku funsoens
- Trata FileNotFoundError
- Uza sorted() ku lambda

Ezemplu di saida:
    === Frekuensia di Palavra ===
    Ficheru: poema.txt
    Total di palavras: 42
    Palavras únikuj: 28

    Top 10:
      di          : 5
      mar         : 3
      ...
"""

import os


def kria_ficheru_ezemplu(kaminu: str):
    """Kria ficheru di tekstu di ezemplu."""
    tekstu = (
        "Mar azul di Kabu Verdi\n"
        "Mar ki ta kanta morabeza\n"
        "Ilha di sol e di mar\n"
        "Nôs terra é sabi\n"
        "Nôs ta ama nôs terra\n"
        "Mar ta leva sodadi\n"
        "Ma mar ta trazi speransa\n"
    )
    with open(kaminu, "w") as f:
        f.write(tekstu)


def le_ficheru(kaminu: str) -> str:
    """Le tudu konteúdu di un ficheru."""
    # TODO 1: Uza with statement pa abri e le ficheru
    # TODO 2: Trata FileNotFoundError
    pass


def konta_palavras(tekstu: str) -> dict[str, int]:
    """Konta frekuensia di kada palavra."""
    # TODO 3: Konverti pa minúskulu, separa palavras
    # TODO 4: Limpa pontuason ku .strip(".,!?;:")
    # TODO 5: Konta ku disionáriu
    pass


def mostra_top_n(frekuensia: dict[str, int], n: int = 10):
    """Mostra top N palavras."""
    # TODO 6: Ordena pa frekuensia (máximu primeiru)
    # TODO 7: Mostra apenas top N
    pass


def skrebi_rezultadu(kaminu: str, frekuensia: dict[str, int]):
    """Skrebi frekuensia na ficheru."""
    # TODO 8: Skrebi tudu palavras ku kontas na ficheru
    pass


def main():
    ficheru_entrada = "poema.txt"

    if not os.path.exists(ficheru_entrada):
        kria_ficheru_ezemplu(ficheru_entrada)

    # TODO 9: Le ficheru, konta palavras, mostra rezultadu
    # TODO 10: Skrebi rezultadu na "frekuensia.txt"

    # Limpeza
    # os.remove(ficheru_entrada)


if __name__ == "__main__":
    main()
