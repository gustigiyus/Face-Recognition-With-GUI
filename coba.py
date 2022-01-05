import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port='3306',
    database='test'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM karyawan')

users = mycursor.fetchall()

for user in users:
    print(user)
    print('username ' + user[1])
    print('password ' + user[2])
