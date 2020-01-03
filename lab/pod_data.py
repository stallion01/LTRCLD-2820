from flask import session
from datetime import datetime
import random

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

def get_uplnk_if_mac(pod, interface):
    data = {
        1:  {1: "A0:EC:F9:BF:03:E7", 2: "A0:EC:F9:BF:03:E8"},
        2:  {1: "A0:EC:F9:BF:18:80", 2: "A0:EC:F9:BF:18:81"},
        3:  {1: "A0:EC:F9:85:5D:B6", 2: "A0:EC:F9:85:5D:B7"},
        4:  {1: "24:E9:B3:FD:07:E8", 2: "24:E9:B3:FD:07:E9"},
        5:  {1: "00:2A:6A:67:74:EF", 2: "00:2A:6A:67:74:F0"},
        6:  {1: "24:E9:B3:FD:AA:FE", 2: "24:E9:B3:FD:AA:FF"},
        7:  {1: "B8:38:61:AF:2C:2E", 2: "B8:38:61:AF:2C:2F"},
        8:  {1: "B8:38:61:AF:2D:25", 2: "B8:38:61:AF:2D:26"},
        9:  {1: "B8:38:61:AF:29:A2", 2: "B8:38:61:AF:29:A3"},
        10: {1: "B8:38:61:F6:BD:34", 2: "B8:38:61:F6:BD:35"},
        11: {1: "B8:38:61:BC:59:76", 2: "B8:38:61:BC:59:77"},
        12: {1: "B8:38:61:BC:31:D4", 2: "B8:38:61:BC:31:D5"},
        13: {1: "B8:38:61:46:92:F8", 2: "B8:38:61:46:92:F9"},
        14: {1: "B8:38:61:46:89:16", 2: "B8:38:61:46:89:17"},
        15: {1: "B8:38:61:AF:19:04", 2: "B8:38:61:AF:19:05"},
        16: {1: "3C:08:F6:16:2E:4A", 2: "3C:08:F6:16:2E:4B"},

    }
    return data[pod][interface].upper()


