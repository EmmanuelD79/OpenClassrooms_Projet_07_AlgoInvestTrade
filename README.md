# OpenClassrooms_Projet_07_AlgoInvest&Trade

Ce projet est le septième de la formation Openclassrooms Développeur d'application PYTHON.
<br>Son but est de coder 2 algorithmes: un de type Bruteforce  et l'autre optimisé en programmation dynamique.<br>
Grâce à un menu sur le terminal, nous pouvons :
<br> - Séléctionner le dataset à analyser
<br> - Choisir le type d'algorithme à utiliser pour l'analyse
<br> - Définir le montant maximal d'investissement
<br> - Définir le niveau de précision (nombre décimal)
<br> - Afficher le résultat sur le terminal
<br> - Ecrire le résultat dans un fichier .txt


## Pour commencer

cloner le projet à l'aide de votre terminal en tapant la commande :
<br> 

```

git clone https://github.com/EmmanuelD79/OpenClassrooms_Projet_07_AlgoInvestTrade.git

```

### Pré-requis

créer un environnement virtuel à l'aide de votre terminal en tapant la commande:
	<br>  
```

python -m venv env

```

puis l'activer :
<br>sur windows :

```

.\env\scripts\activate

```


<br>sur mac et linux : 

```

source env/bin/activate

```


### Installation

Pour utiliser ce projet, il est nécessaire d'installer les modules du fichier requirements.txt.

<br>Pour installer automatiquement ces modules, dans votre terminal, vous devez aller dans le dossier du projet et ensuite taper la commande suivante :
	<br> 
```

pip install -r requirements.txt

```

ou le faire manuellement en consultant le fichier requirements.txt en tapant sur votre terminal la commande :
```

cat requirements.txt

```
puis les installer un par un avec la commande :
```

pip install <nom du paquage>

``` 
## Initialisation

Au préalable, veuillez enregistrer vos datasets dans un dossier ./datasets à la racine du projet afin que l'application retrouve les datasets à analyser.

Si aucun dataset est présent, l'application vous en informera et s'arrêtera.

vos datasets doivent être au format .csv

## Démarrage

Pour démarrer le projet, vous devez aller dans le répertoire du projet et taper sur votre terminal la commande:
	<br> 
```
	
python main.py
	
```

Le menu principal de l'application affiche les fichiers csv présent dans le dossier /datasets:

<br>Un dossier flake-report est présent, nous pouvons y trouver un rapport flake8-html.
<br>Pour générer un rapport, vous devez taper la commande dans le terminal:
```
	
flake8
	
```
## Fabriqué avec

Python 3.9
