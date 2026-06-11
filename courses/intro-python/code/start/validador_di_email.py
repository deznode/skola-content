"""
Validador di Email
==================
Valida formatu di email uzandu regex e funsoens ku type hints.

Regras di un email válidu:
- Ten eksatamenti un '@'
- Parti antes di '@' (lokal) ka é vaziu
- Parti depos di '@' (domíniu) ten pelu menus un '.'
- Ka ten espasu
- Ka kumesa/kaba ku '.' o '@'

Objetivus:
- Uza módulu re (regex) pa validason
- Uza funsoens ku type hints
- Uza raise pa signala errus
- Kombina tudu konseptus di Módulu 3

Ezemplu:
    maria@skola.dev     → ✅ Válidu
    joao@gmail.com      → ✅ Válidu
    ana@                → ❌ Invólidu: domíniu vaziu
    @skola.dev          → ❌ Invólidu: parti lokal vaziu
    pedro skola.dev     → ❌ Invólidu: falta '@'
"""

import re


class EmailInvaliduError(Exception):
    """Exsesan personalizadu pa email invólidu."""
    pass


def valida_email_simples(email: str) -> bool:
    """
    Valida email ku regras báziku (sen regex).
    Retorna True si válidu, lansa EmailInvaliduError si invólidu.
    """
    # TODO 1: Verifica si ten espasu
    # TODO 2: Verifica si ten eksatamenti un '@'
    # TODO 3: Separa na parti lokal e domíniu
    # TODO 4: Verifica si parti lokal ka é vaziu
    # TODO 5: Verifica si domíniu ten pelu menus un '.'
    # TODO 6: Si tudu pasa, retorna True
    # TODO 7: Pa kada falha, raise EmailInvaliduError("mensajen")
    pass


def valida_email_regex(email: str) -> bool:
    """
    Valida email ku regex.
    Pattern: karakter+ @ karakter+ . karakter{2,}
    """
    # TODO 8: Defini pattern regex
    # Dika: r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # TODO 9: Uza re.match() pa verifica
    pass


def testa_emails(emails: list[str]):
    """Testa un lista di emails e mostra rezultadu."""
    # TODO 10: Pa kada email, tenta valida e mostra ✅ o ❌
    pass


def main():
    emails_di_testu = [
        "maria@skola.dev",
        "joao.costa@gmail.com",
        "ana@",
        "@skola.dev",
        "pedro skola.dev",
        "carla@mail",
        "djina@escola.cv",
        "nilton@.com",
    ]

    testa_emails(emails_di_testu)


if __name__ == "__main__":
    main()
