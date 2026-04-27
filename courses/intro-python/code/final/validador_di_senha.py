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
"""

KARAKTER_SPESIAL = "!@#$%^&*()_+-="


def valida_senha(senha: str) -> list[str]:
    """
    Verifica senha e retorna lista di problemas.
    Si lista é vaziu, senha é forti.
    """
    problemas = []

    if len(senha) < 8:
        problemas.append(f"Presiza pelu menus 8 karakter (bo ten {len(senha)})")

    if not any(k.isupper() for k in senha):
        problemas.append("Falta letra maiúskulu")

    if not any(k.islower() for k in senha):
        problemas.append("Falta letra minúskulu")

    if not any(k.isdigit() for k in senha):
        problemas.append("Falta numeru")

    if not any(k in KARAKTER_SPESIAL for k in senha):
        problemas.append("Falta karakter spesial")

    return problemas


def main():
    senha = input("Mete bo senha: ")
    problemas = valida_senha(senha)

    if not problemas:
        print("Senha FORTI! Bo senha ta pasa tudu regra.")
    else:
        print("Senha FRAKU:")
        for problema in problemas:
            print(f"  - {problema}")


if __name__ == "__main__":
    main()
