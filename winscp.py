#!/usr/bin/python3

import re
import requests
import urllib
from bs4 import BeautifulSoup

def get_version():
    url = 'https://winscp.net/eng/download.php'
    ua = 'softverupcheck'

    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    for line in soup.find_all('a'):
        m = re.match('Download WinSCP ([0-9\.]*) ', line.get_text())
        if m:
            return m.group(1)


if __name__ == '__main__':
    print(get_version())
