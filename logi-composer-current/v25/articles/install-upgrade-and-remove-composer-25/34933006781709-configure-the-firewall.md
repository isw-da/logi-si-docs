---
title: "Configure the Firewall"
id: 34933006781709
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933006781709-Configure-the-Firewall
updated_at: 2026-05-26T22:07:25Z
---

# Configure the Firewall

# Configure the Firewall

After you have successfully installed the Composer components onto your server, you need to configure the firewall. Configure "iptables" to accept port 8443 and to forward incoming HTTPS requests on port 443 to the Composer server port 8443. Note that the command lines may differ slightly depending on the Linux environment. Select the appropriate Linux environment below.

* [CentOS Commands](#For2)
* [Ubuntu Commands](#Ubuntu)
* [Windows Defender Firewall](#Windows)

These commands set up the firewall rules to the default `eth0` network interface. If you want to apply them to another network interface, replace it in the commands below. If you want to apply the rules to all the interfaces, remove '`-i eth0`' from the command line.

## CentOS Commands

sudo yum install iptables-services  
sudo systemctl enable iptables  
sudo systemctl start iptables  
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 8443 -j ACCEPT  
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination :8443  
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 80 -j ACCEPT  
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination :8080  
sudo /usr/libexec/iptables/iptables.init save

## Ubuntu Commands

sudo apt-get install iptables-persistent  
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 8443 -j ACCEPT  
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination :8443  
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 80 -j ACCEPT  
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination :8080  
sudo netfilter-persistent save  
sudo netfilter-persistent reload

When prompted for input for the question of `iptables-persistent`, enter `yes`.

## Windows Defender Firewall

See this best practices article: [Best practices for configuring Windows Defender - Windows Security](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/best-practices-configuring).

## Continue Install

Return to the installation topic your are using to continue the installation process:

* [Install Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933011559565-Install-Composer)
* [Install Composer Manually](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933041539853-Install-Composer-Manually)
* [Upgrade Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933226897037-Upgrade-Composer)
