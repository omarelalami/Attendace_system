import customtkinter as ctk
import csv
from modelEcole import Etudiant,MySQLDatabase
from PyQt5 import Qt
from CTkMessagebox import CTkMessagebox




class InscriptionGui:

    def __init__(self, right_dashboard):
        self.idLabel = ctk.CTkLabel(right_dashboard, text="ID Inscription")
        self.idLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.idEntry = ctk.CTkEntry(right_dashboard, placeholder_text="I00001")
        self.idEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.anneeLabel = ctk.CTkLabel(right_dashboard, text="Année universitaire")
        self.anneeLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.anneeEntry = ctk.CTkEntry(right_dashboard, placeholder_text="2022-2023")
        self.anneeEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.niveauLabel = ctk.CTkLabel(right_dashboard, text="Niveau")
        self.niveauLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.niveauEntry = ctk.CTkEntry(right_dashboard, placeholder_text="Licence 3")
        self.niveauEntry.grid(row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.diplomeLabel = ctk.CTkLabel(right_dashboard, text="Diplôme")
        self.diplomeLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.diplomeEntry = ctk.CTkEntry(right_dashboard, placeholder_text="Informatique")
        self.diplomeEntry.grid(row=3, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.filLabel = ctk.CTkLabel(right_dashboard, text="ID Filière")
        self.filLabel.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        self.filEntry = ctk.CTkEntry(right_dashboard, placeholder_text="F00001")
        self.filEntry.grid(row=4, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.etuLabel = ctk.CTkLabel(right_dashboard, text="ID Etudiant")
        self.etuLabel.grid(row=5, column=0, padx=20, pady=20, sticky="ew")

        self.etuEntry = ctk.CTkEntry(right_dashboard, placeholder_text="E00001")
        self.etuEntry.grid(row=5, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.bt_inscription = ctk.CTkButton(right_dashboard, text="Ajouter Inscription", command=self.insert_etudiant)
        self.bt_inscription.grid(row=6, column=4, padx=20, pady=10)

        self.bt_upload = ctk.CTkButton(right_dashboard, text="Upload Fichier CSV", command=self.upload_csv)
        self.bt_upload.grid(row=6, column=3, padx=20, pady=10)




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
