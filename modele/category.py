from math import ceil
import requests

class Category:
    """ class representing the category object """

    def __init__(self, name, nb, en, adresse, id):
        """ Category class constructor """
        self.name = name  # Nom de la catégorie
        self.nb_product = nb  # Nombre de produit dans la catégorie
        self.name_en = en  # Le nom en anglais
        self.adresse = adresse  # L'url de la catégorie
        self.nombre_pages = ceil(self.nb_product / 20)  # Nombre de page
        self.id = id  # id de la catégorie

    def __str__(self):
        pass

    def afficher_categorie(self):
        """ Displays the information of a category in a somewhat presentable way """
        print("\n##############################")
        print(self.id, " - ", end=" ")
        print(self.name, end="       ")
        print("(", self.name_en, ")")
        print("\t Nombre de produits :", self.nb_product, end=" ")
        print("\t Nombre de pages :", self.nombre_pages)
        print("\t", self.adresse)
        print("\n##############################")

    def get_api_products(self, page):
        """ Get a product page from the category """
        adresse = self.adresse + "/" + str(page) + ".json"
        p = requests.get(adresse)
        produits = p.json()
        return produits

    @staticmethod
    def get_api_categories():
        """Réccupère les catégories sur via l'API OFF"""
        print(" . . . Veuillez patienter... Requete en cours. . . ")

        r = requests.get("https://fr.openfoodfacts.org/categories.json")
        categories = r.json()
        nombre_categories = categories.get("count")
        print(" {} catégories présentes sur le site.\n".format(nombre_categories))
        # Environs 12 800 catÃ©gories. Je vais commencer par en prendre une dizaine.
        return categories