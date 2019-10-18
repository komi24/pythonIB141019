
from doctest import testmod


def add(a, b):
    """
      Fonction qui fait une addition entre deux paramètres
      :param a: premier paramètre
      :param b: deuxieme paramètre
      :type a: int
      :type b: int
      :Example:
      >>> add(1,4)
      3
    """
    return a + b


testmod()
