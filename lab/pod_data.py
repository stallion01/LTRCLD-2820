from flask import session
from datetime import datetime

def get_lab_data():
    """
    This data array is to get back into the lab to provide information needed by the
    jinja templates.
    """
    abstract='''Kubernetes continues to gain industry adoption as a enterprise class orchestration for container networking.
        Cisco ACI is the premier SDN platform in the industry. This is a marriage you need to see. In this lab you will configure
        the integration and learn the operational advantages that the integration provides you. If you are interested in Kubernetes
        and want to see how ACI can provide operational benefits, this is the session you need to sign up for!
        '''
    data= {
        "cl_id":                    "LTRCLD-2820",
        "cl_title":                 "Kubernetes, Hyperflex, ACI OH MY!",
        "cl_abstract":              abstract,
        "cl_lab_proctors":          ["Raj Chacko","Justin Barksdale"],
        "cl_lab_proctor_emails":    ["rajchack@cisco.com", "jusbarks@cisco.com"],
        "cl_lab_proctor_titles":    ["Technical Solutions Engineer, Commercial Sales", "Technical Solutions Engineer, Enterprise Sales"],
    }
    return data


def get_pod_data(pod):
    """
    This function returns back a dictionary that contains values that are used to inject
    into the JINJA templates. The call is done by the routes.py code base. Just passing the
    PODID to give back the values specific to that POD.
    """
    domain = ".ecatsrtpdmz.cisco.com"

    #IP Addresses
    apic_controllers = ["10.0.226.41", "10.0.226.42", "10.0.226.43", "10.0.226.43"]
    apic_prompt = ["apic1#", "apic2#", "apic3#", "apic3#"]
    vcenter_dns = "vcenter6.ecatsrtpdmz.cisco.com"
    vcenter_ip = "10.0.226.193"

    pod_numstr = "{:02}".format(pod)
    env_name = "acilab"

    # Credential popover example
    credential_popover = """<h4>DEV1
                                    <a target='_blank' href='%(apic_url)s'>
                                      <img src="/core/static/images/symbols/http_pointer.png" style="height:25px;" >
                                    </a>
                                    <a target='_blank' href='chrome-extension://iodihamcpbpeioajjeobimgagajmlibd/html/nassh.html#%(apic_stdnt_uname)s@%(apic_ip)s:22'>
                                      <img src="/core/static/images/symbols/ssh_pointer.png" style="height:25px;" >
                                    </a>
                         </h4>
                        <ul><li>Username: %(apic_stdnt_uname)s</li><li>Password: %(apic_stdnt_pass)s</li></ul>
                        <h4>DEV2
                                    <a target='_blank' href='%(vmw_url)s'>
                                    <img src="/core/static/images/symbols/http_pointer.png" style="height:25px;" >
                                    </a>
                        </h4>
                        <ul><li>Username: %(vmware_stdnt_uname)s</li><li>Password: %(vmware_stdnt_pass)s</li></ul>
                         <h4>Linux VM's</h4>
                         <ul><li>Master: %(master_ip)s
                         <a target="_blank" href="chrome-extension://iodihamcpbpeioajjeobimgagajmlibd/html/nassh.html#%(centos_uname)s@%(master_ip)s:22">
                            <img src="/core/static/images/symbols/ssh_pointer.png" style="height:20px;" >
                         </a>
                         </li></ul>
                         <ul><li>Node1: %(node1_ip)s
                          <a target="_blank" href="chrome-extension://iodihamcpbpeioajjeobimgagajmlibd/html/nassh.html#%(centos_uname)s@%(node1_ip)s:22">
                           <img src="/core/static/images/symbols/ssh_pointer.png" style="height:20px;" >
                         </a>
                         </li></ul>
                         <ul><li>Node2: %(node2_ip)s
                           <a target="_blank" href="chrome-extension://iodihamcpbpeioajjeobimgagajmlibd/html/nassh.html#%(centos_uname)s@%(node2_ip)s:22">
                            <img src="/core/static/images/symbols/ssh_pointer.png" style="height:20px;" >
                         </a>
                         </li></ul>
                         <hr/>
                        <ul><li>Username: %(centos_uname)s</li><li>Password: %(centos_pass)s</li></ul>
                        """ % {
                            "apic_url": "https://"+apic_controllers[int(pod_numstr[:1])],
                            "apic_ip": apic_controllers[int(pod_numstr[:1])],
                            "vmw_url": "http://"+vcenter_ip+"/ui",
                            "apic_stdnt_uname": "student1",
                            "apic_stdnt_pass": "password3",
                            "vmware_stdnt_uname": "student_x",
                            "vmware_stdnt_pass": "password1",
                            "centos_uname": "student_x",
                            "centos_pass": "password2",
                            "master_ip": "10.0.0.1",
                            "node1_ip": "10.0.0.2",
                            "node2_ip": "10.0.0.3"
                             }

    data = {
        # This dictionary is what will be passed to the JINJA template and references there.
        # You can utilize python code to generate these values as needed.
        "lab_id":                       get_lab_data()['cl_id'],
        "lab_preso_url":                "https://svs-rtp-dmz-files.ciscolive.com/<bucket>/<file>",
        #Credential Popover values with the data and either to show or not in core template
        "credential_popover_data":      credential_popover,
        "credential_popover_show":      True,
        # POD identifiers
        "pod_id":                       pod,
        "pod_numstr":                   pod_numstr,
        "pname":                        "pod{:02}".format(pod),
        "editor":                       "vi",
        "container_prompt":             "root@ubuntu-ciscolive:/#",
        "container_alpine_prompt":      "/ #",
        "linux_prompt_venv":            "({}) pod{:02} ~ $ ".format(env_name, pod ),
    }
    return data
