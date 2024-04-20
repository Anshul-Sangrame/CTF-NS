atob() {
    local ascii="$1"
    local binary=""

    for (( i=0; i<${#ascii}; i++ )); do
        char="${ascii:$i:1}"
        binary+="$(printf '%08d' $(bc <<< "ibase=8; obase=2; $char")) "
    done

    echo "$binary"
}

# # Usage example:
atob "Hello"