#!/bin/bash

echo "Content-type: text/html"
echo ""

text=$(grep "IP1=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-4)
html_text=$(sed "s/IP1:.*/IP1: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/serial/2.html)
echo "$html_text" > ../localhost/page/serial/2.html

text=$(grep "IP2=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-4)
html_text=$(sed "s/IP2:.*/IP2: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/serial/2.html)
echo "$html_text" > ../localhost/page/serial/2.html

text=$(grep "mac1=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-5)
html_text=$(sed "s/mac1:.*/mac1: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/serial/2.html)
echo "$html_text" > ../localhost/page/serial/2.html

text=$(grep "mac2=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-5)
html_text=$(sed "s/mac2:.*/mac2: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/serial/2.html)
echo "$html_text" > ../localhost/page/serial/2.html


text=$(grep "setinterface /dev/ttyM0" ../localhost/com_iface_conf.sh | cut --complement -c 1-24,26- )
if [ $text == "1" ];
then
    html_text=$(sed "s/serial1_none.*/serial1_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_232.*/serial1_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_422.*/serial1_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_485_2.*/serial1_rs_485_2\" selected> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_485_4.*/serial1_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "2" ];
then
    html_text=$(sed "s/serial1_none.*/serial1_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_232.*/serial1_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_422.*/serial1_rs_422\" selected> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_485_2.*/serial1_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_485_4.*/serial1_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "3" ];
then
    html_text=$(sed "s/serial1_none.*/serial1_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_232.*/serial1_rs_232\" selected> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_422.*/serial1_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_485_2.*/serial1_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_485_4.*/serial1_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "4" ];
then
    html_text=$(sed "s/serial1_none.*/serial1_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_232.*/serial1_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_422.*/serial1_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_485_2.*/serial1_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_485_4.*/serial1_rs_485_4\" selected> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
else 
    html_text=$(sed "s/serial1_none.*/serial1_none\" selected><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_232.*/serial1_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_422.*/serial1_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_485_2.*/serial1_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial1_rs_485_4.*/serial1_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

fi

text=$(grep "setinterface /dev/ttyM1" ../localhost/com_iface_conf.sh | cut --complement -c 1-24,26- )
if [ $text == "1" ];
then
    html_text=$(sed "s/serial2_none.*/serial2_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_232.*/serial2_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_422.*/serial2_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_485_2.*/serial2_rs_485_2\" selected> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_485_4.*/serial2_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "2" ];
then
    html_text=$(sed "s/serial2_none.*/serial2_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_232.*/serial2_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_422.*/serial2_rs_422\" selected> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_485_2.*/serial2_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_485_4.*/serial2_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "3" ];
then
    html_text=$(sed "s/serial2_none.*/serial2_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_232.*/serial2_rs_232\" selected> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_422.*/serial2_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_485_2.*/serial2_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_485_4.*/serial2_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "4" ];
then
    html_text=$(sed "s/serial2_none.*/serial2_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_232.*/serial2_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_422.*/serial2_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_485_2.*/serial2_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_485_4.*/serial2_rs_485_4\" selected> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
else 
    html_text=$(sed "s/serial2_none.*/serial2_none\" selected><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_232.*/serial2_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_422.*/serial2_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_485_2.*/serial2_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial2_rs_485_4.*/serial2_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

fi


text=$(grep "setinterface /dev/ttyM2" ../localhost/com_iface_conf.sh | cut --complement -c 1-24,26- )
if [ $text == "1" ];
then
    html_text=$(sed "s/serial3_none.*/serial3_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_232.*/serial3_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_422.*/serial3_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_485_2.*/serial3_rs_485_2\" selected> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_485_4.*/serial3_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "2" ];
then
    html_text=$(sed "s/serial3_none.*/serial3_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_232.*/serial3_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_422.*/serial3_rs_422\" selected> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_485_2.*/serial3_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_485_4.*/serial3_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "3" ];
then
    html_text=$(sed "s/serial3_none.*/serial3_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_232.*/serial3_rs_232\" selected> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_422.*/serial3_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_485_2.*/serial3_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_485_4.*/serial3_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "4" ];
then
    html_text=$(sed "s/serial3_none.*/serial3_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_232.*/serial3_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_422.*/serial3_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_485_2.*/serial3_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_485_4.*/serial3_rs_485_4\" selected> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
else 
    html_text=$(sed "s/serial3_none.*/serial3_none\" selected><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_232.*/serial3_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_422.*/serial3_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_485_2.*/serial3_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial3_rs_485_4.*/serial3_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

fi


text=$(grep "setinterface /dev/ttyM3" ../localhost/com_iface_conf.sh | cut --complement -c 1-24,26- )
if [ $text == "1" ];
then
    html_text=$(sed "s/serial4_none.*/serial4_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_232.*/serial4_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_422.*/serial4_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_485_2.*/serial4_rs_485_2\" selected> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_485_4.*/serial4_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "2" ];
then
    html_text=$(sed "s/serial4_none.*/serial4_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_232.*/serial4_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_422.*/serial4_rs_422\" selected> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_485_2.*/serial4_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_485_4.*/serial4_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "3" ];
then
    html_text=$(sed "s/serial4_none.*/serial4_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_232.*/serial4_rs_232\" selected> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_422.*/serial4_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_485_2.*/serial4_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_485_4.*/serial4_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

elif [ $text == "4" ];
then
    html_text=$(sed "s/serial4_none.*/serial4_none\"><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_232.*/serial4_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_422.*/serial4_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_485_2.*/serial4_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_485_4.*/serial4_rs_485_4\" selected> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
else 
    html_text=$(sed "s/serial4_none.*/serial4_none\" selected><\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_232.*/serial4_rs_232\"> RS-232 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_422.*/serial4_rs_422\"> RS-422 <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_485_2.*/serial4_rs_485_2\"> RS-485-2wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html
    html_text=$(sed "s/serial4_rs_485_4.*/serial4_rs_485_4\"> RS-485-4wire <\/OPTION>/g" < ../localhost/page/serial/2.html)
    echo "$html_text" > ../localhost/page/serial/2.html

fi

cat ../localhost/page/serial/2.html
exit 0


