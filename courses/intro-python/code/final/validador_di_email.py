"""
Validador di Email
==================
Valida formatu di email uzandu regex e funsoens ku type hints.
"""

import re


class EmailInvaliduError(Exception):
    """Exsesan personalizadu pa email invólidu."""
    pass


def valida_email_simples(email: str) -> bool:
    """Valida email ku regras báziku (sen regex)."""
    if " " in email:
        raise EmailInvaliduError("Email ka podi ten espasu")

    if email.count("@") != 1:
        raise EmailInvaliduError("Email presiza eksatamenti un '@'")

    lokal, dominiu = email.split("@")

    if not lokal:
        raise EmailInvaliduError("Parti lokal (antes di @) é vaziu")

    if not dominiu:
        raise EmailInvaliduError("Domíniu (depos di @) é vaziu")

    if "." not in dominiu:
        raise EmailInvaliduError("Domíniu presiza pelu menus un '.'")

    if dominiu.startswith(".") or dominiu.endswith("."):
        raise EmailInvaliduError("Domíniu ka podi kumesa o kaba ku '.'")

    return True


def valida_email_regex(email: str) -> bool:
    """Valida email ku regex."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def testa_emails(emails: list[str]):
    """Testa un lista di emails e mostra rezultadu."""
    print("=== Validason di Email ===\n")
    for email in emails:
        try:
            valida_email_simples(email)
            regex_ok = valida_email_regex(email)
            if regex_ok:
                print(f"  {email:<30} ✅ Válidu")
            else:
                print(f"  {email:<30} ❌ Regex falá")
        except EmailInvaliduError as e:
            print(f"  {email:<30} ❌ {e}")


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
