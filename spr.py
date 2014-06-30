#!/usr/bin/env python2

import requests
import sys
import subprocess

class sprunge:
    def __init__(self):
        self.sprunge = sys.stdin.read()
        self.url = requests.post('http://sprunge.us/', data={'sprunge': self.sprunge}).text
        self.clipboardThatShit()
        print(self.url)

    def clipboardThatShit(self):
        lol = subprocess.Popen(['xsel', '-psbi'], stdin=subprocess.PIPE)
        lol.communicate(input=self.url)
        return True

if __name__ == "__main__":
    sprunge()

"""
<command> | curl -F 'sprunge=<-' http://sprunge.us
"""
