class Etudiant:
    def __init__(self, id_e, nom, filiere_nom):
        self.id = id
        self.nom = nom
        self.filiere_nom = filiere_nom

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
class


class Seance:
    def __init__(self, id_s, matiere, date,id_filiere):
        self.id = id
        self.id_filiere = id_filiere
        self.matiere = matiere
        self.date = date

