__author__ = 'youngchr'

from jinja2 import Environment, FileSystemLoader, Template
import yaml

#This section is for testing only


with open("Provision_Clearpass_Input.yaml") as netglobal:
    network_global =  yaml.load(netglobal)


ENV = Environment(loader=FileSystemLoader('./'))


# Render template and print generated config to console
template = ENV.get_template("Provision_ClearPass_Config.j2")
print (template.render(network_global=network_global))


