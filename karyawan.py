from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Karyawan:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ================== Variable ==================

        self.var_dep = StringVar()
        self.var_id_karyawan = StringVar()
        self.var_nama = StringVar()
        self.var_tahun = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_alamat = StringVar()
        self.var_telepon = StringVar()

        # Label Aplikasi
        f_lbl = Label(self.root, bg="black")
        f_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        f_lbl = Label(self.root, text="Management Karyawan", font=('arial', 30, 'bold'),
                      bd=4, relief=RIDGE, pady=10, padx=20, fg="white", bg="black")
        f_lbl.pack(side=TOP, pady=20, )

        # Background Aplikasi
        img2 = Image.open(r"images\bgimg.jpg")
        img2 = img2.resize((1530, 630), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=130, width=1530, height=630)

        # ---------------------- Main Frame --------------------

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=40, width=1330, height=550)

        # ---------------------- Left Frame --------------------

        left_frame = LabelFrame(main_frame, bd=4, relief=RIDGE, text="Detail Karyawan", font=(
            'times new roman', 12, 'bold'))
        left_frame.place(x=10, y=10, width=642, height=520)

        imgkry = Image.open(r"images\karyawan2.jpg")
        imgkry = imgkry.resize((635, 250), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(imgkry)
        course_image = Label(left_frame, image=self.photoimg3)
        course_image.place(x=0, y=0, width=635, height=250)

        # ---------------------- Data Form ------------------------------

        form_frame = LabelFrame(left_frame, text='Formulir Karyawan', font=(
            'times new roman', 12, 'bold'), bd=2)
        form_frame.place(x=4, y=125, width=630, height=367)
# Department
        label_dep = Label(form_frame, text='Department :', font=(
            'times new roman', 12, 'bold'))
        label_dep.grid(row=0, column=0, padx=10, sticky=W)

        combo_dep = ttk.Combobox(form_frame, font=(
            'times new roman', 12, 'bold'), textvariable=self.var_dep, state='readonly', width=17)
        combo_dep["values"] = (
            "Pilih Department", "Komputer", "IT", "Management", "Mekanik")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)
# Tahun Kerja
        label_tahun = Label(form_frame, text='Tahun :', font=(
            'times new roman', 12, 'bold'))
        label_tahun.grid(row=0, column=2, padx=10, sticky=W)

        combo_tahun = ttk.Combobox(form_frame, font=(
            'times new roman', 12, 'bold'), textvariable=self.var_tahun, state='readonly', width=17)
        combo_tahun["values"] = (
            "Pilih Tahun", "2021", "2022", "2023", "2024", "2025")
        combo_tahun.current(0)
        combo_tahun.grid(row=0, column=3, padx=2, pady=10, sticky=W)
# Nama Karyawan
        label_nama = Label(form_frame, text='Nama Lengkap :', font=(
            'times new roman', 12, 'bold'))
        label_nama.grid(row=1, column=0, padx=10, sticky=W)

        entry_nama = ttk.Entry(form_frame, font=(
            'times new roman', 12, 'bold'), textvariable=self.var_nama, width=19)
        entry_nama.grid(row=1, column=1, padx=2, pady=10, sticky=W)
# ID Karyawan
        label_idkaryawan = Label(form_frame, text='ID Karyawan :', font=(
            'times new roman', 12, 'bold'))
        label_idkaryawan.grid(row=1, column=2, padx=10, sticky=W)

        entry_idkaryawan = ttk.Entry(form_frame, font=(
            'times new roman', 12, 'bold'), textvariable=self.var_id_karyawan, width=19)
        entry_idkaryawan.grid(row=1, column=3, padx=2, pady=10, sticky=W)
# Telepon Pekerja
        label_telp = Label(form_frame, text='Nomor Telepon :', font=(
            'times new roman', 12, 'bold'))
        label_telp.grid(row=2, column=0, padx=10, sticky=W)

        entry_telp = ttk.Entry(form_frame, font=(
            'times new roman', 12, 'bold'), textvariable=self.var_telepon,  width=19)
        entry_telp.grid(row=2, column=1, padx=2, pady=10, sticky=W)
