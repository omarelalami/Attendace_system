import mysql.connector
class Etudiant:
    def __init__(self, id_etudiant, nom, prenom, date_naissance):
        self.id_etudiant = id_etudiant
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

class Filiere:
    def __init__(self, id_filiere, nom):
        self.id_filiere = id_filiere
        self.nom = nom


class Seance:
    def __init__(self, id_seance, date_seance, heure_debut, heure_fin):
        self.id_seance = id_seance
        self.date_seance = date_seance
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin


class Matiere:
    def __init__(self, id_matiere, nom_matiere):
        self.id_matiere = id_matiere
        self.nom_matiere = nom_matiere

class Inscription:
    def __init__(self, id_inscription, annee_universitaires, niveau, diplome, id_fil, id_etu):
        self.id_inscription = id_inscription
        self.annee_universitaires = annee_universitaires
        self.niveau = niveau
        self.diplome = diplome
        self.id_fil = id_fil
        self.id_etu = id_etu

class Presence:
    def __init__(self, id_presence, status, date_presence, heure_presence, id_etu, id_se):
        self.id_presence = id_presence
        self.status = status
        self.date_presence = date_presence
        self.heure_presence = heure_presence
        self.id_etu = id_etu
        self.id_se = id_se

class Gerer:
    def __init__(self,id_matiere,id_filiere,id_seance):
        self.id_gerer=None
        self.id_matiere = id_matiere
        self.id_filiere = id_filiere
        self.id_seance=id_seance


class MySQLDatabase:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def insert_etudiant(self, etudiant):
        query = f"INSERT INTO ETUDIANT VALUES ('{etudiant.id_etudiant}', '{etudiant.nom}', '{etudiant.prenom}', '{etudiant.date_naissance}')"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_inscription (self, inscription):
        query = f"INSERT INTO INSCRIPTION VALUES ('{inscription.id_inscription}', '{inscription.annee_universitaires}', '{inscription.niveau}', '{inscription.diplome}', '{inscription.id_fil}', '{inscription.id_etu}')"
        self.cursor.execute (query)
        self.connection.commit ()



    # Define similar methods for the other tables
    def insert_matiere (self, matiere):
        """
        Inserts a Matiere object into the database.
        """
        query = "INSERT INTO matiere (id_matiere, nom_matiere) VALUES (%s, %s)"
        values = (matiere.id_matiere, matiere.nom_matiere)
        self.cursor.execute (query, values)
        self.connection.commit ()

    def insert_gerer (self, gerer):
        """
        Inserts a Gerer object into the database.
        """
        query = "INSERT INTO gerer (ID_MA, ID_FI, ID_SE) VALUES (%s, %s, %s)"
        values = (gerer.id_matiere, gerer.id_filiere, gerer.id_seance)
        self.cursor.execute (query, values)
        self.connection.commit ()

    def insert_seance (self, seance):
        """
        Inserts a Seance object into the database.
        """
        query = "INSERT INTO seance (id_seance, date_seance, heure_debut, heure_fin) VALUES (%s, %s, %s, %s)"
        values = (seance.id_seance, seance.date_seance, seance.heure_debut, seance.heure_fin)
        self.cursor.execute (query, values)
        self.connection.commit ()

    def get_all_etudiants(self):
        query = "SELECT * FROM ETUDIANT"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        etudiants = []
        for row in result:
            etudiant = Etudiant(row[0], row[1], row[2], row[3])
            etudiants.append(etudiant)
        return etudiants

    def insert_filiere(self, filiere):
        query = f"INSERT INTO FILIERE VALUES ('{filiere.id_filiere}', '{filiere.nom}')"
        self.cursor.execute(query)
        self.connection.commit()

    def getAllFiliere(self):
        query = "SELECT NOM FROM FILIERE"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        names = []
        for row in result:
            name = row [0]
            names.append(name)
        return names

    def close_connection(self):
        self.connection.close()











