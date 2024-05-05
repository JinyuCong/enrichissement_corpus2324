# Enrichissement_corpus2324

## Membres
Jinyu CONG
<br>Yuanlong PENG
<br>Chenzhi SUN
<br>Yu ZHANG

### Les scripts finaux pour que notre page web puisse se connecter à la base de données backend se trouvent dans la branche "Jinyu". 
### Les scripts finaux sur l'extraction des données se trouvent dans cette branche courante "main": 

- ./txt_to_xml_node_virgule.py
<br>---> script final utilisé pour convertir le corpus du format txt au format xml
- ./extraction_enrichi/ver_parcourir
<br>---> scripts finaux utilisés pour extraire les données et les sauvegarder dans des fichiers tsv


## Index des dossiers
***Pour l'extraction des informations, les scripts finaux et leurs sorties finales se trouvent dans : ./extraction_enrichi/ver_parcourir.***

### 1. corpus
Ce dossier contient les corpus originaux choisis au format txt.

Il y a au total 32 textes :
- 7 textes dans le corpus GrandParis
- 7 textes dans le corpus GrandPrixUrbanismeSimple
- tous les 3 textes dans le corpus GrandParisEnrichi
- tous les 15 textes dans le corpus GrandPrixUrbanismeEnrichi

### 2. corpus_xml
Le dossier **corpus_xml** contient le corpus converti au format XML. 
<br>Il comprend 2 sous-dossiers : **CE** et **simple**.

Dans le sous-dossier **CE**, se trouvent les textes des corpus enrichis, tandis que dans le sous-dossier **simple** se trouvent ceux des corpus simples.

### 3. extraction_enrichi

#### 3.1 ver_orig_enrichi
Ce dossier contient les scripts de la première version pour extraire les informations dans différentes balises. 
<br>
Il comprend 7 scripts, chacun pour traiter respectivement les balises `<act>`, `<doc>`, `<dyn>`, `<lieu>`, `<cause> et <res> et <obj>`, `<perc>`, `<tps>`. 

#### 3.2 ver_modi
Ce sous-dossier contient les scripts modifiés dans lesquels nous avons corrigé des bugs. 
<br>
Le script pour extraire le corpus simple est également inclus ici pour plus de lisibilité et de facilité de test.

Les scripts dans les deux sous-dossiers dessus nous permettent d'extraire les informations depuis un fichier défini. 
<br>
Pour que les scripts puissent parcourir le dossier de notre corpus, nous avons adapté les scripts comme dans la version suivante: 

#### 3.3 ver_parcourir
Ce sous-dossier contient les scripts de la version finale. 
<br>
Il comprend 8 scripts, 7 pour les corpus enrichis et 1 pour les corpus simples. 
<br>
Les résultats de chaque script (les sorties au format tsv) sont également inclus.

### 4. extraction_simple
Ce dossier contient le script pour extraire les informations des corpus simples, ainsi qu'un fichier xml pour tester et un fichier tsv comme résultat. 

Le script présent ici ne permet que de lire un fichier déterminé, pas de parcourir un corpus. Pour parcourir les corpus simples, le script se trouve dans le dossier : **../extraction_enrichi/ver_parcourir**.

### 5. to_xml_py_brouillons
Ce dossier contient les brouillons avant d'obtenir le script **../txt_to_xml_node_virgule.py**. 