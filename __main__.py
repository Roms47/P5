from bdd import Database
from category import Category
from products import Product
from reset_bdd import *
from random import *
from mdp_mysql import *
from display import Display

def main():
    url_de_base = "https://fr.openfoodfacts.org/categorie/"  # on rajoute produit/i.json
    nb_produit = LIMITE_PAGES
    total_produit = 0
    total_charge = 0
    total_analyse = 0

    affichage = Display()
    choix = affichage.menu1()

    menu = True
    if choix == 1:
        reset()
        # L'appel à l'API ne doit se faire que à la première utilisation
        instance = Database()
        categories = Category.get_api_categories()
        nombre_a_afficher = int(input("Combien de categories voulez vous charger ?"))
        # Je commence par nombre de produit par catégorie
        for i in range(1, nombre_a_afficher +1):
            categorie = Category(
                categories["tags"][i].get("name"),
                categories["tags"][i].get("nb"),
                categories["tags"][i].get("adresse"),
                categories["tags"][i].get("id"),
                i)
            categorie.afficher_categorie()
            total_produit += categorie.nb_product
            instance.set_categorie(categorie)
            for page in range(1, nb_produit + 1):
                produits = Product.get_api_products(page)
                for k in range(20):
                    total_analyse += 1
                    try:
                        produit = Product(
                            produits["products"][k].get("product_name", colored("XXX", 'red')),
                            produits["products"][k].get("url", colored("url absente", 'red')),
                            produits["products"][k].get("nutrition_grade_fr", "E"),
                            produits["products"][k].get("id", "ID absent"),
                            i,
                            produits["products"][k].get("stores", colored("Information manquante", 'red')),
                            produits["products"][k].get("image_url", colored("Information manquante", 'red')),
                        )
                        affichage.afficher_produit(produit)
                        try:
                            instance.set_product(produit)
                            total_charge += 1
                        except:
                            print("produit ignoré cause BDD")
                    except:
                        print("Produit ignoré pour cause d'information essentielle manquante")
        print(
            "\n Ces {} catégories contiennent {} produits dont {} ont été analysé et {} retenus".format(
                nombre_a_afficher, total_produit, total_analyse, total_charge
            )
        )
    elif choix == 0:
        menu = False
    ### Dans le cas où la base est déjà crée.

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
                print("Veuillez recomencer à la produit")
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