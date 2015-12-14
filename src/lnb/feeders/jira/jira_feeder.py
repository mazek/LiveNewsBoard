#!/usr/bin/python
# coding: utf-8

import requests
import json
import subprocess
import time
import config
from jira.client import JIRA


def get_payload(issue):
    timestamp = int(time.time())
    payload = {
        'author': issue.fields.reporter.name,
        'timestamp': timestamp,
        'sec_level': 0,
        'priority': 0,
        'source': 'jira',
        'message': issue.fields.summary
    }
    return payload


def get_jira_output():
    jira = JIRA(options={
        'server': config.JIRA_URL
    }, basic_auth=(config.LOGIN, config.PASSWORD))

    # Get an issue.
    issue = jira.issue('ZMIR-18098', fields='summary,reporter')
    return issue


def get_jira_payload():
    return get_payload(get_jira_output())


def put_to_dashboard(payload):
    headers = {'Content-Type': 'application/json'}
    r = requests.post('http://localhost:5000/lwb/api/v1.0/posts',
            headers=headers, data=json.dumps(payload)
    )
    return r.content


payload = get_jira_payload()
r = put_to_dashboard(payload)
print(r)
