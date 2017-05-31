#!/bin/bash


#Создаём каталог ksa_old и помещаем в него стыре версии ksa
date=$(date | sed 's/ /_/g')

if [ -e "../localhost/ksa_old" ];
then
:
else
mkdir ../localhost/ksa_old/
chmod 777 ../localhost/ksa_old/
touch ../localhost/ksa_old/old_version.txt
chmod 666 ../localhost/ksa_old/old_version.txt
fi

# Принимаем файл с сервера и пакуем в наш файл.
cat - > ../localhost/ksa.xml

#Проверяем на возможность заливки старого файла
number=$(cat ../localhost/ksa.xml |  sed -n '9p' | sed 's/\r$//')
if (("$number" <= "11"));
then
#Если выбран старый файл, то находим его название
#Название найдено, теперь просто переносим содержимое из сарого файла на место ksa.xml


num=0
i=10

while (( "$number" != "$num" ))
do
text=$(tail ../localhost/ksa_old/old_version.txt | sed -n "$i p")
if [ "$text" != "" ];
then
num=$(($num+1))
i=$(($i-1))
else
i=$(($i-1))
fi
done

cat ../localhost/ksa_old/$text > ../localhost/ksa.xml

html_text=$(sed "s/<td>Установлен.*/<td>Установлен файл ksa.xml:<font color='#FF8000'> $text<\/font><\/td>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
else
# FIXME - Если принимаем файл то вылезит ошибка синтаксиса, не знаю как по другому.
# Редактируем сам файл, убираем конфигурационные данные файла
text=$(sed '/------/d' < ../localhost/ksa.xml)
echo "$text" > ../localhost/ksa.xml

text=$(sed '/Content-Disposition:/d' < ../localhost/ksa.xml)
echo "$text" > ../localhost/ksa.xml

text=$(sed '/Content-Type:/d' < ../localhost/ksa.xml)
echo "$text" > ../localhost/ksa.xml

# Убираем непонятный символ ^M
text=$(sed 's/\r$//' <../localhost/ksa.xml)
echo "$text" > ../localhost/ksa.xml

# Убираем лишний пробел и теперь все хорошо!
text=$(sed '/./,$!d' <../localhost/ksa.xml)
echo "$text" > ../localhost/ksa.xml

#Для того чтобы создавалась маска нового загруженного файла, исправление бага по замене
cp ../localhost/ksa.xml ../localhost/ksa_old/ksa_$date.xml
chmod 666 ../localhost/ksa.xml ../localhost/ksa_old/ksa_$date.xml
text_version_ksa="ksa_$date.xml"
echo "$text_version_ksa" >> ../localhost/ksa_old/old_version.txt
html_text=$(sed "s/<td>Установлен.*/<td>Установлен файл ksa.xml:<font color='#FF8000'> $text_version_ksa<\/font><\/td>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
fi



./read_firware.cgi
exit 0
