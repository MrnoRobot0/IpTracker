from netaddr import valid_ipv4
import termcolor
import requests
import json
import sys


class Tracker():
    def __init__(self):
        self.ip = None

    def get_ip(self):
        if sys.argv[1:]:
            if valid_ipv4(sys.argv[1]):
                self.ip = sys.argv[1]
            else:
                print(termcolor.colored("[-] Match Not Found as Ip", "red", attrs=['bold']))
        else:
            print(termcolor.colored("\n[-] Any Ip provided.", "red", attrs=['bold']))
            sys.exit(1)

    def get_info(self):
        r = json.loads(requests.get("https://ipinfo.io/{}/json".format(self.ip)).text)
        info = {
            "city": r['city'],
            "region": r['region'],
            "country":r['country'],
            "loc": r['loc'],
            "postal": r['postal']
        }
        return info

    def print_info(self):
        info = self.get_info()
        for i in info:
            print(termcolor.colored("[+] ", "blue", attrs=['bold']) + termcolor.colored("{}: {}".format(i.capitalize(), info[i])))

    def main(self):
        self.get_ip()
        self.print_info()


if __name__ == '__main__':
    t = Tracker()
    t.main()
