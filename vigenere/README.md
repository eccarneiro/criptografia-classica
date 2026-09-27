# Cifra de Vigenère

## Como funciona

A Cifra de Vigenère é uma extensão da Cifra de César.
Em vez de um deslocamento fixo, ela usa uma **palavra-chave** que se repete
ao longo da mensagem — cada letra é deslocada pelo valor da letra
correspondente da chave.

**Fórmula:**
- Cifrar:   `C = (M + K) mod 26`
- Decifrar: `M = (C - K + 26) mod 26`

## Como executar

```bash
python vigenere.py
```

## Exemplo

```
Mensagem:  ATACAR
Chave:     LIMALI
Cifrado:   LBMCLZ
```

## Autor

Ygor — Segurança da Informação
