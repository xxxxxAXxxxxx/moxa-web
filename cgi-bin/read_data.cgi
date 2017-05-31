#!/bin/bash

echo "Content-type: text/html"
echo ""

text=$(grep "IP1=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-4)
html_text=$(sed "s/IP1:.*/IP1: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/data/4.html)
echo "$html_text" > ../localhost/page/data/4.html

text=$(grep "IP2=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-4)
html_text=$(sed "s/IP2:.*/IP2: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/data/4.html)
echo "$html_text" > ../localhost/page/data/4.html

text=$(grep "mac1=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-5)
html_text=$(sed "s/mac1:.*/mac1: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/data/4.html)
echo "$html_text" > ../localhost/page/data/4.html

text=$(grep "mac2=[[:digit:]]" ../localhost/net.sh | cut --complement -c 1-5)
html_text=$(sed "s/mac2:.*/mac2: <\/font><font color='#FF8000'>$text<\/font><\/td>/g" < ../localhost/page/data/4.html)
echo "$html_text" > ../localhost/page/data/4.html

cat ../localhost/page/data/4.html
exit 0



