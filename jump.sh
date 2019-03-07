#!/bin/bash

FILENAME=/home_ldap/lpolak/scripts/jump/host_ip.txt

match_count=$(grep -c ^$1 $FILENAME)

if [ "$match_count" -eq "1" ]; then
  IP=`grep $1 $FILENAME | cut -d ' ' -f 2`
  ssh $IP

elif [ "$match_count" -gt "1" ]; then
  echo "More than one host matching provided hostname"

else
  echo "WARNING: No host $1 exists in ISIS database"
  echo "Trying: 'ssh $1'"
  ssh $1
fi
