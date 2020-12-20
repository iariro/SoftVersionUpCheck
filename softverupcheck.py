#!/usr/bin/python3

import os
import re
import requests
import sys
import urllib
from bs4 import BeautifulSoup
import json
import explzh
import winscp

def line_notify(updates):
    token = "nPQEoC190nfvydJRbQmY75SY00Ygvt0CxsaXWoLTUUH"
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + token}
    for update in updates:
        payload = {"message": '%s %s->%s' % (update['app'],
                                             update['version_prev'],
                                             update['version'])}
        requests.post(url, headers=headers, data=payload)


if __name__ == '__main__':
    versions_file_name = '/home/pi/doc/private/python/softverupcheck/versions.json'
    if os.path.exists(versions_file_name):
        versions = json.load(open(versions_file_name))
    else:
        versions = {}

    updates = []
    apps = {'Explzh': explzh.get_explzh_version,
            'WinSCP': winscp.get_winscp_version}
    for app, get_version in apps.items():
        version = get_version()
        version_prev = None
        if app in versions:
            version_prev = versions[app]
        if version_prev != version:
            versions[app] = version
            updates.append({'app': app,
                            'version_prev': version_prev,
                            'version': version})

    if len(updates) > 0:
        line_notify(updates)

        with open(versions_file_name, 'w') as file:
            json.dump(versions, file)
