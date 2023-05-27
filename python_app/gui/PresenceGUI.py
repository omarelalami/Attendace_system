import csv
from tkinter import filedialog
import customtkinter as customtkinter
from CTkMessagebox import CTkMessagebox
from PyQt5 import Qt
import tkinter.ttk as ttk
from model_ecole.modelEcole import Etudiant, MySQLDatabase
import pandas as pd

class PresenceGUI:

    def __init__(self,right_dashboard):


        self.idLabel = customtkinter.CTkLabel(right_dashboard, text="Nom Filère")
        self.idLabel.place(x=22, y=100)
        lis=self.getFiliere()
        self.combobox1 = customtkinter.CTkComboBox(master=right_dashboard,
                                             values=lis,command=self.ForMatiere)
        self.combobox1.place(x=90,y=100)

        self.idLabel1 = customtkinter.CTkLabel(right_dashboard, text="Nom Matière")
        self.idLabel1.place(x=238, y=100)


        self.combobox2 = customtkinter.CTkComboBox(master=right_dashboard,
                                              values=["option 1", "option 2"],state='disabled',command=self.ForSeance)
        self.combobox2.place(x=320, y=100)

        self.idLabel2 = customtkinter.CTkLabel(right_dashboard, text="Date Séance")
        self.idLabel2.place(x=468, y=100)

        self.combobox3 = customtkinter.CTkComboBox(master=right_dashboard,state='disabled',command=self.ForBtn)
        self.combobox3.place(x=548, y=100)




        self.go_btn= customtkinter.CTkButton(right_dashboard, text="Go", command=self.GoResult,state='disabled')
        self.go_btn.place(x=700, y=100)

        self.download_btn = customtkinter.CTkButton(right_dashboard, text="Générer un fichier", command=self.export_data_to_csv,state='disabled')
        self.download_btn.place(x=845, y=100)






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
        table_frame.grid(row=0, column=0, sticky='nsew', padx=15, pady=190)

        # create the table
        self.table = ttk.Treeview(master=table_frame, columns=columns, height=30, selectmode='browse', show='headings')
        self.table.column("#1", anchor="c", minwidth=50, width=170)
        self.table.column("#2", anchor="c", minwidth=120, width=170)
        self.table.column("#3", anchor="c", minwidth=120, width=170)
        self.table.column("#4", anchor="c", minwidth=120, width=170)
        self.table.column("#5", anchor="c", minwidth=120, width=170)
        self.table.column("#6", anchor="e", minwidth=120, width=170)



        self.table.heading('id', text='id')
        self.table.heading('Nom', text='Nom')
        self.table.heading('Prenom', text='Prenom')
        self.table.heading('Filière', text='Filière')
        self.table.heading('Matière', text='Matière')
        self.table.heading('Statut', text='Statut',anchor='w')



        self.table.grid(row=0, column=0, sticky='nsew')

        # create a vertical scrollbar for the table
        ctk_textbox_scrollbar = customtkinter.CTkScrollbar(table_frame, command=self.table.yview)
        ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

        # configure the table to use the scrollbar
        self.table.configure(yscrollcommand=ctk_textbox_scrollbar.set)

    def getFiliere (self):

        db = MySQLDatabase('localhost', 'root', '', 'si_presence')
        listFiliere=db.getAllFiliere()
        return listFiliere


    def ForMatiere(self,event):
        self.combobox1.configure(state='disabled')
        db = MySQLDatabase('localhost', 'root', '', 'si_presence')
        lis=db.getMatiere(str(self.combobox1.get()))
        self.combobox2.configure(state='normal',values=lis)



    def ForSeance(self,event):
        self.combobox3.configure(state='normal')
        self.combobox2.configure(state='disabled')
        db = MySQLDatabase('localhost', 'root', '', 'si_presence')

        lis=db.getSeance(str(self.combobox2.get()),str(self.combobox1.get()))


        self.combobox3.configure(values=lis)
    def ForBtn(self,event):
        self.go_btn.configure(state='normal')
        self.download_btn.configure(state='normal')



    def GoResult(self):
        self.table.delete(*self.table.get_children())
        db = MySQLDatabase('localhost', 'root', '', 'si_presence')
        res=str(self.combobox3.get()).split("|")
        resu=res[1].split("-")
        heure_debut = resu[0].replace(" ", "")
        heure_fin=resu[1].replace(" ","")

        result=db.get_presence_data(str(self.combobox2.get()),str(self.combobox1.get()),res[0],heure_debut,heure_fin)

        for i in result:

            id = i[0]
            nom = i[1]
            prenom = i[2]
            filiere=self.combobox1.get()
            matiere=self.combobox2.get()
            statut=i[3]

            # insert a new item at index 0 under the root item
            self.table.insert("", 0, values=(id, nom, prenom, filiere,matiere,statut))

        # bind the table
        self.table.bind('<Motion>', 'break')



    def export_data_to_csv(self):
        db = MySQLDatabase('localhost', 'root', '', 'si_presence')
        res=str(self.combobox3.get()).split("|")
        resu=res[1].split("-")
        heure_debut = resu[0].replace(" ", "")
        heure_fin=resu[1].replace(" ","")
        result = db.get_presence_data(str(self.combobox2.get()),str(self.combobox1.get()),res[0],heure_debut,heure_fin)
        result1 = []
        for i in result:
            id = i [0]
            nom = i [1]
            prenom = i [2]
            filiere = self.combobox1.get()
            matiere = self.combobox2.get()
            statut = i [3]
            result1.append((id, nom, prenom, filiere, matiere, statut))

        # Convert result set to a pandas DataFrame
        df = pd.DataFrame(result1)

        # Open a file dialog window to choose file path and name
        file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                                 filetypes=[('Excel files', '*.xlsx')])

        # Export data to chosen file path and name
        df.to_excel(file_path, index=False, header=['id_etudiant', 'nom', 'prenom', 'filiere', 'matiere', 'statut'])




