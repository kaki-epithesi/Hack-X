#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass

#excluding http/https
target_url = "enter_your_target_url_here"

with open("enter_your_wordlist_location", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" +  word
        response = request(test_url)
        if response:
            print("[+] Disoverd directories >> " + test_url)
