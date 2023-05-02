import csv

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PyQt5 import Qt

from model_ecole.modelEcole import Seance, MySQLDatabase, Gerer


class SeanceGui:

    def __init__(self, right_dashboard):
        self.idLabel = ctk.CTkLabel(right_dashboard, text="ID Seance")
        self.idLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.idEntry = ctk.CTkEntry(right_dashboard, placeholder_text="S1001")
        self.idEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.dateLabel = ctk.CTkLabel(right_dashboard, text="Date de la seance")
        self.dateLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.dateEntry = ctk.CTkEntry(right_dashboard, placeholder_text="04/01/2023")
        self.dateEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.heureDebutLabel = ctk.CTkLabel(right_dashboard, text="Heure de debut")
        self.heureDebutLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.heureDebutEntry = ctk.CTkEntry(right_dashboard, placeholder_text="09:00")
        self.heureDebutEntry.grid(row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.heureFinLabel = ctk.CTkLabel(right_dashboard, text="Heure de fin")
        self.heureFinLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.heureFinEntry = ctk.CTkEntry(right_dashboard, placeholder_text="12:00")
        self.heureFinEntry.grid(row=3, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.idFiliereEntryLabel = ctk.CTkLabel (right_dashboard, text="ID Filiere")
        self.idFiliereEntryLabel.grid (row=0, column=4, padx=20, pady=20, sticky="ew")

        self.idFiliereEntry = ctk.CTkEntry(right_dashboard, placeholder_text="ID000")
        self.idFiliereEntry.grid(row=0, column=5, columnspan=3, padx=20, pady=20, sticky="ew")


        self.idMatiereEntryLabel = ctk.CTkLabel (right_dashboard, text="ID Matiere")
        self.idMatiereEntryLabel.grid (row=1, column=4, padx=20, pady=20, sticky="ew")

        self.idMatiereEntry = ctk.CTkEntry(right_dashboard, placeholder_text="ID000")
        self.idMatiereEntry.grid(row=1, column=5, columnspan=3, padx=20, pady=20, sticky="ew")

        self.bt_seance = ctk.CTkButton(right_dashboard, text="Ajouter Seance", command=self.insert_seance)
        self.bt_seance.grid(row=6, column=4, padx=20, pady=10)

        self.bt_upload = ctk.CTkButton(right_dashboard, text="Upload Fichier CSV", command=self.upload_csv)
        self.bt_upload.grid(row=6, column=3, padx=20, pady=10)

    def insert_seance (self):
        try:
            # Check if all input fields are non-empty
            if not all ((self.idEntry.get(), self.dateEntry.get(), self.heureDebutEntry.get(), self.heureFinEntry.get(), self.idMatiereEntry.get(),
                         self.idFiliereEntry.get())):
                raise ValueError ("Tous les champs doivent être remplis.")

            # Open database connection and insert new seance
            db = MySQLDatabase ('localhost', 'root', '', 'si_presence')
            seance = Seance(self.idEntry.get(), self.dateEntry.get(), self.heureDebutEntry.get(), self.heureFinEntry.get())
            gerer=Gerer(self.idMatiereEntry.get(),self.idFiliereEntry.get(),self.idEntry.get())
            db.insert_seance (seance)
            db.insert_gerer(gerer)

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


        # TODO: Insert the seance data into the database

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

                    idSe = row [0]
                    date = row [1]
                    heureD = row [2]
                    heureF = row [3]
                    idF  = row [4]
                    idM=row[5]

                    seance = Seance (idSe,date,heureD,heureF)
                    gerer = Gerer (idM, idF, idSe)
                    db.insert_seance (seance)
                    db.insert_gerer (gerer)


                CTkMessagebox (title='Success', message='Operation effectuée avec succès.', icon='check', option_1='OK')

        except ValueError as e:
            CTkMessagebox (title='Error', message=str (e), icon='cancel', option_1='OK')

        except Exception as e:
            CTkMessagebox (title='Error', message='Une erreur est survenue: {}'.format (str (e)), icon='cancel',
                           option_1='OK')

        finally:
            if db is not None:
                db.close_connection ()

