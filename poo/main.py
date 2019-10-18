# -*- coding: utf-8 -*-
from JeuVoiture.TerrainUI import TerrainUI
#from time import sleep
#import os


"""
    Définir dans voiture une classe Voiture
    construite à partir de poistion
    qui contient une position et une direction
    en numpy array: self.direction = np.array([0,1])
    avancer() : position += direction
    tourner()
"""

terrain = TerrainUI()

terrain.start()

# for i in range(50):
#    os.system("cls")
#    terrain.fait_un_tour()
#    terrain.display()
#    sleep(0.5)


def add(a, b):
    """
      Fonction qui fait une addition entre deux paramètres
      :param a: premier paramètre
      :param b: deuxieme paramètre
      :type a: int
      :type b: int
      >> add(1,2)
      3
    """
    return a + b


add(2, 5)
