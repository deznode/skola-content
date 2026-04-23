"""
Exersísiu: Biblioteca (Sistéma di Biblioteca)
=============================================
Konseitu: OOP kompletu — klasis, heransa, enkapsulasion, exsesons

Kria un sistéma di biblioteca ku:
- Exseson personalizadu: LivruIndisponível
- Klasi Livru ku títulu, autor, e estadu
- Klasi Biblioteca ku operasons kompletu
  (adisiona, retira, buska, empresta, devolve)

Livrus di autoris kabu-verdianu e luzófonu:
- Germano Almeida — "O Testamento do Sr. Napumoceno"
- Arménio Vieira — "O Eleito do Sol"
- Jorge Barbosa — "Arquipélago"
"""


class LivruIndisponivel(Exception):
    """Exseson personalizadu — livru ka sta disponível pa empresta."""

    # TODO: Herda di Exception
    # Nota: Ka presiza nada más — 'pass' é sufisienti
    pass


class Livru:
    """Klasi ki representa un livru."""

    def __init__(self, titulo: str, autor: str):
        """
        Inisializa un livru.

        Args:
            titulo: Títulu di livru
            autor: Nomi di autor
        """
        self.titulo = titulo
        self.autor = autor
        # TODO: Kria atributu 'disponivel' ku valor inisial True
        pass

    def __str__(self) -> str:
        """Reprezentason em string di livru."""
        # TODO: Retorna "'{titulo}' di {autor} [Disponível/Emprestadu]"
        # Dika: Uza "Disponível" si disponivel é True, "Emprestadu" si ka
        pass


class Biblioteca:
    """Klasi ki representa un biblioteca."""

    def __init__(self, nomi: str):
        """
        Inisializa biblioteca.

        Args:
            nomi: Nomi di biblioteca
        """
        self.nomi = nomi
        # TODO: Kria lista vazia pa guarda livrus
        pass

    def adisiona_livru(self, livru: Livru) -> None:
        """
        Adisiona un livru na biblioteca.

        Args:
            livru: Livru pa adisiona
        """
        # TODO: Adisiona livru na lista
        # TODO: Mustra mensaji di konfirmasion
        pass

    def retira_livru(self, titulo: str) -> None:
        """
        Retira un livru di biblioteca por títulu.

        Args:
            titulo: Títulu di livru pa retira
        """
        # TODO: Buska livru por títulu
        # TODO: Si inkontra, retira di lista e mustra mensaji
        # TODO: Si ka inkontra, mustra mensaji di erru
        pass

    def buska(self, termu: str) -> list[Livru]:
        """
        Buska livrus por títulu o autor (ka importa maiúskula/minúskula).

        Args:
            termu: Termu di buska

        Returns:
            Lista di livrus ki kombina ku termu
        """
        # TODO: Filtra livrus undi títulu o autor kontén termu
        # Dika: Uza .lower() pa buska sen importa maiúskula/minúskula
        pass

    def empresta(self, titulo: str) -> Livru:
        """
        Empresta un livru di biblioteca.

        Args:
            titulo: Títulu di livru pa empresta

        Returns:
            Livru emprestadu

        Raises:
            LivruIndisponivel: Si livru ka sta disponível
            ValueError: Si livru ka izisti na biblioteca
        """
        # TODO: Buska livru por títulu
        # TODO: Si livru ka izisti, lansa ValueError
        # TODO: Si livru ka sta disponível, lansa LivruIndisponivel
        # TODO: Marka livru komu emprestadu (disponivel = False)
        # TODO: Retorna livru
        pass

    def devolve(self, titulo: str) -> None:
        """
        Devolve un livru emprestadu.

        Args:
            titulo: Títulu di livru pa devolve
        """
        # TODO: Buska livru por títulu
        # TODO: Marka livru komu disponível (disponivel = True)
        # TODO: Mustra mensaji di konfirmasion
        pass

    def __str__(self) -> str:
        """Reprezentason em string di biblioteca."""
        # TODO: Retorna "{nomi} — {N} livru(s) na koleção"
        pass


# ============================================================
# Demonstrasion
# ============================================================
if __name__ == "__main__":
    # Kria biblioteca
    # TODO: bib = Biblioteca("Biblioteca Municipal di Praia")

    # Kria livrus di autoris kabu-verdianu e luzófonu
    # TODO: livru1 = Livru("O Testamento do Sr. Napumoceno", "Germano Almeida")
    # TODO: livru2 = Livru("O Eleito do Sol", "Arménio Vieira")
    # TODO: livru3 = Livru("Arquipélago", "Jorge Barbosa")
    # TODO: livru4 = Livru("Chiquinho", "Baltasar Lopes")

    # Adisiona livrus na biblioteca
    # TODO: bib.adisiona_livru(livru1) ... pa tudu

    # Mustra biblioteca
    # TODO: print(bib)

    # Maria ta buska livrus di "Germano"
    # TODO: print("\nMaria ta buska 'Germano':")
    # TODO: rezultadus = bib.buska("Germano")
    # TODO: Mustra rezultadus

    # João ta empresta un livru
    # TODO: print("\nJoão ta empresta 'Arquipélago':")
    # TODO: bib.empresta("Arquipélago")

    # Edna tenta empresta mesmu livru (debe da erru)
    # TODO: try/except pa empresta "Arquipélago" di novu

    # João devolve livru
    # TODO: bib.devolve("Arquipélago")

    # Nilton ta buska "sol" (buska sen maiúskula/minúskula)
    # TODO: print("\nNilton ta buska 'sol':")
    # TODO: Mustra rezultadus

    print("Diskumenta es TODO-s pa kompleta exersísiu!")
