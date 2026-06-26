---
title: "Install the Discovery Module - Linux - Configuring the Services (with systemctl)"
id: 4406817520663
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817520663-Install-the-Discovery-Module-Linux-Configuring-the-Services-with-systemctl
updated_at: 2022-04-06T06:06:35Z
---

# Install the Discovery Module - Linux - Configuring the Services (with systemctl)

# Install the Discovery Module - Linux - Configuring the Services (with systemctl)

If your OS provides access to systemctl, follow these instructions. We want the Discovery services (daemons) to run as their own user. To do this:

1. Create a new User and Group named "Discovery", as follows:

sudo groupadd Discovery

sudo useradd -M -s /bin/nologin -g Discovery -d /opt/Discovery Discovery

2. Then change the owner of the Discovery directory to the new "Discovery" user:

sudo chown Discovery:Discovery /opt/Discovery -R

3. If you look in Discovery's "bin" directory (/opt/Discovery/platform/bin) you'll see two scripts: logiDataService.sh and logiApplicationService.sh. Both of these scripts need to be run to start the full Discovery server. In this next section, we'll configure a service to start and stop the
   Discovery
   server.  
     
   First, we'll configure the application service:

sudo nano /etc/systemd/system/LogiApplicationService.service

Include these items in the LogiApplicationService.service file:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563252887/installdm31linux_07.png)

Next, for the data service:

sudo nano /etc/systemd/system/LogiDataService.service

Include these items in the LogiDataService.service file:  
  
![](https://devnet.logianalytics.com/hc/article_attachments/4417583902103/installdm31linux_08.png)

4. Finally, run this command so systemd picks up the changes:

sudo systemctl daemon-reload

And then start the services:

sudo service LogiDataService start  
sudo service LogiApplicationService start

Now run this test to see if the server responds:

curl localhost:3000

If you receive a message that says "Cannot GET /" then the installation was successful. Congratulations!

## Start Services on Boot

If you'd like to have both services start on boot, do this:

sudo systemctl LogiApplicationService enable  
sudo systemctl LogiDataService enable