# Alamat Pekerja
        label_alamat = Label(form_frame, text='Alamat :', font=(
            'times new roman', 12, 'bold'))
        label_alamat.grid(row=2, column=2, padx=10, sticky=W)

        entry_alamat = ttk.Entry(form_frame, font=(
            'times new roman', 12, 'bold'), textvariable=self.var_alamat,  width=19)
        entry_alamat.grid(row=2, column=3, padx=2, pady=10, sticky=W)
# Email Pekerja
        label_email = Label(form_frame, text='Email :', font=(
            'times new roman', 12, 'bold'))
        label_email.grid(row=3, column=0, padx=10, sticky=W)

        entry_email = ttk.Entry(form_frame, font=(
            'times new roman', 12, 'bold'), textvariable=self.var_email,  width=19)
        entry_email.grid(row=3, column=1, padx=2, pady=10, sticky=W)
# Jenis Kelamin
        label_gender = Label(form_frame, text='Jenis Kelamin :', font=(
            'times new roman', 12, 'bold'))
        label_gender.grid(row=3, column=2, padx=10, sticky=W)

        combo_gender = ttk.Combobox(form_frame, font=(
            'times new roman', 12, 'bold'), state='readonly', textvariable=self.var_gender,  width=17)
        combo_gender["values"] = (
            "Pilih Jenis Kelamin", "Laki-laki", "Perempuan")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=3, padx=2, pady=10, sticky=W)
# Take Picture
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            form_frame, text="Ambil Foto Sekarang", variable=self.var_radio1, value="Yes")
        radiobtn1.grid(row=4, column=0)

        radiobtn2 = ttk.Radiobutton(
            form_frame, text="Tidak Ada Foto", variable=self.var_radio1, value="No")
        radiobtn2.grid(row=4, column=1)
# Button (Edit/del/add/reset)
        btnn_frame = Frame(form_frame, bd=4, relief=RIDGE, bg='lightblue')
        btnn_frame.place(x=4, y=230, width=617, height=100)

        save_btn = Button(btnn_frame, text='Simpan',
                          bg='green', fg='black', width=15, font=(
                              'times new roman', 12, 'bold'), command=self.add_data)
        save_btn.grid(row=0, column=0, padx=4, pady=5)

        update_btn = Button(btnn_frame, text='Update',
                            bg='orange', fg='black', width=15, font=(
                                'times new roman', 12, 'bold'), command=self.update_data)
        update_btn.grid(row=0, column=1, padx=4, pady=5)

        reset_btn = Button(btnn_frame, text='Reset',
                           bg='blue', fg='black', width=15, font=(
                               'times new roman', 12, 'bold'), command=self.reset_data)
        reset_btn.grid(row=0, column=2, padx=3, pady=5)

        delete_btn = Button(btnn_frame, text='Hapus',
                            bg='red', fg='black', width=15, font=(
                                'times new roman', 12, 'bold'), command=self.delete_data)
        delete_btn.grid(row=0, column=3, padx=3, pady=5)
# Bagian Gambar
        take_gambar_btn = Button(btnn_frame, text='Ambil Gambar', bg='purple', fg='black', width=15, font=(
            'times new roman', 12, 'bold'), bd=2, command=self.generate_dataset)
        take_gambar_btn.grid(row=1, column=1, padx=3, pady=5)

        update_gambar_btn = Button(btnn_frame, text='Update Gambar', bg='pink', fg='black', width=15, font=(
            'times new roman', 12, 'bold'), bd=2)
        update_gambar_btn.grid(row=1, column=2, padx=3, pady=5)

        # ---------------------- Right Frame --------------------

        right_frame = LabelFrame(bg_img, bd=4, relief=RIDGE, text="Data Karyawan", font=(
            'times new roman', 12, 'bold'))
        right_frame.place(x=700, y=50, width=640, height=520)

        imghslkry = Image.open(r"images\karyawan2.jpg")
        imghslkry = imghslkry.resize((635, 250), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(imghslkry)
        course_image_hasil = Label(right_frame, image=self.photoimg4)
        course_image_hasil.place(x=0, y=0, width=627, height=250)

        # ---------------------- Data Form ------------------------------

        form_frame_data = LabelFrame(right_frame, text='Pencarian Data Karyawan', font=(
            'times new roman', 12, 'bold'), bd=2)
        form_frame_data.place(x=4, y=125, width=622, height=73)

        label_search = Label(form_frame_data, text='PENCARIAN :', font=(
            'times new roman', 12, 'bold'), bg='pink', bd=2, relief=RIDGE)
        label_search.grid(row=0, column=0, padx=2, sticky=W)
# pilih pencearian
        combo_search = ttk.Combobox(form_frame_data, font=(
            'times new roman', 12, 'bold'), state='readonly', width=15)
        combo_search["values"] = (
            "Pilih Pencarian", "Nama_Lengkap", "ID_Karyawan")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2, sticky=W)
