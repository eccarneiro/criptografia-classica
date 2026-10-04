def ordem_colunas (chave):
    com_indice = list(enumerate(chave))
    com_indice.sort(key=lambda par: par[1])
    return [indice for indice, letra in com_indice]

def cifrar(texto, chave):
    num_colunas = len(chave)
    colunas = ["" for _ in range(num_colunas)]

    for i, letra in enumerate(texto):
        coluna = i % num_colunas
        colunas[coluna] += letra

    while len(colunas[-1]) < len(colunas[0]):
        colunas[-1] += "X"

    ordem = ordem_colunas(chave)
    resultado = ""
    for i in ordem:
        resultado +=colunas[i]

    return resultado

def descifrar(texto, chave):
    num_colunas = len(chave)
    num_linhas = len(texto) //num_colunas

    ordem = ordem_colunas(chave)

    colunas = [""] * num_colunas
    pos = 0
    for i in ordem:
        colunas [i] = texto[pos:pos + num_linhas]
        pos += num_linhas

    resultado = ""
    for linha in range(num_linhas):
        for coluna in colunas:
            resultado += coluna[linha]

    return resultado.rstrip("X")

while True:
    opcao = input("Escolha uma opção (1 - Cifrar, 2 - Descifrar) ")
    if opcao == "1":
        texto = input("Digite o texto a ser cifrado: ")
        chave = input("Digite a chave: ")
        resultado = cifrar(texto, chave)
        print("Texto cifrado:", resultado)
    elif opcao == "2":
        texto = input("Digite o texto a ser descifrado: ")
        chave = input("Digite a chave: ")
        resultado = descifrar(texto, chave)
        print("Texto descifrado:", resultado)
    else:
        print("Opção inválida. Tente novamente.")