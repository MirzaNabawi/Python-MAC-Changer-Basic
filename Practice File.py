import subprocess
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Change Interface to")
    parser.add_option("-m", "--mac address", dest="new_mac", help="Change MAC Address to")

    return parser.parse_args()


def change_mac( interface,new_mac):
    print("[+]Changing MAC Address for " + interface + "  to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

(options,arguments)=get_arguments()
change_mac(options.interface,options.new_mac)






