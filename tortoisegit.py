#!/usr/bin/python3

import re
import requests
import urllib
from bs4 import BeautifulSoup

def get_version():
    url = 'https://tortoisegit.org/download/'
    ua = 'softverupcheck'

    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")

    for line in soup.find_all('strong'):
        text = line.get_text()
        m = re.match('The current stable version is: ([0-9\.]*)', text)
        if m:
            return m.group(1)


if __name__ == '__main__':
    version = get_version()
    print(version)
