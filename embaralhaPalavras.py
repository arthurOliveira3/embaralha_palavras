import random

def escolhePalavras(tipo, dificuldade):
    cidades = {'araraquara':'dificil', 'aluminio':'dificil', 'sao paulo':'dificil', 'rio de janeiro':'dificil', 'natal':'facil', 'fortaleza':'media', 'pindamonhagaba':'dificil', 'araquari':'media', 'joinville':'media', 'florianopolis':'dificil'}
    cores = {'azul':'facil', 'amarelo':'media', 'vermelho':'media', 'verde':'facil', 'laranja':'media', 'preto':'facil', 'cinza':'facil', 'ciano':'media', 'magenta':'difitil', 'rosa':'facil', 'vinho':'media', 'bege':'facil', 'marrom':'dificil', 'salmao':'media'}
    times = {'palmeiras':'facil', 'corinthians':'media', 'flamengo':'facil', 'fluminense':'media', 'vasco':'facil', 'botafogo':'media', 'portuguesa':'dificil', 'guarani':'dificil', 'ponte preta':'dificil', 'sao paulo':'dificil', 'santos':'media', 'bragantino':'media', 'fortaleza':'media', 'ceara':'facil', 'atletico goianiense':'dificil', 'goias':'facil', 'bahia':'facil', 'vitoria':'media'}
    paises = {'brasil':'media', 'alemanha':'media', 'chile':'facil', 'noruega':'media', 'suiça':'facil', 'estados unidos':'dificil', 'mexico':'media', 'colombia':'media', 'argentina':'dificil', 'uruguai':'media', 'equador':'media', 'bolivia':'media', 'peru':'facil'}
    objetos = {'caneta':'media', 'tesoura':'media', 'microfone':'dificil', 'cadeira':'media', 'teclado':'media', 'projetor':'media', 'quadro':'media', 'ar condicionado':'dificil', 'armario':'media', 'monitor':'media', 'tomada':'media', 'corrente':'media', 'fonte':'media'}

    if tipo == "cidades":
        random.shuffle(cidades)
        return cidades[0]
    elif tipo == 'cores':
        random.shuffle(cores)
        return cores[0]
    elif tipo == 'times':
        random.shuffle(times)
        return times[0]
    elif tipo == "paises":
        random.shuffle(paises)
        return paises[0]
    elif tipo == 'objetos':
        random.shuffle(objetos)
        return objetos[0]
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
    dificuldade = input('Insira o nível de dificuldade que você quer: Facil, Media ou Dificil\nSem acentos ou espaços:\n')
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