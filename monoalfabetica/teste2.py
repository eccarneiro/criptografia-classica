ALFABETO = "abcdefghijklmnopqrstuvwxyz"

def gerar_chave_manual(chave):
    """
    1- Receber a chave
    2- Remover letras duplicadas
    3- Posicionar no início do alfabeto cifrado
    4- Preencher com as letras que ainda não foram usadas (em ordem alfabética)
    """

    """
    Remover os caracteres repetidos da string
    """
    chave = chave.replace(" ", "")
    chave_limpa = "".join(chave.lower())

    chave_completa = []
    for letra in chave_limpa:
        chave_completa.append(letra)

    alfabeto_copia = []

    for letra in ALFABETO:
        alfabeto_copia.append(letra)

    for letra in alfabeto_copia:
        chave_completa.append(letra)

    return "".join(dict.fromkeys(chave_completa))


print(gerar_chave_manual("Felipe carca erguida"))