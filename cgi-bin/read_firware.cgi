#!/bin/bash

echo "Content-type: text/html"
echo ""


text=$(grep "IP1=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-4)
html_text=$(sed "s/IP1:.*/IP1: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html

text=$(grep "IP2=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-4)
html_text=$(sed "s/IP2:.*/IP2: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html

text=$(grep "mac1=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-5)
html_text=$(sed "s/mac1:.*/mac1: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html

text=$(grep "mac2=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-5)
html_text=$(sed "s/mac2:.*/mac2: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html

#ТЕСТ Надо добавить версии файлов old_ksa.xml для последующего выбора.

#Выковыриваем имена старых версий файлов из файла old_version
text_1=$(tail ../localhost/ksa_old/old_version.txt | sed -n '1p')
text_2=$(tail ../localhost/ksa_old/old_version.txt | sed -n '2p')
text_3=$(tail ../localhost/ksa_old/old_version.txt | sed -n '3p')
text_4=$(tail ../localhost/ksa_old/old_version.txt | sed -n '4p')
text_5=$(tail ../localhost/ksa_old/old_version.txt | sed -n '5p')
text_6=$(tail ../localhost/ksa_old/old_version.txt | sed -n '6p')
text_7=$(tail ../localhost/ksa_old/old_version.txt | sed -n '7p')
text_8=$(tail ../localhost/ksa_old/old_version.txt | sed -n '8p')
text_9=$(tail ../localhost/ksa_old/old_version.txt | sed -n '9p')
text_10=$(tail ../localhost/ksa_old/old_version.txt | sed -n '10p')

number=1

if [ "$text_10" != "" ];
then
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\">$text_10<\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
else
:
fi

if [ "$text_9" != "" ];
then
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\">$text_9<\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
else
:
fi


if [ "$text_8" != "" ];
then
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\">$text_8<\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
else
:
fi


if [ "$text_7" != "" ];
then
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\">$text_7<\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
else
:
fi

if [ "$text_6" != "" ];
then
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\">$text_6<\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
else
:
fi

if [ "$text_5" != "" ];
then
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\">$text_5<\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
else
:
fi

if [ "$text_4" != "" ];
then
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\">$text_4<\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
else
:
fi

if [ "$text_3" != "" ];
then
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\">$text_3<\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
else
:
fi

if [ "$text_2" != "" ];
then
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\">$text_2<\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
else
:
fi

if [ "$text_1" != "" ];
then
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\">$text_1<\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
else
:
fi

while (( "$number" < "11" ))
do
html_text=$(sed "s/<option value=\"$number\".*/<option value=\"$number\"><\/option>/g" < ../localhost/page/firware/3.html)
echo "$html_text" > ../localhost/page/firware/3.html
number=$(($number + 1))
done

cat ../localhost/page/firware/3.html

exit 0

