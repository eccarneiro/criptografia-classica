def vigenere(texto, chave, modo=1):
    texto = texto.upper()
    chave = chave.upper()
    resultado = []
    ki = 0

    for c in texto:
        if c.isalpha():
            shift = (ord(c) - ord('A') + modo * (ord(chave[ki % len(chave)]) - ord('A')) + 26) % 26
            resultado.append(chr(shift + ord('A')))
            ki += 1
        else:
            resultado.append(c)

    return ''.join(resultado)


if __name__ == '__main__':
    print("CIFRA DE VIGENÈRE\n1 - Cifrar\n2 - Decifrar")
    op = input("\nOpção: ").strip()

    if op not in ('1', '2'):
        print("Opção inválida.")
    else:
        texto = input("Mensagem: ").strip()
        chave = input("Chave:    ").strip()

        if not chave.isalpha():
            print("A chave deve conter apenas letras.")
        else:
            saida = vigenere(texto, chave, modo=1 if op == '1' else -1)
            print(f"\n{'Cifrado' if op == '1' else 'Decifrado'}: {saida}")