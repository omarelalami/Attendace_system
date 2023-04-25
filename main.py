# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDialog, QFormLayout, QLabel, QLineEdit, QFileDialog,QMessageBox
# import mysql.connector
# from PyQt5.QtGui import QPixmap
# import csv
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         # Set up the main window
#         self.setWindowTitle('Face Recognition System')
#         self.setGeometry(300, 400, 1000, 1000)  # Set window dimensions
#         self.setFixedSize(800, 600)  # Fix window dimensions
#
#         # Create a vertical layout for the main window
#         layout = QVBoxLayout()
#
#         # Add logo image
#         logo_label = QLabel()
#         pixmap = QPixmap('./JO.PNG')  # Replace 'logo.png' with the path to your logo image
#         logo_label.setPixmap(pixmap.scaledToWidth(800))  # Scale the image to a width of 200 pixels
#         layout.addWidget(logo_label)
#
#         # Create a "Insert Filière" button
#         btn_insert_filiere = QPushButton('Insert Filière', self)
#         btn_insert_filiere.clicked.connect(self.open_insert_filiere_dialog)
#         layout.addWidget(btn_insert_filiere)
#
#         # Create a "Insert student" button
#         btn_insert_student = QPushButton('Insert Student', self)
#         btn_insert_student.clicked.connect(self.open_insert_student_dialog)
#         layout.addWidget(btn_insert_student)
#
#         # Create a "Insert student" button
#         btn_insert_matiere = QPushButton('Insert Matière', self)
#         btn_insert_matiere.clicked.connect(self.open_insert_student_dialog)
#         layout.addWidget(btn_insert_matiere)
#
#         # Create a "Insert student" button
#         btn_insert_seance = QPushButton('Insert Seance', self)
#         btn_insert_seance.clicked.connect(self.open_insert_student_dialog)
#         layout.addWidget(btn_insert_seance)
#
#
#
#         # Create a "Lancer la detection" button
#         btn_lancer_detection = QPushButton('Lancer La detection', self)
#         btn_insert_filiere.clicked.connect(self.open_insert_filiere_dialog)
#         layout.addWidget(btn_lancer_detection)
#
#
#         # Set the layout for the main window
#         self.setLayout(layout)
#
#     def open_insert_student_dialog(self):
#         # Open a new window for inserting student information
#         dialog = QDialog(self)
#         dialog.setWindowTitle('Insert Student Information')
#
#         # Create a form layout for the new window
#         form_layout = QFormLayout()
#
#         # Create labels and line edits for student information
#         lbl_id = QLabel('ID:')
#         le_id = QLineEdit()
#         form_layout.addRow(lbl_id, le_id)
#
#         lbl_nom = QLabel('Nom:')
#         le_nom = QLineEdit()
#         form_layout.addRow(lbl_nom, le_nom)
#
#         lbl_filiere_nom = QLabel('Filière Nom:')
#         le_filiere_nom = QLineEdit()
#         form_layout.addRow(lbl_filiere_nom, le_filiere_nom)
#
#         # Create a button for uploading CSV file
#         btn_upload_csv = QPushButton('Upload CSV')
#         btn_upload_csv.clicked.connect(self.upload_csv)
#         form_layout.addRow(btn_upload_csv)
#
#         # Create a button for inserting student information
#         btn_insert = QPushButton('Insert')
#         btn_insert.clicked.connect(lambda: self.insert_student(le_id.text(), le_nom.text(), le_filiere_nom.text()))
#         form_layout.addRow(btn_insert)
#
#         # Set the form layout for the new window
#         dialog.setLayout(form_layout)
#
#         # Show the new window
#         dialog.exec_()
#
#     def open_insert_filiere_dialog(self):
#         # Open a new window for inserting filière information
#         dialog = QDialog(self)
#         dialog.setWindowTitle('Insert Filière Information')
#
#         # Create a form layout for the new window
#         form_layout = QFormLayout()
#
#         # Create labels and line edits for filière information
#         lbl_id = QLabel('ID:')
#         le_id = QLineEdit()
#         form_layout.addRow(lbl_id, le_id)
#
#         lbl_nom = QLabel('Nom:')
#         le_nom = QLineEdit()
#         form_layout.addRow(lbl_nom, le_nom)
#
#         lbl_id_etudiant = QLabel('ID Étudiant:')
#         le_id_etudiant = QLineEdit()
#         form_layout.addRow(lbl_id_etudiant, le_id_etudiant)
#
#         lbl_id_matiere = QLabel('ID Matière:')
#         le_id_matiere = QLineEdit()
#         form_layout.addRow(lbl_id_matiere, le_id_matiere)
#
#         # Create a button for inserting filière information
#         btn_insert = QPushButton('Insert')
#         btn_insert.clicked.connect(
#             lambda: self.insert_filiere(le_id.text(), le_nom.text(), le_id_etudiant.text(), le_id_matiere.text()))
#         form_layout.addRow(btn_insert)
#
#         # Set the form layout for the new window
#         dialog.setLayout(form_layout)
#
#         # Show the new window
#         dialog.exec_()
#
#     def upload_csv(self):
#         # Open a file dialog to choose a CSV file
#         file_path, _ = QFileDialog.getOpenFileName(self, 'Open CSV File', '', 'CSV Files (*.csv)')
#
#         # Read the CSV file and insert students into the database
#         if file_path:
#             with open(file_path, 'r') as csvfile:
#                 reader = csv.reader(csvfile)
#                 next(reader)  # Skip the header row
#                 for row in reader:
#                     id = row[0]
#                     nom = row[1]
#                     filiere_nom = row[2]
#                     self.insert_student(id, nom, filiere_nom)
#
#     def insert_student(self, id, nom, filiere_nom):
#         # Insert student information into the database
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='',
#             database='si_presence'
#         )
#         cursor = conn.cursor()
#
#         # Insert the student into the database
#         query = "INSERT INTO etudiant (id_e, nom, filiere_nom) VALUES (%s, %s, %s)"
#         values = (id, nom, filiere_nom)
#         cursor.execute(query, values)
#
#         # Commit the transaction and close the connection
#         conn.commit()
#         cursor.close()
#         conn.close()
#
#         # Show a message box indicating successful insertion
#         QMessageBox.information(self, 'Success', 'Student information inserted successfully!')
#
#     def insert_filiere(self, id, nom, id_etudiant, id_m):
#         # Insert filière information into the database
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='',
#             database='si_presence'
#         )
#         cursor = conn.cursor()
#
#         # Insert the filière into the database
#         query = "INSERT INTO filiere (id_f, nom, id_etudiant, id_m) VALUES (%s, %s, %s, %s)"
#         values = (id, nom, id_etudiant, id_m)
#         cursor.execute(query, values)
#
#         # Commit the transaction and close the connection
#         conn.commit()
#         cursor.close()
#         conn.close()
#
#         # Show a message box indicating successful insertion
#         QMessageBox.information(self, 'Success', 'Filière information inserted successfully!')
#
#
# # Create the PyQt application
# app = QApplication(sys.argv)
#
# # Create the main window
# window = MainWindow()
# window.show()
#
# # Run the PyQt event loop
# sys.exit(app.exec_())
#
#
#
#
#
#
