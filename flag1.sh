# curl -s -N http://$1:1574/ | grep -o 'flag1{.*}'
curl -s -N http://$1:$2/ | grep -o 'flag1{.*}'