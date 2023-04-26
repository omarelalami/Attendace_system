import customtkinter as ctk
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDialog, QFormLayout, QLabel, QLineEdit, \
    QFileDialog, QMessageBox
import csv
import tkinter
import tkinter.messagebox as tkmb
def ThemeEtudiant(right_dashboard):

    idLabel = ctk.CTkLabel(right_dashboard,text="ID Etudiant")
    idLabel.grid(row=0, column=0, padx=20, pady=20,sticky="ew")

    nameEntry = ctk.CTkEntry(right_dashboard,placeholder_text="N1990909")
    nameEntry.grid(row=0, column=1,
                        columnspan=3, padx=20,
                        pady=20, sticky="ew")

    nameLabel = ctk.CTkLabel(right_dashboard,text="Name")
    nameLabel.grid(row=1, column=0, padx=20, pady=20,sticky="ew")

    # Name Entry Field
    nameEntry = ctk.CTkEntry(right_dashboard,placeholder_text="Omar")
    nameEntry.grid(row=1, column=1,
                        columnspan=3, padx=20,
                        pady=20, sticky="ew")

    # Age Label
    ageLabel = ctk.CTkLabel(right_dashboard,text="Prenom")
    ageLabel.grid(row=2, column=0,
                       padx=20, pady=20,
                       sticky="ew")

    # Age Entry Field
    ageEntry = ctk.CTkEntry(right_dashboard,placeholder_text="Elalami")
    ageEntry.grid(row=2, column=1,columnspan=3, padx=20,pady=20, sticky="ew")

    ageLabel = ctk.CTkLabel(right_dashboard,text="Prenom")
    ageLabel.grid(row=2, column=0,padx=20, pady=20,sticky="ew")

    #Naissance Label
    NaissanceLabel = ctk.CTkLabel(right_dashboard,text="Date de naissance")
    NaissanceLabel.grid(row=3, column=0,
                       padx=20, pady=20,
                       sticky="ew")

    # DateNaissance Entry Field
    NaissanceEntry = ctk.CTkEntry(right_dashboard,placeholder_text="04/01/2001")
    NaissanceEntry.grid(row=3, column=1,columnspan=3, padx=20,pady=20, sticky="ew")

    bt_etudiant = ctk.CTkButton(right_dashboard, text="Ajouter Etudiant", command=test)

    bt_etudiant.grid(row=6, column=4, padx=20, pady=10)
    bt_upload = ctk.CTkButton(right_dashboard, text="Upload Fichier CSV", command=upload_csv)

    bt_upload.grid(row=6, column=3, padx=20, pady=10)

from PyQt5 import Qt
def upload_csv():
    # Open a file dialog to choose a CSV file

         app = Qt.QApplication([])
         file_path,= Qt.QFileDialog.getOpenFileName(None,'Open CSV File', '', 'CSV Files (*.csv)')

         # Read the CSV file and insert students into the database
         if file_path:
             with open(file_path, 'r') as csvfile:
                 reader = csv.reader(csvfile)
                 next(reader)  # Skip the header row
                 for row in reader:
                     id = row[0]
                     nom = row[1]
                     filiere_nom = row[2]
from CTkMessagebox import CTkMessagebox
def test():
    CTkMessagebox(title="Good", message="Operation effectuer avec succes",icon="check", option_1="OK")

