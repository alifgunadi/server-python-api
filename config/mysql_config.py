import mysql.connector


def db():
    mysql.connector.connect(host="localhost", user="ravelware", password="R4v3lw4r3")
