"""
Kalkuladora Simples
===================
Kria un kalkuladora ki ta pidi dois numeru e un operason (+, -, *, /)
e ta mostra resultadu.
"""


def kalkuladora():
    num1 = float(input("Mete primeiru numeru: "))
    num2 = float(input("Mete segundu numeru: "))
    operason = input("Skolhe operason (+, -, *, /): ")

    if operason == "+":
        resultadu = num1 + num2
    elif operason == "-":
        resultadu = num1 - num2
    elif operason == "*":
        resultadu = num1 * num2
    elif operason == "/":
        if num2 == 0:
            print("Erru: ka podi dividi pa zero!")
            return
        resultadu = num1 / num2
    else:
        print(f"Erru: operason '{operason}' ka é válidu. Uza +, -, * o /")
        return

    print(f"Resultadu: {num1} {operason} {num2} = {resultadu}")


if __name__ == "__main__":
    kalkuladora()