def public_subnet_info(pod,subnet_select):
    subnet_dict={"node": 144, "extern_dynamic": 145, "extern_static": 146}
    subnet = subnet_dict[subnet_select]
    data = {
        1:  {"subnet": "10.0.%d.0" % subnet,   "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.1" % subnet,   "n1": "10.0.%d.3" % subnet, "n2": "10.0.%d.4" % subnet, "n3": "10.0.%d.5" % subnet },
        2:  {"subnet": "10.0.%d.8" % subnet,   "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.9" % subnet,   "n1": "10.0.%d.11" % subnet, "n2": "10.0.%d.12" % subnet, "n3": "10.0.%d.13" % subnet },
        3:  {"subnet": "10.0.%d.16" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.17" % subnet,  "n1": "10.0.%d.19" % subnet, "n2": "10.0.%d.20" % subnet, "n3": "10.0.%d.21" % subnet   },
        4:  {"subnet": "10.0.%d.24" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.25" % subnet,  "n1": "10.0.%d.27" % subnet, "n2": "10.0.%d.28" % subnet, "n3": "10.0.%d.29" % subnet   },
        5:  {"subnet": "10.0.%d.32" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.33" % subnet,  "n1": "10.0.%d.35" % subnet, "n2": "10.0.%d.36" % subnet, "n3": "10.0.%d.37" % subnet   },
        6:  {"subnet": "10.0.%d.40" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.41" % subnet,  "n1": "10.0.%d.43" % subnet, "n2": "10.0.%d.44" % subnet, "n3": "10.0.%d.45" % subnet   },
        7:  {"subnet": "10.0.%d.48" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.49" % subnet,  "n1": "10.0.%d.51" % subnet, "n2": "10.0.%d.52" % subnet, "n3": "10.0.%d.53" % subnet   },
        8:  {"subnet": "10.0.%d.56" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.57" % subnet,  "n1": "10.0.%d.59" % subnet, "n2": "10.0.%d.60" % subnet, "n3": "10.0.%d.61" % subnet   },
        9:  {"subnet": "10.0.%d.64" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.65" % subnet,  "n1": "10.0.%d.67" % subnet, "n2": "10.0.%d.68" % subnet, "n3": "10.0.%d.69" % subnet   },
        10: {"subnet": "10.0.%d.72" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.73" % subnet,  "n1": "10.0.%d.75" % subnet, "n2": "10.0.%d.76" % subnet, "n3": "10.0.%d.77" % subnet   },
        11: {"subnet": "10.0.%d.80" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.81" % subnet,  "n1": "10.0.%d.83" % subnet, "n2": "10.0.%d.84" % subnet, "n3": "10.0.%d.85" % subnet   },
        12: {"subnet": "10.0.%d.88" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.89" % subnet,  "n1": "10.0.%d.91" % subnet, "n2": "10.0.%d.92" % subnet, "n3": "10.0.%d.93" % subnet   },
        13: {"subnet": "10.0.%d.96" % subnet,  "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.97" % subnet,  "n1": "10.0.%d.99" % subnet, "n2": "10.0.%d.100" % subnet, "n3": "10.0.%d.101" % subnet   },
        14: {"subnet": "10.0.%d.104" % subnet, "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.105" % subnet, "n1": "10.0.%d.107" % subnet, "n2": "10.0.%d.108" % subnet, "n3": "10.0.%d.109" % subnet  },
        15: {"subnet": "10.0.%d.112" % subnet, "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.113" % subnet, "n1": "10.0.%d.115" % subnet, "n2": "10.0.%d.116" % subnet, "n3": "10.0.%d.117" % subnet  },
        16: {"subnet": "10.0.%d.120" % subnet, "mask": "29", "lm":"255.255.255.248", "dg": "10.0.%d.121" % subnet, "n1": "10.0.%d.123" % subnet, "n2": "10.0.%d.124" % subnet, "n3": "10.0.%d.125" % subnet  },
}
    return data[pod]

def public_subnet_service_ip(pod, type ):
    subnet_types={"static":146, "dynamic":145}
    subnet = subnet_types[type]
    data = {
        1:  { "dg": "10.0.%d.1" % subnet,   "mylabapp": "10.0.%d.3" % subnet,  "gbapp":"10.0.%d.4" % subnet,   "gbapp-proxy": "10.0.%d.5" % subnet,   "gbapp_url": "gbapp-pod%02d" % pod },
        2:  { "dg": "10.0.%d.9" % subnet,   "mylabapp": "10.0.%d.11" % subnet, "gbapp":"10.0.%d.12" % subnet,  "gbapp-proxy": "10.0.%d.13" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        3:  { "dg": "10.0.%d.17" % subnet,  "mylabapp": "10.0.%d.19" % subnet, "gbapp":"10.0.%d.20" % subnet,  "gbapp-proxy": "10.0.%d.21" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        4:  { "dg": "10.0.%d.25" % subnet,  "mylabapp": "10.0.%d.27" % subnet, "gbapp":"10.0.%d.28" % subnet,  "gbapp-proxy": "10.0.%d.29" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        5:  { "dg": "10.0.%d.33" % subnet,  "mylabapp": "10.0.%d.35" % subnet, "gbapp":"10.0.%d.36" % subnet,  "gbapp-proxy": "10.0.%d.37" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        6:  { "dg": "10.0.%d.41" % subnet,  "mylabapp": "10.0.%d.43" % subnet, "gbapp":"10.0.%d.44" % subnet,  "gbapp-proxy": "10.0.%d.45" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        7:  { "dg": "10.0.%d.49" % subnet,  "mylabapp": "10.0.%d.51" % subnet, "gbapp":"10.0.%d.52" % subnet,  "gbapp-proxy": "10.0.%d.53" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        8:  { "dg": "10.0.%d.57" % subnet,  "mylabapp": "10.0.%d.59" % subnet, "gbapp":"10.0.%d.60" % subnet,  "gbapp-proxy": "10.0.%d.61" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        9:  { "dg": "10.0.%d.65" % subnet,  "mylabapp": "10.0.%d.67" % subnet, "gbapp":"10.0.%d.68" % subnet,  "gbapp-proxy": "10.0.%d.69" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        10: { "dg": "10.0.%d.73" % subnet,  "mylabapp": "10.0.%d.75" % subnet, "gbapp":"10.0.%d.76" % subnet,  "gbapp-proxy": "10.0.%d.77" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        11: { "dg": "10.0.%d.81" % subnet,  "mylabapp": "10.0.%d.83" % subnet, "gbapp":"10.0.%d.84" % subnet,  "gbapp-proxy": "10.0.%d.85" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        12: { "dg": "10.0.%d.89" % subnet,  "mylabapp": "10.0.%d.91" % subnet, "gbapp":"10.0.%d.92" % subnet,  "gbapp-proxy": "10.0.%d.93" % subnet,  "gbapp_url": "gbapp-pod%02d" % pod },
        13: { "dg": "10.0.%d.97" % subnet,  "mylabapp": "10.0.%d.99" % subnet, "gbapp":"10.0.%d.100" % subnet, "gbapp-proxy": "10.0.%d.101" % subnet, "gbapp_url": "gbapp-pod%02d" % pod },
        14: { "dg": "10.0.%d.105" % subnet, "mylabapp": "10.0.%d.107" % subnet,"gbapp":"10.0.%d.108" % subnet, "gbapp-proxy": "10.0.%d.109" % subnet, "gbapp_url": "gbapp-pod%02d" % pod },
        15: { "dg": "10.0.%d.113" % subnet, "mylabapp": "10.0.%d.115" % subnet,"gbapp":"10.0.%d.116" % subnet, "gbapp-proxy": "10.0.%d.117" % subnet, "gbapp_url": "gbapp-pod%02d" % pod },
        16: { "dg": "10.0.%d.121" % subnet, "mylabapp": "10.0.%d.123" % subnet,"gbapp":"10.0.%d.124" % subnet, "gbapp-proxy": "10.0.%d.125" % subnet, "gbapp_url": "gbapp-pod%02d" % pod },
}
    return data[pod]


def private_subnet_info(pod):
    data={
        "pod_subnet": "10.2%02d.0.0" % pod,
        "pod_dg": "10.2%02d.0.1" % pod,
        "pod_mask": "16",
        "pod_lm": "255.255.0.0",
        "node_service_subnet": "10.1%02d.2.0" % pod,
        "node_service_dg": "10.1%02d.2.1" % pod,
        "node_service_mask": "24",
        "node_service_lm": "255.255.255.0",
        "nodenet_master_ip": "10.1%02d.2.10" % pod,
        "nodenet_node1_ip": "10.1%02d.2.11" % pod,
        "nodenet_node2_ip": "10.1%02d.2.12" % pod,
    }
    return data

def floatpool(pod):
    data = {
        1:  {"subnet": "10.0.239.0",   "mask": "/29", "dg": "10.0.239.1",  "dhcps": "10.0.239.2", "dhcpe": "10.0.239.6" },
        2:  {"subnet": "10.0.239.8",   "mask": "/29", "dg": "10.0.239.9",  "dhcps": "10.0.239.10", "dhcpe": "10.0.239.14" },
        3:  {"subnet": "10.0.239.16",  "mask": "/29", "dg": "10.0.239.17",  "dhcps": "10.0.239.18", "dhcpe": "10.0.239.22" },
        4:  {"subnet": "10.0.239.24",  "mask": "/29", "dg": "10.0.239.25",  "dhcps": "10.0.239.26", "dhcpe": "10.0.239.30" },
        5:  {"subnet": "10.0.239.32",  "mask": "/29", "dg": "10.0.239.33",  "dhcps": "10.0.239.34", "dhcpe": "10.0.239.38" },
        6:  {"subnet": "10.0.239.40",  "mask": "/29", "dg": "10.0.239.41",  "dhcps": "10.0.239.42", "dhcpe": "10.0.239.46" },
        7:  {"subnet": "10.0.239.48",  "mask": "/29", "dg": "10.0.239.49",  "dhcps": "10.0.239.50", "dhcpe": "10.0.239.54" },
        8:  {"subnet": "10.0.239.56",  "mask": "/29", "dg": "10.0.239.57",  "dhcps": "10.0.239.58", "dhcpe": "10.0.239.62" },
        9:  {"subnet": "10.0.239.64",  "mask": "/29", "dg": "10.0.239.65",  "dhcps": "10.0.239.66", "dhcpe": "10.0.239.70" },
        10: {"subnet": "10.0.239.72",  "mask": "/29", "dg": "10.0.239.73",  "dhcps": "10.0.239.74", "dhcpe": "10.0.239.78" },
        11: {"subnet": "10.0.239.80",  "mask": "/29", "dg": "10.0.239.81",  "dhcps": "10.0.239.82", "dhcpe": "10.0.239.86" },
        12: {"subnet": "10.0.239.88",  "mask": "/29", "dg": "10.0.239.89",  "dhcps": "10.0.239.90", "dhcpe": "10.0.239.94" },
        13: {"subnet": "10.0.239.96",  "mask": "/29", "dg": "10.0.239.97",  "dhcps": "10.0.239.98", "dhcpe": "10.0.239.102" },
        14: {"subnet": "10.0.239.104", "mask": "/29", "dg": "10.0.239.105",  "dhcps": "10.0.239.106", "dhcpe": "10.0.239.110" },
        15: {"subnet": "10.0.239.112", "mask": "/29", "dg": "10.0.239.113",  "dhcps": "10.0.239.114", "dhcpe": "10.0.239.118" },
        16: {"subnet": "10.0.239.120", "mask": "/29", "dg": "10.0.239.121",  "dhcps": "10.0.239.122", "dhcpe": "10.0.239.126" },
}
    return data[pod]


def link_level_policy_group(pod):
    return {
        "name":                         "k8s_pod%02d_pg" % pod,
        "llpg":                         "k8s_10GB",
        "cdp":                          "k8s_CDP_enable",
        "lldp":                         "k8s_LLDP_enable",
        "pc":                           "k8s_LACP_active",
        "mcp":                          "k8s_MCP_enable",
        "l2":                           "k8s_L2_global"
    }

def pod_vm_info(pod):
    data =  \
        {
          1:{"node1":"10.0.222.11", "node2":"10.0.222.12","master":"10.0.222.13"},
          2:{"node1":"10.0.222.14", "node2":"10.0.222.15","master":"10.0.222.16"},
          3:{"node1":"10.0.222.17", "node2":"10.0.222.18","master":"10.0.222.19"},
          4:{"node1":"10.0.222.20", "node2":"10.0.222.21","master":"10.0.222.22"},
          5:{"node1":"10.0.222.23", "node2":"10.0.222.24","master":"10.0.222.25"},
          6:{"node1":"10.0.222.26", "node2":"10.0.222.27","master":"10.0.222.28"},
          7:{"node1":"10.0.222.29", "node2":"10.0.222.30","master":"10.0.222.31"},
          8:{"node1":"10.0.222.32", "node2":"10.0.222.33","master":"10.0.222.34"},
          9:{"node1":"10.0.222.35", "node2":"10.0.222.36","master":"10.0.222.37"},
         10:{"node1":"10.0.222.38", "node2":"10.0.222.39","master":"10.0.222.40"},
         11:{"node1":"10.0.222.41", "node2":"10.0.222.42","master":"10.0.222.43"},
         12:{"node1":"10.0.222.44", "node2":"10.0.222.45","master":"10.0.222.46"},
         13:{"node1":"10.0.222.47", "node2":"10.0.222.48","master":"10.0.222.49"},
         14:{"node1":"10.0.222.50", "node2":"10.0.222.51","master":"10.0.222.52"},
         15:{"node1":"10.0.222.53", "node2":"10.0.222.54","master":"10.0.222.55"},
         16:{"node1":"10.0.222.56", "node2":"10.0.222.57","master":"10.0.222.58"},
    }
    return data[pod]

def pod_jump_host(pod):
    data =  \
        {
          1:{"node1":"10.139.14.11", "node2":"10.139.14.12","jumphost":"10.139.14.21"},
          2:{"node1":"10.139.14.14", "node2":"10.139.14.15","jumphost":"10.139.14.22"},
          3:{"node1":"10.139.14.17", "node2":"10.139.14.18","jumphost":"10.139.14.23"},
          4:{"node1":"10.139.14.20", "node2":"10.139.14.21","jumphost":"10.139.14.24"},
          5:{"node1":"10.139.14.23", "node2":"10.139.14.24","jumphost":"10.139.14.25"},
          6:{"node1":"10.139.14.26", "node2":"10.139.14.27","jumphost":"10.139.14.26"},
          7:{"node1":"10.139.14.29", "node2":"10.139.14.30","jumphost":"10.139.14.27"},
          8:{"node1":"10.139.14.32", "node2":"10.139.14.33","jumphost":"10.139.14.28"},
          9:{"node1":"10.139.14.35", "node2":"10.139.14.36","jumphost":"10.139.14.29"},
         10:{"node1":"10.139.14.38", "node2":"10.139.14.39","jumphost":"10.139.14.30"},
         11:{"node1":"10.139.14.41", "node2":"10.139.14.42","jumphost":"10.139.14.31"},
         12:{"node1":"10.139.14.44", "node2":"10.139.14.45","jumphost":"10.139.14.32"},
         13:{"node1":"10.139.14.47", "node2":"10.139.14.48","jumphost":"10.139.14.33"},
         14:{"node1":"10.139.14.50", "node2":"10.139.14.51","jumphost":"10.139.14.34"},
         15:{"node1":"10.139.14.53", "node2":"10.139.14.54","jumphost":"10.139.14.35"},
         16:{"node1":"10.139.14.56", "node2":"10.139.14.57","jumphost":"10.139.14.36"},
    }
    return data[pod]

def get_pod_data(pod):
    domain = ".ecatsrtpdmz.cisco.com"
    link_level_pg = link_level_policy_group(pod)

    #IP Addresses
    apic_controllers = ["10.136.10.5", "10.136.10.6", "10.136.10.7"]
    apic_prompt = ["apic1#", "apic2#", "apic3#"]
    vcenter_dns = "req-vcsa.csc.richfield.cisco.com"
    vcenter_ip = "10.101.128.100"
    ccp_ip = "10.139.13.50"
    hyperflex_ip = "10.139.11.10"

    pod_numstr = "%02d" % pod
    env_name = "acilab"
    req_dir = "requests"
    toolkit_dir = "toolkit"
    js_dir = "jsapps"
    js_create_dir = "js_profile"
    packager_venv_name = "packager"
    js_endpoint_dir = "ep-viewer"
    js_appstore_dir = "appstore"
    leaf_pair = {1:"207",2:"208"}
    appstore_pkg_dir = "aci-packager"
    js_code_dir = "js"
    playbooks_dir = "playbooks"
    playbooks_programmable_fabric_dir = "programmable-fabric"
    playbooks_programmable_fabric_roles_dir = "roles"
    appstore_packager_file = "cisco_aci_app_packager-1.0.tgz"
    appstore_pkg_extract_dir = "cisco_aci_app_packager-1.0"
    final_packaged_filename = "ExampleDomain-EndpointViewer-1.0.aci"

    #k8s nodes definition
    pod_master_dns = "pod%02d-master.ecatsrtpdmz.cisco.com" % pod
    pod_node1_dns = "pod%02d-node1.ecatsrtpdmz.cisco.com" % pod
    pod_node2_dns = "pod%02d-node1.ecatsrtpdmz.cisco.com" % pod
    pod_master_hostname = "pod%02d-master" % pod
    pod_node1_hostname = "pod%02d-node1" % pod
    pod_node2_hostname = "pod%02d-node2" % pod
    pod_master_ip = pod_jump_host(pod)['jumphost']
    pod_node1_ip = pod_vm_info(pod)['node1']
    pod_node2_ip = pod_vm_info(pod)['node2']

    # Need to define credentials here as placed in various places.
    apic_stdnt_uname = "student%02d" % pod
    apic_stdnt_pass = "C1sco12345!"
    vmware_stdnt_uname = "student%02d" % pod
    vmware_stdnt_pass = "C1sco12345!"
    centos_uname = "root"
    centos_pass = "C1sco12345!"

    credential_popover = """<h4>APIC

                                    <a target='_blank' href='%(apic_url)s'>
                                      <img src="/core/static/images/symbols/http_pointer.png" style="height:25px;" >
                                    </a>
                                    <a target='_blank' href='chrome-extension://pnhechapfaindjhompbnflcldabbghjo/html/nassh.html#%(apic_stdnt_uname)s@%(apic_ip)s:22'>
                                      <img src="/core/static/images/symbols/ssh_pointer.png" style="height:25px;" >
                                    </a>
                         </h4>
                        <ul><li>Username: %(apic_stdnt_uname)s</li><li>Password: %(apic_stdnt_pass)s</li></ul>
                        <h4>VMware vCenter
                                    <a target='_blank' href='%(vmw_url)s'>
                                    <img src="/core/static/images/symbols/http_pointer.png" style="height:25px;" >
                                    </a>
                        </h4>
                        <ul><li>Username: %(vmware_stdnt_uname)s</li><li>Password: %(vmware_stdnt_pass)s</li></ul>
                        <h4>CCP Control Plane
                                    <a target='_blank' href='%(ccp_url)s'>
                                    <img src="/core/static/images/symbols/http_pointer.png" style="height:25px;" >
                                    </a>
                        </h4>
                        <ul><li>Username: admin </li><li>Password: admin </li></ul>

                         <h4>Jumphost VM</h4>
                         <ul><li>Address: %(master_ip)s
                         <a target="_blank" href="chrome-extension://pnhechapfaindjhompbnflcldabbghjo/html/nassh.html#%(centos_uname)s@%(master_ip)s:22">
                            <img src="/core/static/images/symbols/ssh_pointer.png" style="height:20px;" >
                         </a>
                         </li></ul>
                         <hr/>
                        <ul><li>Username: %(centos_uname)s</li><li>Password: %(centos_pass)s</li></ul>
                        """ % {
                            "apic_url": "http://"+random.choice(apic_controllers),
                            "apic_ip": apic_controllers[int(pod_numstr[:1])],
                            "vmw_url": "http://"+vcenter_ip+"/ui",
                            "ccp_url": "http://"+ccp_ip+"/ver/3/clusters",
                            "apic_stdnt_uname": apic_stdnt_uname,
                            "apic_stdnt_pass": apic_stdnt_pass,
                            "vmware_stdnt_uname": vmware_stdnt_uname,
                            "vmware_stdnt_pass": vmware_stdnt_pass,
                            "centos_uname": centos_uname,
                            "centos_pass": centos_pass,
                            "master_ip": pod_master_ip,
                            "node1_ip": pod_node1_ip,
                            "node2_ip": pod_node2_ip
                             }

    data = {
        "credential_popover_data":      credential_popover,
        "credential_popover_show":      True,
        "lab_id":                       "LTRACI-2967",
        "infra_vlan":                   3967,
        # POD identifiers
        "pod_id":                       pod,
        "pod_numstr":                   pod_numstr,
        "pname":                        "pod%02d" % pod,
        "editor":                       "vi",
        "vpn_source_ip":                "10.0.250.X/32",
        # Ansible related
        "ansible_dir":                  "ansible",
        "centos_pass":                  "cisco.123",
        # VM IP and hostnames
        "pod_master_dns":               pod_master_dns,
        "pod_node1_dns":                pod_node1_dns,
        "pod_node2_dns":                pod_node2_dns,
        "pod_master_hostname":          pod_master_hostname,
        "pod_node1_hostname":           pod_node1_hostname,
        "pod_node2_hostname":           pod_node2_hostname,
        "pod_master_ip":                pod_master_ip,
        "pod_node1_ip":                 pod_node1_ip,
        "pod_node2_ip":                 pod_node2_ip,
        # Alpine version
        "alpine_docker_hub":            "alpine:3.10",
        # Docker and Kubernetes Version
        "docker_ce_version":            "docker-ce-3:18.09.9-3.el7.x86_64",
        "kubelet_version":              "kubelet-0:1.15.7-0.x86_64",
        "kubeadm_version":              "kubeadm-0:1.15.7-0.x86_64",
        "kubectl_version":              "kubectl-0:1.15.7-0.x86_64",
        "kubecni_version":              "kubernetes-cni-0:0.7.5-0.x86_64",
        #"kubelet_version":              "kubelet-0:1.9.7-0.x86_64",
        #"kubeadm_version":              "kubeadm-0:1.9.7-0.x86_64",
        #"kubectl_version":              "kubectl-0:1.9.7-0.x86_64",
        #"kubecni_version":              "kubernetes-cni-0:0.6.0-0.x86_64",
        # Files for release 3.1.1
        #"software_server":              "10.0.226.7",
        #"software_http_url":            "http://10.0.226.7/kube/",
        #"dist_rpms":                    "dist-rpms-3.1.1-kubernetes1.7-20171215.tar.gz",
        #"dist_gen":                     "dist-generics-3.1.1-kubernetes1.7-20171215.tar.gz",
        #"acc_prov_rpm_name":            "acc-provision-1.7.1-31.el7.x86_64.rpm",
        # Files for release 3.1.2
        "docker_compose_on_server":     "docker-compose-Linux-x86_64_v1.25",
        "software_server":              "10.0.226.7",
        "software_http_url":            "https://svs-rtp-dmz-files.ciscolive.com/ltraci-2967/",
        "dist_rpms":                    "dist-rpms-3.1.2-kubernetes1.7_1.8-20180312.tar.gz",
        "dist_gen":                     "dist-generics-3.1.2-kubernetes1.7_1.8-20180312.tar.gz",
        "acc_prov_rpm_name":            "acc-provision-1.7.2-34.el7.x86_64.rpm",
        "helm_binary":                  "helm-v2.9.1-linux-amd64.tar.gz",
        # Provision file names
        "template_file_name":           "aci-fabric-config.yaml",
        "k8s_integration_file_name":    "aci-k8s-config.yaml",
        # Kubernetes YAML file variables
        "kube_system_id":               "k8s_pod%02d" % pod,
        "kube_compute":                 "10.0.236.%d" % (pod + 100),
        "kube_compute_cimc":            "10.0.236.%d" % (pod + 200),
        "mcast_range":                  {"start":"239.%d.1.1" % pod,"end":"239.%d.255.255" % pod},
        "mcast_mask":                   "255.255.0.0",
        "infra_vlan":                   3967,
        "kubeapi_vlan":                 3100 + pod,
        "service_vlan":                 3200 + pod,
        "k8s_namespace_cli":            "--namespace", # "--namespace="
        "pod_k8s_gb_namespace":         "gb-pod%02d" % pod, # "gb-pod%02d" % pod
        "pod_k8s_wp_namespace":         "wp-pod%02d" % pod, # "wp-pod%02d" % pod
        "k8s_api_version":              "v1",
        # credential popover HTML
        "credential_popover":           credential_popover,
        # Infrastructure ports, uplinks and other
        "pod_uplink_port":              {1: str(pod), 2: str(pod)},
        "pod_uplink_leaf":              leaf_pair,
        "pod_extl3_port":               {"leaf":"203","port":"1/%d" % pod },
        "fabric_ext_epg":               "fabric_l3out_extepg",
        "bond_int_name":                "bond0",
        "int_name":                     "ens224",
        # VMware domain variables
        "vmware_pod_compute":           "pod%02d-compute1" % pod,
        "vmware_vlan_pool_name":        "k8s_pod%02d_vmmpool" % pod,
        "vmware_domain_name":           "k8s_pod%02d_dvs" % pod,
        "vmware_dvs_name":              "k8s_pod%02d_dvs" % pod,
        "vmware_cred_profile_name":     "k8s_pod%02d_crd" % pod,
        "vmware_cred_username":         vmware_stdnt_uname,
        "vmware_cred_password":         vmware_stdnt_pass,
        "vmware_cont_pname":            "k8s_pod%02d_vcenter" % pod,
        "vmware_cont_ip":               vcenter_ip,
        "vmware_cont_dns":              vcenter_dns,
        "vmware_dvs_ver":               "vCenter Default",
        "vmware_datacenter":            "k8s_pod%02d" % pod,
        "vmware_portgroup":             "k8s_pod%02d" % pod,
        "vmware_dynVlanPool_start":     "1%02d1" % pod,
        "vmware_dynVlanPool_end":       "1%02d9" % pod,
        "vmware_dynVlanPool_str":       "1%02d1-1%02d9" % ( pod, pod ),
        #Centos credentials
        "centos_password":              centos_pass,
        # ACI fabric credentials
        "apic_stdnt_uname":             apic_stdnt_uname,
        "apic_stdnt_pass":              apic_stdnt_pass,
        "apic_admin_uname":             "admin",
        "apic_admin_pwd":               "cisco.123",
        # ACI Fabric VMM policy values
        "pod_tenant":                   "k8s_pod%02d" % pod,
        "pod_tenant_description":       "Tenant for POD %02d" % pod,
        "pod_aep_name":                 "k8s_pod%02d_aep" % pod,
        "pod_vrf_name":                 "k8s_vrf",
        "pod_intf_pg_name":             link_level_pg['name'] , #"k8s_pod%02d_pg" %pod,
        "pod_intf_pg_policies":         link_level_pg,
        "pod_intf_profile_name":        "k8s_pod%02d_int_profile" % pod ,
        "pod_intf_port_selector":       "k8s_pod%02d_access_port" % pod,
        "pod_access_port_IntID":        "1/%d" % pod,
        "pod_switch_profile_name":      "k8s_pod%02d_sw_profile" % pod,
        "pod_switch_profile_ls_name":   "sw_%s_%s" % (leaf_pair[1], leaf_pair[2]),
        "pod_switch_profile_block_id":  "ltraci2967pod%02d_lpblock" % pod,
        "pod_l3out_name":               "k8s",
        "pod_l3out_epg":                "k8s-epg",
        "pod_leaf1":                    leaf_pair[1],
        "pod_leaf2":                    leaf_pair[2],
        "pod_user":                     "userpod" + str(pod),
        "date":                         "{:%m/%d/%Y}".format(datetime.now()),
        #subnets for k8s
        "nodenet_subnet":               public_subnet_info(pod,"node")["subnet"],
        "nodenet_subnet_dg":            public_subnet_info(pod,"node")["dg"],
        "nodenet_subnet_mask":          public_subnet_info(pod,"node")["mask"],
        "nodenet_subnet_lm":            public_subnet_info(pod,"node")["lm"],
        "extern_dynamic_subnet":        public_subnet_info(pod,"extern_dynamic")["subnet"],
        "extern_dynamic_subnet_dg":     public_subnet_info(pod,"extern_dynamic")["dg"],
        "extern_dynamic_subnet_mask":   public_subnet_info(pod,"extern_dynamic")["mask"],
        "extern_dynamic_subnet_lm":     public_subnet_info(pod,"extern_dynamic")["lm"],
        "extern_static_subnet":         public_subnet_info(pod,"extern_static")["subnet"],
        "extern_static_subnet_dg":      public_subnet_info(pod,"extern_static")["dg"],
        "extern_static_subnet_mask":    public_subnet_info(pod,"extern_static")["mask"],
        "extern_static_subnet_lm":      public_subnet_info(pod,"extern_static")["lm"],
        "pod_subnet":                   private_subnet_info(pod)["pod_subnet"],
        "pod_subnet_dg":                private_subnet_info(pod)["pod_dg"],
        "pod_subnet_mask":              private_subnet_info(pod)["pod_mask"],
        "pod_subnet_lm":                private_subnet_info(pod)["pod_lm"],
        "node_service_subnet_dg":       private_subnet_info(pod)["node_service_dg"],
        "node_service_subnet_mask":     private_subnet_info(pod)["node_service_mask"],
        "node_service_subnet_lm":       private_subnet_info(pod)["node_service_lm"],
        # K8s Node Subnet IP's
        "nodenet_master_ip":            public_subnet_info(pod,"node")['n1'],
        "nodenet_node1_ip":             public_subnet_info(pod,"node")['n2'],
        "nodenet_node2_ip":             public_subnet_info(pod,"node")['n3'],
        # APIC fabric values
        "apic_controller":              apic_controllers,
        "apic4pod":                     apic_controllers[int(pod_numstr[:1])],
        "apic_1":                       apic_controllers[0],
        "apic_2":                       apic_controllers[1],
        "apic_3":                       apic_controllers[2],
        "imgtitlebgc":                  "#2c3e50",
        "ntp_server":                   "10.0.236.10 (ntp-vlan336.ecatsrtpdmz.cisco.com)",
        # Local Registry information
        "registry_url":                 "svs-rtp-dmz-registry.ciscolive.com",
        "registry_myapp":               "myplayapp:v1",
        "registry_username":            "svs",
        "registry_password":            "cisco.123cisco.123",
        # MyApp Local
        "my_app_folder":                "my_app",
        # MyAPP Kubernetes
        "pod_mylabapp_name":            "mylabapp",
        "pod_mylabapp_epg":             "kube-mylabapp",
        "pod_mylabapp_deployment":      "mylabapp",
        "pod_mylabapp_namespace":       "mylabapp",
        "pod_mylabapp_deployment_file": "mylabapp-deployment.yaml",
        "pod_mylabapp_service_file":    "mylabapp-service.yaml",
        "pod_mylabapp_service_ip":      public_subnet_service_ip(pod,"static")["mylabapp"],
        # Guestbook Kubernetes
        "pod_gb_service_ip":            public_subnet_service_ip(pod,"static")["gbapp"],
        "pod_gb_service_proxy":         public_subnet_service_ip(pod,"static")["gbapp-proxy"],
        "pod_gb_service_url":           public_subnet_service_ip(pod,"static")["gbapp_url"]+".ecatsrtpdmz.cisco.com",
        # URL's with traefik
        "pod_traefik_url":              "dashboard.acik8s-pod%02d.ecatsrtpdmz.cisco.com" % pod,
        "pod_mylabapp_url":             "mylabapp.acik8s-pod%02d.ecatsrtpdmz.cisco.com" % pod,
        "pod_guestbook_url":            "guestbook.acik8s-pod%02d.ecatsrtpdmz.cisco.com" % pod,
        # Ingress Controller stuff
        "ingress_dns_wildcard":         "*.acik8s-pod%02d.ecatsrtpdmz.cisco.com" %pod,
        "ingress_dns_return_ip":        public_subnet_service_ip(pod,"static")["gbapp-proxy"],
        #  Word Press Kubernetes related
        "wordpresspassword":            "wp_pass_pod%02d" % pod,
        "mysql_deploy_yml_file":        "wp-mysql-deployment.yaml",
        "mysql_service_yml_file":       "wp-mysql-service.yaml",
        "mysql_pv_yml_file":            "wp-mysql-pv.yaml",
        "wp_deploy_yml_file":           "wp-wordpress-deployment.yaml",
        "wp_pv_yml_file":               "wp-wordpress-pv.yaml",
        "wp_service_yml_file":          "wp-wordpress-service.yaml",
        # Kubernetes Persistent Volumes
        "k8s_pv_file":                  "k8s-pv-deployment.yaml",
        "datadir":                      "/var/data",
        # Kubernetes ACI PBR Page
        "aci_epg_net_mylabapp":         "k8s_pod%02d_svc_default_%s" % ( pod, "mylabapp" ),
        "aci_mylabapp_graph":           "k8s_pod%02d_svc_global" %  pod,
        # All Linux prompts for CLI mimick on document
        "home_prompt":                  "pod%02d ~ " % pod ,
        "master_prompt":                "[root@pod%02d-master ~]#" % pod ,
        "master_prompt_my_app":         "[root@pod%02d-master my_app]#" % pod ,
        "master_prompt_dockerplay":     "[root@pod%02d-master dockerplay]#" % pod ,
        "master_prompt_wp":             "[root@pod%02d-master wp_local]#" % pod ,
        "node1_prompt":                 "[root@pod%02d-node1 ~]#" % pod ,
        "node2_prompt":                 "[root@pod%02d-node2 ~]#" % pod ,
        "linux_prompt":                 "pod%02d ~ $ " % pod ,
        "apic_prompt":                  apic_prompt[int(pod_numstr[:1])],
        "container_prompt":             "root@ubuntu-ciscolive:/#",
        "container_alpine_prompt":      "/ #",
        "linux_prompt_venv":            "(" +env_name+ ") pod%02d ~ $ " % ( pod ),
        "linux_prompt_venv_req":        "(" +env_name+ ") pod%02d ~/%s $ " % (pod, req_dir),
        "linux_prompt_venv_tk":         "(" +env_name+ ") pod)%02d ~/%s $ " % (pod, toolkit_dir),
        "linux_prompt_js":              "pod%02d ~/%s $ " % (pod, js_dir),
        "linux_prompt_js_ep":           "pod%02d ~/%s/%s $ " % (pod, js_dir, js_endpoint_dir),
        "linux_prompt_js_ep_js":        "pod%02d ~/%s/%s/%s $ " % (pod, js_dir, js_endpoint_dir, js_code_dir ),
        "linux_prompt_js_app":          "pod%02d ~/%s/%s $ " % (pod, js_dir, js_appstore_dir),
        "linux_prompt_js_as_build":     "pod%02d ~/%s/%s/build $ " % (pod, js_dir, js_appstore_dir),
        "linux_prompt_pkg":             "pod%02d ~/%s/%s $ " % (pod, js_dir, appstore_pkg_dir),
        "linux_prompt_js_profile":      "pod%02d ~/%s/%s $ " % (pod, js_dir, js_create_dir),
        "linux_prompt_pkg_venv":        "("+ packager_venv_name+ ") pod%02d ~/%s/%s $ " % (pod, js_dir, appstore_pkg_dir),
        "linux_prompt_pb":              "pod%02d ~/%s $ " % (pod, playbooks_dir),
        "linux_prompt_pb_aci":          "pod%02d ~/%s/%s $ " % (pod, playbooks_dir, playbooks_programmable_fabric_dir),
        "linux_prompt_pb_aci_roles":    "pod%02d ~/%s/%s/%s $ " % ( pod, playbooks_dir, playbooks_programmable_fabric_dir, playbooks_programmable_fabric_roles_dir),
   }
    return data
