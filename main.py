from data.bdd import *
from modele.products import Product
from modele.category import Category
from vue.display import Display
from data import reset_bdd
from random import *
from config import *

def main():

    url_de_base = "https://fr.openfoodfacts.org/categorie/"  # add produit/i.json
    nb_produit = LIMITE_PAGES
    total_produit = 0
    total_charge = 0
    total_analyse = 0

    affichage = Display()
    choix = affichage.menu1()

    menu = True
    if choix == 1:
        resetBDD.reset()
        # The API should only be called on first use
        instance = Database()
        categories = Category.get_api_categories()
        nombre_a_afficher = int(input("How many categories do you want to charge ? "))
        # I start with the number of products per category
        for i in range(1, nombre_a_afficher +1):
            categorie = Category(
                categories["tags"][i].get("name"),
                categories["tags"][i].get("products"),
                categories["tags"][i].get("id"),
                categories["tags"][i].get("url"),
                i,
            )
            categorie.afficher_categorie()
            total_produit += categorie.nb_product
            instance.set_categorie(categorie)
            for page in range(1, nb_produit + 1):
                produits = categorie.get_api_products(page)
                for k in range(20):
                    total_analyse += 1
                    try:
                        produit = Product(
                            produits["products"][k].get("product_name", "XXX"),
                            produits["products"][k].get("url", "url absente"),
                            produits["products"][k].get("nutrition_grade_fr", "E"),
                            produits["products"][k].get("id", "ID absent"),
                            i,
                            produits["products"][k].get("stores", "Information manquante"),
                            produits["products"][k].get("image_url", "Information manquante")
                        affichage.afficher_produit(produit)
                        try:
                            instance.set_product(produit)
                            total_charge += 1
                        except:
                            print(" produit ignoré cause BDD ")
                    except:
                        print(
                            colored("Produit ignoré pour cause d'information essentielle manquante", 'red')
                        )
        print(
            "\n Ces {} catégories contiennent {} produits dont {} ont été analysé et {} retenus".format(
                nombre_a_afficher, total_produit, total_analyse, total_charge
            )
        )
    elif choix == 0:
        menu = False
    ### If the database is already created.

    instance = Database()
    menu_accueil = True
    while menu_accueil and menu:
        choix = choix = affichage.menu2()
        if choix == 1:
            instance.print_all_categories()
            choix = int(input("Numéro de la catégorie :\n"))
            liste = instance.print_product_from_categorie(choix)
            choix = int(input("Sélectionnez un produit : \n"))
            print("------------ Votre selection ------------")

            produit = Product(
                liste[choix - 1][2],
                liste[choix - 1][1],
                liste[choix - 1][3],
                liste[choix - 1][0],
                liste[choix - 1][4],
                liste[choix - 1][5],
                liste[choix - 1][6],
            )
            affichage.afficher_produit(produit)
            print("------------ Votre substitut ------------")
            liste = instance.search_substitut(produit.categorie, produit.grade)
            n = randint(0, len(liste)-1)
            substitut = Product(
                liste[n][2],
                liste[n][1],
                liste[n][3],
                liste[n][0],
                liste[n][4],
                liste[n][5],
                liste[n][6],
            )
            affichage.afficher_produit(substitut)
            choix = input("Souhaitez vous le sauvgarder ? O/N\n").upper()
            if choix == "O":
                instance.set_favoris(substitut)
            elif choix == "N":
                pass
            else:
                print("Veuillez recomencer à la page produit")
                pass
        elif choix == 2:
            instance.print_all_favoris()
        elif choix == 0:
            print("Vous quittez le programme")
            menu_accueil = False
        else:
            print("Veuillez réessayer en regardant votre clavier")

    print("*** FIN ***")


if __name__ == "__main__":
    # execute only if run as a script
    main()