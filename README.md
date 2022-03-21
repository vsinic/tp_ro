Templeton William \\
Truong Minh Ky Valentin\\


# Installation
```
pip install -r requirements.txt
```

# Exercice 1 

## Outputs
```python
L'affectation par chambre est :
        Chambre 0 : étudiant  2 et étudiant  6 | Niveau de bonheur : 14.0
        Chambre 1 : étudiante 7 et étudiante 1 | Niveau de bonheur : 17.0
        Chambre 2 : étudiante 9 et étudiant  4 | Niveau de bonheur : 18.0
        Chambre 3 : étudiante 5 et étudiant  3 | Niveau de bonheur : 14.0
        Chambre 4 : étudiant  8 et étudiante 0 | Niveau de bonheur : 12.0
Le bonheur total vaut 75.0
Méthode utilisée : Monte Carlo. Temps d'exécution : 1.890e-01s

L'affectation par chambre est :
        Chambre 0 : étudiant  2 et étudiant  6 | Niveau de bonheur : 14.0
        Chambre 1 : étudiant  7 et étudiante 1 | Niveau de bonheur : 17.0
        Chambre 2 : étudiante 4 et étudiant  9 | Niveau de bonheur : 18.0
        Chambre 3 : étudiant  5 et étudiante 3 | Niveau de bonheur : 14.0
        Chambre 4 : étudiante 8 et étudiant  0 | Niveau de bonheur : 12.0
Le bonheur total vaut 75.0
Méthode utilisée : Glouton Aléatoire. Temps d'exécution : 1.905e-01s

L'affectation par chambre est :
        Chambre 0 : étudiant  2 et étudiant  6 | Niveau de bonheur : 14.0
        Chambre 1 : étudiante 8 et étudiante 0 | Niveau de bonheur : 12.0
        Chambre 2 : étudiant  5 et étudiant  3 | Niveau de bonheur : 14.0
        Chambre 3 : étudiante 9 et étudiante 4 | Niveau de bonheur : 18.0
        Chambre 4 : étudiante 1 et étudiante 7 | Niveau de bonheur : 17.0
Le bonheur total vaut 75.0
Méthode utilisée : Recuit. Temps d'exécution : 1.860e-01s
```


# Exercice 2

## Lancement
Dans un IDE, exécuter le programme; ou `python3 ./exercice2.py`

##Output
La solution minimale est de 9 conteneurs; la répartition est: 
```python
[list([4, 6, 5, 1, 4, 1, 3, 3, 2, 6, 5, 3, 1])
 list([1, 3, 6, 3, 5, 6, 2, 6, 3, 5, 6, 2, 5])
 list([4, 5, 6, 5, 6, 2, 4, 4, 6, 5, 6, 1, 4, 6])
 list([5, 2, 5, 5, 4, 2, 3, 6, 4, 2, 5, 6, 4])
 list([4, 3, 4, 6, 6, 3, 6, 4, 2, 4, 1, 3, 2, 3])
 list([4, 3, 4, 6, 5, 6, 5, 3, 6, 3, 4, 4, 1, 1])
 list([3, 4, 1, 5, 4, 2, 2, 6, 5, 6, 6, 3, 3])
 list([4, 5, 3, 4, 3, 4, 4, 6, 6, 6, 2, 2, 3, 4])
 list([5, 4, 6, 1, 6, 6, 6, 6, 3, 6, 1, 4, 1, 4])]
J_ref =  9
```

