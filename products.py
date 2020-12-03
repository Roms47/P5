from math import ceil
import requests


class Product:
    """ Class representing the object product """

    compteur_instance = 0

    def __init__(self, name, url, note, id, categorie, stores, image_url):
        """ Product class's constructor """
        self.name = name  # product_name_fr #generic_name #categories
        self.grade = note
        self.url = url
        self.code_barre = id
        self.categorie = categorie
        self.image_url = image_url
        self.stores = stores
        self.clean_product()

    def clean_product(self):
        """ Method to classify a product """
        if self.grade in ["a", "b", "c", "d", "e"]:
            self.grade = self.grade.upper()
        elif self.grade not in ["A", "B", "C", "D", "E"]:
            print(self.grade)