#!/usr/bin/python3.4

# Copyright 2016 Daniel Dent (https://www.danieldent.com/)

import time
import urllib.parse
import urllib.request
import json


def get_current_services():
    headers = {
        'User-Agent': "prom-cowhand/0.1",
        'Accept': 'application/json'
    }
    req = urllib.request.Request('http://rancher-metadata/2015-12-19/containers', headers=headers)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf8 '))


def is_monitored_service(service):
    return 'labels' in service and 'com.danieldent.cowhand.prom.port' in service['labels']


def monitoring_config(service):
    return {
        "targets": [service['primary_ip'] + ':' + service['labels']['com.danieldent.cowhand.prom.port']],
        "labels": {
            'instance': service['hostname'],
            'name': service['name'],
            'service_name': service['service_name'],
            'stack_name': service['stack_name'],
        }
    }


def get_monitoring_config():
    return list(map(monitoring_config, filter(is_monitored_service, get_current_services())))


if __name__ == '__main__':
    while True:
        with open('/prom-cowhand-data/rancher.json', 'w') as config_file:
            json.dump(get_monitoring_config(), config_file, indent=2)
        time.sleep(30)
