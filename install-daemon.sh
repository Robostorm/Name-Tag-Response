#!/bin/bash
mkdir /opt/ntrs
cp * /opt/ntrs
cp ntrs /etc/init.d/ntrs
chmod +x /etc/init.d/ntrs
update-rc.d ntrs defaults