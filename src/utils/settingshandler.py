import mysql.connector as mysql
import os

pw=os.getenv('SCHOOLBUDDY_SQLPWD')

db = mysql.connect(
    host="localhost",
    user="schoolbuddy",
    pw=pw,
    database="schoolbuddy"
)

def getSettings():
    return #Settingsarray


def getSetting(settname:str):
    return #Setting

def setInitSettings():

    return True
