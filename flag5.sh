curl -s -N  http://10.200.33.61:1594 | grep -o '<meta name="description" content=".*">' | grep -o 'content=".*"' | sed 's/"//g; s/content=//g; s/"/ /g' | base64 -d && echo