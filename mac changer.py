import subprocess
subprocess.run(["ifconfig","wlan0","down"]) 
subprocess.run(["macchanger","-r","wlan0"])
subprocess.run(["ifconfig","wlan0","up"])