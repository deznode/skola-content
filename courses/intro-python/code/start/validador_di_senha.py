"""
Validador di Senha
==================
Verifica si un senha é forti o fraku.

Un senha forti ta presiza:
- Minimu 8 karakter
- Pelu menus 1 letra maiúskulu (A-Z)
- Pelu menus 1 letra minúskulu (a-z)
- Pelu menus 1 numeru (0-9)
- Pelu menus 1 karakter spesial (!@#$%^&*()_+-=)

Objetivus:
- Uza string methods (.isupper(), .islower(), .isdigit())
- Uza any() ku generator expression
- Uza len() pa verifica tamañu
- Uza kondisionais pa da feedback

Ezemplu di uzu:
    Mete bo senha: abc
    Senha FRAKU:
    - Presiza pelu menus 8 karakter (bo ten 3)
    - Falta letra maiúskulu
    - Falta numeru
    - Falta karakter spesial

    Mete bo senha: M4ria@Skola!
    Senha FORTI! Bo senha ta pasa tudu regra.
"""

KARAKTER_SPESIAL = "!@#$%^&*()_+-="


def valida_senha(senha: str) -> list[str]:
    """
    Verifica senha e retorna lista di problemas.
    Si lista é vaziu, senha é forti.
    """
    problemas = []

    # TODO 1: Verifica si senha ten pelu menus 8 karakter
    # Si nau, ajunta mensajen na lista 'problemas'

    # TODO 2: Verifica si ten pelu menus 1 letra maiúskulu
    # Dika: uza any(k.isupper() for k in senha)

    # TODO 3: Verifica si ten pelu menus 1 letra minúskulu

    # TODO 4: Verifica si ten pelu menus 1 numeru
    # Dika: uza any(k.isdigit() for k in senha)

    # TODO 5: Verifica si ten pelu menus 1 karakter spesial
    # Dika: uza any(k in KARAKTER_SPESIAL for k in senha)

    return problemas


def main():
    senha = input("Mete bo senha: ")
    problemas = valida_senha(senha)

    # TODO 6: Si ka ten problema, mostra "Senha FORTI!"
    # Si ten problemas, mostra "Senha FRAKU:" e lista kada problema
    pass


if __name__ == "__main__":
    main()
