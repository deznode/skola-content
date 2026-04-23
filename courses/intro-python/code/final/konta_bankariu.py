"""
Exersísiu: Konta Bankáriu (Solusion Kompletu)
==============================================
Konseitu: klasi, enkapsulasion, @property

Klasi KontaBankariu ku enkapsulasion di saldo,
validason di operasons, e reprezentason em string.

Moeda: ECV (Escudo Cabo-Verdiano)
"""


class KontaBankariu:
    """Klasi ki representa un konta bankáriu."""

    def __init__(self, titular: str, saldo_inisial: float = 0):
        """
        Inisializa konta bankáriu.

        Args:
            titular: Nomi di donu di konta
            saldo_inisial: Saldo inisial (padrão: 0 ECV)
        """
        if saldo_inisial < 0:
            raise ValueError("Saldo inisial ka pode ser negativu")
        self.titular = titular
        self.__saldo = saldo_inisial

    @property
    def saldo(self) -> float:
        """Property pa asesa saldo di konta (somenti leitura)."""
        return self.__saldo

    def deposita(self, montanti: float) -> None:
        """
        Deposita dinheru na konta.

        Args:
            montanti: Valor pa deposita (debe ser positivu)

        Raises:
            ValueError: Si montanti é negativu o zero
        """
        if montanti <= 0:
            raise ValueError("Montanti di depósitu debe ser positivu")
        self.__saldo += montanti
        print(f"Depósitu di {montanti:.2f} ECV realisadu ku susesu")

    def retira(self, montanti: float) -> None:
        """
        Retira dinheru di konta.

        Args:
            montanti: Valor pa retira

        Raises:
            ValueError: Si montanti é negativu o zero
            ValueError: Si saldo é insufisienti
        """
        if montanti <= 0:
            raise ValueError("Montanti di retirada debe ser positivu")
        if montanti > self.__saldo:
            raise ValueError(
                f"Saldo insufisienti. Saldo atual: {self.__saldo:.2f} ECV"
            )
        self.__saldo -= montanti
        print(f"Retirada di {montanti:.2f} ECV realisadu ku susesu")

    def __str__(self) -> str:
        """Reprezentason em string di konta."""
        return f"Konta di {self.titular}: {self.__saldo:.2f} ECV"


# ============================================================
# Demonstrasion
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  Sistéma Bankáriu di Kabo Verdi")
    print("=" * 50)

    # Ana abri un konta ku 5000 ECV
    konta_ana = KontaBankariu("Ana", 5000)
    print(f"\n{konta_ana}")

    # Ana deposita 2500 ECV
    print("\n--- Ana ta deposita 2500 ECV ---")
    konta_ana.deposita(2500)
    print(f"{konta_ana}")

    # Ana retira 1000 ECV
    print("\n--- Ana ta retira 1000 ECV ---")
    konta_ana.retira(1000)
    print(f"{konta_ana}")

    # Mustra saldo final
    print(f"\nSaldo final di Ana: {konta_ana.saldo:.2f} ECV")

    # Tenta retira más ki saldo
    print("\n--- Tenta retira 10000 ECV (debe da erru) ---")
    try:
        konta_ana.retira(10000)
    except ValueError as e:
        print(f"Erru: {e}")

    # Tenta deposita valor negativu
    print("\n--- Tenta deposita -500 ECV (debe da erru) ---")
    try:
        konta_ana.deposita(-500)
    except ValueError as e:
        print(f"Erru: {e}")

    # Pedro abri konta sen saldo inisial
    print("\n--- Pedro abri konta novu ---")
    konta_pedro = KontaBankariu("Pedro")
    print(f"{konta_pedro}")
    konta_pedro.deposita(15000)
    print(f"{konta_pedro}")
