import random

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

def gerar_chave_aleatoria():
    chave_aleatoria = []
    for letra in ALFABETO:
        chave_aleatoria.append(letra)

    random.shuffle(chave_aleatoria)

    return chave_aleatoria

def criptografar(chave, texto, opcao):
    """
    2- Nós precisamos usar isso para substituir pelo alfabeto randomizado
    """


    """
    Descobrimos a posição de cada caractere no alfabeto,
    preservando a informação se era ou não uma letra maiúscula
    """
    contador = 0
    posicoes_texto = []
    posicoes_maiusculas = []

    for letraTexto in texto:
        if letraTexto == " ":
            posicoes_texto.append(letraTexto)
            contador = 0
        else:
            for letraAlfabeto in ALFABETO:
                contador+=1

                if letraTexto.lower() == letraAlfabeto:
                    if letraTexto.isupper():
                        posicoes_texto.append(contador)
                        posicoes_maiusculas.append(True)
                    else:
                        posicoes_texto.append(contador)
                        posicoes_maiusculas.append(False)
            contador = 0

    """
    Substituir as posições
    """
    texto_criptografado = []
    match opcao:
        case "1":
            for posicao in posicoes_texto:
                if posicao == " ":
                    texto_criptografado.append(" ")
                for i in range(len(chave)):
                    if i == posicao:
                        texto_criptografado.append(chave[i-1].lower())


            texto_criptografado_string = "".join(texto_criptografado)
            return texto_criptografado_string

        case "2":
            for posicao in posicoes_texto:
                if posicao == " ":
                    texto_criptografado.append(" ")
                for i in range(len(chave)):
                    if i == posicao:
                        texto_criptografado.append(chave[i-1].lower())


            texto_criptografado_string = "".join(texto_criptografado)
            return texto_criptografado_string


def descriptografar(chave, texto):
    pass


def main():
    while True:
        print("\n==== Cifra de Substituição Monoalfabética ====")
        print("1 - Criptografar com chave aleatória")
        print("2 - Criptografar com sua chave")

        print("3 - Descriptografar")

        print("4 - Fechar programa")
        opcao = input("Digite o número:")

        match opcao:
            case "1":
                texto = input("\nDigite o texto para criptografar:")
                chave_aleatoria = gerar_chave_aleatoria()
                print("\nCopie a chave (para descriptografar):\n"+"".join(chave_aleatoria))
                print("\nTexto criptografado:")
                print(criptografar(chave_aleatoria, texto, opcao))
                
            case "2":
                chave_manual = gerar_chave_manual(input("\nDigite a chave:"))
                print("\nCopie a chave (para descriptografar):\n"+"".join(chave_manual))
                texto = input("\nDigite o texto para criptografar:\n")
                print("\nTexto criptografado:")
                print(criptografar(chave_manual, texto, opcao))
                
            case "3":
                chave = input("\nDigite a chave: ")
                texto = input("Digite o texto criptografado: ")
                print(descriptografar(chave, texto))

            case "4":
                break      

main()
