import subprocess
import optparse

def argument():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest = "interface" , help = "Interface to change MAC Address")
    parser.add_option("-m","--mac_address",dest = "new_mac",help = "New MAC address")

    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] Changing MAC Address of ", interface, " to ", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

(options,arguments)=argument()
change_mac(options.interface, options.new_mac)




