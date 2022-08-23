import random

def embaralhaPalavras(palavra):
    lista = list(palavra)
    random.shuffle(lista)
    palavraEmbaralhada = ''.join(lista)
    return palavraEmbaralhada

def palavras_de_animo():
    palavras = ["tente novamente!", "você consegue!", "na próxima você vai conseguir!", "não desista!", "persista!"]
    random.shuffle(palavras)
    return palavras


palavra = "masqueico"
embaralhada = embaralhaPalavras(palavra)
palavra_animo = palavras_de_animo()
index = 0

for item in range(5):
    print(f"\n\nVocê tem {5 - item} tentativas!")
    print(f"\nA palavra é: {embaralhada}")

    tentativa = input("\nDigite a palavra que você acha certa: ")
    tentativa = tentativa.strip()
    tentativa = tentativa.lower()
    
    if tentativa == palavra:
        print("PARABÉNS VOCÊ GANHOU!!!")
        print(f"Você utilizou {item + 1} tentativas")
        break
    elif len(tentativa) > len(embaralhada):
        print("A sua tentativa tem mais letras do que o permitido")
    elif  len(tentativa) < len(embaralhada):
        print("A sua tentativa tem menos letras do que o permitido")
    elif item != 4:
        print(f"\nVocê errou, mas {palavra_animo[index]}")
    else:
        print(f"\nVocê perdeu \nA palavra certa é: {palavra}")
    index +=1