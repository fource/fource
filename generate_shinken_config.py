#!/usr/bin/env python
#
# Generate Shinken configuration files
#


import fnmatch
from jinja2 import Template
import os

PWD = os.path.dirname(__file__)

EXTENSION_LIST = ['yml']
FOURCE_CONFIG_DIR = '/etc/fource'
CONFIG_DIR = os.path.join(PWD, 'config', 'checks')
HOST_TEMPLATE_FILE = os.path.join(PWD, 'config', 'shinken', 'host.j2')
SERVICE_TEMPLATE_FILE = os.path.join(PWD, 'config', 'shinken', 'service.j2')
GENERATE_FILE = os.path.join(PWD, 'dockerize', 'custom_configs', 'fource.cfg')


with open(HOST_TEMPLATE_FILE, 'r') as f:
    host_template = Template(f.read())
with open(SERVICE_TEMPLATE_FILE, 'r') as f:
    service_template = Template(f.read())

config_file_list = []
for root, dirnames, filenames in os.walk(CONFIG_DIR):
    for extension in EXTENSION_LIST:
        for filename in fnmatch.filter(filenames, '*.%s' % extension):
            config_file_list.append(os.path.join(root, filename))


config_dict = {}
for config_file in config_file_list:
    hostname = config_file.split('/')[-2]
    service = '.'.join(config_file.split('/')[-1].split('.')[:-1])
    vars_dict = {
        'hostname': hostname,
        'service': service,
        'path': '/'.join([FOURCE_CONFIG_DIR, config_file]),
    }
    host_config = host_template.render(**vars_dict)
    service_config = service_template.render(**vars_dict)

    if not config_dict.get(hostname):
        config_dict[hostname] = {'hostconfig': host_config}
    if not config_dict[hostname].get('services'):
        config_dict[hostname]['services'] = []
    config_dict[hostname]['services'].append(service_config)


with open(GENERATE_FILE, 'w') as f:
    for hostname, config in config_dict.items():
        f.write(config['hostconfig'])
        for service_config in config['services']:
            f.write(service_config)
            f.write('\n\n')
