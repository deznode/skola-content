"""
Prosesador di Ficheru
=====================
Le un ficheru CSV ku dadus di vendas, prosesa, e skrebi rezumu.

Funsionalidadis:
- Le ficheru CSV ku vendas (produtu, presi, kwantidadi)
- Kalkula total pa kada produtu
- Atxa produtu ku más venda
- Skrebi rezumu na ficheru novu

Objetivus:
- Uza with statement pa abri ficheru
- Uza diferenti modus di ficheru (r, w)
- Trata FileNotFoundError
- Uza disionárius pa agrega dadus

Ficheru di entrada (vendas.csv):
    produtu,presi,kwantidadi
    Katchupa,350,5
    Grogue,200,10
    Ponche,150,8
    Katchupa,350,3
    Grogue,200,5

Saida (rezumu.txt):
    === Rezumu di Vendas ===
    Katchupa: 8 unidadis — 2800.00 ECV
    Grogue: 15 unidadis — 3000.00 ECV
    Ponche: 8 unidadis — 1200.00 ECV
    ---
    Total jeral: 7000.00 ECV
    Produtu más vendidu: Grogue (15 unidadis)
"""

import os


def kria_ficheru_ezemplu(kaminu: str):
    """Kria ficheru CSV di ezemplu pa testu."""
    with open(kaminu, "w") as f:
        f.write("produtu,presi,kwantidadi\n")
        f.write("Katchupa,350,5\n")
        f.write("Grogue,200,10\n")
        f.write("Ponche,150,8\n")
        f.write("Katchupa,350,3\n")
        f.write("Grogue,200,5\n")
    print(f"Ficheru '{kaminu}' kriadu ku susesu!")


def le_vendas(kaminu: str) -> list[dict]:
    """Le ficheru CSV e retorna lista di vendas."""
    # TODO 1: Abri ficheru ku with statement
    # TODO 2: Le primeiru liña (header) e ignora
    # TODO 3: Pa kada liña, separa ku .split(",")
    # TODO 4: Kria dict {"produtu": ..., "presi": float(...), "kwantidadi": int(...)}
    # TODO 5: Trata FileNotFoundError
    pass


def agrega_vendas(vendas: list[dict]) -> dict[str, dict]:
    """
    Agrega vendas pa produtu.
    Retorna: {"Katchupa": {"kwantidadi": 8, "total": 2800.0}, ...}
    """
    # TODO 6: Kria disionáriu vaziu
    # TODO 7: Pa kada venda, akumula kwantidadi e total (presi * kwantidadi)
    # Dika: uza .get() pa inisializa
    pass


def skrebi_rezumu(kaminu: str, agregadu: dict[str, dict]):
    """Skrebi rezumu di vendas na ficheru."""
    # TODO 8: Abri ficheru ku modu "w"
    # TODO 9: Skrebi header, depos kada produtu, depos total jeral
    # TODO 10: Atxa produtu ku más vendas (máximu kwantidadi)
    pass


def main():
    ficheru_entrada = "vendas.csv"
    ficheru_saida = "rezumu.txt"

    # Kria ficheru di ezemplu si ka ezisti
    if not os.path.exists(ficheru_entrada):
        kria_ficheru_ezemplu(ficheru_entrada)

    # TODO 11: Le vendas, agrega, e skrebi rezumu
    # TODO 12: Mostra mensajen di susesu

    # Limpeza (opsinonal)
    # os.remove(ficheru_entrada)
    # os.remove(ficheru_saida)


if __name__ == "__main__":
    main()
