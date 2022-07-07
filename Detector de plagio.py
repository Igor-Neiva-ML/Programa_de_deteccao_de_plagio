import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)

    frases = []
    for sentenca in sentencas:
        frases += separa_frases(sentenca)

    palavras = []
    for frase in frases:
        palavras += separa_palavras(frase)

    soma_tam_palavras = 0
    for palavra in palavras:
        soma_tam_palavras += len(palavra)
    wal_b = soma_tam_palavras / len(palavras)

    palavras_unicas = []
    i = 0
    for palavra in palavras:
        while palavra != palavras_unicas[i]:
            i += 1
            if i == len(palavras_unicas):
                palavras_unicas.append(palavra)
                break
    ttr_b = len(palavras_unicas) / len(palavras)

    palavra_uma_vez = []
    cont = 0
    for i in range(len(palavras)):
        j = 1
        while j < (len(palavras) - i):
            if palavra[i] == palavra[i+j]:
                cont += 1
            j = j + 1
        if cont == 0:
            palavra_uma_vez.append(palavra[i])
    hlr_b = len(palavra_uma_vez) / len(palavras)

    soma_caractere_sentencas = 0
    for sentenca in sentencas:
            soma_caractere_sentencas += len(sentenca)
    sal_b = soma_caractere_sentencas / len(sentencas)

    sac_b = len(frases) / len(sentencas)

    soma_caractere_frases = 0
    for frase in frases:
        soma_caractere_frases += len(frase)
    pal_b = soma_caractere_frases / len(frases)

    return [wal_b, ttr_b, hlr_b, sal_b, sac_b, pal_b]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass