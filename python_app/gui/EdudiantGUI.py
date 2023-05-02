import csv

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PyQt5 import Qt

from model_ecole.modelEcole import Etudiant, MySQLDatabase


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

        db = MySQLDatabase ('localhost', 'root', '', 'si_presence')
        try:
            # Check if all input fields are non-empty
            if not all (
                    (self.idEntry.get (), self.prenomEntry.get (), self.nomEntry.get (), self.NaissanceEntry.get ())):
                raise ValueError ("Tous les champs doivent être remplis.")

            # Open database connection and insert new student

            etudiant = Etudiant (self.idEntry.get (), self.prenomEntry.get (), self.nomEntry.get (),
                                 self.NaissanceEntry.get ())
            db.insert_etudiant (etudiant)
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
        db = MySQLDatabase ('localhost', 'root', '', 'si_presence')
        try:
            app = Qt.QApplication ([])
            file_path, _ = Qt.QFileDialog.getOpenFileName (None, 'Open CSV File', '', 'CSV Files (*.csv)')

            if not file_path:
                raise ValueError ('No file selected.')




            with open (file_path, 'r') as csvfile:
                reader = csv.reader (csvfile)
                next (reader)  # Skip the header row
                for row in reader:
                    id = row [0]
                    prenom = row [1]
                    nom = row [2]
                    date_naissance = row [3]

                    etudiant = Etudiant (id, prenom, nom, date_naissance)
                    db.insert_etudiant (etudiant)
                    print (etudiant)

                CTkMessagebox (title='Success', message='Operation effectuée avec succès.', icon='check', option_1='OK')


        except ValueError as e:
            CTkMessagebox (title='Error', message=str (e), icon='cancel', option_1='OK')

        except Exception as e:
            CTkMessagebox (title='Error', message='Une erreur est survenue: {}'.format (str (e)), icon='cancel',
                           option_1='OK')

        finally:
            if db is not None:
                db.close_connection ()

