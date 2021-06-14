# -*- coding: utf-8 -*-
import os, sys

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = raw_input("Qual letra? ")
        # tira os espaços da string no inicio e no final
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            # upper muda as letras para maiuscula
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index += 1
        
        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
