#!/bin/bash


lan_ip1=`echo "$QUERY_STRING" | sed -n 's/^.*lan_ip1=\([^&]*\).*$/\1/p'| sed "s/%20/ /g"`
lan_ip2=`echo "$QUERY_STRING" | sed -n 's/^.*lan_ip2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
lan_mask1=`echo "$QUERY_STRING" | sed -n 's/^.*lan_mask1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
lan_mask2=`echo "$QUERY_STRING" | sed -n 's/^.*lan_mask2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
lan1_multicast=`echo "$QUERY_STRING" | sed -n 's/^.*lan1_multicast=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
lan2_multicast=`echo "$QUERY_STRING" | sed -n 's/^.*lan2_multicast=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
dgw=`echo "$QUERY_STRING" | sed -n 's/^.*dgw=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`


wlan_ip=`echo "$QUERY_STRING" | sed -n 's/^.*wlan_ip=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
wlan_mask=`echo "$QUERY_STRING" | sed -n 's/^.*lan_mask=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
wlan_multicast=`echo "$QUERY_STRING" | sed -n 's/^.*wlan_multicast=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
wlan_sid=`echo "$QUERY_STRING" | sed -n 's/^.*wlan_sid=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

wlan=`echo "$QUERY_STRING" | sed -n 's/^.*wlan=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
lan2=`echo "$QUERY_STRING" | sed -n 's/^.*lan2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

if [ $wlan == "on" ];
then
# Пустая команда
a="1"
else
wlan_ip=""
wlan_mask=""
wlan_multicast=""
wlan_sid=""
fi

if [ $lan2 == "on" ];
then
# Пустая команда
a="1"
else
lan_ip2=""
lan_mask2=""
lan2_multicast=""
fi

code=$(sed "s/^IP1=.*/IP1=$lan_ip1/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^IP2=.*/IP2=$lan_ip2/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^mac1=.*/mac1=$lan_mask1/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^mac2=.*/mac2=$lan_mask2/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^WIP=.*/WIP=$wlan_ip/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^Wmac=.*/Wmac=$wlan_mask/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^L1multicast=.*/L1multicast=$lan1_multicast/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^L2multicast=.*/L2multicast=$lan2_multicast/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^Wmulticast=.*/Wmulticast=$wlan_multicast/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^DGW=.*/DGW=$dgw/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^WSId=.*/WSId=$wlan_sid/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^Wlan=.*/Wlan=$wlan/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

code=$(sed "s/^Lan2=.*/Lan2=$lan2/g" <../localhost/net.sh)
echo "$code" > ../localhost/net.sh

./read_networking.cgi
exit 0
    