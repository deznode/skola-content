"""
Numeru Primu
============
Atxa tudu numeru primu entre 1 e 100.

Un numeru primu é un numeru ki só ta dividi pa 1 e pa e mesmu.
"""


def e_primu(numeru: int) -> bool:
    """Retorna True si numeru é primu, False si nau."""
    if numeru < 2:
        return False
    for i in range(2, numeru):
        if numeru % i == 0:
            return False
    return True


def main():
    print("Numerus primu entre 1 e 100:")

    primus = []
    for numeru in range(1, 101):
        if e_primu(numeru):
            primus.append(numeru)

    print(" ".join(str(n) for n in primus))
    print(f"Total: {len(primus)} numerus primu")


if __name__ == "__main__":
    main()
