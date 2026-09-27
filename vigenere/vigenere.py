# vigenere.py

def preparar_chave(mensagem, chave):
    """
    Repete (ou corta) a chave para ter o mesmo comprimento da mensagem,
    ignorando caracteres não-alfabéticos na contagem.
    
    Ex: mensagem="OLA MUNDO", chave="LIM" -> "LIM LIML" 
    (espaço é mantido no lugar, mas não consome letra da chave)
    """
    chave = chave.upper()
    chave_expandida = []
    indice_chave = 0  # controla qual letra da chave usar

    for caractere in mensagem:
        if caractere.isalpha():
            # Pega a letra da chave na posição atual, e avança o índice
            chave_expandida.append(chave[indice_chave % len(chave)])
            indice_chave += 1
        else:
            # Espaços, números, pontuação: mantém o caractere sem consumir a chave
            chave_expandida.append(caractere)

    return "".join(chave_expandida)


def cifrar(mensagem, chave):
    """
    Cifra a mensagem usando a Cifra de Vigenère.
    
    Para cada letra:
      - Converte para número (A=0, B=1, ..., Z=25)
      - Soma com o valor da letra correspondente da chave
      - Aplica módulo 26 para "fechar" o alfabeto (ex: Z+2 = B)
      - Converte de volta para letra
    """
    mensagem = mensagem.upper()
    chave_expandida = preparar_chave(mensagem, chave)
    texto_cifrado = []

    for i, caractere in enumerate(mensagem):
        if caractere.isalpha():
            valor_mensagem = ord(caractere) - ord('A')
            valor_chave = ord(chave_expandida[i]) - ord('A')
            valor_cifrado = (valor_mensagem + valor_chave) % 26
            texto_cifrado.append(chr(valor_cifrado + ord('A')))
        else:
            texto_cifrado.append(caractere)

    return "".join(texto_cifrado)


def decifrar(texto_cifrado, chave):
    """
    Decifra um texto cifrado com Vigenère, dado a chave original.
    
    Fórmula: (C - K + 26) mod 26
    O +26 garante que o resultado nunca seja negativo antes do mod.
    """
    texto_cifrado = texto_cifrado.upper()
    chave_expandida = preparar_chave(texto_cifrado, chave)
    texto_claro = []

    for i, caractere in enumerate(texto_cifrado):
        if caractere.isalpha():
            valor_cifrado = ord(caractere) - ord('A')
            valor_chave = ord(chave_expandida[i]) - ord('A')
            valor_decifrado = (valor_cifrado - valor_chave + 26) % 26
            texto_claro.append(chr(valor_decifrado + ord('A')))
        else:
            texto_claro.append(caractere)

    return "".join(texto_claro)


# ------------------------------------------------------------------
# Programa principal — interface simples no terminal
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 45)
    print("       CIFRA DE VIGENÈRE")
    print("=" * 45)

    print("\nOpções:")
    print("  1 - Cifrar mensagem")
    print("  2 - Decifrar mensagem")

    opcao = input("\nEscolha uma opção (1 ou 2): ").strip()

    if opcao == "1":
        mensagem = input("Digite a mensagem:  ").strip()
        chave    = input("Digite a chave:     ").strip()

        if not chave.isalpha():
            print("\n[ERRO] A chave deve conter apenas letras.")
        else:
            resultado = cifrar(mensagem, chave)
            print(f"\nTexto cifrado:  {resultado}")

    elif opcao == "2":
        texto_cifrado = input("Digite o texto cifrado: ").strip()
        chave         = input("Digite a chave:         ").strip()

        if not chave.isalpha():
            print("\n[ERRO] A chave deve conter apenas letras.")
        else:
            resultado = decifrar(texto_cifrado, chave)
            print(f"\nTexto decifrado: {resultado}")

    else:
        print("\n[ERRO] Opção inválida.")
