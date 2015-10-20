__author__ = 'youngchr'

from jinja2 import Environment, FileSystemLoader, Template
import yaml

#This section is for testing only

network_global = yaml.load('''radius_server:
- {server_ip: 10.101.0.200, auth_key: my_shared_secret}
- {server_ip: 10.101.0.201, auth_key: my_shared_secret}
- {server_ip: 10.101.0.202, auth_key: my_shared_secret}
dhcp_server:
- {server_ip: 10.3.10.2}
- {server_ip: 10.101.254.1}
- {server_ip: 10.101.0.202}
dhcp_snooping_vlans:
    vlans: [2, 3, 4, 5, 6]
trust_port_list:
- interface: "1/23"
- interface: "1/24"''')

ENV = Environment(loader=FileSystemLoader('./'))


# Render template and print generated config to console
template = ENV.get_template("Provision_ClearPass_Config.j2")
print (template.render(network_global=network_global))
