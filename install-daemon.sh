#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

cp ntrs /etc/init.d/ntrs
chmod +x /etc/init.d/ntrs
update-rc.d ntrs defaults