import random

def escolhePalavras(tipo, dificuldade):
    cidades_facil = ['natal', 'belem', 'para']
    cidades_media = ['sao paulo', 'fortaleza', 'araquari', 'joinville']
    cidades_dificil = ['araraquara', 'rio de janeiro', 'pindamonhagaba', 'florianopolis']
    cores_facil = ['azul', 'verde', 'preto', 'cinza', 'rosa', ]
    cores_media = ['amarelo', 'vermelho', 'laranja', 'ciano', 'vinho', 'bege', 'marrom', 'salmao']
    cores_dificil = ['magenta', 'purpura']
    times_facil = ['vasco', 'santos', 'ceara', 'goias', 'bahia',' vitoria', 'sport']
    times_media = ['palmeiras', 'flamengo', 'fluminense', 'botafogo', 'guarani', 'fortaleza']
    times_dificil = ['corinthians', 'portuguesa', 'ponte preta', 'sao paulo', 'bragantino', 'atletico goianiense', 'athletico paranaense']
    paises_facil = ['chile', 'brasil', 'suiça', 'peru', 'russia']
    paises_media = ['alemanha', 'noruega', 'mexico', 'colombia', 'argentina', 'uruguai', 'equador', 'bolivia']
    paises_dificil = ['estados unidos', 'reino unido', 'azerbaijao']
    objetos_facil = ['caneta', 'tesoura', 'cadeira', 'quadro', 'fonte']
    objetos_media = ['microfone', 'teclado', 'projetor', 'armario', 'monitor', 'tomada', 'corrente']
    objetos_dificil = ['ar condicionado', 'escrivaninha', 'paralelepipedo', 'andaime']

    if tipo == "cidades":
        if dificuldade == 'facil':
            random.shuffle(cidades_facil)
            return cidades_facil[0]
        elif dificuldade == 'media':
            random.shuffle(cidades_media)
            return cidades_media[0]
        else:
            random.shuffle(cidades_dificil)
            return cidades_dificil[0]
    elif tipo == "cores":
        if dificuldade == 'facil':
            random.shuffle(cores_facil)
            return cores_facil[0]
        elif dificuldade == 'media':
            random.shuffle(cores_media)
            return cores_media[0]
        else:
            random.shuffle(cores_dificil)
            return cores_dificil[0]
    elif tipo == "times":
        if dificuldade == 'facil':
            random.shuffle(times_facil)
            return times_facil[0]
        elif dificuldade == 'media':
            random.shuffle(times_media)
            return times_media[0]
        else:
            random.shuffle(times_dificil)
            return timees_dificil[0]
    elif tipo == "paises":
        if dificuldade == 'facil':
            random.shuffle(paises_facil)
            return paises_facil[0]
        elif dificuldade == 'media':
            random.shuffle(paises_media)
            return paises_media[0]
        else:
            random.shuffle(paises_dificil)
            return paises_dificil[0]
    elif tipo == "objetos":
        if dificuldade == 'facil':
            random.shuffle(objetos_facil)
            return objetos_facil[0]
        elif dificuldade == 'media':
            random.shuffle(objetos_media)
            return objetos_media[0]
        else:
            random.shuffle(objetos_dificil)
            return objetos_dificil[0]
    else:
        return "TIPO INVÁLIDO!!!!!!!!!!!"


def embaralhaPalavras(palavra):
    lista = list(palavra)
    random.shuffle(lista)
    palavraEmbaralhada = ''.join(lista)
    return palavraEmbaralhada


def palavras_de_animo():
    palavras = ["tente novamente!", "você consegue!", "na próxima você vai conseguir!", "não desista!", "persista!"]
    random.shuffle(palavras)
    return palavras


def jogo():
    tipoPalavra = input('Insira o tipo de palavra que você quer: Cidades, Cores, Times, Países ou Objetos\nSem acentos ou espaços:\n')
    dificuldade = input('Insira o nível de dificuldade que você quer: Fácil, Média, Difícil\nSem acentos ou espaços:\n')
    palavra = escolhePalavras(tipoPalavra, dificuldade)
    embaralhada = embaralhaPalavras(palavra)
    palavra_animo = palavras_de_animo()

    for item in range(5):
        if palavra == "TIPO INVÁLIDO!!!!!!!!!!!":
            print("TIPO INVÁLIDO!!!!!!!!!!!")
            break
        else:
            print(f"\n\nVocê tem {5 - item} tentativas!")
            print(f'\nO seu tipo é {tipoPalavra}')
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
            elif len(tentativa) < len(embaralhada):
                print("A sua tentativa tem menos letras do que o permitido")
            elif item != 4:
                print(f"\nVocê errou, mas {palavra_animo[item]}")
            else:
                print(f"\nVocê perdeu \nA palavra certa é: {palavra}")

jogo()