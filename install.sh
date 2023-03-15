#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Please run this script with sudo"
    exit
fi

declare -A SETT_ARRAY=()

currentpage="main"

configuremysql () {
    usrstr="CREATE USER 'schoolbuddy'@'localhost' IDENTIFIED BY '""${SETT_ARRAY[sqlpwd]}"
    mysql -u root -e "CREATE schoolbuddy"
    mysql -u root schoolbuddy < mysqlconfig.sql
    mysql -u root -e "$usrstr"
    mysql -u root -e "GRANT SELECT, INSERT, UPDATE ON 'schoolbuddy'.* TO 'schoolbuddy'@'localhost'"
    mysql -u root -e "FLUSH PRIVILEGES"
    return
}

setconfig () {
    clear 
    echo $'\nDone\n\n'
    if [ -e "/etc/profile.d/schoolbuddy.sh" ]; then
        rm /etc/profile.d/schoolbuddy.sh
    fi
    for key in "${!SETT_ARRAY[@]}"; do
        upkey=$(echo "$key" | tr "[:lower:]" "[:upper:]")
        str="export ""SCHOOLBUDDY_""$upkey""=\"""${SETT_ARRAY[$key]}""\""$'\n'
        echo "$str" >> /etc/profile.d/schoolbuddy.sh
    done
    echo "export ""SCHOOLBUDDY_FIRSTRUN""=\"""yes""\""$'\n' >> /etc/profile.d/schoolbuddy.sh
    configuremysql
}

configure () {
    if [ "$1" == "init" ]; then
        renderconfigdisplay "main"
    else
        read -rp $'\n> ' readval
        if [ "$readval" == "b" ] && [ "$currentpage" != "main" ]; then
            currentpage="main"
            renderconfigdisplay "main"
        elif [ "$readval" == "c" ] && [ "$currentpage" == "main" ]; then
            if [ "$( getmissing )" == "none" ]; then
                setconfig
            else
                renderfail "notcomplete"
                renderconfigdisplay "$currentpage"
            fi
        else
            name=""
            type="none"
            if [ "$readval" == "1" ]; then
                case "$currentpage" in
                    "main")
                    name="admpwd"
                    type="pwd"
                    ;;
                    "wifi")
                    name="wifissid"
                    type="ssid"
                    ;;
                    "webu")
                    name="webuserver"
                    type="url"
                    ;;
                esac
            elif [ "$readval" == "2" ]; then
                case "$currentpage" in
                    "main")
                    name="sqlpwd"
                    type="pwd"
                    ;;
                    "wifi")
                    name="wifipwd"
                    type="pwd"
                    ;;
                    "webu")
                    name="webuschool"
                    type="text"
                    ;;
                esac
            elif [ "$readval" == "3" ]; then
                case "$currentpage" in
                    "main")
                    name="wifi"
                    type="chngpg"
                    ;;
                    "wifi")
                    name=""
                    type="none"
                    ;;
                    "webu")
                    name="webuuser"
                    type="text"
                    ;;
                esac
            elif [ "$readval" == "4" ]; then
                case "$currentpage" in
                    "main")
                    name="webu"
                    type="chngpg"
                    ;;
                    "wifi")
                    name=""
                    type="none"
                    ;;
                    "webu")
                    name="webupwd"
                    type="pwd"
                    ;;
                esac
            elif [ "$readval" == "5" ]; then
                if [ "$currentpage" == "webu" ]; then
                    name="webuclass"
                    type="class"
                fi
            fi
            if [ "$type" == "none" ]; then
                renderfail "nooption"
                renderconfigdisplay "$currentpage"
            elif [ "$type" == "chngpg" ]; then
                currentpage="$name"
                renderconfigdisplay "$name"
            else
                clear
                local pwd=false
                local readval=""
                case "$name" in
                    "admpwd")
                    pwd=true
                    echo $'\nSetting SchoolBuddy Admin Password'
                    echo $'\nYou can use (a-z)(A-Z)(0-9) and (!?_)'
                    echo $'\nWith a minimum length of 8 and maximum length of 24 characters'
                    ;;
                    "sqlpwd")
                    pwd=true
                    echo $'\nSetting MySQL Database Password'
                    echo $'\nYou can use (a-z)(A-Z)(0-9) and (!?_)'
                    echo $'\nWith a minimum length of 8 and maximum length of 24 characters'
                    ;;
                    "wifissid")
                    echo $'\nSetting Wifi SSID'
                    echo $'\nYou can use (a-z)(A-Z)(0-9) and (-_)'
                    echo $'\nWith a minimum length of 4 and maximum length of 16 characters'
                    ;;
                    "wifipwd")
                    pwd=true
                    echo $'\nSetting Wifi Password'
                    echo $'\nYou can use (a-z)(A-Z)(0-9) and (!?_)'
                    echo $'\nWith a minimum length of 8 and maximum length of 24 characters'
                    ;;
                    "webuserver")
                    echo $'\nSetting WebUntis Server'
                    echo $'\nPlease respond with a URL (Example: https://asopo.webuntis.com)'
                    ;;
                    "webuschool")
                    echo $'\nSetting WebUntis School'
                    echo $'\nPlease respond with you school name in the WebUntis format'
                    echo $'\n[For more information see configuration page in repository]'
                    ;;
                    "webuuser")
                    echo $'\nSetting WebUntis Username'
                    echo $'\nPlease respond with the username you use to login to WebUntis'
                    ;;
                    "webupwd")
                    pwd=true
                    echo $'\nSetting WebUntis Password'
                    echo $'\nPlease respond with the password you use to login to WebUntis'
                    ;;
                    "webuclass")
                    echo $'\nSetting WebUntis Initial Class'
                    echo $'\nPlease respond with the class you attend to (Make sure you do not capitalize the letter e.g. 11p)'
                    echo $'\n(Don\'t worry, you can still change this setting later)'
                    ;;
                esac
                if [ "$pwd" == true ]; then
                    read -rsp $'\n> ' readval
                else
                    read -rp $'\n>' readval
                fi
                checkinput "$type" "$readval"
                if [ "$?" == 1 ]; then
                    renderfail "syntax"
                else
                    SETT_ARRAY[$name]="$readval"
                fi
                renderconfigdisplay "$currentpage"
            fi
        fi
    fi
}

