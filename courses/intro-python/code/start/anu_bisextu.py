"""
Anu Bisextu
===========
Verifica si un anu é bisextu (leap year) o nau.

Regras:
- Un anu é bisextu si e ta dividi pa 4
- MA si e ta dividi pa 100, e KA é bisextu
- MA si e ta dividi pa 400, e É bisextu

Ezemplu:
    2024 → É bisextu (dividi pa 4, ka dividi pa 100)
    1900 → KA é bisextu (dividi pa 100, ka dividi pa 400)
    2000 → É bisextu (dividi pa 400)
    2023 → KA é bisextu (ka dividi pa 4)

Objetivus:
- Uza nested conditionals (if dentru di if)
- Uza operador modulus (%) pa verifica divisibilidadi
- Uza f-strings pa mostra resultadu
"""


def verifica_anu_bisextu(anu: int) -> bool:
    """Retorna True si anu é bisextu, False si nau."""
    # TODO: Implementa lójika di anu bisextu
    # Dika: Kumesa ku regra di 400, depos 100, depos 4
    pass


def main():
    anu = int(input("Mete un anu: "))

    # TODO: Xama verifica_anu_bisextu() e mostra resultadu
    # Formatu: "{anu} é un anu bisextu!" o "{anu} KA é un anu bisextu."
    pass


if __name__ == "__main__":
    main()
