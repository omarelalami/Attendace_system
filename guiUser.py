import customtkinter
import tkinter

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("Dark")
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("small example app")
        self.minsize(300, 200)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="Insert Etudiant")
        self.button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        self.textbox.insert("insert", self.combobox.get() + "\n")

