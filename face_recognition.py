from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1352x790+0+0")
        self.root.title("Face Recognition System")

        # Label Aplikasi
        f_lbl = Label(self.root, bg="black")
        f_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        f_lbl = Label(self.root, text="Face Recognition", font=('arial', 30, 'bold'),
                      bd=4, relief=RIDGE, pady=10, padx=20, fg="white", bg="black")
        f_lbl.pack(side=TOP, pady=20, )

        # Background Aplikasi
        img2 = Image.open(r"images\bgimg.jpg")
        img2 = img2.resize((1530, 630), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=130, width=1530, height=630)

        # Button
        b1 = Button(bg_img, text="Scan Face Now",
                    cursor="hand2", font=('arial', 20, 'bold'), bg="red", fg="white", command=self.recognition)
        b1.place(x=550, y=250, width=250, height=60)

    # ======================== Face Recognition ======================

    def recognition(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host='localhost', user='root', password='root', port='3306', database='deteksi_wajah')
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select nama_lengkap from karyawan where id_karyawan="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "SELECT gender FROM karyawan WHERE id_karyawan="+str(id))
                gnr = my_cursor.fetchone()
                gnr = "+".join(gnr)

                my_cursor.execute(
                    "SELECT department FROM karyawan WHERE id_karyawan="+str(id))
                dp = my_cursor.fetchone()
                dp = "+".join(dp)

                if confidence > 77:
                    cv2.putText(img, f"Nama:{n}", (x, y-55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Jenis Kelamin:{gnr}", (x, y-30),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{dp}", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, f"Wajah Tidak Dikenal", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1,
                                  10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognationr", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
