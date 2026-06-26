---
title: "Install and Configure the Composer Service Monitor"
id: 43701162883597
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162883597-Install-and-Configure-the-Composer-Service-Monitor
updated_at: 2026-05-29T14:09:27Z
---

# Install and Configure the Composer Service Monitor

# Install and Configure the Composer Service Monitor

The Composer Service Monitor microservice is not installed as part of a default Composer installation. The microservice name is `zoomdata-admin-server`.

**Note:** 
If you are installing Composer in a Windows environment, you can install the Service Monitor as part of running the initial bootstrap script. See [Install Composer in a Windows Environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072833421-Install-Composer-in-a-Windows-Environment) and [Windows Bootstrap Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120362381-Windows-Bootstrap-Reference).

**Install, configure, and start the Service Monitor**

1. Open your SSH client.
2. Use the following command to install the Composer Service Monitor in a CentOS environment:

   sudo yum install zoomdata-admin-server -y

   Use the following command to install the Composer Service Monitor in an Ubuntu environment:

   sudo apt-get install zoomdata-admin-server
3. After the Service Monitor is installed, you must specify a user name and password in its properties file. The properties file is called `admin-server.properties` and can be found in the `/etc/zoomdata/` directory (Linux) or the `<install-path>/conf-modify/` directory (Windows). If the properties file is not there, create it. The properties that must be defined are:

   * `monitor.user.name=<username>`
   * `monitor.user.password=<password>`

   Edit the properties file with a text editor and substitute a Service Monitor user name for `<username>` and its associated password for `<password>`. The user name and password can be any user name and password you want.

   When you have finished, save the file.
4. Add the following properties to the `zoomdata.properties` file, located in the `/etc/zoomdata` directory (Linux) or the `<install-path>/conf-modify/` (Windows). These properties ensure that the Service Monitor has access to the Composer server actuator endpoints.

   * `actuator.user.name=<composer-admin-username>`
   * `actuator.user.password=<composer-pswd>`
   * `actuator.logging.external-file=<log-file-path>`

   Edit the properties file and substitute the valid user name and password of a Composer administrator for `<Composer-admin-username>` and `<Composer-pswd>`. If the default Composer log file path is not used for your installation, substitute your custom log file path for `<log-file-path>`. The default log file path is `/opt/zoomdata/logs/zoomdata.log` for Linux and `<install-path>/logs/zoomdata.log` for Windows.

   **Note:** 
   Setting these properties exposes valid Composer credentials as plain text in both the properties file and as tags in the Composer Consul. Anyone in your network with the ability to communicate directly with the Consul API or view the Consul UI will be able to see these values.

   When finished, save the file.
5. Start the microservice. For example, use the following command to start the Composer Service Monitor using `systemd` in a CentOS or Ubuntu environment:

   sudo systemctl start zoomdata-admin-server

   See also  [Start Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Start).
