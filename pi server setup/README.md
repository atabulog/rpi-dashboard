# Raspberry pi 4 server setup
This details the approximate path needed to replicate the current raspberry pi server setup I have running right now. 

## Overview 
My Raspberry pi 4 is configured as a headless home server. The rpi is running the most recent release of raspbian lite (released 10/30/2021) and boots from an external SSD. This server is setup to use SSH through only one machine by a static IP. Since I know next to nothing about network security, all setup features were made to be as restrictive as possible. The Pi server will be used as a basic home server, and is currently not in a complete build state. As development progresses, more tools will be added, and should be reflected here. In the event where the setup must be replicated, look to the following sections for guidance.

## Setting up secure root and SSH
The bulk of the detail can be found [here](https://pimylifeup.com/raspberry-pi-security/).

below are some notes in the approach of how I did this.

1. Write down the username and password on the device. You will 100% forget if you leave the system alone for a few weeks.
2. I did not do the 2 factor, so It can be skipped
3. All the firewall stuff is likely already done. I did not do it manually. Note, you will likely have to check your router settings to ensure the SSH is not blocked by the router. Set it to a specific port (22) if it is.
4. Fail2Ban is a good thing to have, but since we are setting this up to only ssh into one device, it shouldn't be necessary. 
5. You should click the link for the SSH key authentication and follow its steps. This is the most critical step for the security of the pi over ssh.


## Install packages
1. sudo apt-get install python3
2. sudo apt-get install pip
3. sudo apt-get install git
4. sudo apt-get install mysql-server

## setup SQL server
Follow install and basic demo setup [here](https://bytesofgigabytes.com/raspberrypi/how-to-install-mysql-database-on-raspberry-pi/).

Notes on some modifications:
1. For the sake of not knowing anything about security, setup a default user for each device (specified by local IP) that is to connect directly to the server.
2. Create a default user for local device, so every application does not need to save a copy of the admin password.
3. Set the admin password to the rpi root password. This way you only need the password written on the device to access everything. I know this is dumb, but hey it's not critical software and not a vunerable part of the system. Sidenote: this should not be done with sensitive data.

## C++ tools



