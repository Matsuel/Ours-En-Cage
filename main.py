DICO=['aime','brie','bris','bure','cage','cime','cire','cure','dame','dime','fart','gage','gaie','hale','hors','hure','iris','lire','loge','luge','mage','mers','mime','mire','mors','ours','page','paie','pale','pame','paru','pere','pers','pipe','pire','rage','raie','rale','rame','rape','rues','sape','sari','scie','sure','toge','tore','tors','tort','truc']

def distance(mot1,mot2):
  """
  Entrées : str, 2 mots
  Sortie : int
  Renvoie le nombre de lettre différentes entre 2 mots.
  """
  L_mot2=[(lettre)for lettre in mot2] #On met mot2 sous forme de liste
  for lettre in mot1:
    L=[]
    for i in range(len(L_mot2)):
      if L_mot2[i]== lettre:
        L.append(i)
    if L!= []:
      L_mot2.pop(L[0])
  return len(L_mot2)  

def ListeVoisins(mot):
  """
  Entrée: mot sous la forme d'un str.
  Sortie: Liste des voisins du mot, c'est-à-dire les mots ayant une lettre de différence avec lui.
  """
  rep=[]
  for mots in DICO:
    if distance(mots,mot)==1:
      rep.append(mots)
  return rep

class Graphe:
  
  def __init__ (self):
    """
    Créer un graphe avec comme atribut un dictionnaire qui contiendra la liste des successeurs.
    """
    self.__successeurs={}
    
  def GetSommets(self):
    """
    Renvoie la liste des sommets du graphe.
    """
    return list((self.__successeurs).keys())

  def NbSommets(self):
    """
    Renvoie le nombre de sommet du graphe.
    """
    return len(self.__successeurs)

  def AjouterSommet(self, valeur):
    """
    Ajoute dans le dictionnaire le sommet avec la valeur passée en paramètre.
    """
    self.__successeurs[valeur]=[]
  
  def AjouterArc(self,mot,succ):
    """
    Ajoute une liaison entre un mot et un autre en ajoutant le mot comme valeur de la clé mot.
    """
    self.__successeurs[mot].append(succ)
        
  def GetDicoSucc(self):
    """
    Renvoie la liste des successeurs.
    """
    return self.__successeurs
  
  def SuiteDico(self,mot1,mot2):
    """
    Entrée: 2 mots sous forme str
    Sortie: Dictionnaire avec la liste des mots et de leurs successeurs.
    """
    mots_vues={}#On initialise le dictionnaire qui sert de réponse
    possible=[mot1] #On initialise possible comme potentiel valeur 
    mots_vues[(possible[0])]=None #On ajoute possible dans mots_vues avec comme valeur None
    mot_trouve=False # On initialise le booléen pour réaliser la boucle tant qu'on a pas trouvé le mot2
    mots_vues_cles=list(mots_vues.keys()) #On utilise mots_vues.keys() car sinon on a une erreur lorsqu'on fait if not mot in mots_vues car la taille du dictionnaire change.
    while not mot_trouve:#On répète la boucle tant que l'on a pas croisé le mot2
      courant=possible[0] #On définit le mot courant comme le premier mot de possible
      possible.pop(0) #On supprime ensuite ce mot
      if courant==mot2: #Si on a croisé mot2
        mot_trouve=True ##Comme on a vu mot2 on l'a donc trouvé
      else:#Si on a pas vu mot2
        for mot in ListeVoisins(courant): #On parcourt les voisisn de courant
          if mot not in mots_vues_cles: # Si le mot n'est pas dans le dictionanire
            possible.append(mot)#On l'ajoute dans possible
            mots_vues[mot]=courant #On ajoute dans le dictionnaire l'élément mot de valeur courant
            mots_vues_cles.append(mot)# On ajoute ensuite mot dans la liste contenant les clés
    return mots_vues#On renvoie le dictionnaire

  def Suitemots(self,mot1,mot2):
    """
    Entrées : str, 2 mots
    Sortie : Liste de str
    Renvoie la liste des mots nécessaire pour aller d'un mot à l'autre de manière stylée.
    """
    Dico=self.SuiteDico(mot1,mot2) # Récupère le dictionnaire avec la liste des mots et de leurs successeurs.
    mot=mot2 # La variable mot qui aura comme valeur mot2 point de départ de la suite.
    rep=[mot] # Liste qui contiendra la suite de mot à l'envers.
    Suite=[] # Liste qui contiendra la suite de mot.
    while mot != mot1 : # Tant que le mot actuel n'est pas égal à mot1.
      mot = Dico[mot] # Mot devient la valeur du mot associé .
      rep.append(mot) # Ajoute le mot à la suite de mot.
    while rep != []: # Tant que la liste rep n'est pas vide.
      x=rep.pop(-1) # Retire le dernier élément de la suite de mot et le stock dans la variable x
      Suite.append(x) # Ajoute le mot de la variable x dans la liste Suite
    ##Représentation de la suite avec des flèches.##
    suite_str="" # Variable qui contiendra la suite de mot sous forme de chaîne de caractère
    for i in range(len(Suite)-1):
      suite_str+=str(Suite[i])+" --> " # Ajoute, sous forme de str, le mot d'indice i ainsi qu'une flèche
    suite_str+=str(Suite[-1]) # Ajoute le dernier mot de la Suite de mot
    return suite_str # Renvoie la suite de mot sous forme d'str


Reseau=Graphe() #On créé le graphe Reseau
for el in DICO: #On parcourt les éléments de DICO
  Reseau.AjouterSommet(el) #On ajoute comme sommet l'élément
for mot in DICO: #On parcort les Mots de DICO
  for succ in Reseau.GetDicoSucc(): #On parcourt tous les successeurs du graphe
    if distance(mot,succ)==1: #Si mot et succ sont voisins donc à 1 lettre d'écart
      Reseau.AjouterArc(mot,succ) #On ajoute un arc entre mot et succ

print(Reseau.Suitemots("aime","hors"))
print(Reseau.Suitemots("brie","ours"))