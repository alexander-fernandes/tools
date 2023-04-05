#!/bin/bash
# -------------------------------------------------------------------------
# a sample shell script to print domain ip address hosting information such as
# location of server, city, ip address owner, country and network range.  
# this tool is useful to track spammers or for general research purpose. 
# -------------------------------------------------------------------------
 
# get all domains in arguments
_dom=$@
 
# die if no domains are given
[ $# -eq 0 ] && { echo "usage: $0 domain1.com domain2.com ..."; exit 1; }
# for domain in the list of domains
# get ip of the domain name and then grep whois
for d in $_dom
do
	_ip=$(host $d | grep 'has add' | head -1 | awk '{ print $4}')
	[ "$_ip" == "" ] && { echo "error: $d is not valid domain or dns error."; continue; }
	echo "getting information for domain: $d [ $_ip ]..."
	echo "+-----------------------------------------------+"
	whois "$_ip" | egrep -w 'OrgName:|City:|Country:|OriginAS:|NetRange:'
	echo ""
done