getsettval () {
    
    echo "$readval"
}

renderconfigdisplay () {
    clear
    if [ "$1" == "main" ]; then
        local missstr
        missstr="$(getmissing)"

        echo $'\nSchoolBuddy Configuration'
        echo $'\nPlease choose one of the following options: '
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
        echo $'\n5 - Class (Initial class to get info for. Don\'t worry you can change it later.)'
        echo $'\n'
        echo $'\nB - Go Back'
    fi
    configure "$1"
}

getmissing () {
    local missstr=""
    if [[ -z "${SETT_ARRAY[admpwd]}" ]]; then
        missstr+=" 1"
    fi
    if [[ -z "${SETT_ARRAY[sqlpwd]}" ]]; then
        missstr+=" 2"
    fi
    if [[ -z "${SETT_ARRAY[wifissid]}" ]] || [[ -z "${SETT_ARRAY[wifipwd]}" ]];  then
        missstr+=" 3"
    fi
    if [[ -z "${SETT_ARRAY[webuserver]}" ]] || [[ -z "${SETT_ARRAY[webuuser]}" ]] || [[ -z "${SETT_ARRAY[webupwd]}" ]] || [[ -z "${SETT_ARRAY[webuschool]}" ]] || [[ -z "${SETT_ARRAY[webuclass]}" ]]; then
        missstr+=" 4"
    fi
    if [ "$missstr" == "" ]; then
        echo "none"
    else 
        echo "$missstr"
    fi
}

checkinput () {
    local fail=false
    if [ "$1" == "pwd" ] && [[ ! "$2" =~ ^[A-Za-z0-9\?!_]{8,24}$ ]]; then
        fail=true
    elif [ "$1" == "ssid" ] && [[ ! "$2" =~ ^[A-Za-z0-9\-]{4,16}$ ]]; then
        fail=true
    elif [ "$1" == "url" ] && [[ ! "$2" =~ ^https:\/\/[a-z0-9]*.?webuntis.com$ ]]; then
        fail=true
    elif [ "$1" == "class" ] && [[ ! "$2" =~ ^[1-2]?[0-9][a-z]$ ]]; then
        fail=true
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
    elif [ "$1" == "notcomplete" ]; then
        echo $'\nERROR: Cannot proceed'
        echo $'\nYou have not configured all values yet.'
    fi
    read -rp $'\nPress Enter to continue'
}

uninstall () {
    clear
    cd /home/schoolbuddy/ || exit 2
    su schoolbuddy -c "pipenv -rm"
    su schoolbuddy -c "pip3 uninstall pipenv"
    systemctl stop schoolbuddy.service
    rm -f /etc/systemd/system/schoolbuddy.service
    systemctl daemon-reload
    userdel schoolbuddy
    rm -R /home/schoolbuddy/
    # If remove mysql etc.
    if [ "$1" == "y" ]; then
        apt-get uninstall mysql-server ffmpeg apache2 espeak-ng -y
    fi
}

read -rp $'\nSchoolBuddy Install Script\n\nPlease choose:\n\n1 - Install and configure SchoolBuddy\n2 - Uninstall SchoolBuddy\nEnter - Cancel\n\n> ' act

if [ "$act" == 1 ]; then
    echo $'\nPlease wait while we install the required packages.\n'

    apt-get update
    apt-get install software-properties-common -y
    ln -s /usr/lib/python3/dist-packages/gi/_gi.cpython-{36m,37m}-x86_64-linux-gnu.so
    ln -s /usr/lib/python3/dist-packages/apt_pkg.cpython-{36m,37m}-x86_64-linux-gnu.so
    add-apt-repository -y ppa:deadsnakes/ppa
    apt-get update
    apt-get install "python3.7" python3-pip "python3.7-dev" "python3-pyaudio" "portaudio19-dev" mysql-server ffmpeg apache2 espeak-ng -y
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
    su schoolbuddy -c "pipenv run pip install torch==1.13.1 --no-cache-dir"
    su schoolbuddy -c "pipenv install"

    echo $'\nInstallation complete.'

    configure "init"

elif [ "$act" == 2 ]; then
    clear
    read -rp $'\nAre you sure you want to uninstall SchoolBuddy? (y/n)[Default: n]' answr
    if [ "$answr" != "y" ]; then
        echo $'\nCancelled'
        exit
    fi
    unset answr
    read -rp $'\nDo you want to remove all packages that were installed? (y/n/(c)ancel)[default: n]' answr
    if [ "$answr" == "c" ]; then
        echo $'\nCancelled'
        exit
    fi
    uninstall "$answr"
    clear
    echo $'\nSuccessfully uninstalled SchoolBuddy. Sad to see you go.'
    exit
elif [ "$act" == 3 ]; then
    configure "init"
else
    echo $'\nCancelled.'
    exit
fi
