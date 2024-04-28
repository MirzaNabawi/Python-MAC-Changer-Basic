import subprocess
import optparse

subprocess.call("ifconfig")

parser= optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface" , help="Interface to change MAC Address")
parser.add_option("-m","--mac address",dest="new_mac",help="New MAC address")

parser.parse_args()

interface= input("interface > ")
new_mac= input("new_mac > ")

print("[+]Changing MAC address " + interface + " to " + new_mac )


subprocess.call(["ifconfig", interface , "down"])
subprocess.call(["ifconfig", interface , "hw" , "ether" , new_mac])
subprocess.call(["ifconfig", interface , "up"])



