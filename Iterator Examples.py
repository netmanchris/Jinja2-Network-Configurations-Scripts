__author__ = 'christopheryoung'

import yaml
from jinja2 import Environment, FileSystemLoader, Template


ENV = Environment(loader=FileSystemLoader('./'))

vlans = [{'name': 'management', 'description': 'management vlan', 'id': '10'},
         {'name': 'users', 'description': 'users vlan', 'id': '15'},
         {'name': 'phones', 'description': 'phones vlan', 'id': '16'},
         {'name': 'servers vlan', 'description': 'servers vlan', 'id': '20'},
         {'name': 'mobility vlan', 'description': 'mobility vlan', 'id': '30'},
         {'name': 'guest vlan', 'description': 'guest vlan', 'id': '40'}
         ]

text_file = ('''#vlan config
{% for vlan in vlans -%}
vlan {{ vlan['id'] }}
    name {{ vlan['name'] }}
    description vlan -  {{ vlan['description'] }}
{% endfor %}''')

template = Template(text_file)

print (template.render(vlans=vlans))
