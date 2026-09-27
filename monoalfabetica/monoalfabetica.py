ALFABETO = "abcdefghijklmnopqrstuvwxyz"

def gerar_alfabeto_cifrado(chave):
    """
    1- Receber a chave
    2- Remover letras duplicadas
    3- Posicionar no início do alfabeto cifrado
    4- Preencher com as letras que ainda não foram usadas (em ordem alfabética)
    """
    pass


def criptografar(chave, texto):
    return "Criptografado"


def descriptografar(chave, texto):
    return "Descriptografado"


def main():
    while True:
        print("\n==== Cifra de Substituição Monoalfabética ====")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Fechar programa")
        opcao = input("Digite o número: ")

        match opcao:
            case "1":
                chave = input("\nDigite a chave: ")
                texto = input("Digite o texto para criptografar: ")
                print(criptografar(chave, texto))
                
            case "2":
                chave = input("\nDigite a chave: ")
                texto = input("Digite o texto criptografado: ")
                print(descriptografar(chave, texto))
                
            case "3":
                break

main()
