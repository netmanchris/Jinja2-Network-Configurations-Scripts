def get_vm_host_info(hostId):
    if auth == None or url == None:  # checks to see if the imc credentials are already available
        imc_creds()
    get_vm_host_info_url = "/imcrs/vrm/host?hostId="+str(hostId)
    f_url = url + get_vm_host_info_url
    payload = None
    r = requests.get(f_url, auth=auth,
                      headers=headers)  # creates the URL using the payload variable as the contents
    print (r.status_code)
    if r.status_code == 204:
        vm_host_info = json.loads(r.text)
        if vm_host_info is not None:
            return vm_host_info
        
    else:
        print("An Error has occured")__author__ = 'christopheryoung'
