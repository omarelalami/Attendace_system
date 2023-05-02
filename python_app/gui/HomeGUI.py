import threading
import tkinter

import customtkinter

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")
import gui.EdudiantGUI as et
import gui.InscriptionGUI as ins
import gui.FiliereGUI as fil
import gui.SeanceGui as sea
import gui.MatiereGUI as mat
from reco_model.Model_Recognition import AttendanceSystem


class HomeGUI(customtkinter.CTk):


    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.title("Change Frames")

        # remove title bar , page reducer and closing page !!!most have a quit button with app.destroy!!! (this app have a quit button so don't worry about that)

        # make the app as big as the screen (no mater wich screen you use)

        # root!
        self.main_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        self.left_side_panel = customtkinter.CTkFrame(self.main_container, width=150, corner_radius=10)
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)

        self.left_side_panel.grid_columnconfigure(0, weight=1)
        self.left_side_panel.grid_rowconfigure((0, 1, 2, 3,4,5), weight=0)
        self.left_side_panel.grid_rowconfigure((8,9), weight=2)
        self.left_side_panel.grid_rowconfigure((10, 11), weight=1)

        # self.left_side_panel WIDGET
        self.logo_label = customtkinter.CTkLabel(self.left_side_panel, text="Attendance System\n",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))



        self.bt_Quit = customtkinter.CTkButton(self.left_side_panel, text="Quit", fg_color='#EA0000', hover_color='#B20000',command=self.close_window)
        self.bt_Quit.grid(row=9, column=0, padx=20, pady=10)
 



        # button to select correct frame IN self.left_side_panel WIDGET
        self.bt_etudiant = customtkinter.CTkButton(self.left_side_panel, text="Ajouter Etudiant", command=self.GoEtudiant)

        self.bt_etudiant.grid(row=1, column=0, padx=20, pady=10)

        self.bt_inscription = customtkinter.CTkButton(self.left_side_panel, text="Inscription", command=self.GoInscription)
        self.bt_inscription.grid(row=2, column=0, padx=20, pady=10)

        self.bt_matiere = customtkinter.CTkButton(self.left_side_panel, text="Ajouter Matière",
                                                     command=self.GoMatiere)
        self.bt_matiere.grid(row=3, column=0, padx=20, pady=10)



        self.bt_filiere = customtkinter.CTkButton(self.left_side_panel, text="Ajouter Filière",
                                                     command=self.GoFiliere)
        self.bt_filiere.grid(row=4, column=0, padx=20, pady=10)

        self.bt_seance = customtkinter.CTkButton (self.left_side_panel, text="Ajouter Séance",
                                                  command=self.GoSeance)
        self.bt_seance.grid (row=5, column=0, padx=20, pady=10)

        self.bt_presence = customtkinter.CTkButton(self.left_side_panel, text="Liste De Presence",
                                                     command=self.categories)
        self.bt_presence.grid(row=6, column=0, padx=20, pady=10)

        self.bt_lancer = customtkinter.CTkButton(self.left_side_panel, text="Lancer la detection",
                                                 command=self.reco_with_progress_bar,width=170,height=50,border_width=1,fg_color="#515A5A",hover_color='#424949')

        self.bt_lancer.grid(row=8, column=0, padx=20, pady=10)

        # right side panel -> have self.right_dashboard inside it
        self.right_side_panel = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)

        self.right_dashboard = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#23242A")
        self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0,
                                  pady=0)


    #  self.right_dashboard   ----> dashboard widget
    def GoEtudiant(self):
        self.clear_frame()

        et.EtudiantGui(self.right_dashboard)

    def GoInscription(self):
        self.clear_frame()
        ins.InscriptionGui(self.right_dashboard)

    def GoFiliere(self):
        self.clear_frame()
        fil.FiliereGui(self.right_dashboard)

    def GoSeance(self):
        self.clear_frame()
        sea.SeanceGui(self.right_dashboard)

    def GoMatiere(self):
        self.clear_frame()
        mat.MatiereGui(self.right_dashboard)
    # close the entire window
    def close_window(self):
        HomeGUI.destroy(self)






    # CLEAR ALL THE WIDGET FROM self.right_dashboard(frame) BEFORE loading the widget of the concerned page
    def clear_frame(self):
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()


    def statement(self):
        pass
    def categories(self):
        pass

    def reco_with_progress_bar(self):
        self.bt_lancer.configure(state="disabled")
        self.clear_frame()


        def reco_thread():
            attendanceSystem = AttendanceSystem()
            attendanceSystem.start_attendance_system(self.right_dashboard)
            self.bt_lancer.configure(state="normal")

            # Once the reco is finished, stop the progress bar and destroy it


        # Start the reco in a separate thread
        reco_thread = threading.Thread(target=reco_thread)
        reco_thread.start()







