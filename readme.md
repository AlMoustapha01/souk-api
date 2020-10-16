# SOUK
SOUK est un projet de comparaison des prix des articles proposés par les sites de ecommerce.

Ce depôt constitue l'API de de ce système

Pour l'installation:

1- il faut installer python >= 3.7.0 et pip
2- pip install requirements.txt
3- se rendre dans souk_api/settings.py et chercher la variable DATABASES puis verifier les paramètres de base de données
3- python manage.py makemigrations
4- python manage.py migrate
3- python manage.py runserver

les modules de cette API sont:
- comparator:
    les routes sont les suivantes:
    * 'v1/sites/' : liste des sites
    * 'v1/sites/<int:id>/' : site spécifique par id 
    * 'v1/categories/' : listes des catégories d'article
    * 'v1/categories/<int:id>/': catégorie spécifique par id
    * 'v1/lowcategories/' : listes des sous catégories d'article
    * 'v1/lowcategories/<int:id>' :sous catégorie spécifique par id
    * 'v1/products/' : liste des produits 
    * 'v1/products/<int:id>/' : produit spécifique par id
    * 'v1/prices/' : liste des prix 
    * 'v1/prices/<int:id>/': prix spécifique par id
- user:
    les routes sont les suivantes:
    * 'v1/users/' : liste des utilisateurs
    * 'v1/users/<int:id>/' : utilisateur spécifique par id
    * 'v1/notify/' : liste des notifications
    * 'v1/notify/<int:id>/' : notification spécifique par id
    * 'v1/followprice/': liste des prix d'article suivis
    * 'v1/followprice/<int:id>/': prix spécifique suivi par id
    * 'v1/storeproduct/': liste des produits suivis
    * 'v1/storeproduct/<int:id>/': produit spécifique suivi
    * 'v1/auth/token/login/': generation de token
    * 'v1/auth/users/me/': authentification par le token
    * 'v1/auth/token/logout/' : deconnexion soit la suppression du token
    * 'v1/docs/' : documentation de l'API

