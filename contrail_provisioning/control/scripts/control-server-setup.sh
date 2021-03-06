#!/usr/bin/env bash

if [ "`grep server /etc/puppet/puppet.conf`" ]; then
    chkconfig puppetagent on
    service puppetagent restart

    # allow puppet to retreive certificate from server
    tries=0
    while [ $tries -lt 10 ]; do
        x=$(ls -l /var/lib/puppet/ssl/certs | grep `hostname` | cut -d ' ' -f 3)
        if [ "$x" == "puppet" ]; then break; fi;
        tries=$(($tries + 1))
        echo "Waiting to obtain certificate from Puppet master"
        sleep 3
    done
fi

if [ -f /etc/lsb-release ] && (egrep -q 'DISTRIB_RELEASE.*16.04' /etc/lsb-release); then
    #setup script for contrail-control package under systemd
    for svc in control control-nodemgr dns named; do
            chkconfig contrail-$svc on
            service contrail-$svc restart
    done
else
    #setup script for contrail-control package under supervisord
    chkconfig supervisor-control on
    service supervisor-control restart
fi
