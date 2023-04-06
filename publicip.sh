#!/bin/bash
#

if [ "$1" == "-help" ] || [ "$1" == "--help" ]; then
    echo "fetching public IP from 'ipinfo.io'.. "
    exit 0;
fi

result=$(wget https://ipinfo.io/ip -qO -)

echo "public IP is: $result"