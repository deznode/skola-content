"""
Prosesador di Ficheru
=====================
Le ficheru CSV ku dadus di vendas, prosesa, e skrebi rezumu.
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
    vendas = []
    try:
        with open(kaminu, "r") as f:
            header = f.readline()  # ignora header
            for liña in f:
                partis = liña.strip().split(",")
                venda = {
                    "produtu": partis[0],
                    "presi": float(partis[1]),
                    "kwantidadi": int(partis[2]),
                }
                vendas.append(venda)
    except FileNotFoundError:
        print(f"Erru: ficheru '{kaminu}' ka atxadu!")
    return vendas


def agrega_vendas(vendas: list[dict]) -> dict[str, dict]:
    """Agrega vendas pa produtu."""
    agregadu = {}
    for venda in vendas:
        nomi = venda["produtu"]
        if nomi not in agregadu:
            agregadu[nomi] = {"kwantidadi": 0, "total": 0.0}
        agregadu[nomi]["kwantidadi"] += venda["kwantidadi"]
        agregadu[nomi]["total"] += venda["presi"] * venda["kwantidadi"]
    return agregadu


def skrebi_rezumu(kaminu: str, agregadu: dict[str, dict]):
    """Skrebi rezumu di vendas na ficheru."""
    with open(kaminu, "w") as f:
        f.write("=== Rezumu di Vendas ===\n")
        total_jeral = 0.0
        max_produtu = ""
        max_kwantidadi = 0

        for nomi, dadus in agregadu.items():
            f.write(f"{nomi}: {dadus['kwantidadi']} unidadis — {dadus['total']:.2f} ECV\n")
            total_jeral += dadus["total"]
            if dadus["kwantidadi"] > max_kwantidadi:
                max_kwantidadi = dadus["kwantidadi"]
                max_produtu = nomi

        f.write("---\n")
        f.write(f"Total jeral: {total_jeral:.2f} ECV\n")
        f.write(f"Produtu más vendidu: {max_produtu} ({max_kwantidadi} unidadis)\n")

    print(f"Rezumu skrebidu na '{kaminu}'")


def main():
    ficheru_entrada = "vendas.csv"
    ficheru_saida = "rezumu.txt"

    if not os.path.exists(ficheru_entrada):
        kria_ficheru_ezemplu(ficheru_entrada)

    vendas = le_vendas(ficheru_entrada)
    if vendas:
        agregadu = agrega_vendas(vendas)
        skrebi_rezumu(ficheru_saida, agregadu)

        with open(ficheru_saida, "r") as f:
            print(f.read())

    # Limpeza
    for f in [ficheru_entrada, ficheru_saida]:
        if os.path.exists(f):
            os.remove(f)


if __name__ == "__main__":
    main()
