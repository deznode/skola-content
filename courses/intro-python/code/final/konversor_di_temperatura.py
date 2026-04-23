"""
Konversor di Temperatura
========================
Konverti entre Celsius, Fahrenheit e Kelvin ku validason.
"""


def celsius_pa_fahrenheit(celsius: float) -> float:
    """Konverti Celsius pa Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_pa_celsius(fahrenheit: float) -> float:
    """Konverti Fahrenheit pa Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_pa_kelvin(celsius: float) -> float:
    """Konverti Celsius pa Kelvin."""
    kelvin = celsius + 273.15
    if kelvin < 0:
        raise ValueError("Temperatura abaxu di zero absoluto ka é posível!")
    return kelvin


def kelvin_pa_celsius(kelvin: float) -> float:
    """Konverti Kelvin pa Celsius."""
    if kelvin < 0:
        raise ValueError("Kelvin ka podi ser negatifu!")
    return kelvin - 273.15


def main():
    print("Skolhe konversun:")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")

    opsun = input("Opsun: ")

    try:
        temp = float(input("Mete temperatura: "))

        if opsun == "1":
            rezultadu = celsius_pa_fahrenheit(temp)
            print(f"{temp:.1f}°C = {rezultadu:.1f}°F")
        elif opsun == "2":
            rezultadu = fahrenheit_pa_celsius(temp)
            print(f"{temp:.1f}°F = {rezultadu:.1f}°C")
        elif opsun == "3":
            rezultadu = celsius_pa_kelvin(temp)
            print(f"{temp:.1f}°C = {rezultadu:.1f}K")
        elif opsun == "4":
            rezultadu = kelvin_pa_celsius(temp)
            print(f"{temp:.1f}K = {rezultadu:.1f}°C")
        else:
            print("Opsun invólidu!")

    except ValueError as e:
        print(f"Erru: {e}")


if __name__ == "__main__":
    main()
