"""
Analiza di Nota
===============
Analiza notas di estudantis e kalkula estatístikas.
"""


def kalkula_media(notas: list[int]) -> float:
    """Kalkula média di notas."""
    return sum(notas) / len(notas)


def klasifika_nota(nota: int) -> str:
    """
    Klasifika nota pa letra (skala 0-20):
    A = 16-20, B = 14-15, C = 12-13, D = 10-11, F = 0-9
    """
    if nota >= 16:
        return "A"
    elif nota >= 14:
        return "B"
    elif nota >= 12:
        return "C"
    elif nota >= 10:
        return "D"
    else:
        return "F"


def konta_distribuison(notas: list[int]) -> dict[str, int]:
    """Konta quantu nota pa kada letra."""
    distribuison = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for nota in notas:
        letra = klasifika_nota(nota)
        distribuison[letra] += 1
    return distribuison


def main():
    notas = [15, 12, 8, 18, 9, 14, 16, 7, 11, 19]

    print("=== Analiza di Nota ===")
    print(f"Notas: {notas}")

    media = kalkula_media(notas)
    print(f"Média: {media:.1f}")
    print(f"Nota máximu: {max(notas)} | Nota mínimu: {min(notas)}")

    pasadu = len([n for n in notas if n >= 10])
    falidu = len(notas) - pasadu
    print(f"Pasadu: {pasadu} | Falidu: {falidu}")

    dist = konta_distribuison(notas)
    dist_str = ", ".join(f"{letra}={konta}" for letra, konta in dist.items())
    print(f"Distribuison: {dist_str}")


if __name__ == "__main__":
    main()
