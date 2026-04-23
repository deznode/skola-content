"""
Kontador di Palavra (Ficheru)
=============================
Konta frekuensia di palavras lidu di un ficheru di tekstu.
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
    try:
        with open(kaminu, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erru: ficheru '{kaminu}' ka atxadu!")
        return ""


def konta_palavras(tekstu: str) -> dict[str, int]:
    """Konta frekuensia di kada palavra."""
    palavras = tekstu.lower().split()
    frekuensia = {}
    for palavra in palavras:
        palavra = palavra.strip(".,!?;:")
        if palavra:
            frekuensia[palavra] = frekuensia.get(palavra, 0) + 1
    return frekuensia


def mostra_top_n(frekuensia: dict[str, int], n: int = 10):
    """Mostra top N palavras."""
    ordenadu = sorted(frekuensia.items(), key=lambda x: x[1], reverse=True)
    print(f"\nTop {n}:")
    for palavra, konta in ordenadu[:n]:
        print(f"  {palavra:<12}: {konta}")


def skrebi_rezultadu(kaminu: str, frekuensia: dict[str, int]):
    """Skrebi frekuensia na ficheru."""
    ordenadu = sorted(frekuensia.items(), key=lambda x: x[1], reverse=True)
    with open(kaminu, "w") as f:
        f.write("=== Frekuensia di Palavra ===\n\n")
        for palavra, konta in ordenadu:
            f.write(f"{palavra:<12}: {konta}\n")
    print(f"Rezultadu skrebidu na '{kaminu}'")


def main():
    ficheru_entrada = "poema.txt"
    ficheru_saida = "frekuensia.txt"

    if not os.path.exists(ficheru_entrada):
        kria_ficheru_ezemplu(ficheru_entrada)

    tekstu = le_ficheru(ficheru_entrada)
    if tekstu:
        frekuensia = konta_palavras(tekstu)
        total = sum(frekuensia.values())
        uniku = len(frekuensia)

        print(f"=== Frekuensia di Palavra ===")
        print(f"Ficheru: {ficheru_entrada}")
        print(f"Total di palavras: {total}")
        print(f"Palavras únikuj: {uniku}")

        mostra_top_n(frekuensia)
        skrebi_rezultadu(ficheru_saida, frekuensia)

    # Limpeza
    for f in [ficheru_entrada, ficheru_saida]:
        if os.path.exists(f):
            os.remove(f)


if __name__ == "__main__":
    main()
