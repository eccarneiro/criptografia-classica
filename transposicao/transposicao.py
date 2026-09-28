def cifrar(texto,chave):

        n = chave
        lista = ["" for _ in range(n)]

        trilho_atual = 0
        direcao = 1
        for letra in texto:
            lista[trilho_atual] += letra
            if trilho_atual == 0:
                    direcao = 1
            elif trilho_atual == chave - 1:
                    direcao = -1
            trilho_atual += direcao

        return "".join(lista)

def decifrar(texto,chave):
        
        trilho_atual = 0
        direcao = 1
        padrao = []
        
        for letra in texto:
            padrao.append(trilho_atual)
            if trilho_atual == 0:
                    direcao = 1
            elif trilho_atual == chave - 1:
                    direcao = -1
            trilho_atual += direcao
          
        contagens = []
        
        for t in range(chave):
            contagens.append(padrao.count(t))
        pedacos = []
        inicio = 0
        for c in contagens:
            pedacos.append(texto[inicio:inicio + c])
            inicio = inicio + c

        ponteiros = [0 for _ in range(chave)]
        resultado = ""
        
        for p in padrao:
            resultado += pedacos[p][ponteiros[p]]
            ponteiros[p] += 1                    
            
        return resultado

while True:
    opcao = input("Algoritmo Cifra de Transposição RAIL FENCE. Digite 1 para cifrar ou 2 para decifrar: ")
    mensagem = input("Digite a mensagem: ")
    chave = int(input("Digite a chave (número de trilhos): "))

    if opcao == "1":
        print(cifrar(mensagem, chave))
    elif opcao == "2":
        print(decifrar(mensagem, chave))
    else:
        print("Opção inválida")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        print("Fim do programa da Cifra de Transposição 'RAIL FENCE'!")
        break
