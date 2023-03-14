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

    cursor = db.cursor()
    
    settings = {}
    settings['adm_pwd']=os.getenv('SCHOOLBUDDY_ADMPWD')
    settings['default_wifi_ssid']=os.getenv('SCHOOLBUDDY_WIFISSID')
    settings['default_wifi_pwd']=os.getenv('SCHOOLBUDDY_WIFIPWD')
    settings['webu_server']=os.getenv('SCHOOLBUDDY_WEBUSERVER')
    settings['webu_user']=os.getenv('SCHOOLBUDDY_WEBUUSER')
    settings['webu_pwd']=os.getenv('SCHOOLBUDDY_WEBUPWD')
    settings['webu_school']=os.getenv('SCHOOLBUDDY_WEBUSCHOOL')
    settings['webu_class']=os.getenv('SCHOOLBUDDY_WEBUCLASS')

    sql = "UPDATE settings SET value = %s WHERE setting_name = %s;"
    data = []
    for x in settings:
        val = (settings[x],x)
        data.append(val)

    cursor.executemany(sql,data)
    db.commit()

    return True
