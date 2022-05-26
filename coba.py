import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port='3306',
    database='deteksi_wajah'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM karyawan')

users = mycursor.fetchall()

for user in users:
    print(user)
