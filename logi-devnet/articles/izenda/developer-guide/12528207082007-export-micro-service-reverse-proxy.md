---
title: "Export Micro Service Reverse Proxy"
id: 12528207082007
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528207082007-Export-Micro-Service-Reverse-Proxy
updated_at: 2023-02-23T15:15:16Z
---

# Export Micro Service Reverse Proxy

# Export Micro Service Reverse Proxy

## Deploying Export Micro Service on Separate Linux Server

Export micro service can also run on the same server as Izenda back-end application. For installation on same server, follow the steps mentioned here [Export Micro Service](https://devnet.logianalytics.com/hc/en-us/articles/12528207078039-Export-Micro-Service)

### Pre-deployment steps

**Node JS**

1. Izenda Export service needs Node JS runtime environment to execute. Login as root user and run following commands.

   > ```
   > sudo curl -fsSL https://deb.nodesource.com/setup_12.x | sudo -E bash -
   > 											sudo apt-get install -y nodejs
   > 											sudo nodejs -v
   > 										
   > ```

**PM2**

1. Izenda Export service leverages PM2 as process manager. Login as root user and run following commands.

   > ```
   > sudo npm install pm2@4.5.0 -g
   > 											sudo pm2 --version
   > 										
   > ```

### Deployment steps

1. Login as root user and copy Export Service at desired location. Run following commands.

   > ```
   > tar -xvf <export service archive>
   > 											cd package
   > 											sudo pm2 start app.js -- --port 5775
   > 											sudo pm2 startup systemd
   > 											sudo pm2 save
   > 											sudo pm2 list
   > 										
   > ```
2. On successful completion of these commands, Export Service will start listening on specified port number.

   > [![../_images/service_started_linux.png](https://devnet.logianalytics.com/hc/article_attachments/12528146263319/service_started_linux_653x110.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146247191/service_started_linux.png)

### Post-deployment steps

**Apache Reverse Proxy**

1. Login as root user and run following commands.

   1. Update Ubuntu packages to the latest stable version: `sudoapt-getupdate`
   2. Install the Apache web server on Ubuntu: `sudoapt-getinstallapache2-y`
   3. Enable the Apache required modules

      ```
      sudo a2enmod rewritesudo a2enmod proxysudo a2enmod proxy_httpsudo a2enmod headerssudo a2enmod ssl –- if you want to configure as SSLsudo service apache2 restart
      ```
   4. Verify Apache installation by running localhost.

      [![../_images/Ubuntu_Stadnalone_Apache.png](https://devnet.logianalytics.com/hc/article_attachments/12528146338967/ubuntu_stadnalone_apache_653x523.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146314519/ubuntu_stadnalone_apache.png)
   5. Enter domain name in to **apache2.conf** file

      ```
      sudo nano /etc/apache2/apache2.confServerName localhost
      ```
   6. Enter port in to **ports.conf** file

      ```
      Sudo nano /etc/apache2/ports.confListen 9001
      ```
   7. Create **9001.conf** under /etc/apache2/sites-available: `sudonano/etc/apache2/sites-available/9001.conf`

      ```
      <VirtualHost *:9001>
      											ProxyPreserveHost On
      											ProxyRequests Off
      											ProxyPass / http://localhost:5775/
      											ProxyPassReverse / http://localhost:5775/
      											ServerName localhost
      											ErrorLog /var/log/apache2/9001-api-error.log
      											CustomLog /var/log/apache2/9001-api-access.log common
      											</VirtualHost>
      										
      ```
   8. Active the service site.

      ```
      sudo a2ensite 9001.conf
      ```
2. Verify the configuration: `sudoapachectlconfigtest`. If the configuration is correct, the result will be `SyntaxOk`. If not, there is an issue in the configuration.
3. Restart the website: `sudoserviceapache2restart`

## Deploying Export Micro Service on Separate Windows Server

Export micro service can also run on the same server as Izenda back-end application. For installation on same server, follow the steps mentioned here [Export Micro Service](https://devnet.logianalytics.com/hc/en-us/articles/12528207078039-Export-Micro-Service)

### Pre-deployment steps

**Node JS**

1. Izenda Export service needs Node JS runtime environment to execute. Download and install Node JS from `node-v12.21.0-x64.msi` by navigating to <https://nodejs.org/dist/latest-v12.x/>

### Deployment steps

1. Copy export service at desired location and unzip Export Service archive. Open command prompt in administrative mode and navigate to extracted location. Run following command.

   > ```
   > cd package
   > 											node app.js --port 5775
   > 										
   > ```
2. On successful completion of these commands, Export Service will start listening on specified port number.

   > [![../_images/service_started_windows.png](https://devnet.logianalytics.com/hc/article_attachments/12528146285591/service_started_windows_653x102.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146268183/service_started_windows.png)

### Post-deployment steps

**IIS Reverse Proxy**

1. Install Application Request Routing and URL Rewrite Components
2. Open Microsoft Web Platform Installer’s [download page](https://www.microsoft.com/web/downloads/platform.aspx). This can also be opened from IIS Manager Actions panel, “Get New Web Platform Components” link.
3. Download and run the installer.
4. Open Microsoft Web Platform Installer.
5. Search for “Application Request Routing” and click Add.
6. Similarly search for “URL Rewrite 2.0” and click Add.
7. Click Install.

   > ![../_images/web-installer.png](https://devnet.logianalytics.com/hc/article_attachments/12528146341399/web-installer_653x315.png)
8. Setup Reverse Proxy in IIS. Open IIS Manager.
9. Select a server node in the tree view on the left hand side and then click on the “Application Request Routing” feature.

   > [![../_images/arr.png](https://devnet.logianalytics.com/hc/article_attachments/12528146362135/arr_653x324.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146355351/arr.png)
10. Check the “Enable Proxy” check box. Leave the default values for all the other settings on this page:
11. Select Apply.

    > [![../_images/enable-proxy.png](https://devnet.logianalytics.com/hc/article_attachments/12528162430231/enable-proxy_653x365.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146367511/enable-proxy.png)
12. Right-click on a server node in the tree view and add a new website.
13. Click the ellipsis (…) button to select the location of the extracted Izenda export service containing the app.js file.

    > [![../_images/site.png](https://devnet.logianalytics.com/hc/article_attachments/12528146412439/site_653x582.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146393367/site.png)
14. Select your website under sites in left side section. Now select “URL Rewrite” option.

    > [![../_images/url-rewrite.png](https://devnet.logianalytics.com/hc/article_attachments/12528146426135/url-rewrite_653x372.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146422423/url-rewrite.png)
15. Now click on “Add Rule(s)…” in actions section on the right side.
16. Now select Reverse Proxy under inbound and outbound section.

    > [![../_images/add-reverse-proxy.png](https://devnet.logianalytics.com/hc/article_attachments/12528146442135/add-reverse-proxy_653x439.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146435607/add-reverse-proxy.png)
17. Add the server name or IP address with port under inbound rules input box. This is the URL of the export service running locally on the server.

    > [![../_images/add-url.png](https://devnet.logianalytics.com/hc/article_attachments/12528146462103/add-url_653x599.png)](https://devnet.logianalytics.com/hc/article_attachments/12528162512919/add-url.png)
18. At this point, the reverse proxy setup has been done.

## BI Application changes

1. Export micro service can be enabled by setting `EnableExportService` to `1` in `IzendaSystemSetting` table.
2. Additionally, make an entry into `IzendaExportService` table specifying URL of Export Service. For example:

   > ```
   > INSERT INTO [IzendaExportService]([Id],[Url],[RequestCount]) VALUES ('9195E7BE-96A3-4529-985A-C4DC88646FFE','http://52.152.230.0:9001',0);
   > 									
   > ```

## Service Scalability

1. This is an optional step.
2. Export micro service is designed to scale out horizontally into multiple instances. A typical use case scenario would be a heavy load on export functionality. In such situations the load will be shared among multiple instances and multiple simultaneous exports will take relatively lesser time.
3. Deployment Steps

   > > 1. Navigate to the location where service is extracted and simply start the service on a different port.
   > > 2. Additionally, make an entry into IzendaExportService table specifying URL of Export Service. For example, if new service got started on <http://52.152.230.0:9002>, make an entry as following.
   > >
   > > ```
   > > INSERT INTO [IzendaExportService]([Id],[Url],[RequestCount]) VALUES ('5A93C3B8-56CF-409E-B45C-2F288732A53F','http://52.152.230.0:9002',0);
   > > 											
   > > ```
   >
   > [![../_images/micro-services-export-micro-services.png](https://devnet.logianalytics.com/hc/article_attachments/12528146305943/micro-services-export-micro-services_1024x608.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146294423/micro-services-export-micro-services.png)
