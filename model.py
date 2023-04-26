class Etudiant:
    def __init__(self, id_e, nom ,prenom,date_naissance):
        self.id = id_e
        self.nom = nom
        self.prenom=prenom
        self.date_naissance=date_naissance

class Presence:
    def __init__(self, id_p, date, heure, id_etudiant, nom, seance):
        self.id = id
        self.date = date
        self.heure = heure
        self.id_etudiant = id_etudiant
        self.nom = nom
        self.seance = seance

class Filiere:
    def __init__(self, id_f, nom, id_etudiant, id_m):
        self.id = id
        self.nom = nom
        self.id_etudiant = id_etudiant
        self.id_m = id_m

class Matiere:
    def __init__(self, id_m, nom_m):
        self.id_m = id_m
        self.nom_m = nom_m



class Seance:
    def __init__(self, id_s, matiere, date,id_filiere):
        self.id = id
        self.id_filiere = id_filiere
        self.matiere = matiere
        self.date = date

