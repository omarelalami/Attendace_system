import tkinter
import customtkinter

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")
import EdudiantGUI as ts
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
        self.bt_etudiant = customtkinter.CTkButton(self.left_side_panel, text="Ajouter Etudiant", command=self.ok)

        self.bt_etudiant.grid(row=1, column=0, padx=20, pady=10)

        self.bt_inscription = customtkinter.CTkButton(self.left_side_panel, text="Inscription", command=self.statement)
        self.bt_inscription.grid(row=2, column=0, padx=20, pady=10)

        self.bt_matiere = customtkinter.CTkButton(self.left_side_panel, text="Ajouter Matière",
                                                     command=self.categories)
        self.bt_matiere.grid(row=3, column=0, padx=20, pady=10)


        self.bt_filiere = customtkinter.CTkButton(self.left_side_panel, text="Ajouter Filière",
                                                     command=self.categories)
        self.bt_filiere.grid(row=4, column=0, padx=20, pady=10)


        self.bt_presence = customtkinter.CTkButton(self.left_side_panel, text="Liste De Presence",
                                                     command=self.categories)
        self.bt_presence.grid(row=5, column=0, padx=20, pady=10)

        # right side panel -> have self.right_dashboard inside it
        self.right_side_panel = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)

        self.right_dashboard = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0,
                                  pady=0)


    #  self.right_dashboard   ----> dashboard widget
    def ok(self):
        self.clear_frame()
        ts.ThemeEtudiant(self.right_dashboard)

    # close the entire window
    def close_window(self):
        App.destroy(self)


    # CLEAR ALL THE WIDGET FROM self.right_dashboard(frame) BEFORE loading the widget of the concerned page
    def clear_frame(self):
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()


    def statement(self):
        pass
    def categories(self):
        pass

