#!/usr/bin/env python3
__author__      = "Joy Ghosh"
__copyright__   = "Copyright 2021, SYSTEM00 SECURITY"
from colorama import Fore, Back, Style
import requests
import argparse
import json
def logo():
    print(Fore.RED+"""

█▀▀ █ ▀█▀ ▄▄ █▀▀ █░█ █▀▀
█▄█ █ ░█░ ░░ █▄▄ ▀▄▀ ██▄
------------------------------
Find Cve Exploits from github [SYSTEM00 SECURITY]
------------------------------
    """+Fore.WHITE)
try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", help="Enter CVE release year Ex: -y '2020' ", type=str)
    parser.add_argument("-cve", "--cve", help="Enter CVE Number Ex: -cve 'CVE-2020-1423' ", type=str)
    args = parser.parse_args()
except TypeError:
    print("Type -h To See all the options")
except():
    exit()
def cve():
    try:
        cve_url=requests.get('https://raw.githubusercontent.com/System00-Security/PoC-in-GitHub/master/'+args.year+'/'+args.cve+'.json')
        cve_text=cve_url.json()
        cve_conv=cve_text[0]
        cve_dump=json.dumps(cve_conv)
        cve_load=json.loads(cve_dump)
        print(Fore.GREEN+'[+] Description : '+Fore.BLUE+cve_load['description']+Fore.WHITE)
        print(Fore.GREEN+'[+] Git Url : '+Fore.BLUE+cve_load['html_url']+Fore.WHITE)
    except TypeError:
        print(Fore.RED+"CVE Not found / Other Problem"+Fore.WHITE)
    except:
        exit()
try:
    logo()
    cve()
except KeyboardInterrupt:
    print("CTRL+C Detected Stoping")
except:
    exit()
