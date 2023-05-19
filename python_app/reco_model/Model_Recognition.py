import os
from datetime import datetime

import customtkinter
import cv2
import face_recognition
import numpy as np
import threading
import winsound
from model_ecole.modelEcole import  MySQLDatabase

class AttendanceSystem:
    def __init__(self):

        self.classNames = []
        self.encoded_face_train = []
        self.path = 'student_images'
        self.attendance_file = 'Attendance_marked/Attendance.csv'
        self.db=MySQLDatabase('localhost', 'root', '', 'si_presence')

    def load_images(self):
        name=self.db.get_etudiant_byday()
        mylist = name
        for cl in mylist:
            curImg = cv2.imread(os.path.join(self.path, cl+ '.jpg'))
            self.classNames.append(os.path.splitext(cl)[0])
            curImg = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)
            encoded_face = face_recognition.face_encodings(curImg)[0]
            self.encoded_face_train.append(encoded_face)

    def mark_attendance(self, name):

            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            self.db.set_presence_data(date,time,name)
            print(time)


    def play_sound(self, wait=False):
        success_sound = r'C:\Attendance_system\Attendance_system\python_app\reco_model\success.wav'  # change to the path of your desired WAV sound file
        flags = winsound.SND_FILENAME
        if wait:
            flags = flags & ~winsound.SND_ASYNC
            winsound.PlaySound(success_sound,winsound.SND_FILENAME)

    def start_attendance_system(self,right_dashboard):
        sound_playing = False
        progressbar = customtkinter.CTkProgressBar(master=right_dashboard)
        progressbar.configure(mode="indeterminate",width=290,height=20)
        x = (right_dashboard.winfo_width() - progressbar.winfo_width()) / 2
        y = (right_dashboard.winfo_height() - progressbar.winfo_height()) / 2
        progressbar.place(x=x, y=y)
        progressbar.start()
        self.load_images()

        cap = cv2.VideoCapture(0)
        progressbar.stop()
        progressbar.destroy()

        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)

            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            faces_in_frame = face_recognition.face_locations(imgS)
            encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)



            for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
                matches = face_recognition.compare_faces(self.encoded_face_train, encode_face)
                faceDist = face_recognition.face_distance(self.encoded_face_train, encode_face)
                matchIndex = np.argmin(faceDist)
                if faceDist [matchIndex] <0.5:
                    name = self.classNames[matchIndex].upper().lower()
                    if  self.db.if_etudiant(name):
                        print(self.db.if_etudiant(name))
                        y1, x2, y2, x1 = faceloc
                        # since we scaled down by 4 times
                        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                        self.mark_attendance(name)

                        if not sound_playing:
                            sound_playing = True
                            self.play_sound(wait=True)
                            sound_playing = False


            cv2.imshow('webcam', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        return True