# entry cari
        entry_seacrh = ttk.Entry(form_frame_data, font=(
            'times new roman', 12, 'bold'), width=17)
        entry_seacrh.grid(row=0, column=2, padx=2, sticky=W)
# tombol cari
        cari_btn = Button(form_frame_data, text='Cari',
                          bg='red', fg='black', width=10, font=(
                              'times new roman', 12, 'bold'))
        cari_btn.grid(row=0, column=3, padx=2, pady=5)
# tombol tampil data
        tampil_btn = Button(form_frame_data, text='Tampil Data',
                            bg='orange', fg='black', width=10, font=(
                                'times new roman', 12, 'bold'))
        tampil_btn.grid(row=0, column=4, padx=2, pady=5)

# ---------------------- Data Tabel Karyawan ------------------------------

        tabel_frame_data = Frame(right_frame, bd=2, relief=RIDGE)
        tabel_frame_data.place(x=4, y=196, width=622, height=295)
# scroll dalam Tabel
        scroll_x = ttk.Scrollbar(tabel_frame_data, orient=HORIZONTAL)
        scrool_y = ttk.Scrollbar(tabel_frame_data, orient=VERTICAL)
# Heading Tabel
        self.karyawan_tabel = ttk.Treeview(tabel_frame_data, columns=(
            "id_kar", "dep", "nama", "gender", "alamat", "tahun", "telp", "email", "foto"), xscrollcommand=scroll_x.set, yscrollcommand=scrool_y.set)
# config scroll
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_x.config(command=self.karyawan_tabel.xview)
        scrool_y.pack(side=RIGHT, fill=Y)
        scrool_y.config(command=self.karyawan_tabel.yview)
# isi Tabel
        self.karyawan_tabel.heading("id_kar", text="ID Karyawan")
        self.karyawan_tabel.heading("dep", text="Department")
        self.karyawan_tabel.heading("nama", text="Nama Lengkap")
        self.karyawan_tabel.heading("gender", text="Jenis Kelamin")
        self.karyawan_tabel.heading("alamat", text="Alamat")
        self.karyawan_tabel.heading("tahun", text="Tahun")
        self.karyawan_tabel.heading("telp", text="Telepon")
        self.karyawan_tabel.heading("email", text="Email")
        self.karyawan_tabel.heading("foto", text="Photo")
        self.karyawan_tabel["show"] = "headings"

        self.karyawan_tabel.pack(fill=BOTH, expand=1)
        self.karyawan_tabel.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

