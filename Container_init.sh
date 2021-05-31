#!/bin/bash
#
#

container_dir="/home/jthomas/dev/tradeapp"
container_name="tradeapp:docker"


echo "Money time!"
echo "Getting things ready.."
echo "Note: Docker Daemon must be running, or this script will fail."

# 1 - Launch Docker daemon
#     sudo dockerd
# TODO: need to execute this in a new shell
#       so the script can continue

# 2 - Port forwarding
	echo "Forwarding Port"
    # Get WSL ip address
    wsl_ip=`ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'`
    #  Using Powershell, forward the WSL port so we can access Jupyter Lab from a browser in Windows
    powershell.exe "Start-Process powershell.exe -Verb runAs -ArgumentList 'netsh interface portproxy add v4tov4 listenport=4445 listenaddress=127.0.0.1 connectport=4445 connectaddress=$wsl_ip'"
        # powershell.exe                :: invokes powershell
        # Start-Process powershell.exe  :: runs another instance of powershell. 
		#                                  Required because our first instance cannot run as admin.
        # -Verb runAs                   :: runs the second instance as admin
        # -ArgumentList "..."           :: the actual powershell command
    echo "Port forwarded"
	
# 3 - Launch Container
	echo "Launching Docker Container. I hope you launched dockerd..."
	docker run -p 4445:4445 --mount type=bind,source="$(pwd)"/tradeapp,target=/root/tradeapp tradeapp:docker
#	docker run -p 4445:4445 --mount type=bind,source=/home/jthomas/dev/tradeapp/tradeapp,target=/root/tradeapp tradeapp:docker
    echo "Container Launched"




# # 3 - Other materials
#     powershell.exe 'C:\Users\jthomas\Learning\"_trading and finance"\"_Algorithmic Trading"\"Hilpisch Y. Python for Algorithmic Trading 2020.pdf"'
#     echo "Let's Go!"