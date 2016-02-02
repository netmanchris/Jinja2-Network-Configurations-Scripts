from jinja2 import Environment, FileSystemLoader, Template
import yaml
import json

ENV = Environment(loader=FileSystemLoader('./'))

with open("L3Fabricinputs.yaml") as inputfile:
    devglobals =  yaml.load(inputfile)

with open('devices.yaml') as inputfile:
    devs = yaml.load(inputfile)

for dev in devs:
    template = ENV.get_template("L3Fabric.j2")
    #print (template.render(devglobals=devglobals, dev=dev))
    with open(dev['sysname']+".cfg", "w") as file:
        file.write(template.render(devglobals=devglobals, dev=dev))

# Print dictionary generated from yaml    


# Render template and print generated config to console
#template = ENV.get_template("Comware5_Template.j2")
#print (template.render(network_global=network_global, device_values = device_values, site= site))

