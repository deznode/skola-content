"""
Konversor di Temperatura
========================
Konverti entre Celsius, Fahrenheit e Kelvin ku validason.

Funsionalidadis:
- Celsius → Fahrenheit: F = C × 9/5 + 32
- Fahrenheit → Celsius: C = (F - 32) × 5/9
- Celsius → Kelvin: K = C + 273.15
- Kelvin → Celsius: C = K - 273.15

Objetivus:
- Uza funsoens ku type hints
- Uza kondisionais pa skolhe konversun
- Uza validason (Kelvin ka podi ser negatifu)
- Uza f-strings pa formata rezultadu

Ezemplu di uzu:
    Skolhe konversun:
    1. Celsius → Fahrenheit
    2. Fahrenheit → Celsius
    3. Celsius → Kelvin
    4. Kelvin → Celsius
    Opsun: 1
    Mete temperatura: 100
    100.0°C = 212.0°F
"""


def celsius_pa_fahrenheit(celsius: float) -> float:
    """Konverti Celsius pa Fahrenheit."""
    # TODO 1: Implementa fórmula F = C × 9/5 + 32
    pass


def fahrenheit_pa_celsius(fahrenheit: float) -> float:
    """Konverti Fahrenheit pa Celsius."""
    # TODO 2: Implementa fórmula C = (F - 32) × 5/9
    pass


def celsius_pa_kelvin(celsius: float) -> float:
    """Konverti Celsius pa Kelvin."""
    # TODO 3: Implementa fórmula K = C + 273.15
    # TODO 4: Valida ki rezultadu ka é negatifu (Kelvin mínimu é 0)
    pass


def kelvin_pa_celsius(kelvin: float) -> float:
    """Konverti Kelvin pa Celsius."""
    # TODO 5: Valida ki kelvin ka é negatifu
    # TODO 6: Implementa fórmula C = K - 273.15
    pass


def main():
    print("Skolhe konversun:")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")

    opsun = input("Opsun: ")

    # TODO 7: Pidi temperatura e xama funsun apropriadu
    # TODO 8: Mostra rezultadu formatadu ku 1 kaza desimal
    # TODO 9: Trata ValueError si uzuáriu mete tekstu en vez di numeru
    pass


if __name__ == "__main__":
    main()
