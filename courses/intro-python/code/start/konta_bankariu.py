"""
Exersísiu: Konta Bankáriu
=========================
Konseitu: klasi, enkapsulasion, @property

Kria un klasi KontaBankariu ku:
- Atributu privadu pa saldo
- Property pa asesa saldo
- Métudu pa deposita ku validason
- Métudu pa retira ku verifikason di saldo
- Reprezentason em string

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
        self.titular = titular
        # TODO: Kria atributu privadu __saldo ku saldo_inisial
        # Nota: Valida ma saldo_inisial ka pode ser negativu
        pass

    @property
    def saldo(self) -> float:
        """Property pa asesa saldo di konta (somenti leitura)."""
        # TODO: Retorna valor di __saldo
        pass

    def deposita(self, montanti: float) -> None:
        """
        Deposita dinheru na konta.

        Args:
            montanti: Valor pa deposita (debe ser positivu)

        Raises:
            ValueError: Si montanti é negativu o zero
        """
        # TODO: Valida montanti (debe ser > 0)
        # TODO: Adisiona montanti na saldo
        # TODO: Mustra mensaji di konfirmasion
        pass

    def retira(self, montanti: float) -> None:
        """
        Retira dinheru di konta.

        Args:
            montanti: Valor pa retira

        Raises:
            ValueError: Si montanti é negativu o zero
            ValueError: Si saldo é insufisienti
        """
        # TODO: Valida montanti (debe ser > 0)
        # TODO: Verifica si saldo é sufisienti
        # TODO: Subtrai montanti di saldo
        # TODO: Mustra mensaji di konfirmasion
        pass

    def __str__(self) -> str:
        """Reprezentason em string di konta."""
        # TODO: Retorna "Konta di {titular}: {saldo:.2f} ECV"
        pass


# ============================================================
# Demonstrasion
# ============================================================
if __name__ == "__main__":
    # Kria konta pa Ana ku saldo inisial di 5000 ECV
    # TODO: konta_ana = KontaBankariu("Ana", 5000)

    # Mustra konta
    # TODO: print(konta_ana)

    # Ana deposita 2500 ECV
    # TODO: konta_ana.deposita(2500)

    # Ana retira 1000 ECV
    # TODO: konta_ana.retira(1000)

    # Mustra saldo final
    # TODO: print(f"Saldo final di Ana: {konta_ana.saldo:.2f} ECV")

    # Tenta retira más ki saldo (debe da erru)
    # TODO: try/except pa retira 10000 ECV

    # Tenta deposita valor negativu (debe da erru)
    # TODO: try/except pa deposita -500 ECV

    print("Diskumenta es TODO-s pa kompleta exersísiu!")
