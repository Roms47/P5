import mysql.connector  # mysql-connector-python
from config.mdp_mysql import *
from termcolor import colored
# Singleton à faire
class Database:
    """ Interaction class with the DataBase """

    def __init__(self):
        """ Constructor of class DataBase """
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=MDP,
            database="mydatabase"  # The Base must exist.
            # auth_plugin='mysql_native_password'
        )
        self.mycursor = self.mydb.cursor()

    ##############################################################
    #                        Insertion of Data                   #
    ##############################################################
    def set_categorie(self, categorie):
        """ Saves categories in DataBase """
        sql = """INSERT INTO Categories(nom) VALUES (%s)"""
        val = (categorie.name,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def set_product(self, produit):
        """ Add product to the DataBase """
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
        print(colored(self.mycursor.rowcount, 'red'), colored("record inserted.",'green'))

    def set_favoris(self, produit):
        """ Add a product to favourites """
        sql = """INSERT INTO Favoris(produit)\
                VALUES (%s)"""
        val = (produit.code_barre,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    ##############################################################
    #                         Data selection                     #
    ##############################################################

    def get_all_categorie(self):
        """ Method that returns the set of categories in DataBase """
        self.mycursor.execute("SELECT * FROM Categories")
        return self.mycursor.fetchall()

    def print_all_categories(self):
        """ Displays all categories """
        liste = self.get_all_categorie()
        for i in range(len(liste)):
            print(liste[i][0], ".\t", liste[i][1])

    def get_product_from_categorie(self, id):
        """ Method that returns the set of products of the category id """
        sql = """SELECT * FROM Produits WHERE categorie = (%s)"""
        val = (id,)
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()

    def print_product_from_categorie(self, id):
        """ Displays products in a specific category """
        liste = self.get_product_from_categorie(id)
        for i in range(len(liste)):
            print(i + 1, ".\t", liste[i][2], "(", liste[i][3], ")")
        return liste

    def get_all_favoris(self):
        """ Method that returns the set of favourites in DataBase """
        sql = """SELECT *
                FROM Produits 
                INNER JOIN Favoris ON Produits.id_produits = Favoris.produit"""
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    def print_all_favoris(self):
        """ Displays all favourites """
        liste = self.get_all_favoris()
        for i in range(len(liste)):
            print(i + 1, ".\t", liste[i][2], "(", liste[i][3], ")")

    def search_substitut(self, cat, grade):
        """ Retourne LES produits de catégorie cat
        avec une notre mieux que grade classé par ordre de grade """
        sql = """SELECT * 
                FROM Produits 
                WHERE categorie = (%s) AND grade <= (%s)
                ORDER BY grade"""
        val = (cat, grade)
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()