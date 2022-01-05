from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1352x790+0+0")
        self.root.title("Face Recognition System")

        # Label Aplikasi
        f_lbl = Label(self.root, bg="black")
        f_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        f_lbl = Label(self.root, text="Train Data", font=('arial', 30, 'bold'),
                      bd=4, relief=RIDGE, pady=10, padx=20, fg="white", bg="black")
        f_lbl.pack(side=TOP, pady=20, )

        # Background Aplikasi
        img2 = Image.open(r"images\bgimg.jpg")
        img2 = img2.resize((1530, 630), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=130, width=1530, height=630)

        b1 = Button(bg_img, text="Train Data Set",
                    cursor="hand2", font=('arial', 20, 'bold'), bg="red", fg="white", command=self.train_classifier)
        b1.place(x=550, y=250, width=250, height=60)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert("L")  # Gray Scale Image
            image_np = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training Data User", image_np)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # =================== Train Classifier dan Save ============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training data set selesai!!", )


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
