"""
Kalkuladora Simples
===================
Kria un kalkuladora ki ta pidi dois numeru e un operason (+, -, *, /)
e ta mostra resultadu.

Objetivus:
- Uza input() pa resebe dadus di uzuáriu
- Uza float() pa konverti string pa numeru
- Uza if/elif/else pa skolhe operason
- Trata erru di divison pa zero

Ezemplu di uzu:
    Mete primeiru numeru: 10
    Mete segundu numeru: 3
    Skolhe operason (+, -, *, /): *
    Resultadu: 10.0 * 3.0 = 30.0
"""


def kalkuladora():
    # TODO 1: Pidi primeiru numeru e konverti pa float
    num1 = ...

    # TODO 2: Pidi segundu numeru e konverti pa float
    num2 = ...

    # TODO 3: Pidi operason (+, -, *, /)
    operason = ...

    # TODO 4: Uza if/elif/else pa kalkula resultadu
    # - Si operason é '+', soma num1 + num2
    # - Si operason é '-', subtrai num1 - num2
    # - Si operason é '*', multiplika num1 * num2
    # - Si operason é '/', dividi num1 / num2 (ma verifica si num2 KA é 0!)
    # - Si operason é invólidu, mostra mensajen di erru

    # TODO 5: Mostra resultadu ku f-string
    # Formatu: "Resultadu: {num1} {operason} {num2} = {resultadu}"
    pass


if __name__ == "__main__":
    kalkuladora()
