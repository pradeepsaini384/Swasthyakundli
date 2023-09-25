import mysql.connector

conn = mysql.connector.connect(host = "localhost",user= "root",password ="",database="swasthyakundli")
cursor = conn.cursor()


def authentication(email,password):
    cursor.execute("""SELECT * FROM `user` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users = cursor.fetchall()
    return users


def registration(list):
    cursor.execute("""INSERT INTO `user` (`user_id`,`name`,`email`,`password`,`mobile_no`,`dob`) VALUES ('{}','{}','{}','{}','{}','{}')""".format(102,list[0],list[1],list[2],list[3],list[4]))
    conn.commit()
    return 202

def partnership_form(list):
    cursor.execute("""INSERT INTO `partnership` (`name`,`email`,`type`,`mobile`,`message`) VALUES ('{}','{}','{}','{}','{}')""".format(list[0],list[1],list[2],list[3],list[4]))
    conn.commit()
    return 202