import re

texto = "Digite sua Senha:"
print(texto)

def validar_senha(senha):
    if not any(c.isupper() for c in senha):
        return "Senha invalida."
    
    if not any(c.islower() for c in senha):
        return "Senha invalida."

    if not any(c.isdigit() for c in senha):
        return "Senha invalida."

    if not re.match("^[a-zA-Z0-9]*$", senha):
        return "Senha invalida."

    if not 6 <= len(senha) <= 32:
        return "Senha invalida."

    return "Senha valida."

while True:
    try:
        senha = input().strip()
        resultado = validar_senha(senha)
        print(resultado)
    except EOFError:
        break
