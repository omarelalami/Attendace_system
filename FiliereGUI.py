import customtkinter as ctk
import csv
from modelEcole import Etudiant,MySQLDatabase
from PyQt5 import Qt
from CTkMessagebox import CTkMessagebox

class FiliereGui:

    def __init__(self, right_dashboard):
        self.idLabel = ctk.CTkLabel(right_dashboard, text="ID Filiere")
        self.idLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.idEntry = ctk.CTkEntry(right_dashboard, placeholder_text="F01")
        self.idEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.nomLabel = ctk.CTkLabel(right_dashboard, text="Nom Filiere")
        self.nomLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.nomEntry = ctk.CTkEntry(right_dashboard, placeholder_text="Informatique")
        self.nomEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.bt_filiere = ctk.CTkButton(right_dashboard, text="Ajouter Filiere", command=self.insert_filiere)
        self.bt_filiere.grid(row=6, column=4, padx=20, pady=10)

        self.bt_upload = ctk.CTkButton (right_dashboard, text="Upload Fichier CSV", command=self.upload_csv)

        self.bt_upload.grid (row=6, column=3, padx=20, pady=10)

    def insert_filiere(self):
        pass
    def upload_csv(self):
        pass