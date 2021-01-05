#!/usr/bin/python3

import re
import requests
import urllib
from bs4 import BeautifulSoup

def get_version():
    url = 'https://forest.watch.impress.co.jp/library/software/utf8teraterm/'
    ua = 'softverupcheck'

    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    for line in soup.select("div[class='list-tlt-spec']"):
        app = line.select_one('h3').get_text()
        version = line.select_one('dd').get_text()
        if app == 'Tera Term':
            m = re.match('(v[0-9\.]*).*', version)
            if m:
                return m.group(1)


if __name__ == '__main__':
    print(get_version())
