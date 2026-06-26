---
title: "Configure the Maximum Number of Open Processes and Files"
id: 43701104850445
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104850445-Configure-the-Maximum-Number-of-Open-Processes-and-Files
updated_at: 2026-05-29T14:08:40Z
---

# Configure the Maximum Number of Open Processes and Files

# Configure the Maximum Number of Open Processes and Files

Configuring the maximum number of open processes and open files that can run in your operating environment keeps Composer processes from hitting or exceeding the resource limits that may be imposed by your operating system.

Instructions are provided here for the following operating environments:

### CentOS Instructions

If you are installing via RPM using CentOS or Red Hat, the recommended settings differ slightly. Because `systemd` is responsible for starting the various Composer microservices, you need to amend the files and microservices that are launched so the `limits.conf` file is not ignored.

Composer recommends that you create an override directory specifically for the microservices you want to override.

1. Create a new `systemd` directory:

   mkdir /etc/systemd/system/<servicename>.service.d/

   Replace <servicename> with the microservice you need to override.
2. The file name for the microservice you want to override needs to be in `.conf`, so use the following command:

   touch /etc/systemd/system/<servicename>.service.d/<servicename>.conf

For more information about managing microservices for Red Hat, see the [Red Hat documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-managing_services_with_systemd).

If Composer stops operating and you receive the error message `too many files, cannot operate`, you may need to increase the system limits in your CentOS or supported Ubuntu environments. Make the following changes:

1. In the `service.d` folder for each microservice, open the `limits.conf` file. If the configuration file does not exist, this command creates it.

   vi /etc/systemd/system/<servicename>.service.d/limits.conf
2. Add the following to the file:

   [Service]  
   LimitNOFILE=10000
3. Restart the init service:

   systemctl daemon-reload
4. Restart the `zoomdata` microservice:

   systemctl restart zoomdata.service
5. Verify your changes were applied:

   ps -ef | grep zoomdata-web | grep -v grep | awk '{system("cat /proc/"$2"/limits")}' | grep -i "Max open files"
6. In the output, you should see the following, indicating that your changes were applied:

   Max open files 10000 10000 files

Return to the installation topic you are using to continue the installation process:

* [Install Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072793997-Install-Composer)
* [Install Composer Manually](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105134605-Install-Composer-Manually)
