"""
Numeru Primu
============
Atxa tudu numeru primu entre 1 e 100.

Un numeru primu é un numeru ki só ta dividi pa 1 e pa e mesmu.
Ezemplu: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

Objetivus:
- Uza nested loops (loop dentru di loop)
- Uza break pa otimiza
- Uza for-else (else ta korre si loop ka uza break)
- Uza range() ku diferenti argumentus

Saida esperadu:
    Numerus primu entre 1 e 100:
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
    Total: 25 numerus primu
"""


def e_primu(numeru: int) -> bool:
    """Retorna True si numeru é primu, False si nau."""
    # TODO 1: Numeru menor ki 2 ka é primu
    # TODO 2: Uza loop di 2 até numeru pa verifica si ten divisor
    # Dika: si numeru % i == 0, e ka é primu
    # Bónus: bo só presiza verifica até raiz quadrada di numeru
    pass


def main():
    # TODO 3: Uza loop pa atxa tudu numeru primu entre 1 e 100
    # TODO 4: Konta total di numerus primu
    # TODO 5: Mostra lista e total
    pass


if __name__ == "__main__":
    main()
