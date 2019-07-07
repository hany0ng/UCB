##UFW Configuration

#Scenario
In this exercise you will set up their firewall for their Linux server. We provided you with a VM that already has preconfigured network services, namely: SSH, telnet, Apache and FTP. The VM already has UFW enabled, with defaults set to deny all incoming and outgoing traffic. Make the following configuration changes.

[x] Enable the Apache Full UFW profile
    sudo ufw allow 'Apache Full'
[x] Allow outbound DNS
    sudo ufw allow out to any port 53
[x] Allow inbound SSH only from the local subnet
    sudo ufw allow from 10.0.2.0/24 to any port 22
[x] Allow inbound telnet only from the local subnet
    sudo ufw allow from 10.0.2.0/24 to any port 23
[x] Allow FTP only from the local subnet
    sudo ufw allow from 10.0.2.0/24 to any port 21
    sudo ufw allow out from 10.0.2.0/24 to any port 21
[x] Drop inbound ICMP from outside the local subnet
    edit /etc/ufw/before.rules and change before-icmp input to DROP
[x] You have also been asked to enable logging, at level high/info.