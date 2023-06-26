from dotenv import load_dotenv
import os

# Get settings from .env file
gotenv = load_dotenv()

def get_settings():
    if (not gotenv):
        return {
            "error": "sett-1",
            "value": ""
        }
    
    settings = {}
    settings["webuserver"] = os.getenv("SCHOOLBUDDY_WEBUSERVER")
    settings["webuschool"] = os.getenv("SCHOOLBUDDY_WEBUSCHOOL")
    settings["webuuser"] = os.getenv("SCHOOLBUDDY_WEBUUSER")
    settings["webupwd"] = os.getenv("SCHOOLBUDDY_WEBUPWD")
    settings["webuclass"] = os.getenv("SCHOOLBUDDY_WEBUCLASS")

    # Return settings
    return {
        "error": "",
        "value": settings
    }


# Old sql stuff
'''import mysql.connector as mysql
import os

pw=os.getenv('SCHOOLBUDDY_SQLPWD')

db = mysql.connect(
    host="localhost",
    user="schoolbuddy",
    password=pw,
    database="schoolbuddy",
)

def get_settings(valueonly: bool = True):
    try:
        cursor = db.cursor()

        sql = "SELECT "
        if (valueonly):
            sql += "setting_name, value, type"
        else:
            sql += "*"
        sql += " FROM settings;"

        cursor.execute(sql)

        sqlres = cursor.fetchall()

        result = {}

        for x in sqlres:
            val = {
                "value": x[1],
                "type": x[2]
            }
            result[x[0]] = val

        ret = {
            "error": "",
            "value": result
        }
        return ret
    
    except:
        return {
            "error": "mysql-1",
            "value": ""
        }

def get_setting(settname: str, valueonly: bool = True):
    try:
        cursor = db.cursor()
        sql = "SELECT "

        if (valueonly):
            sql += "setting_name, value, type"
        else:
            sql += "*"
        
        sql += " FROM settings WHERE setting_name =" + "'" + settname + "';"

        cursor.execute(sql)

        sqlres = cursor.fetchonce()

        result = {
            "value": sqlres[1],
            "type": sqlres[2]
        }

        return {
            "error": "",
            "value": {
                sqlres[0]: result
            }
        }
    
    except:
        return {
            "error": "mysql-1",
            "value": ""
        }

def set_init_settings():
    try:
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
    except:
        return {
            "error": "mysql-1",
            "value": ""
        }

    return {
        "error": "",
        "value": "true"
    }'''
