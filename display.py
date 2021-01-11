from termcolor import colored

class Display:
    """Class that manages displays"""
    def __init__(self):
        pass

    def menu1(self):
        print(colored("------------------------------------------------------",
                      'blue'))
        print(colored(
            "1. Création et initialisation de la BDD avant d'utiliser l'appli",
            'blue'))
        print(colored("2. Utiliser directement l'application ", 'blue'))
        print(colored("0. Pour quitter directement l'application ", 'blue'))
        print(colored("------------------------------------------------------",
                      'blue'))
        choix = int(input(colored("\n ---> ", 'green')))
        return choix

    def menu2(self):
        print(colored("------------------------------------------------------",
                      "blue"))
        print(colored("1. Afficher les catégories et commencer une recherche ",
                      "blue"))
        print(colored("2. Afficher les favoris sauvgardés", "blue"))
        print(colored("0. Quitter le programme", "blue"))
        print(colored("------------------------------------------------------",
                      "blue"))
        choix = int(input())
        return choix

    def afficher_produit(self, produit):
        """ Displays product information"""

        print(colored("-------------------------------------------", 'magenta'))
        print(
            colored("Nom : \t", "blue"), produit.name, end="         "
        )  # product_name_fr #generic_name #categories
        print(colored("Grade : \t", "blue"), produit.grade.upper())
        print(colored("url : \t", "blue"), produit.url)
        print(colored("Code barre : \t", "blue"), produit.code_barre)
        print(colored("Catégorie : \t", "blue"), produit.categorie)
        print(colored("En vente ici : ", "blue"), produit.stores, end="          ")
        print(colored("Image : ", "blue"), produit.image_url)
        print(colored("-------------------------------------------", 'magenta'))