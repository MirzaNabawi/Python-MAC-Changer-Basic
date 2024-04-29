import subprocess
import optparse
import re

def argument():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest = "interface" , help = "Interface to change MAC Address")
    parser.add_option("-m","--mac_address",dest = "new_mac",help = "New MAC address")
    (options, argument)= parser.parse_args()
    if not options.interface:
        parser.error("Please specify a proper Interface or use --help for more information")
    elif not options.new_mac:
        parser.error("Please specify a proper MAC Address or use --help for more information")
    
    return options 


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address of ", interface, " to ", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options=argument()
change_mac(options.interface, options.new_mac)

ifconfig_result= subprocess.check_output([ "ifconfig", options.interface])
print(ifconfig_result)

mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w","ifconfig_result")
if mac_address_result:
    print(mac_address_result.group(0))
else:
    print("[-] Could not find MAC Address")



