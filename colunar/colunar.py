def ordena_letra(par):
    return par[1]

def ordem_colunas (chave):
    pares = list(enumerate(chave))
    pares.sort(key=ordena_letra)
    return [indice for indice, letra in pares]

def cifrar(texto, chave):
    num_colunas = len(chave)
    colunas = ["" for _ in range(num_colunas)]

    for i, letra in enumerate(texto):
        coluna = i % num_colunas
        colunas[coluna] += letra

    for i in range(num_colunas):
        while len(colunas[i]) < len(colunas[0]):
            colunas[i] += "X"

    ordem = ordem_colunas(chave)
    resultado = ""
    for i in ordem:
        resultado +=colunas[i]

    return resultado

def decifrar(texto, chave):
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
    opcao = input("Escolha uma opção (1 - Cifrar, 2 - Decifrar) ")
    if opcao == "1":
        texto = input("Digite o texto a ser cifrado: ")
        chave = input("Digite a chave: ")
        resultado = cifrar(texto, chave)
        print("Texto cifrado:", resultado)
    elif opcao == "2":
        texto = input("Digite o texto a ser decifrado: ")
        chave = input("Digite a chave: ")
        resultado = decifrar(texto, chave)
        print("Texto decifrado:", resultado)
    else:
        print("Opção inválida. Tente novamente.")