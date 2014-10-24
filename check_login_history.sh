#!/bin/sh
sudo cat /var/log/auth.log* | egrep Accepted
