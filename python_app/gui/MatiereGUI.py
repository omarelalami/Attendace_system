import csv

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PyQt5 import Qt

from model_ecole.modelEcole import *


class MatiereGui:

    def __init__(self, right_dashboard):
        self.idLabel = ctk.CTkLabel(right_dashboard, text="ID Matiere")
        self.idLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.idEntry = ctk.CTkEntry(right_dashboard, placeholder_text="F01")
        self.idEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.nomLabel = ctk.CTkLabel(right_dashboard, text="Nom Mariere")
        self.nomLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.nomEntry = ctk.CTkEntry(right_dashboard, placeholder_text="Oracle")
        self.nomEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.bt_filiere = ctk.CTkButton(right_dashboard, text="Ajouter Matiere", command=self.insert_matiere)
        self.bt_filiere.grid(row=6, column=4, padx=20, pady=10)

        self.bt_upload = ctk.CTkButton (right_dashboard, text="Upload Fichier CSV", command=self.upload_csv)

        self.bt_upload.grid (row=6, column=3, padx=20, pady=10)

    def insert_matiere (self):
        try:
            # Check if all input fields are non-empty
            if not all ((self.idEntry.get (), self.nomEntry.get ())):
                raise ValueError ("Tous les champs doivent être remplis.")

            # Open database connection and insert new matiere
            db = MySQLDatabase ('localhost', 'root', '', 'si_presence')
            matiere = Matiere (self.idEntry.get (), self.nomEntry.get ())
            db.insert_matiere (matiere)
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

    def upload_csv(self):
        """
        Displays a file dialog to choose a CSV file and inserts the data into the database.
        """
        db = MySQLDatabase ('localhost', 'root', '', 'si_presence')
        try:
            app = Qt.QApplication([])
            file_path, _ = Qt.QFileDialog.getOpenFileName(None, 'Open CSV File', '', 'CSV Files (*.csv)')

            if not file_path:
                raise ValueError('No file selected.')



            with open(file_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    id_matiere = row[0]
                    nom_matiere = row[1]

                    matiere = Matiere(id_matiere, nom_matiere)
                    db.insert_matiere(matiere)
                    print(matiere)

            CTkMessagebox(title='Success', message='Operation effectuée avec succès.', icon='check', option_1='OK')

        except ValueError as e:
            CTkMessagebox(title='Error', message=str(e), icon='cancel', option_1='OK')

        except Exception as e:
            CTkMessagebox(title='Error', message='Une erreur est survenue: {}'.format(str(e)), icon='cancel',
                           option_1='OK')

        finally:
            if db is not None:
                db.close_connection()