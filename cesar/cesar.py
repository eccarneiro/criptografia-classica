import sys # import nativo do python (system) que permite interagir com o interpretador e pegar os argumentos do terminal

alfabeto = "abcdefghijklmnopqrstuvwxyz"

texto = sys.argv[1].lower() # -> pega o primeiro argumento do terminal e transforma em minúsculo
key = int(sys.argv[2]) # -> pega o segundo argumento, que é a chave da criptografia, e transforma em inteiro


def criptografar(texto, key):
    texto_criptografado = ""  #cria uma string vaiza pra ir populando com os caracteres criptografados letra por letra.
    for i in range(len(texto)): # for percorre cada letra do texto
        char = texto[i] #extrai a letra atual do texto com base no indice i
        encontrou = False #variavel booleana que indica se a letra foi encontrada no alfabeto, uma flag....
        for j in range(len(alfabeto)): #segundo loop para percorrer o alfabeto e encontrar a letra correspondente
            if char == alfabeto[j]: 
                posicao = j # compara as letras do texto com as letras do alfabeto, se encontrar, pega a posição da letra no alfabeto
                novaPosicao = (posicao + key) % 26 # calculo a nova posiçao da letra no alfabeto, somando a posição atual com a chave. Modulo de 26b pra garantir que nao passe de 25 e recomeca o ciclo.
                texto_criptografado += alfabeto[novaPosicao] # pega a letra correspondente a nova posição e adiciona na string de texto criptografado
                encontrou = True # vira a flag
                break
        if encontrou == False:
            texto_criptografado += char
    return texto_criptografado

#descriptografia é basicamente o mesmo algoritmo mas subtraindo.

def descriptografar(texto_criptografado, key):
    texto_descriptografado = ""
    for i in range(len(texto_criptografado)):
        char = texto_criptografado[i]
        encontrou = False
        for j in range(len(alfabeto)):
            if char == alfabeto[j]:
                posicao = j
                novaPosicao = (posicao - key) % 26
                texto_descriptografado += alfabeto[novaPosicao]
                encontrou = True
                break
        if encontrou == False:
            texto_descriptografado += char
    return texto_descriptografado


texto_criptografado = criptografar(texto, key)
print("Texto criptografado:", texto_criptografado)

texto_descriptografado = descriptografar(texto_criptografado, key)
print("Texto descriptografado:", texto_descriptografado)
