__author__ = 'youngchr'

from jinja2 import Environment, FileSystemLoader, Template
import yaml, datetime

#This section is for testing only


def main():
    with open("Provision_Clearpass_Input.yaml") as netglobal:
        network_global =  yaml.load(netglobal)
    ENV = Environment(loader=FileSystemLoader('./'))
    # Render template and print generated config to console
    template = ENV.get_template("Provision_ClearPass_Config.j2")
    current_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d %H%M%S')
    config_name = str("Provision_Clearpass"+current_date+".txt")
    with open(config_name, "w") as text_file:
        print (template.render(network_global=network_global), file=text_file)




if __name__ == "__main__":
    main()