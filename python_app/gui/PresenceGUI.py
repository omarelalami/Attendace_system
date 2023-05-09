import csv

import customtkinter as customtkinter
from CTkMessagebox import CTkMessagebox
from PyQt5 import Qt
import tkinter.ttk as ttk
from model_ecole.modelEcole import Etudiant, MySQLDatabase


class PresenceGUI:

    def __init__(self,right_dashboard):


        self.idLabel = customtkinter.CTkLabel(right_dashboard, text="ID Filiere")
        self.idLabel.place(x=25, y=100)
        lis=self.getFiliere()
        self.combobox1 = customtkinter.CTkComboBox(master=right_dashboard,
                                             values=lis,command=self.ForMatiere)
        self.combobox1.place(x=90,y=100)

        self.idLabel = customtkinter.CTkLabel(right_dashboard, text="ID Filiere")
        self.idLabel.place(x=250, y=100)

        self.combobox2 = customtkinter.CTkComboBox(master=right_dashboard,
                                              values=["option 1", "option 2"],state='disabled')
        self.combobox2.place(x=315, y=100)

        self.idLabel = customtkinter.CTkLabel(right_dashboard, text="ID Filiere")
        self.idLabel.place(x=475, y=100)

        self.combobox3 = customtkinter.CTkComboBox(master=right_dashboard,
                                              values=["option 1", "option 2"])
        self.combobox3.place(x=550, y=100)




        self.bt_upload = customtkinter.CTkButton(right_dashboard, text="Go", command=self.getFiliere)
        self.bt_upload.place(x=710, y=100)

        self.bt_upload = customtkinter.CTkButton(right_dashboard, text="Générer un fichier", command=self.getFiliere)
        self.bt_upload.place(x=870, y=100)






        # create a custom style for the table
        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])

        # create the table
        columns = ('id', 'Nom', 'Prenom', 'Filière','Matière','Séance','Statut')

        # create a frame to hold the table and the scrollbar
        table_frame = ttk.Frame(master=right_dashboard)
        table_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=190)

        # create the table
        table = ttk.Treeview(master=table_frame, columns=columns, height=30, selectmode='browse', show='headings')
        table.column("#1", anchor="c", minwidth=50, width=170)
        table.column("#2", anchor="c", minwidth=220, width=170)
        table.column("#3", anchor="c", minwidth=120, width=170)
        table.column("#4", anchor="c", minwidth=120, width=170)
        table.column("#5", anchor="c", minwidth=120, width=170)
        table.column("#6", anchor="c", minwidth=120, width=170)

        table.heading('id', text='id')
        table.heading('Nom', text='Nom')
        table.heading('Prenom', text='Prenom')
        table.heading('Filière', text='Filière')
        table.heading('Matière', text='Matière')
        table.heading('Statut', text='Statut')

        table.grid(row=0, column=0, sticky='nsew')

        # create a vertical scrollbar for the table
        ctk_textbox_scrollbar = customtkinter.CTkScrollbar(table_frame, command=table.yview)
        ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

        # configure the table to use the scrollbar
        table.configure(yscrollcommand=ctk_textbox_scrollbar.set)

        for i in range(100):
            id = i + 1
            item = f"Item {id}"
            date_added = "2022-05-07"
            date_of_manufacture = "2022-01-01"
            # insert a new item at index 0 under the root item
            table.insert("", 0, values=(id, item, date_added, date_of_manufacture))

        # bind the table
        table.bind('<Motion>', 'break')
        self.ForMatiere()

    def getFiliere (self):

        db = MySQLDatabase('localhost', 'root', '', 'si_presence')
        listFiliere=db.getAllFiliere()
        return listFiliere


    def ForMatiere(self):
        self.combobox2.configure(state='disabled')
        lis=self.getFiliere()
        self.combobox2.configure(state='normal',values=lis)







