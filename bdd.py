import mysql.connector
from mdp_mysql import *

class Database:
    """ Classe d'interaction avec la BDD"""

    def __init__(self):
        """Constructeur de la class Database"""
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=MDP,
            database="mydatabase" 
        )
        self.mycursor = self.mydb.cursor()

    ##############################################################
    #                       Insertion  des données               #
    ##############################################################
    def set_categorie(self, categorie):
        """enregistre les catégories en BDD"""
        sql = """INSERT INTO Categories(nom) VALUES (%s)"""
        val = (categorie.name,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def set_product(self, produit):
        """Méthode qui ajoute un produit dans la base"""
        sql = """INSERT INTO Produits(id_produits, url, nom, grade, categorie, magasin, image) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        val = (
            produit.code_barre,
            produit.url,
            produit.name,
            produit.grade,
            produit.categorie,
            produit.stores,
            produit.image_url,
        )
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount)

    def set_favoris(self, produit):
        """Méthode qui ajoute un produit dans la base"""
        sql = """INSERT INTO Favoris(produit)\
                VALUES (%s)"""
        val = (produit.code_barre,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    ##############################################################
    #                       Selection  des données               #
    ##############################################################

    def get_all_categorie(self):
        """ Méthode qui retourne l'ensemble des catégories en BDD"""
        self.mycursor.execute("SELECT * FROM Categories")
        return self.mycursor.fetchall()

    def print_all_categories(self):
        """affiche toutes les catégories"""
        liste = self.get_all_categorie()
        for i in range(len(liste)):
            print(liste[i][0], ".\t", liste[i][1])

    def get_product_from_categorie(self, id):
        """ Méthode qui retourne l'ensemble des produits de la catégorie id"""
        sql = """SELECT * FROM Produits WHERE categorie = (%s)"""
        val = (id,)
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()

    def print_product_from_categorie(self, id):
        """Affiche les produits d'une catégorie donnée"""
        liste = self.get_product_from_categorie(id)
        for i in range(len(liste)):
            print(i + 1, ".\t", liste[i][2], "(", liste[i][3], ")")
        return liste

    def get_all_favoris(self):
        """ Méthode qui retourne l'ensemble des favoris en BDD"""
        sql = """SELECT *
                FROM Produits 
                INNER JOIN Favoris ON Produits.id_produits = Favoris.produit"""
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    def print_all_favoris(self):
        """Permet d'afficher tous les favoris"""
        liste = self.get_all_favoris()
        for i in range(len(liste)):
            print(i + 1, ".\t", liste[i][2], "(", liste[i][3], ")")

    def search_substitut(self, cat, grade):
        """Retourne LES produits de catégorie cat
         avec une notre mieux que grade classé par ordre de grade"""
        sql = """SELECT * 
                FROM Produits 
                WHERE categorie = (%s) AND grade <= (%s)
                ORDER BY grade"""
        val = (cat, grade)
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()