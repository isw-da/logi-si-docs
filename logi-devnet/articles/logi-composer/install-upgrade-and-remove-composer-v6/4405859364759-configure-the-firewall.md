---
title: "Configure the Firewall"
id: 4405859364759
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859364759-Configure-the-Firewall
updated_at: 2021-09-21T01:28:44Z
---

# Configure the Firewall

# Configure the Firewall

After you have successfully installed the Composer components onto your server, you need to configure the firewall. Configure "iptables" to accept port 8443 and to forward incoming HTTPS requests on port 443 to the Composer server port 8443. Note that the command lines may differ slightly depending on the Linux environment. Select the appropriate Linux environment below.

* [*CentOS 7 or 8 Commands*](#For2)
* [*Ubuntu 16 or 18 Commands*](#Ubuntu)

These commands set up the firewall rules to the default eth0 network interface. If you want to apply them to another network interface, replace it in the commands below . If you want to apply the rules to all the interfaces, remove '-i eth0' from the command line.

## CentOS 7 or 8 Commands

```
sudo yum install iptables-services  
sudo systemctl enable iptables  
sudo systemctl start iptables  
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 8443 -j ACCEPT  
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination :8443  
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 80 -j ACCEPT  
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination :8080  
sudo /usr/libexec/iptables/iptables.init save
```

## Ubuntu 16 or 18 Commands

```
sudo apt-get install iptables-persistent  
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 8443 -j ACCEPT  
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination :8443  
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 80 -j ACCEPT  
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination :8080  
sudo netfilter-persistent save  
sudo netfilter-persistent reload
```

When prompted for input for the question of `iptables-persistent`, enter `yes`.

Return to the installation topic your are using to continue the installation process:

* [*Install Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859373719-Install-Composer)
* [*Install Composer Manually*](https://devnet.logianalytics.com/hc/en-us/articles/4405851085207-Install-Composer-Manually)
* [*Upgrade Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859509271-Upgrade-Composer)
