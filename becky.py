#!/usr/bin/python3

import re
import requests
import urllib
from bs4 import BeautifulSoup

def get_explzh_version():
    url = 'https://www.rimarts.co.jp/becky-j.htm'
    ua = 'softverupcheck'

    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")

    for line in soup.find_all('a'):
        text = line.get_text()
        m = re.match('Becky! Internet Mail Ver.2 \(([0-9\.]*)\)', text)
        if m:
            return m.group(1)


if __name__ == '__main__':
    version = get_explzh_version()
    print(version)
