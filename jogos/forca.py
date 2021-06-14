# -*- coding: utf-8 -*-
import os, sys

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = raw_input("Qual letra? ")
        # tira os espaços da string no inicio e no final
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            # upper muda as letras para maiuscula
            if(chute.upper() == letra.upper()):
                print("Encotrei a letra na posição {} na posição {}.".format(letra, index))
            index += 1
        
        print("jogando ...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
