import csv

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PyQt5 import Qt

from model_ecole.modelEcole import *


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

        self.bt_inscription = ctk.CTkButton(right_dashboard, text="Ajouter Inscription", command=self.insert_inscription)
        self.bt_inscription.grid(row=6, column=4, padx=20, pady=10)

        self.bt_upload = ctk.CTkButton(right_dashboard, text="Upload Fichier CSV", command=self.upload_csv)
        self.bt_upload.grid(row=6, column=3, padx=20, pady=10)

    def insert_inscription (self):
        try:
            # Check if all input fields are non-empty
            if not all ((
                        self.idEntry.get (), self.anneeEntry.get (), self.niveauEntry.get (),
                        self.diplomeEntry.get (), self.filEntry.get (), self.etuEntry.get ())):
                raise ValueError ("Tous les champs doivent être remplis.")

            # Open database connection and insert new inscription
            db = MySQLDatabase ('localhost', 'root', '', 'si_presence')
            inscription = Inscription (self.idEntry.get (), self.anneeEntry.get (),
                                       self.niveauEntry.get (), self.diplomeEntry.get (), self.filEntry.get (),
                                       self.etuEntry.get ())
            db.insert_inscription (inscription)
            db.close_connection ()

            # Show success message
            CTkMessagebox (title="Succès", message="Opération effectuée avec succès.", icon="info", option_1="OK")
        except ValueError as e:
            # Show error message for invalid input
            CTkMessagebox (title="Erreur", message=str (e), icon="cancel", option_1="OK")
        except Exception as e:
            # Show error message for other exceptions
            CTkMessagebox (title="Erreur", message="Une erreur s'est produite : " + str (e), icon="cancel",
                           option_1="OK")

    def upload_csv (self):
        """
        Displays a file dialog to choose a CSV file and inserts the data into the database.
        """
        try:
            app = Qt.QApplication ([])
            file_path, _ = Qt.QFileDialog.getOpenFileName (None, 'Open CSV File', '', 'CSV Files (*.csv)')

            if not file_path:
                raise ValueError ('No file selected.')

            db = MySQLDatabase ('localhost', 'root', '', 'si_presence')

            with open (file_path, 'r') as csvfile:
                reader = csv.reader (csvfile)
                next (reader)  # Skip the header row
                for row in reader:
                    id_inscription = row [0]
                    annee_universitaires = row [1]
                    niveau = row [2]
                    diplome = row [3]
                    id_fil = row [4]
                    id_etu = row [5]

                    inscription = Inscription (id_inscription, annee_universitaires, niveau, diplome, id_fil, id_etu)
                    db.insert_inscription (inscription)
                    print (inscription)

                CTkMessagebox (title='Success', message='Operation effectuée avec succès.', icon='check', option_1='OK')

        except ValueError as e:
            CTkMessagebox (title='Error', message=str (e), icon='cancel', option_1='OK')

        except Exception as e:
            CTkMessagebox (title='Error', message='Une erreur est survenue: {}'.format (str (e)), icon='cancel',
                           option_1='OK')

        finally:
            if db is not None:
                db.close_connection ()
