import subprocess

subprocess.call("ifconfig")

interface= input("interface > ")
new_mac= input("new_mac > ")

print("[+]Changing MAC address " + interface + " to " + new_mac )


subprocess.call(["ifconfig ", interface , " down "], shell=True)
subprocess.call(["ifconfig ", interface , " hw "," ether "], shell=True)
subprocess.call(["ifconfig ", interface , " up "], shell=True)



