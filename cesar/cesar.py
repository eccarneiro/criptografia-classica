import sys

alfabeto = "abcdefghijklmnopqrstuvwxyz"

texto = sys.argv[1].lower()
key = int(sys.argv[2])


def criptografar(texto, key):
    texto_criptografado = ""
    for i in range(len(texto)):
        char = texto[i]
        encontrou = False
        for j in range(len(alfabeto)):
            if char == alfabeto[j]:
                posicao = j
                novaPosicao = (posicao + key) % 26
                texto_criptografado += alfabeto[novaPosicao]
                encontrou = True
                break
        if encontrou == False:
            texto_criptografado += char
    return texto_criptografado


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
