---
title: "Install the Discovery Module - Linux - Configuring the Services (without systemctl)"
id: 4406817519639
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817519639-Install-the-Discovery-Module-Linux-Configuring-the-Services-without-systemctl
updated_at: 2022-04-06T06:06:36Z
---

# Install the Discovery Module - Linux - Configuring the Services (without systemctl)

# Install the Discovery Module - Linux - Configuring the Services (without systemctl)

If your OS *does not* provide access to systemctl, follow these instructions. The examples are from Centos 6.9. Start by logging in as root, then download from DevNet and save the file [logiDiscovery.sh](https://clm.logianalytics.com/downloads/info/logiDiscovery.sh).

Move the file to /etc/init.d and make it executable:

mv logiDiscovery.sh /etc/init.d  
chmod +x logiDiscovery.sh

Use a text editor to open the file and edit the DISCOVERYHOME, NODE\_HOME, and JAVA\_HOME values to match your installation location. For example, these are the values for the default location:

DISCOVERYHOME = /opt/Discovery  
NODE\_HOME = /opt/Discovery/platform/node.js  
JAVA\_HOME = /opt/Discovery/platform/java/jre1.8.0\_102 (JRE directory may vary with different Discovery releases)

You should now be able to immediately start the services, from within the /etc/init.d directory, with:

./logiDiscovery.sh start

Now run this test to see if the server responds:

curl localhost:3000

If you receive a message that says "Cannot GET /" then the installation was successful. Congratulations!

## Start Services on Boot

To ensure that the services will start on their own if the server is restarted, edit the top of the logiDiscovery.sh file, changing:

#!/bin/bash  
#

To:

#!/bin/bash  
#  
# Discovery 3.1  
#  
# chkconfig: - 10 90  
#

Then, as root, run:

chkconfig --add logiDiscovery.sh  
chkconfig logiDiscovery on
