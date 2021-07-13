#!/usr/bin/env python3
#
# standard imports
import urllib.request, urllib.error, urllib.parse
import re, sys


def fetcher():

    if len(sys.argv) < 2:
        print("No url given. Please input a url to scan.")
        url = input(": ")
    else:
        url = sys.argv[1]


    print(f"\nScanning {url} for emails..")

    response = urllib.request.Request(url)
    content = urllib.request.urlopen(response).read().decode('utf-8')

    # regex needs fine tuning, it picks up often on things that aren't emails
    # TODO: find emails containing a certain username, in any combination,
    # not case sensitive
    pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+[-a-zA-Z0-9._]+")
    emails = re.findall(pattern, content)

    print("\nPossible emails found:\n")
    for email in emails:
        print(f"\t- {email}")

    print("\n")


if __name__ == "__main__":
    fetcher()
