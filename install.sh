#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Please run this script with sudo"
    exit
fi

declare -A SETT_ARRAY=()

currentpage="main"

read -rp $'\nSchoolBuddy Install Script\n\nPlease choose:\n\n1 - Install and configure SchoolBuddy\n2 - Uninstall SchoolBuddy\nEnter - Cancel\n\n> ' act

if [ "$act" == 1 ]; then
    echo $'\nPlease wait while we install the required packages.\n'

    apt-get update
    apt-get install software-properties-common -y
    add-apt-repository -y ppa:deadsnakes/ppa
    apt-get update
    apt-get install "python3.7" python3-pip mysql-server ffmpeg apache2 espeak-ng -y
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
    update-alternatives --set python3 /usr/bin/python3.7

    cp schoolbuddy.service /etc/systemd/system/schoolbuddy.service
    systemctl daemon-reload
    useradd -m schoolbuddy
    cp -r . /home/schoolbuddy/
    chmod -R 777 /home/schoolbuddy
    cd /home/schoolbuddy/ || exit 2

    su schoolbuddy -c "pip3 install pipenv==2022.4.8"
    su schoolbuddy -c "pipenv --python 3.7"
    su schoolbuddy -c "pipenv install --verbose" 

    echo $'\nInstallation complete.'

    configure "init"

elif [ "$act" == 2 ]; then
    echo $'\nThis is not yet possible.'

elif [ "$act" == 3 ]; then
    configure "init"
else
    echo $'\nCancelled.'
fi

setconfig () {

}

configure () {
    if [ "$1" == "init" ]; then
        renderconfigdisplay "main"
    else
        read -n 1 -rp $'\n> ' readval
        if [ "$readval" == "b" ] && [ "$currentpage" != "main" ]; then
            currentpage="main"
            renderconfigdisplay "main"
        elif [ "$readval" == "c" ] && [ "$currentpage" == "main" && "$(getmissing)" == "none" ]; then
            setconfig
        else
            local name=""
            local type="none"
            if [ "$readval" == "1" ]; then
                case "$currentpage" in
                    main)
                    name="admpwd"
                    type="pwd"
                    ;;
                    wifi)
                    name="wifissid"
                    type="ssid"
                    ;;
                    webu)
                    name="webuserver"
                    type="url"
                    ;;
                esac
            elif [ "$readval" == "2" ]; then
                case "$currentpage" in
                    main)
                    name="sqlpwd"
                    type="pwd"
                    ;;
                    wifi)
                    name="wifipwd"
                    type="pwd"
                    ;;
                    webu)
                    name="webuschool"
                    type="text"
                    ;;
                esac
            elif [ "$readval" == "3" ]; then
                case "$currentpage" in
                    main)
                    name="wifi"
                    type="chngpg"
                    ;;
                    wifi)
                    name=""
                    type="none"
                    ;;
                    webu)
                    name="webuuser"
                    type="text"
                    ;;
                esac
            elif [ "$readval" == "4" ]; then
                case "$currentpage" in
                    main)
                    name="webu"
                    type="chngpg"
                    ;;
                    wifi)
                    name=""
                    type="none"
                    ;;
                    webu)
                    name="webupwd"
                    type="pwd"
                    ;;
                esac
            fi
            if [ "$type" == "none" ]; then
                renderfail "nooption"
                renderconfigdisplay "$currentpage"
            elif [ "$type" == "chngpg" ]; then
                currentpage="$name"
                renderconfigdisplay "$name"
            else
                val=$(getsettval "$name")
                checkinput "$type" "$val"
                if [ "$?" == 1]; then
                    renderfail "syntax"
                else
                    SETT_ARRAY[$name]="$val"
                fi
                renderconfigdisplay "$currentpage"
            fi
        fi
    fi
}

