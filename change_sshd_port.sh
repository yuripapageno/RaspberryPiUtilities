#!/bin/sh
# -*- coding: utf-8 -*-

PEPLINE=`Port $1`
sudo sed -e "s/^Port.*/$PEPLINE/g" test.conf
#sudo sed -e "s/^Port.*\n/Port $1\n/g" /etc/ssh/sshd_config

#sudo vi /etc/ssh/sshd_config
sudo service ssh restart


