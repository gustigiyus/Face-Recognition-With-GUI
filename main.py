from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from karyawan import Karyawan
from train import Train
from face_recognition import Face_Recognition
import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Label Aplikasi
        f_lbl = Label(self.root, bg="black")
        f_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        f_lbl = Label(self.root, text="Face Recognicition System", font=('arial', 30, 'bold'),
                      bd=4, relief=RIDGE, pady=10, padx=20, fg="white", bg="black")
        f_lbl.pack(side=TOP, pady=20, )

        # Background Aplikasi
        img2 = Image.open(r"images\bgimg.jpg")
        img2 = img2.resize((1530, 630), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=130, width=1530, height=630)

        # ---------------------- BUTTON APLIKASI --------------------

        # Button Pengelolaan Data
        img3 = Image.open(r"images\img2face.jpg")
        img3 = img3.resize((200, 200), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img, image=self.photoimg3, bd=3,
                    relief=RIDGE, command=self.karyawan_details)
        b1.place(x=160, y=70, width=200, height=200)

        b1_1 = Button(bg_img, text="Data Mahasiswa", cursor="hand2", font=('arial', 15, 'bold'),
                      fg="white", bg="blue", command=self.karyawan_details)
        b1_1.place(x=160, y=230, width=200, height=40)

        # Button Face Detector
        img4 = Image.open(r"images\img3face.jpg")
        img4 = img4.resize((200, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b2 = Button(bg_img, image=self.photoimg4, bd=3,
                    relief=RIDGE, command=self.face_recognition_details)
        b2.place(x=460, y=70, width=200, height=200)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=('arial', 15, 'bold'),
                      fg="white", bg="blue", command=self.face_recognition_details)
        b2_1.place(x=460, y=230, width=200, height=40)

        # Button Attendence
        img5 = Image.open(r"images\img3face.jpg")
        img5 = img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b3 = Button(bg_img, image=self.photoimg5, bd=3, relief=RIDGE)
        b3.place(x=760, y=70, width=200, height=200)

        b3_1 = Button(bg_img, text="Attendence", cursor="hand2", font=('arial', 15, 'bold'),
                      fg="white", bg="blue")
        b3_1.place(x=760, y=230, width=200, height=40)

        # Button Help Desk
        img6 = Image.open(r"images\img3face.jpg")
        img6 = img6.resize((200, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b4 = Button(bg_img, image=self.photoimg6, bd=3, relief=RIDGE)
        b4.place(x=1060, y=70, width=200, height=200)

        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=('arial', 15, 'bold'),
                      fg="white", bg="blue")
        b4_1.place(x=1060, y=230, width=200, height=40)

        # ------ Button Bagian Bawah --------

        # Button Train Data
        img7 = Image.open(r"images\img2face.jpg")
        img7 = img7.resize((200, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b5 = Button(bg_img, image=self.photoimg7, bd=3,
                    relief=RIDGE, command=self.train_details)
        b5.place(x=160, y=350, width=200, height=200)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2", font=('arial', 15, 'bold'),
                      fg="white", bg="blue", command=self.train_details)
        b5_1.place(x=160, y=510, width=200, height=40)

        # Button Gallery Face
        img8 = Image.open(r"images\img3face.jpg")
        img8 = img8.resize((200, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b6 = Button(bg_img, image=self.photoimg8, bd=3,
                    relief=RIDGE, command=self.open_img)
        b6.place(x=460, y=350, width=200, height=200)

        b6_1 = Button(bg_img, text="Gallery Face", cursor="hand2", font=('arial', 15, 'bold'),
                      fg="white", bg="blue", command=self.open_img)
        b6_1.place(x=460, y=510, width=200, height=40)

        # Button Developer
        img9 = Image.open(r"images\img3face.jpg")
        img9 = img9.resize((200, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b7 = Button(bg_img, image=self.photoimg9, bd=3, relief=RIDGE)
        b7.place(x=760, y=350, width=200, height=200)

        b7_1 = Button(bg_img, text="Developer", cursor="hand2", font=('arial', 15, 'bold'),
                      fg="white", bg="blue")
        b7_1.place(x=760, y=510, width=200, height=40)

        # Button Exit
        img10 = Image.open(r"images\img3face.jpg")
        img10 = img10.resize((200, 200), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b8 = Button(bg_img, image=self.photoimg10, bd=3, relief=RIDGE)
        b8.place(x=1060, y=350, width=200, height=200)

        b8_1 = Button(bg_img, text="Exit", cursor="hand2", font=('arial', 15, 'bold'),
                      fg="white", bg="blue")
        b8_1.place(x=1060, y=510, width=200, height=40)

    def open_img(self):
        os.startfile("data")

    # ====================== Function Buttons =========================

    def karyawan_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Karyawan(self.new_window)

    def train_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recognition_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
