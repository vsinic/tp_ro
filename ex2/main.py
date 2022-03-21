import numpy as np
import matplotlib.pyplot as plt

#PROBVC
class ProbVC:
    def __init__(self, n):
        self.n = n
        coords = np.random.random(2 * self.n)
        self.villes = coords.reshape(self.n, 2)

    def affiche_chemin(self, s, method=None):
        plt.figure()
        for i in range(self.n):
            plt.plot(self.villes[i][0], self.villes[i][1], 'x')
            plt.plot((self.villes[s[i]][0], self.villes[s[(i + 1) % self.n]][0]),
                     (self.villes[s[i]][1], self.villes[s[(i + 1) % self.n]][1]))
        if method is not None:
            plt.title(method + ' - coût global : ' + str(self.J(s)))
        else:
            plt.title('Coût global : ' + str(self.J(s)))
        plt.draw()  # block = False)

    def randomVoisin(self, s):
        s_prim = list(s)  # clone
        n = len(s)
        i, j = np.random.randint(n), np.random.randint(n)
        s_prim[i], s_prim[j] = s_prim[j], s_prim[i]
        return s_prim

    def tousLesVoisins(self, s):
        liste_voisins = []
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                s_prim = np.copy(s)
                s_prim[i], s_prim[j] = s_prim[j], s_prim[i]
                liste_voisins += [s_prim]
        return liste_voisins

    def J(self, s):
        J = 0
        J = len(s)
        return J

    def argmin_J(self, s, tabou=[]):
        if tuple(s) not in tabou:
            J_ref = self.J(s)
            voisin_ref = s
        else:
            J_ref = 1e8
        tous_les_poids = []
        for i in range(len(s)):
            for j in range(len(s[i])):
                tous_les_poids.append(s[i][j])
        s = extraire_liste_poids(tous_les_poids)
        #print(s)
        liste_voisins = self.tousLesVoisins(s)
        for voisin in liste_voisins:
            s_voisin = conteneurisation(voisin)
            if self.J(s_voisin) < J_ref and tuple(s_voisin) not in tabou:
                J_ref = self.J(s_voisin)
                voisin_ref = s_voisin
        return voisin_ref

#FONCTIONS AUXILIAIRES
def conteneurisation(liste_poids):
    #[A,B,C,D] -> [[A,B], [C,D]]
    #print("Before cont: ", len(liste_poids))
    s = []
    current = []
    current_weight = 0
    for i in range(len(liste_poids)):
        # print("i = ",i, "| index dans poids = ", poids.index(permute[i]))
        current.append(liste_poids[i])
        current_weight += liste_poids[i]
        if current_weight > 245:
            current.pop()
            s.append(current)
            current = [liste_poids[i]]
            current_weight = liste_poids[i]
    #print("After cont: ", len(s))
    return s

def deconteneurisation(liste_poids):
    #[[A,B], [C,D]] -> [A,B,C,D]
    #print("Before decont: ", len(liste_poids))
    L = []
    for cont in liste_poids:
        for i in cont:
            L.append(i)
    #print("After decont: ", len(L))
    return L

def extraire_liste_poids(s):
    L = []
    for i in s:
        L.append(poids[i])
    return L

# METHODES
def monte_carlo(probVC, N):
    J_ref = 1e8
    print('*** Monte-Carlo ***')
    for i in range(N):
        permute = list(all_weights)
        np.random.shuffle(permute)
        s = conteneurisation(permute)
        # print(probVC.J(s), J_ref)
        if probVC.J(s) < J_ref:
            s_ref = np.copy(s)
            J_ref = probVC.J(s)
    print(s_ref)
    print("J_ref = ", J_ref)
    return s_ref


def glouton(probVC, s):
    J_ref = 1e8
    print('*** Glouton ***')
    s_cont = conteneurisation(s)
    while probVC.J(s_cont) < J_ref:
        J_ref = probVC.J(s_cont)
        s = probVC.argmin_J(s_cont)
    print(s_cont)
    print("J_ref = ", J_ref)
    return s_cont

def glouton_aleatoire(probVC, s, N):
    J_ref = float('inf')
    print('*** Glouton Aléatoire ***')
    for i in range(N):
        random_voisin = probVC.randomVoisin((all_weights))
        s_prime = conteneurisation(random_voisin)
        if probVC.J(s_prime) < probVC.J(s):
            J_ref = probVC.J(s_prime)
            s = np.copy(s_prime)
    #print(s)
    print("J_ref = ", J_ref)
    return s

def tabou(probVC, s, N, K):
    J_ref = 1e8
    tabou = []
    print('*** Tabou ***')
    cpt = 0
    for i in range(N):
        if probVC.J(s) < J_ref:
            s_ref = np.copy(s)
            J_ref = probVC.J(s)
        tabou.append(tuple(s))
        if len(tabou) > K:
            tabou = tabou[1:]
        s = probVC.argmin_J(s, tabou=tabou)
        cpt += 1
    return s_ref


def recuit(probVC, s, N, beta_0, eps):
    print('*** Recuit ***')
    beta = beta_0
    for i in range(1, N):
        s_prime = list(s)
        np.random.shuffle(s_prime)
        s_prime = conteneurisation(s_prime)
        s = conteneurisation(s)
        if probVC.J(s_prime) < probVC.J(s):
            CHOICE = True
        else:
            proba = np.exp(-beta * (probVC.J(s_prime) - probVC.J(s)))
            x = np.random.random()
            if x < proba:
                CHOICE = True
            else:
                CHOICE = False
        if CHOICE:
            s = deconteneurisation(s_prime)
            print("decont", len(s))
        else:
            s = deconteneurisation(s)
            print("decont", len(s))
        beta = (1+eps) * beta
    print(s)
    s = conteneurisation(s)
    print(s)
    print("J_ref = ", probVC.J(s))
    return s

#PROGRAMME PRINCIPAL
n = 20
probVC = ProbVC(n)
s = np.random.permutation(n)
N = 10000000
K = 30
beta_0 = 1
eps = 0.001

#Poids, Nombre
p1 = [20,13]
p2 = [22,15]
p3 = [18,25]
p4 = [15,30]
p5 = [21,18]
p6 = [16,35]

poids = [20,22,18,15,21,16]
nombre = [13,15,25,30,18,35]
NOMBRE_TOT = 136
capacite = 245
all_weights = []
for i in range(len(nombre)):
    for j in range(nombre[i]):
        all_weights.append(poids[i])


s_mc = monte_carlo(probVC, N)

s_glouton_aleatoire = glouton_aleatoire(probVC, np.copy(all_weights), N)

s_glouton = glouton(probVC, np.copy(all_weights))

#s_tabou = tabou(probVC, np.copy(s), N, K)

#Attention: recuit ne marche pas à cause d'un bug du deconteneurisation
s_recuit = recuit(probVC, all_weights, N, beta_0, eps)

#plt.show()