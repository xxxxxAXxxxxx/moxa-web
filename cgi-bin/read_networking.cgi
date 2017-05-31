#!/bin/bash

echo "Content-type: text/html"
echo ""

text=$(grep "IP1=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-4)
html_text=$(sed "s/IP1: <\/font>.*/IP1: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html

html_text=$(sed "s/IP1: <INPUT.*/IP1: <INPUT name=\"lan_ip1\" type=\"text\" value=\"$text\" size=\"22\"><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html


text=$(grep "IP2=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-4)
html_text=$(sed "s/IP2: <\/font>.*/IP2: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html

html_text=$(sed "s/IP2: <INPUT.*/IP2: <INPUT name=\"lan_ip2\" type=\"text\" value=\"$text\" size=\"22\"><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html


text=$(grep "mac1=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-5)
html_text=$(sed "s/mac1: <\/font>.*/mac1: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html

html_text=$(sed "s/mask1: <INPUT.*/mask1: <INPUT name=\"lan_mask1\" type=\"text\" value=\"$text\" size=\"21\"><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html


text=$(grep "mac2=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-5)
html_text=$(sed "s/mac2: <\/font>.*/mac2: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html

html_text=$(sed "s/mask2: <INPUT.*/mask2: <INPUT name=\"lan_mask2\" type=\"text\" value=\"$text\"><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html


text=$(grep "L1multicast=[[:lower:]]" ../localhost/net.sh | cut --complement -c 1-12)
if [ $text == "on" ];
then
    html_text=$(sed "s/Multicast <INPUT name=\"lan1_multicast\".*/Multicast <INPUT name=\"lan1_multicast\" type=\"checkbox\" checked><\/td>/g" < ../localhost/page/networking/1.html)
else
    html_text=$(sed "s/Multicast <INPUT name=\"lan1_multicast\".*/Multicast <INPUT name=\"lan1_multicast\" type=\"checkbox\"><\/td>/g" < ../localhost/page/networking/1.html)
fi
echo "$html_text" > ../localhost/page/networking/1.html


text=$(grep "L2multicast=[[:lower:]]" ../localhost/net.sh | cut --complement -c 1-12)
if [ $text == "on" ];
then
    html_text=$(sed "s/Multicast <INPUT name=\"lan2_multicast\".*/Multicast <INPUT name=\"lan2_multicast\" type=\"checkbox\" checked><\/td>/g" < ../localhost/page/networking/1.html)
else
    html_text=$(sed "s/Multicast <INPUT name=\"lan2_multicast\".*/Multicast <INPUT name=\"lan2_multicast\" type=\"checkbox\"><\/td>/g" < ../localhost/page/networking/1.html)
fi
echo "$html_text" > ../localhost/page/networking/1.html

text=$(grep "Lan2=[[:lower:]]" ../localhost/net.sh | cut --complement -c 1-5)
if [ $text == "on" ];
then
    html_text=$(sed "s/<INPUT name=\"lan2\".*/<INPUT name=\"lan2\" type=\"checkbox\" checked> Lan2<\/td>/g" < ../localhost/page/networking/1.html)
else
    html_text=$(sed "s/<INPUT name=\"lan2\".*/<INPUT name=\"lan2\" type=\"checkbox\"> Lan2<\/td>/g" < ../localhost/page/networking/1.html)
fi
echo "$html_text" > ../localhost/page/networking/1.html

text=$(grep "Wlan=[[:lower:]]" ../localhost/net.sh | cut --complement -c 1-5)
if [ $text == "on" ];
then
    html_text=$(sed "s/<INPUT name=\"wlan\".*/<INPUT name=\"wlan\" type=\"checkbox\" checked> Wlan<\/td>/g" < ../localhost/page/networking/1.html)
else
    html_text=$(sed "s/<INPUT name=\"wlan\".*/<INPUT name=\"wlan\" type=\"checkbox\"> Wlan<\/td>/g" < ../localhost/page/networking/1.html)
fi
echo "$html_text" > ../localhost/page/networking/1.html

text=$(grep "WIP=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-4)
html_text=$(sed "s/Wlan IP: <INPUT.*/Wlan IP: <INPUT name=\"wlan_ip\" type=\"text\" value=\"$text\"><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html


text=$(grep "Wmac=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-5)
html_text=$(sed "s/Wlan mask: <INPUT.*/Wlan mask: <INPUT name=\"wlan_mask\" type=\"text\" value=\"$text\" size=\"18\"><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html

text=$(grep "WSId=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-5)
html_text=$(sed "s/Wlan SID: <INPUT.*/Wlan SID: <INPUT name=\"wlan_sid\" type=\"text\" value=\"$text\" size=\"18\"><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html

text=$(grep "DGW=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-4)
html_text=$(sed "s/DGW: <INPUT.*/DGW: <INPUT name=\"dgw\" type=\"text\" value=\"$text\" size=\"18\"><\/td>/g" < ../localhost/page/networking/1.html)
echo "$html_text" > ../localhost/page/networking/1.html

text=$(grep "Wmulticast=[[:lower:]]" ../localhost/net.sh | cut --complement -c 1-11)
if [ $text == "on" ];
then
    html_text=$(sed "s/Multicast <INPUT name=\"wlan_multicast\".*/Multicast <INPUT name=\"wlan_multicast\" type=\"checkbox\" checked><\/td>/g" < ../localhost/page/networking/1.html)
else
    html_text=$(sed "s/Multicast <INPUT name=\"wlan_multicast\".*/Multicast <INPUT name=\"wlan_multicast\" type=\"checkbox\"><\/td>/g" < ../localhost/page/networking/1.html)
fi
echo "$html_text" > ../localhost/page/networking/1.html

cat ../localhost/page/networking/1.html
exit 0




