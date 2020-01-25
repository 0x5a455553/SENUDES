#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests


def cls():
    os.system(('cls' if os.name == 'nt' else 'clear'))

cls()

sig = '''\033[33m
 .---..---..-..-..-..-..--. .---..---.
  \ \ | |- | .` || || || \ \| |-  \ \ 
 `---'`---'`-'`-'`----'`-'-'`---'`---'\033[0m
 lf@zelensky:~$
'''

def dor(api):
    try:
        links    = 'https://api.sendgrid.com/v3/user/credits'
        payload  = '{}'
        headers  = {'authorization': 'Bearer ' + api}
        response = \
                   requests.request('GET', links, data=payload, headers=headers)
        if 'total' in response.text:
            print '\033[32m[+] ' + api + '\n\033[37m' + response.text + '\033[0m'
            open('live-apikey.txt', 'a').write(api + '\n' + response.text + '\n')
        else:
            print '\033[31m[-] ' + api + '\033[0m'
    except:
        pass


def ler():
    print sig
    list = \
        [line.rstrip('\n') for line in open(raw_input('\033[33m [API List] : \033[0m'))]
    print ''
    for api in list:
        try:
            dor(api)
        except:
            pass

ler()

print "\n\033[33m SAVED! [live-apikey.txt]\033[0m"