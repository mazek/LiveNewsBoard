#!/usr/bin/python
# coding: utf-8

import requests
import json
import subprocess
import time

AUTHOR = 'jan dlugosz'


def get_payload(message):
    timestamp = int(time.time())
    payload = {
        'author': AUTHOR,
        'timestamp': timestamp,
        'sec_level': 0,
        'priority': 0,
        'source': 'twitter',
        'message': message
    }
    return payload


def get_fortune_output():
    return subprocess.check_output(["/usr/local/bin/fortune",
                                    "-s", "linuxcookie"])


def get_fortune_payload():
    return get_payload(get_fortune_output())


def put_to_dashboard(payload):
    headers = {'Content-Type': 'application/json'}
    r = requests.post('http://localhost:5000/lwb/api/v1.0/posts',
                      headers=headers, data=json.dumps(payload))
    return r.content


payload = get_fortune_payload()
r = put_to_dashboard(payload)
print(r)
