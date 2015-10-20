__author__ = 'christopheryoung'



from jinja2 import Environment, FileSystemLoader, Template
import yaml

ENV = Environment(loader=FileSystemLoader('./'))

with open("global.yaml") as netglobal:
    network_global =  yaml.load(netglobal)

with open("cisco_device.yaml")  as device:
    device_values = yaml.load(device)

with open('branch_site.yaml')as site:
    site = yaml.load(site)

# Print dictionary generated from yaml
print (network_global)

print (device_values)

# Render template and print generated config to console
template = ENV.get_template("Cisco_Template.j2")
print (template.render(network_global=network_global, device_values = device_values, site= site))

text_file = open("cisco_config.txt", "w")
print (template.render(network_global=network_global, device_values = device_values, site= site), file=text_file)

text_file.close

