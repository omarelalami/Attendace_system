import customtkinter as ctk
import csv
from modelEcole import Etudiant,MySQLDatabase
from PyQt5 import Qt
from CTkMessagebox import CTkMessagebox

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

    def insert_matiere(self):
        pass
    def upload_csv(self):
        pass