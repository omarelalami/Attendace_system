import customtkinter as ctk
import csv
from modelEcole import Etudiant,MySQLDatabase
from PyQt5 import Qt
from CTkMessagebox import CTkMessagebox


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


        self.idMatiereEntryLabel = ctk.CTkLabel (right_dashboard, text="ID Seance")
        self.idMatiereEntryLabel.grid (row=1, column=4, padx=20, pady=20, sticky="ew")

        self.idMatiereEntry = ctk.CTkEntry(right_dashboard, placeholder_text="ID000")
        self.idMatiereEntry.grid(row=1, column=5, columnspan=3, padx=20, pady=20, sticky="ew")

        self.bt_seance = ctk.CTkButton(right_dashboard, text="Ajouter Seance", command=self.insert_seance)
        self.bt_seance.grid(row=6, column=4, padx=20, pady=10)

        self.bt_upload = ctk.CTkButton(right_dashboard, text="Upload Fichier CSV", command=self.upload_csv)
        self.bt_upload.grid(row=6, column=3, padx=20, pady=10)

    def insert_seance(self):
        id_seance = self.idEntry.get()
        date_seance = self.dateEntry.get()
        heure_debut = self.heureDebutEntry.get()
        heure_fin = self.heureFinEntry.get()
        # TODO: Insert the seance data into the database
        print(f"Seance {id_seance} added to the database.")

    def upload_csv(self):
        # TODO: Implement CSV file upload functionality
        print("CSV file uploaded.")
