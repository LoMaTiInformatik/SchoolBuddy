import mysql.connector as mysql
import os

pw=os.getenv('SCHOOLBUDDY_SQLPWD')

db = mysql.connect(
    host="localhost",
    user="schoolbuddy",
    pw=pw,
    database="schoolbuddy"
)

def get_settings():
    return #Settingsarray


def get_setting(settname:str):
    return #Setting

def set_init_settings():
    admpwd=os.getenv('SCHOOLBUDDY_ADMPWD')
    wifissid=os.getenv('SCHOOLBUDDY_WIFISSID')
    wifipwd=os.getenv('SCHOOLBUDDY_WIFIPWD')
    return True
