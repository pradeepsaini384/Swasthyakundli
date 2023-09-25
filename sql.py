import mysql.connector

conn = mysql.connector.connect(host = "localhost",user= "root",password ="",database="swasthyakundli")
cursor = conn.cursor()


def authentication(email,password):
    cursor.execute("""SELECT * FROM `user` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users = cursor.fetchall()
    return users
