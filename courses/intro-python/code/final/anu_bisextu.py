"""
Anu Bisextu
===========
Verifica si un anu é bisextu (leap year) o nau.

Regras:
- Un anu é bisextu si e ta dividi pa 4
- MA si e ta dividi pa 100, e KA é bisextu
- MA si e ta dividi pa 400, e É bisextu
"""


def verifica_anu_bisextu(anu: int) -> bool:
    """Retorna True si anu é bisextu, False si nau."""
    if anu % 400 == 0:
        return True
    elif anu % 100 == 0:
        return False
    elif anu % 4 == 0:
        return True
    else:
        return False


def main():
    anu = int(input("Mete un anu: "))

    if verifica_anu_bisextu(anu):
        print(f"{anu} é un anu bisextu!")
    else:
        print(f"{anu} KA é un anu bisextu.")


if __name__ == "__main__":
    main()
