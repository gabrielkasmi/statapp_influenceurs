
## Notebooks

Ce dossier contient les notebooks utilisés. Le projet implique la gestion de plusieurs entrées/sorties. Ces fichiers annexes sont dans les dossiers scripts et text_files. Pour s'y retrouver, voici une description des différents fichiers:

Notebook 1 - Initialisation de la liste de followers:
• liste_users1 : correspond aux followers des cinq comptes fournis par les GL
• users : correspond à la liste des followers expurgée des comptes qui n'ont pas 
          pas assez d'abonnés ou trop d'abonnements
• final_users : correspond à la liste des followers précédente, expurgée des utilisateurs
		institutionnels et/ou marques
• users_to_scrap : correspond au fichier de sortie, divisé en trois pour être traité 
		   en trois parties distinctes. 

On a aussi des fichiers de sauvegarde crées au fur et à mesure et déplacés dans le 
dossier draps.

C'est à partir du fichier users_to_scrap qu'on initialise la liste users1 du notebook 2.

Notebook 2 - Extraction de la liste des comptes suivis par les utilisateurs

Lorsque l'on exécute le Notebook, faire attention à bien vérifier que l'algorithme ne se plante pas dans les utilisateurs recommandés. Il suffit pour le dégager de là de scroller verticalement. 

Ce notebook prend en entrée le fichier users_to_scrap.txt qu'il "renomme" usernames.txt. Le fichier usernames.txt est prit en entrée par le script, qui donne en sortie le fichier followers_list.txt. 

Dans la pratique, le temps pour scrapper les comptes étant très long, le fichier users_to_scrap est découpé. Si le fichier d'entrée pour le script est le même à chaque fois, on stocke dans un dossier followers_lists le fichier followers_lists.txt (renommé pour l'occasion followers_list1, followers_list2, etc)  généré à chaque itération du script. 
A titre d'information, le temps d'exécution par compte varie de quelques secondes à plusieurs minutes. 

Les différents fichiers sont regroupés manuellement dans un premier grand fichier qui est ensuite assemblé aux autres fichiers du groupe. Le gros fichier synthétisant tout le scrapping est followers_list_complet.txt, utilisé dans le notebook 3.

Notebook 3  - Construction du graphe

La partie construction du graphe ne pose pas trop de problème. 

On exporte deux fichiers, l'un contenant la liste des comptes retenus sur la base des deux critères (confondus, pour ensuite construire leurs indicateurs dans le notebook 4). 
Un second fichier présente sous forme de tableau les comptes ainsi que les mesures
• central_points.txt contient les utilisateurs sélectionnés
• dict_centrality.txt contient un dictionnaire avec les mesures de centralité 

Dans le second document, le premier élément de la liste correspond à la valeur de la centralisé de vecteur propre et le second au PageRank. Les cases sont laissées vides le cas échéant. 


Notebook 4 - Construction d'indicateurs

Attention à ne pas fermer la session tant que le scrapping n'est pas terminé (pas de fichiers de sauvegarde externe dans ce notebook).

On crée quatre fichiers .csv :

• users_dataframe.csv qui contient tous les utilisateurs retenus
• posts_dataframe.csv qui reprend les posts les plus récents des utilisateurs
• metrics_dataframe.csv qui synthétise les différents indicateurs pour chaque utilisateur
• summary_metrics.csv qui présente les statistiques descriptives pour chaque métrique

On exporte un fichier avec les utilisateurs retenus (shortlist_influenceurs.txt).

Notebook 5 - Analyse qualitative

Il n'y a rien de particulier à signaler pour ce notebook.
