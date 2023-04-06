#!/bin/bash
#

if [ "$1" == "-help" ] || [ "$1" == "--help" ]; then
    echo "fetches public IP from 'ipinfo.io' as well as your local IP"
    exit 0;
fi

echo "fetching public IP from 'ipinfo.io'.. "

public=$(wget https://ipinfo.io/ip -qO -)
local=$(ifconfig | grep broadcast | awk '{print $2}')

echo "public IP is: $public"
echo "local IP is: $local"