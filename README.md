# AlgoInvest&Trade
## Description
### **Le projet AlgoInvest&trade à pour but de trouver la meilleur combinaison d'actions a acheter en fonction de leur bénéfices après 2 ans**
### Deux version sont proposées :
* [Version bruteforce](#bruteforce)
* [Version optimisée(Algorithme du sac à dos)](#optimized)
## Cloner le projet

````bash
$ git clone https://github.com/Jogodev/P7_algo_invest.git
$ cd P7_algo_invest
````

### Créer l'environnement virtuel

````bash
$ python -m venv env
````

### Activater l'environnement virtuel

#### Windows
````bash
$ . env\scripts\activate 
````
#### Mac
````bash
$ source env\scripts\activate 
````
#### linux
````bash
$ source env\scripts\activate 
````

### Installer les paquets

````bash
$ pip install -r requirements.txt
````

## Lancer le programme
### Version bruteforce <a name="bruteforce"></a>

````bash
$ python bruteforce.py
````
#### Cette commande fera le calcul du fichier csv de 20 actions pour un montant total de 500 €
### Version dynamique <a name="optimized"></a>

````bash
$ python optimized.py
````
#### Cette commande fera le calcul du fichier csv de 20 actions pour un montant total de 500 €.
#### Pour lancer le programme sur un autre dataset décommenter celui_ci en haut du ficher optimized.py

![comment.png](images/comment.png)