#!/bin/bash





serial1=`echo "$QUERY_STRING" | sed -n 's/^.*serial1=\([^&]*\).*$/\1/p'| sed "s/%20/ /g" | cut --complement -c 1-8` 
serial2=`echo "$QUERY_STRING" | sed -n 's/^.*serial2=\([^&]*\).*$/\1/p'| sed "s/%20/ /g" | cut --complement -c 1-8` 
#Пока не реализованно
serial3=`echo "$QUERY_STRING" | sed -n 's/^.*serial3=\([^&]*\).*$/\1/p'| sed "s/%20/ /g" | cut --complement -c 1-8` 
serial4=`echo "$QUERY_STRING" | sed -n 's/^.*serial4=\([^&]*\).*$/\1/p'| sed "s/%20/ /g" | cut --complement -c 1-8` 

if [ $serial1 == "rs_232" ];
then
    #Файл конфигурации измениться, но работать не будет так как на moxa нет такого интерфейса
    code=$(sed "s/^setinterface \/dev\/ttyM0.*/setinterface \/dev\/ttyM0 3	\#set to RS-232/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial1 == "rs_422" ];
then
    code=$(sed "s/^setinterface \/dev\/ttyM0.*/setinterface \/dev\/ttyM0 2	\#set to RS-422/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial1 == "rs_485_2" ];
then
    code=$(sed "s/^setinterface \/dev\/ttyM0.*/setinterface \/dev\/ttyM0 1	\#set to RS-485 \(2wire\)/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial1 == "rs_485_4" ];
then
    #Файл конфигурации измениться, но работать не будет так как на moxa нет такого интерфейса
    code=$(sed "s/^setinterface \/dev\/ttyM0.*/setinterface \/dev\/ttyM0 4	\#set to RS-485 \(4wire\)/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh
else
    code=$(sed "s/^setinterface \/dev\/ttyM0.*/setinterface \/dev\/ttyM0 0	\#set to None/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

fi

if [ $serial2 == "rs_232" ];
then
    #Файл конфигурации измениться, но работать не будет так как на moxa нет такого интерфейса
    code=$(sed "s/^setinterface \/dev\/ttyM1.*/setinterface \/dev\/ttyM1 3	\#set to RS-232/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial2 == "rs_422" ];
then
    code=$(sed "s/^setinterface \/dev\/ttyM1.*/setinterface \/dev\/ttyM1 2	\#set to RS-422/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial2 == "rs_485_2" ];
then
    code=$(sed "s/^setinterface \/dev\/ttyM1.*/setinterface \/dev\/ttyM1 1	\#set to RS-485 \(2wire\)/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial2 == "rs_485_4" ];
then
    #Файл конфигурации измениться, но работать не будет так как на moxa нет такого интерфейса
    code=$(sed "s/^setinterface \/dev\/ttyM1.*/setinterface \/dev\/ttyM1 4	\#set to RS-485 \(4wire\)/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh
else
    code=$(sed "s/^setinterface \/dev\/ttyM1.*/setinterface \/dev\/ttyM1 0	\#set to None/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

fi


#Нет ещё дополнительных портов

if [ $serial3 == "rs_232" ];
then
    #Файл конфигурации измениться, но работать не будет так как на moxa нет такого интерфейса
    code=$(sed "s/^setinterface \/dev\/ttyM2.*/setinterface \/dev\/ttyM2 3	\#set to RS-232/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial3 == "rs_422" ];
then
    code=$(sed "s/^setinterface \/dev\/ttyM2.*/setinterface \/dev\/ttyM2 2	\#set to RS-422/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial3 == "rs_485_2" ];
then
    code=$(sed "s/^setinterface \/dev\/ttyM2.*/setinterface \/dev\/ttyM2 1	\#set to RS-485 \(2wire\)/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial3 == "rs_485_4" ];
then
    #Файл конфигурации измениться, но работать не будет так как на moxa нет такого интерфейса
    code=$(sed "s/^setinterface \/dev\/ttyM2.*/setinterface \/dev\/ttyM2 4	\#set to RS-485 \(4wire\)/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh
else    
    code=$(sed "s/^setinterface \/dev\/ttyM2.*/setinterface \/dev\/ttyM2 0	\#set to None/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

fi

if [ $serial4 == "rs_232" ];
then
    #Файл конфигурации измениться, но работать не будет так как на moxa нет такого интерфейса
    code=$(sed "s/^setinterface \/dev\/ttyM3.*/setinterface \/dev\/ttyM3 3	\#set to RS-232/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial4 == "rs_422" ];
then
    code=$(sed "s/^setinterface \/dev\/ttyM3.*/setinterface \/dev\/ttyM3 2	\#set to RS-422/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial4 == "rs_485_2" ];
then
    code=$(sed "s/^setinterface \/dev\/ttyM3.*/setinterface \/dev\/ttyM3 1	\#set to RS-485 \(2wire\)/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

elif [ $serial4 == "rs_485_4" ];
then
    #Файл конфигурации измениться, но работать не будет так как на moxa нет такого интерфейса
    code=$(sed "s/^setinterface \/dev\/ttyM3.*/setinterface \/dev\/ttyM3 4	\#set to RS-485 \(4wire\)/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh
else
    code=$(sed "s/^setinterface \/dev\/ttyM3.*/setinterface \/dev\/ttyM3 0	\#set to None/g" <../localhost/com_iface_conf.sh)
    echo "$code" > ../localhost/com_iface_conf.sh

fi

./read_serial.cgi
exit 0