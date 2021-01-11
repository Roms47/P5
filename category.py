import requests
from math import ceil

class Category:
    """ Class representing the object category """

    def __init__(self, name, nb, adresse, id):
        """ Category class's constructor """
        self.name = name  # Category name
        self.nb_product = nb  # Number of products in the category
        self.adresse = adresse  # Category's url
        self.nombre_pages = ceil(self.nb_product / 20)  # Number of pages
        self.id = id  # Category's id

    def __str__(self):
        pass

    def afficher_categorie(self):
        """ Displays category information """
        print(self.id, " - ", end=" ")
        print(self.name, end=" ")
        print(self.nb_product, end=" ")
        print(self.nombre_pages)
        print(self.adresse)

    def get_api_categories(self):
        """ Get the categories from the official API """

        r = requests.get("https://fr.openfoodfacts.org/categories.json")
        categories = r.json()
        nombre_categories = categories.get("count")
        print(" {} category on the site.\n").format(nombre_categories)
        # Environs 12 800 catÃ©gories. Je vais commencer par en prendre une dizaine.
        return categories