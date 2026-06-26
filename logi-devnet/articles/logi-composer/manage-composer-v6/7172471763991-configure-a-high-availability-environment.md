---
title: "Configure a High Availability Environment"
id: 7172471763991
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/7172471763991-Configure-a-High-Availability-Environment
updated_at: 2022-07-01T19:33:44Z
---

# Configure a High Availability Environment

# Configure a High Availability Environment

A high availability environment is designed to ensure concurrent users having access to the same microservices at the same time, including the COMPOSER-WEB service. To have a high availability environment, you need to *[Configure a High Load Environment](https://devnet.logianalytics.com/hc/en-us/articles/7173395309591)* along with setting up at least two instances of each microservice, including COMPOSER-WEB. These services must be accessible through a Load Balancer.

![Use this as a guide to set up your HA environment for your microservices.](https://devnet.logianalytics.com/hc/article_attachments/7049212314519/highavailibilityloadbalancer.png "High availability with Load Balancer.")

Note how this is different from how you would *[Configure a High Load Environment](https://devnet.logianalytics.com/hc/en-us/articles/7173395309591)*, because you are adding multiple instances of each microservice.

## Setting Up Your Load Balancer

The following steps provide an example of setting up HAProxy as a load balancer. Regardless of what kind of load balancer you use, ensure that port 443 is open on it.

To set up an HAProxy load balancer:

1. On your machine, run the following command to install HAProxy:

   ```
   sudo yum install haproxy
   ```
2. Navigate to the HAProxy folder.

   ```
   cd /etc/haproxy
   ```
3. Create a certificate or copy an existing certificate to the `/etc/haproxy` folder. If you need to create a certificate, run the following commands:

   ```
   sudo openssl genrsa -out ca.key 1024  
   sudo openssl req -new -key ca.key -out ca.csr  
   sudo openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt  
   sudo vi cert.pem #Create and save an empty file  
   sudo chmod a+w cert.pem  
   sudo cat ca.key ca.crt > cert.pem
   ```
4. In the same folder, replace the contents of the `haproxy.cfg` file with the contents of the *[Composer haproxy configuration file](https://devnet.logianalytics.com/hc/article_attachments/7049224519703/haproxy.txt)*. In the file, replace the `<node1-ip>` and `<node2-ip>` with the IP addresses of your servers. If you have more than two servers, add additional lines for each server.
5. Save your changes and exit the file.
6. Start the HAProxy microservice

   ```
   sudo service haproxy restart
   ```
7. Use the following command to configure the HAProxy microservice to start automatically in CentOS 7 environments:

   ```
   sudo systemctl enable haproxy
   ```
8. Ensure that port 443 is open on your load balancer. If not, run the following command:

   ```
   sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT  
   sudo service iptables save
   ```

For assistance with configuring SAML for use with HAProxy, contact Composer Technical Support.
