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
    chave_limpa = "".join(dict.fromkeys(chave))

    chave_completa = []
    for letra in chave_limpa:
        chave_completa.append(letra)

    contador = 0
    posicoes_chave = []

    for letraChave in chave_completa:
        if letraChave == " ":
            posicoes_chave.append(letraChave)
            contador = 0
        else:
            for letraAlfabeto in ALFABETO:
                contador+=1

                if letraChave.lower() == letraAlfabeto:
                    posicoes_chave.append(contador)
            contador = 0

    alfabeto_copia = []
    for letra in ALFABETO:
        alfabeto_copia.append(letra)

    for i in posicoes_chave:
        alfabeto_copia.pop(i-1)

    for letra in alfabeto_copia:
        chave_completa.append(letra)

    return chave_completa


def gerar_chave_aletaoria():
    return random.shuffle(ALFABETO)

def criptografar(chave, texto):
    """
    2- Nós precisamos usar isso para substituir pelo alfabeto randomizado
    """


    """
    Descobrimos a posição de cada caractere no alfabeto,
    preservando a informação se era ou não uma letra maiúscula
    """
    contador = 0
    posicoes_texto = []

    for letraTexto in texto:
        if letraTexto == " ":
            posicoes_texto.append(letraTexto)
            contador = 0
        else:
            for letraAlfabeto in ALFABETO:
                contador+=1

                if letraTexto.lower() == letraAlfabeto:
                    if letraTexto.isupper():
                        posicoes_texto.append(str(contador) + " True")
                    else:
                        posicoes_texto.append(str(contador))
            contador = 0

    """
    Trocamos pelo caractere do alfabeto randomizado
    """
    


def descriptografar(chave, texto):
    pass


def main():
    while True:
        print("\n==== Cifra de Substituição Monoalfabética ====")
        print("1 - Criptografar com chave aleatória")
        print("2 - Criptografar com sua chave")

        print("3 - Descriptografar")

        print("4 - Fechar programa")
        opcao = input("Digite o número: ")

        match opcao:
            case "1":
                texto = input("\nDigite o texto para criptografar: ")
                chave_aleatoria = gerar_chave_aletaoria()
                print("Copie a chave (para descriptografar): ", chave_aleatoria)
                print("Texto criptografado:")
                print(criptografar(chave_aleatoria, texto))
                
            case "2":
                chave = input("\nDigite a chave: ")
                texto = input("Digite o texto: ")
                print(criptografar(chave, texto))
                
            case "3":
                chave = input("\nDigite a chave: ")
                texto = input("Digite o texto criptografado: ")
                print(descriptografar(chave, texto))

            case "4":
                break      