# ========================== Function Kelola Database ==========================

    def add_data(self):
        if self.var_dep.get() == 'Pilih Department' or self.var_nama.get() == "" or self.var_id_karyawan.get() == "":
            messagebox.showerror(
                "Error", "Semua data diperlukan, tolong isi terlebih dahulu!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', user='root', password='root', port='3306', database='deteksi_wajah')
                mycursor = conn.cursor()
                mycursor.execute("INSERT INTO karyawan VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_id_karyawan.get(),
                    self.var_dep.get(),
                    self.var_nama.get(),
                    self.var_gender.get(),
                    self.var_alamat.get(),
                    self.var_tahun.get(),
                    self.var_telepon.get(),
                    self.var_email.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Data berhasil ditambhakan", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Masalah pada :{str(es)}", parent=self.root)

# ========================== Fetch Data dari Database ==========================

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', user='root', password='root', port='3306', database='deteksi_wajah')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM karyawan")
        data = mycursor.fetchall()

        if len(data) != 0:
            self.karyawan_tabel.delete(*self.karyawan_tabel.get_children())
            for i in data:
                self.karyawan_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()

# ========================== Get Data dari Pointer(Cursor) ==========================

    def get_cursor(self, event=""):
        cursor_focus = self.karyawan_tabel.focus()
        content = self.karyawan_tabel.item(cursor_focus)
        data = content["values"]

        self.var_id_karyawan.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_nama.set(data[2]),
        self.var_gender.set(data[3]),
        self.var_alamat.set(data[4]),
        self.var_tahun.set(data[5]),
        self.var_telepon.set(data[6]),
        self.var_email.set(data[7]),
        self.var_radio1.set(data[8])
# Update Data

    def update_data(self):
        if self.var_dep.get() == 'Pilih Department' or self.var_nama.get() == "" or self.var_id_karyawan.get() == "":
            messagebox.showerror(
                "Error", "Semua data diperlukan, tolong isi terlebih dahulu!", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Apakah kamu yakin akan mengupdate data ini?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host='localhost', user='root', password='root', port='3306', database='deteksi_wajah')
                    mycursor = conn.cursor()
                    mycursor.execute(
                        "UPDATE karyawan SET department=%s,nama_lengkap=%s,gender=%s,alamat=%s,tahun_masuk=%s,telepon=%s,email=%s,photo=%s WHERE id_karyawan=%s", (
                            self.var_dep.get(),
                            self.var_nama.get(),
                            self.var_gender.get(),
                            self.var_alamat.get(),
                            self.var_tahun.get(),
                            self.var_telepon.get(),
                            self.var_email.get(),
                            self.var_radio1.get(),
                            self.var_id_karyawan.get()
                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "Success", "Data karyawan berhasil diperbarui", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Masalah pada :{str(es)}", parent=self.root)
# Delete Data

    def delete_data(self):
        if self.var_id_karyawan.get() == "":
            messagebox.showerror(
                "Error", "Semua data diperlukan, tolong isi terlebih dahulu!", parent=self.root)
        else:
            try:
                hapus = messagebox.askyesno(
                    "Hapus Karyawan", "Apakah kamu yakin akan menghapus data ini?", parent=self.root)
                if hapus > 0:
                    conn = mysql.connector.connect(
                        host='localhost', user='root', password='root', port='3306', database='deteksi_wajah')
                    mycursor = conn.cursor()
                    sql_delete = ("DELETE FROM karyawan where id_karyawan=%s")
                    val = (self.var_id_karyawan.get(),)
                    mycursor.execute(sql_delete, val)
                else:
                    if not hapus:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Data karyawan berhasil diperbarui", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Masalah pada :{str(es)}", parent=self.root)

# Reset Data
    def reset_data(self):
        self.var_id_karyawan.set(""),
        self.var_dep.set("Pilih Department"),
        self.var_nama.set(""),
        self.var_gender.set("Pilih Jenis Kelamin"),
        self.var_alamat.set(""),
        self.var_tahun.set("Pilih Tahun"),
        self.var_telepon.set(""),
        self.var_email.set(""),
        self.var_radio1.set("")

# ========================== Get Data Set atau Ambil Foto ==========================

    def generate_dataset(self):
        if self.var_dep.get() == 'Pilih Department' or self.var_nama.get() == "" or self.var_id_karyawan.get() == "":
            messagebox.showerror(
                "Error", "Semua data diperlukan, tolong isi terlebih dahulu!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', user='root', password='root', port='3306', database='deteksi_wajah')
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM karyawan")
                myresult = mycursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                mycursor.execute(
                    "UPDATE karyawan SET department=%s,nama_lengkap=%s,gender=%s,alamat=%s,tahun_masuk=%s,telepon=%s,email=%s,photo=%s WHERE id_karyawan=%s", (
                        self.var_dep.get(),
                        self.var_nama.get(), 
                        self.var_gender.get(),
                        self.var_alamat.get(),
                        self.var_tahun.get(),
                        self.var_telepon.get(),
                        self.var_email.get(),
                        self.var_radio1.get(),
                        self.var_id_karyawan.get() == id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ============= Load Fredifiend data on Face Frontal from opencv ===================

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scalling factor = 1.3
                    # Minimum Neighbor = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set compled!!!")
            except EXCEPTION as es:
                messagebox.showerror(
                    "Error", f"Masalah pada :{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Karyawan(root)
    root.mainloop()
