# -*- coding: UTF-8 -*-
import os, sys
import random

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    # vai adicionar "_", para cada posição da string
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros_contador = 0
    
    while(not enforcou and not acertou):

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros_contador += 1

        # compara se erros_contador é igual a 6, se sim, encerra o jogo
        enforcou = erros_contador == 6

        # o "_" não devieria estar dentro das letras acertadas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    # abrir e ler o aqruivo
    arquivo = open("palavra.txt", "r")
    palavras = []

    # loop para pegar as linhas do arquivo
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    # fechar o arquivo
    arquivo.close()

    # pegar uma palavra do arquivi aleatoriamente 
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute =  input("Qual letra? ")
    # tira os espaços da string no inicio e no final
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        # upper muda as letras para maiuscula
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Você ganhou!!")

def imprime_mensagem_perdedor():
    print("Você perdeu!!")

# chama a função jogar
if(__name__ == "__main__"):
    jogar()