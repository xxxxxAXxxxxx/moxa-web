#!/bin/bash



IP1=123
IP2=123123
mac1=23123
mac2=123123
L1multicast=on
L2multicast=
DGW=3

WIP=
Wmac=
Wmulticast=
WSId=

Wlan=
Lan2=on

config_wlan()
{
#ifconfig wlan0 down
iwconfig wlan0 mode ad-hoc
iwconfig wlan0 channel 4
iwconfig wlan0 Bit 54Mb/s
iwconfig wlan0 essid 'UEP-MPK_adhoc'
ifconfig wlan0 192.168.4.127 netmask 255.255.255.0 up
ifconfig wlan0 up
#route add -net 224.0.0.0 netmask 240.0.0.0 wlan0
#echo 1 > /proc/sys/net/ipv4/ip_forward
#iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
}

config_eth()
{
ifconfig eth0 192.168.127.198 netmask 255.255.255.0 up
route add -net 224.0.0.0 netmask 240.0.0.0 eth0
}

sw=`ifconfig`
if [[ "$sw" == *wlan* ]]
then
    echo "config_wlan begin"
    config_wlan
    echo "config_wlan end"
    echo "config_fired begin"
    config_eth    
    echo "config_fired end"

else
    echo "config_fired begin"
    config_eth    
    echo "config_fired end"
fi          
