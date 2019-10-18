from argparse import ArgumentParser

parser = ArgumentParser(description="Script qui dit bonjour")
parser.add_argument("name", help="Nom de la première personne")
parser.add_argument("-n", "--name2",
                    help="Nom de la deuxième personne")

args = parser.parse_args()

print("Bonjour")
print(args.name)
print(args.name2 in ["Toto", "Hello", None])

liste = [3, 4, 5, 7, 1, 3, 7]
mon_set = set(liste)
print(8 in mon_set)