getsettval () {
    clear
    local pwd = false
    local readval = ""
    if [ "$1" == "admpwd" ]; then
        pwd = true
        echo $'\nSetting SchoolBuddy Admin Password'
        echo $'\nYou can use (a-z)(A-Z)(0-9) and (!?_)'
    elif [ "$1" == "sqlpwd" ]; then
        pwd = true
        echo $'\nSetting MySQL Database Password'
        echo $'\nYou can use (a-z)(A-Z)(0-9) and (!?_)'
    elif [ "$1" == "wifissid" ]; then
        echo $'\nSetting Wifi SSID'
        echo $'\nYou can use (a-z)(A-Z)(0-9) and (-_)'
    elif [ "$1" == "wifipwd" ]; then
        pwd = true
        echo $'\nSetting Wifi Password'
        echo $'\nYou can use (a-z)(A-Z)(0-9) and (!?_)'
    elif [ "$1" == "webuserver" ]; then
        echo $'\nSetting WebUntis Server'
        echo $'\nPlease respond with a URL (Example: https://asopo.webuntis.com)'
    elif [ "$1" == "webuschool" ]; then
        echo $'\nSetting WebUntis School'
        echo $'\nPlease respond with you school name in the WebUntis format'
        echo $'\n[For more information see configuration page in repository]'
    elif [ "$1" == "webuuser" ]; then
        echo $'\nSetting WebUntis Username'
        echo $'\nPlease respond with the username you use to login to WebUntis'
    elif [ "$1" == "webupwd" ]; then
        pwd = true
        echo $'\nSetting WebUntis Password'
        echo $'\nPlease respond with the password you use to login to WebUntis'
    fi
    if [ "$pwd" === true]; then
        read -rsp $'\n> ' readval
    else
        read -rp $'\n>' readval
    fi
    echo "$readval"
}

renderconfigdisplay () {
    clear
    if [ "$1" == "main" ]; then
        local missstr = "$(getmissing)"

        echo $'\nSchoolBuddy Configuration'
        echo $'\nPlease choose one of the following options: '
        echo $'\n'
        echo $'\n1 - SchoolBuddy Admin Password'
        echo $'\n2 - MySQL Database Password'
        echo $'\n3 - Wifi Settings'
        echo $'\n4 - WebUntis Settings'
        echo $'\n'
        echo $'\nC - Complete Configuration'

        if [ "$missstr" != "none" ]; then
            echo " (Cannot proceed. You're missing settings in sections"
            echo "$missstr"
            echo ".)"
        fi
    elif [ "$1" == "wifi" ]; then
        echo $'\nWifi Configuration'
        echo $'\nPlease choose one of the following options: '
        echo $'\n'
        echo $'\n1 - SSID (SSID of the wifi network SchoolBuddy will host.)'
        echo $'\n2 - Password (Password of the wifi network SchoolBuddy will host.)'
        echo $'\n'
        echo $'\nB - Go Back'
    elif [ "$1" == "webu" ]; then
        echo $'\n WebUntis Configuration'
        echo $'\nPlease choose one of the following options: '
        echo $'\n'
        echo $'\n1 - Server (URL of the WebUntis server)'
        echo $'\n2 - School (Name of your school in WebUntis format [See configuration page in repository])'
        echo $'\n3 - Username (Usename you use to login to WebUntis)'
        echo $'\n4 - Password (Password you use to login to WebUntis)'
        echo $'\n'
        echo $'\nB - Go Back'
    fi
    configure "$1"
}

getmissing () {
    local missstr = ""
    if [![ -n "${SETT_ARRAY[admpwd]}" ]]; then
        missstr += " 1"
    fi
    if [![ -n "${SETT_ARRAY[sqlpwd]}" ]]; then
        missstr += " 2"
    fi
    if [![ -n "${SETT_ARRAY[wifissid]}" ]] || [![ -n "${SETT_ARRAY[wifipwd]}"]];  then
        missstr += " 3"
    fi
    if [![ -n "${SETT_ARRAY[webuserver]}" ]] || [![ -n "${SETT_ARRAY[webuuser]}" ]] || [![ -n "${SETT_ARRAY[webupwd]}" ]] || [![ -n "${SETT_ARRAY[webuschool]}" ]] || [![ -n "${SETT_ARRAY[webuclass]}" ]]; then
        missstr += " 4"
    fi
    if [ "$missstr" == "" ]; then
        echo "none"
    else 
        echo "$missstr"
    fi
}

checkinput () {
    local fail = false
    if [ "$1" == "pwd" ] && [![ "$2" =~ ^[A-Za-z0-9\?\!\_]{8,24} ]]; then
        fail = true
    elif [ "$1" == "ssid" ] && [![ "$2" =~ ^[A-Za-z0-9\-]{8,16} ]]; then
        fail = true
    elif [ "$1" == "url" ] && [![ "$2" =~ ^https\:\/\/[a-z]\.webuntis\.com$ ]]; then
        fail = true
    fi

    if [ "$fail" == true ]; then
        return 1
    else
        return 0
    fi
}

renderfail () {
    clear
    if [ "$1" == "syntax" ]; then
        echo $'\nERROR: Could not save setting'
        echo $'\nPlease make sure you follow the correct syntax'
    elif [ "$1" == "nooption" ]; then
        echo $'\nThat option doesn\'t exist'
    fi
    read -rp $'\nPress Enter to continue' usl
}