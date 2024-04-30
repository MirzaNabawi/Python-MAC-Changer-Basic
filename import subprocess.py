import subprocess
import optparse
import re
def user_interface():
    parser= optparse.OptionParser()
    parser.add_option( "-i" , dest= "interface" , help = "Give Interface")
    parser.add_option( "-m" , dest= "new_mac" , help = "Give MAC Address")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[+] Please Specify Interface> ")
    elif not options.new_mac:
        parser.error("[+] Please Specify MAC Address")
    return options
def change_mac(interface,new_mac):
    subprocess.call(["ifconfig", interface , "down"])
    subprocess.call(["ifconfig", interface , "hw","ether" , new_mac])
    subprocess.call(["ifconfig", interface , "up"])
def get_current_mac(interface):
    ifconfig_result=str(subprocess.check_output(["ifconfig", interface]),"ascii")
    mac_address=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if mac_address:
        return (mac_address.group(0))
    else:
        print("[+] Could Not find MAC Address")
options=user_interface()
current_mac=get_current_mac(options.interface)
print("User interface is " , options.interface)
print("Current MAC is",current_mac)
change_mac(options.interface,options.new_mac)
current_mac=get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("New MAC Address " , current_mac)
else:
    print("[+] MAC Address did not change ")













