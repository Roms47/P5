class Display:
    """ Class that manages displays """
    def __init__(self):
        pass

    def menu1(self):
        print('------------------------------------------------------')
        print(
            "1. Creation and initialization of the DataBase before using the application ")
        print("2. Directly using the application ")
        print("0. To exit the application directly ")
        print("------------------------------------------------------")
        choix = int(input("\n ---> "))
        return choix

    def menu2(self):
        print("------------------------------------------------------")
        print("1. Display categories and start a search ")
        print("2. Show saved favourites")
        print("0. Exit the program")
        print("------------------------------------------------------")
        choix = int(input())
        return choix

    def afficher_produit(self, produit):
        """ Displays the information of a product """

        print("-------------------------------------------")
        print("Nom : \t"), produit.name, end="         "  # product_name_fr #generic_name #categories
        print("Grade : \t"), produit.grade.upper()
        print("url : \t"), produit.url()
        print("Code barre : \t"), produit.code_barre()
        print("Catégorie : \t"), produit.categorie()
        print("En vente ici : "), produit.stores, end="          "
        print("Image : "), produit.image_url()
        print("-------------------------------------------")