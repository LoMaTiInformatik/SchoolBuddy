#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Please run this script with sudo"
    exit
fi

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

    su schoolbuddy -c "pip3 install pipenv"
    su schoolbuddy -c "pipenv --python 3.7"
    su schoolbuddy -c "pipenv install --verbose" 

    echo $'\nInstallation complete.'

elif [ "$act" == 2 ]; then
    echo $'\nThis is not yet possible.'

else
    echo $'\nCancelled.'
fi
