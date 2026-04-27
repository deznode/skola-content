"""
Analiza di Nota
===============
Analiza notas di estudantis e kalkula estatístikas.

Funsionalidadis:
- Kalkula média, nota máximu e mínimu
- Konta quantu estudanti pasa/fali (nota >= 10 pa pasa, skala 0-20)
- Klasifika notas pa letra (A, B, C, D, F)
- Mostra rezumu

Objetivus:
- Uza listas e funsoens built-in (sum, len, max, min)
- Uza list comprehension ku kondison
- Uza disionáriu pa konta frekuensia

Ezemplu di saida:
    === Analiza di Nota ===
    Notas: [15, 12, 8, 18, 9, 14, 16, 7, 11, 19]
    Média: 12.9
    Nota máximu: 19 | Nota mínimu: 7
    Pasadu: 7 | Falidu: 3
    Distribuison: A=2, B=2, C=2, D=1, F=3
"""


def kalkula_media(notas: list[int]) -> float:
    """Kalkula média di notas."""
    # TODO 1: Retorna média (sum / len)
    pass


def klasifika_nota(nota: int) -> str:
    """
    Klasifika nota pa letra (skala 0-20):
    A = 16-20 (Exselenti)
    B = 14-15 (Bon)
    C = 12-13 (Sufisienti)
    D = 10-11 (Satisfatóriu)
    F = 0-9   (Falidu)
    """
    # TODO 2: Uza if/elif/else pa retorna letra
    pass


def konta_distribuison(notas: list[int]) -> dict[str, int]:
    """Konta quantu nota pa kada letra."""
    # TODO 3: Kria disionáriu ku kontas {"A": 0, "B": 0, ...}
    # TODO 4: Uza loop pa klasifika kada nota e konta
    pass


def main():
    notas = [15, 12, 8, 18, 9, 14, 16, 7, 11, 19]

    print("=== Analiza di Nota ===")
    print(f"Notas: {notas}")

    # TODO 5: Kalkula e mostra média
    # TODO 6: Mostra nota máximu e mínimu (uza max() e min())
    # TODO 7: Konta quantu pasa e fali (nota >= 10 pa pasa)
    # Dika: uza list comprehension ku kondison e len()
    # TODO 8: Mostra distribuison pa letra
    pass


if __name__ == "__main__":
    main()
