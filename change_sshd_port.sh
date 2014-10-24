#!/bin/sh
# -*- coding: utf-8 -*-

sudo sed -e "s/^Port.*/Port 23456/g" test.conf > temp.conf
sudo cat temp.conf > /etc/ssh/sshd_config
sudo rm temp.conf

#sudo vi /etc/ssh/sshd_config
sudo service ssh restart
