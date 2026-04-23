"""
Exersísiu: Biblioteca (Solusion Kompletu)
=========================================
Konseitu: OOP kompletu — klasis, heransa, enkapsulasion, exsesons

Sistéma di biblioteca ku exseson personalizadu,
klasi Livru e Biblioteca, ku operasons kompletu.

Livrus di autoris kabu-verdianu e luzófonu:
- Germano Almeida — "O Testamento do Sr. Napumoceno"
- Arménio Vieira — "O Eleito do Sol"
- Jorge Barbosa — "Arquipélago"
- Baltasar Lopes — "Chiquinho"
"""


class LivruIndisponivel(Exception):
    """Exseson personalizadu — livru ka sta disponível pa empresta."""
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
        self.disponivel = True

    def __str__(self) -> str:
        """Reprezentason em string di livru."""
        estadu = "Disponível" if self.disponivel else "Emprestadu"
        return f"'{self.titulo}' di {self.autor} [{estadu}]"


class Biblioteca:
    """Klasi ki representa un biblioteca."""

    def __init__(self, nomi: str):
        """
        Inisializa biblioteca.

        Args:
            nomi: Nomi di biblioteca
        """
        self.nomi = nomi
        self.__livrus: list[Livru] = []

    def adisiona_livru(self, livru: Livru) -> None:
        """
        Adisiona un livru na biblioteca.

        Args:
            livru: Livru pa adisiona
        """
        self.__livrus.append(livru)
        print(f"Livru adisionadu: {livru}")

    def retira_livru(self, titulo: str) -> None:
        """
        Retira un livru di biblioteca por títulu.

        Args:
            titulo: Títulu di livru pa retira
        """
        for livru in self.__livrus:
            if livru.titulo.lower() == titulo.lower():
                self.__livrus.remove(livru)
                print(f"Livru retiradu: {livru}")
                return
        print(f"Livru '{titulo}' ka foi inkontrádu na biblioteca")

    def buska(self, termu: str) -> list[Livru]:
        """
        Buska livrus por títulu o autor (ka importa maiúskula/minúskula).

        Args:
            termu: Termu di buska

        Returns:
            Lista di livrus ki kombina ku termu
        """
        termu_lower = termu.lower()
        return [
            livru for livru in self.__livrus
            if termu_lower in livru.titulo.lower()
            or termu_lower in livru.autor.lower()
        ]

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
        for livru in self.__livrus:
            if livru.titulo.lower() == titulo.lower():
                if not livru.disponivel:
                    raise LivruIndisponivel(
                        f"Livru '{titulo}' já sta emprestadu"
                    )
                livru.disponivel = False
                print(f"Livru emprestadu: {livru}")
                return livru
        raise ValueError(f"Livru '{titulo}' ka izisti na biblioteca")

    def devolve(self, titulo: str) -> None:
        """
        Devolve un livru emprestadu.

        Args:
            titulo: Títulu di livru pa devolve
        """
        for livru in self.__livrus:
            if livru.titulo.lower() == titulo.lower():
                livru.disponivel = True
                print(f"Livru devolvidu: {livru}")
                return
        print(f"Livru '{titulo}' ka foi inkontrádu na biblioteca")

    def __str__(self) -> str:
        """Reprezentason em string di biblioteca."""
        return f"{self.nomi} — {len(self.__livrus)} livru(s) na koleção"


# ============================================================
# Demonstrasion
# ============================================================
if __name__ == "__main__":
    print("=" * 55)
    print("  Sistéma di Biblioteca di Kabo Verdi")
    print("=" * 55)

    # Kria biblioteca
    bib = Biblioteca("Biblioteca Municipal di Praia")

    # Kria livrus di autoris kabu-verdianu e luzófonu
    livru1 = Livru("O Testamento do Sr. Napumoceno", "Germano Almeida")
    livru2 = Livru("O Eleito do Sol", "Arménio Vieira")
    livru3 = Livru("Arquipélago", "Jorge Barbosa")
    livru4 = Livru("Chiquinho", "Baltasar Lopes")

    # Adisiona livrus na biblioteca
    print("\n--- Adisiona Livrus ---")
    bib.adisiona_livru(livru1)
    bib.adisiona_livru(livru2)
    bib.adisiona_livru(livru3)
    bib.adisiona_livru(livru4)

    # Mustra biblioteca
    print(f"\n{bib}")

    # Maria ta buska livrus di "Germano"
    print("\n--- Maria ta buska 'Germano' ---")
    rezultadus = bib.buska("Germano")
    for livru in rezultadus:
        print(f"  {livru}")

    # João ta empresta un livru
    print("\n--- João ta empresta 'Arquipélago' ---")
    bib.empresta("Arquipélago")

    # Edna tenta empresta mesmu livru
    print("\n--- Edna tenta empresta 'Arquipélago' ---")
    try:
        bib.empresta("Arquipélago")
    except LivruIndisponivel as e:
        print(f"Erru: {e}")

    # João devolve livru
    print("\n--- João devolve 'Arquipélago' ---")
    bib.devolve("Arquipélago")

    # Agora Edna konsigi empresta
    print("\n--- Edna tenta empresta 'Arquipélago' di novu ---")
    bib.empresta("Arquipélago")

    # Nilton ta buska "sol" (buska sen importa maiúskula/minúskula)
    print("\n--- Nilton ta buska 'sol' ---")
    rezultadus = bib.buska("sol")
    for livru in rezultadus:
        print(f"  {livru}")

    # Kelvin tenta empresta livru ki ka izisti
    print("\n--- Kelvin tenta empresta livru ki ka izisti ---")
    try:
        bib.empresta("Livru Fantázma")
    except ValueError as e:
        print(f"Erru: {e}")
