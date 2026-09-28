ALFABETO = "abcdefghijklmnopqrstuvwxyz"

texto = "Cacique da tRiBo"

qtd_caracteres = len(texto)
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

print(posicoes_texto)