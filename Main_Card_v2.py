#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     22/03/2023
# Copyright:   (c) Administrateur 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import *

couleur = ("trèfle", "pique", "coeur", "carreau")
valeur = ("As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi")


class Paquet_Carte() :
    def __init__(self) :
        self.couleur = ("trèfle", "pique", "coeur", "carreau")
        self.valeur = ("As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi")
        self.picked = []

    def Carte(self) :
        self.pack = []
        for i in range (len(couleur)) :
            for j in range (len(valeur)):
                self.carte = self.valeur[j] + " de " + self.couleur[i]
                self.pack.append(self.carte)

    def affiche_1carte(self) :
        ''' permet pour l'affichage du front'''
        return self.carte

    def affichage_cartes(self) :
        ''' permet pour l'affichage du front'''
        return self.pack

    def Melange(self) :
        shuffle(self.pack)

    def Pick(self) :

        self.pick = choice(self.pack)
        self.picked.append(self.pick)
        self.pack.remove(self.pick)

        print(self.pick)

    def Reset(self) :
        self.pack = []
        for i in range (len(couleur)) :
            for j in range (len(valeur)):
                self.carte = self.valeur[j] + " de " + self.couleur[i]
                self.pack.append(self.carte)
        self.picked = []

    def Melange_Affiche(self) :
        shuffle(self.pack)
        return self.pack

deck = Paquet_Carte()
deck.Carte()