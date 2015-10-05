#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a small utility that helps to retrieve
all FOIA requests from FragDenStaat.de.
"""

import sys
from urllib.parse import urljoin
import requests
import json

BASE_URL = 'https://fragdenstaat.de'
START = '/api/v1/request/?offset=0&limit=100'


def get_requests():
    i = 0
    with sys.stdout as f:
        url = urljoin(BASE_URL, START)

        while True:
            i += 100
            r = requests.get(url)

            assert r.ok
            json_content = r.json()

            for el in json_content['objects']:
                f.write(json.dumps(el))
                f.write('\n')

            if json_content['meta']['next']:
                url = urljoin(BASE_URL, json_content['meta']['next'])
            else:
                return

if __name__ == '__main__':
    get_requests()
