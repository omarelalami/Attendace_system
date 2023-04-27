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

    def get_all_etudiants(self):
        query = "SELECT * FROM ETUDIANT"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        etudiants = []
        for row in result:
            etudiant = Etudiant(row[0], row[1], row[2], row[3])
            etudiants.append(etudiant)
        return etudiants

    # Define similar methods for the other tables

    def close_connection(self):
        self.connection.close()











