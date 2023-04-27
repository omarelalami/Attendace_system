import customtkinter as ctk
import csv
from modelEcole import Etudiant,MySQLDatabase
from PyQt5 import Qt
from CTkMessagebox import CTkMessagebox

class EtudiantGui:

    def __init__(self,right_dashboard):
        self.idLabel = ctk.CTkLabel (right_dashboard, text="ID Etudiant")
        self.idLabel.grid (row=0, column=0, padx=20, pady=20, sticky="ew")

        self.idEntry = ctk.CTkEntry (right_dashboard, placeholder_text="N1990909")
        self.idEntry.grid (row=0, column=1,columnspan=3, padx=20, pady=20, sticky="ew")

        self.prenomLabel = ctk.CTkLabel (right_dashboard, text="Prenom")
        self.prenomLabel.grid (row=1, column=0, padx=20, pady=20, sticky="ew")

        # Prenom Entry Field
        self.prenomEntry = ctk.CTkEntry (right_dashboard, placeholder_text="Omar")
        self.prenomEntry.grid (row=1, column=1,columnspan=3, padx=20,pady=20, sticky="ew")

        # Prenom Label
        self.nomLabel = ctk.CTkLabel (right_dashboard, text="Nom")
        self.nomLabel.grid (row=2, column=0,padx=20, pady=20,sticky="ew")

        # Nom Entry Field
        self.nomEntry = ctk.CTkEntry (right_dashboard, placeholder_text="Elalami")
        self.nomEntry.grid (row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew")



        # Naissance Label
        self.NaissanceLabel = ctk.CTkLabel (right_dashboard, text="Date de naissance")
        self.NaissanceLabel.grid (row=3, column=0,
                             padx=20, pady=20,
                             sticky="ew")

        # DateNaissance Entry Field
        self.NaissanceEntry = ctk.CTkEntry (right_dashboard, placeholder_text="04/01/2001")
        self.NaissanceEntry.grid (row=3, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.bt_etudiant = ctk.CTkButton (right_dashboard, text="Ajouter Etudiant", command=self.insert_etudiant)

        self.bt_etudiant.grid (row=6, column=4, padx=20, pady=10)
        self.bt_upload = ctk.CTkButton (right_dashboard, text="Upload Fichier CSV", command=self.upload_csv)

        self.bt_upload.grid (row=6, column=3, padx=20, pady=10)


    def getDataEtudiant(self):

        return [self.idEntry.get(),self.prenomEntry.get(),self.nomEntry.get(),self.NaissanceEntry.get()]

    def insert_etudiant (self):
        try:
            db = MySQLDatabase ('localhost', 'root', '', 'si_presence')
            etudiant = Etudiant (self.idEntry.get(),self.prenomEntry.get(),self.nomEntry.get(),self.NaissanceEntry.get())
            db.insert_etudiant (etudiant)
            db.close_connection ()
            CTkMessagebox (title="Good", message="Operation effectuer avec succes", icon="check", option_1="OK")
        except Exception:
            CTkMessagebox (title="Good", message="Essayer de corriger vous entrer", icon="cancel", option_1="OK")

    def upload_csv (self):
        # Open a file dialog to choose a CSV file
        try:
            app = Qt.QApplication ([])
            file_path, _ = Qt.QFileDialog.getOpenFileName(None, 'Open CSV File', '', 'CSV Files (*.csv)')

            db = MySQLDatabase ('localhost', 'root', '', 'si_presence')
            # Read the CSV file and insert students into the database
            if file_path:
                with open (file_path, 'r') as csvfile:
                    reader = csv.reader (csvfile)
                    next (reader)  # Skip the header row
                    for row in reader:
                        id = row [0]
                        prenom=row[1]
                        nom = row [2]
                        date_naissance = row [3]

                        etudiant = Etudiant (id, prenom, nom,date_naissance)
                        db.insert_etudiant (etudiant)

            db.close_connection ()
            CTkMessagebox (title="Good", message="Operation effectuer avec succes", icon="check", option_1="OK")
        except  Exception:
            CTkMessagebox (title="Good", message="Essayer de corriger vous entrer", icon="cancel", option_1="OK")
