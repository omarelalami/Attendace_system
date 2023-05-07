import csv

import customtkinter as customtkinter
from CTkMessagebox import CTkMessagebox
from PyQt5 import Qt
import tkinter as tk
from model_ecole.modelEcole import Etudiant, MySQLDatabase


class EtudiantGui:

    def __init__(self,right_dashboard):

        headers2 = ['#', 'Name']
        _tree = tk.ttk.Treeview(master=right_dashboard, height=25, columns=headers2, show='headings')
        _tree.heading('#', text='#')
        _tree.heading('Name', text='Name')
        _tree.pack()
        cursor = ((u"1", u"Name A"),
                  (u"2", u"Name B"))
        for row in cursor:
            _tree.insert('', 'end', values=row)
            for i, item in enumerate(row):
                _tree.column(headers2 [i], width=col_width, anchor=tk.CENTER)


    def insert_etudiant (self):


        try:
            # Check if all input fields are non-empty
            if not all (
                    (self.idEntry.get (), self.prenomEntry.get (), self.nomEntry.get (), self.NaissanceEntry.get ())):
                raise ValueError ("Tous les champs doivent être remplis.")
            db = MySQLDatabase('localhost', 'root', '', 'si_presence')
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
        db=None
        try:
            app = Qt.QApplication ([])
            file_path, _ = Qt.QFileDialog.getOpenFileName (None, 'Open CSV File', '', 'CSV Files (*.csv)')

            if not file_path:
                raise ValueError ('No file selected.')

            db = MySQLDatabase('localhost', 'root', '', 'si_presence')


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

