import numpy as np
import time
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

class ProbApp():
    def __init__(self, n_eleve = 10, n_chambre = 5, taille_chambre = 2):
        self.n_eleve = n_eleve # nbre eleves
        self.taille_chambre = taille_chambre #nbre de lits par chambre
        self.n_chambre = n_chambre # nbre de chambre
        self.J = 0
        self.methode = "aléatoire"
        self.end_time = 0
        
        if not (n_eleve == 2*n_chambre) :
            raise ValueError("La condition n_eleve = 2*n_chambre n'est pas vérifiée.")

        # preferences des eleves
        z = -np.inf
        self.pref = np.array([[z,7,6,2,4,7,4,1,8,3],
                            [1,z,3,1,10,5,2,9,4,2],
                            [10,1,z,5,6,1,8,2,7,4],
                            [1,8,4,z,10,7,5,4,2,7],
                            [8,7,3,5,z,2,1,5,2,9],
                            [2,2,3,7,8,z,8,2,1,5],
                            [1,7,6,1,7,7,z,8,1,5],
                            [6,8,1,1,10,8,1,z,4,7],
                            [4,1,2,2,8,1,7,5,z,2],
                            [1,5,4,3,9,7,1,4,6,z]])

        self.A = self.randomAffectation()

    def randomAffectation(self):
        """tire une affectation au hasard
        """
        A = np.random.choice(self.n_eleve, (self.n_chambre, self.taille_chambre),
                replace=False)
        return np.array(A, dtype = int)

    def randomVoisin(self, A=None):
        """permutte deux eleves
        """
        if A is None : A = self.A
        A_prim = A.copy() #clone
        i = (0,0) ; j = (0,0) 
        while i==j :            
            i = (np.random.randint(self.n_chambre),
                np.random.randint(self.taille_chambre))
            j = (np.random.randint(self.n_chambre),
                np.random.randint(self.taille_chambre))
        A_prim[i], A_prim[j] = A_prim[j], A_prim[i]
        return np.array(A_prim, dtype = int)

    def _cost(self, A=None):
        """retourne le cout
        """
        if A is None : A = self.A
        cost = 0
        for eleves in A :
            cost += self.pref[eleves[0], eleves[1]]
            cost += self.pref[eleves[1], eleves[0]]
        return cost  

### RESOLUTION ###

    def monte_carlo(self, N, display=True):
        """retourne le plus court chemin selon la methode de Monte Carlo"""    
        self.methode = "Monte Carlo"    
        self.J = 0
        start_time = time.time()
        for _ in tqdm(range(N), desc=self.methode):
            A = self.randomAffectation()
            cost = self._cost(A)
            if cost > self.J :
                self.J = cost
                self.A = A
        self.end_time = time.time()-start_time
        if display : print(self)
        return self.J, self.A, self.end_time  

    def glouton_random(self, N, display=True):
        """retourne le plus court chemin selon la methode Glouton Aléatoire"""  
        self.methode = "Glouton Aléatoire"    
        start_time = time.time()         
        self.J = 0
        for _ in tqdm(range(N), desc=self.methode):
            A = self.randomVoisin()
            cost = self._cost(A)
            if cost > self.J :
                self.J = cost
                self.A = A
        self.end_time = time.time()-start_time
        if display : print(self)
        return self.J, self.A, self.end_time

    def recuit(self, N, beta, eps, display=True):
        """retourne le plus court chemin selon la methode du Recuit"""  
        self.methode = "Recuit"    
        start_time = time.time()         
        self.J = 0        
        accepter = 0
        for _ in tqdm(range(N), desc=self.methode):
            voisin = self.randomVoisin()
            cost = self._cost(voisin)
            if cost > self.J :
                accepter = True
            else :
                p = np.exp(-beta*(self.J-cost))
                x = np.random.randint(low=0, high=1)
                accepter = x < p

            if accepter : 
                self.A = voisin
                self.J = cost
            beta = beta * (1 + eps)
        self.end_time = time.time()-start_time
        if display : print(self)
        return self.J, self.A, self.end_time

    def __str__(self):
        s = f"\nL'affectation par chambre est :\n"
        for idx, chambre in enumerate(self.A):
            s += f"\tChambre {idx} : étudiant{'e' if np.random.randint(2)>0.5 else ' '} {chambre[0]} et étudiant{'e' if np.random.randint(2)>0.5 else ' '} {chambre[1]}"
            cost = self.pref[chambre[0], chambre[1]]
            cost += self.pref[chambre[1], chambre[0]]
            s += f" | Niveau de bonheur : {cost}\n"
        s += f"Le bonheur total vaut {self.J}\n"
        s += f"Méthode utilisée : {self.methode}. Temps d'exécution : {self.end_time:3.3e}s\n"
        return s
