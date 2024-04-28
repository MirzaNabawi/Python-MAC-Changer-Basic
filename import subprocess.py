import subprocess
subprocess.call("ifconfig")
x= input("x > ")
y= input("y > ")
print("[+]Changing MAC address " + x + " to " + y )

subprocess.call("ifconfig "+ x +" down ", shell=True) 
subprocess.call("ifconfig "+ x + " hw ether " +y , shell=True) 
subprocess.call("ifconfig "+ x + " up ", shell=True) 
