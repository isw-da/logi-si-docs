---
title: "Export Micro Service"
id: 12528207078039
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528207078039-Export-Micro-Service
updated_at: 2023-02-23T15:15:05Z
---

# Export Micro Service

# Export Micro Service

## Deploying Export Micro Service on Linux

Export micro service does not required to be installed on same server as Izenda back-end or front-end. It can also run on any separate server. This topic describes deploying Micro Services with the Izenda BI.

For installation on separate server, follow the steps mentioned here [Export Micro Service](https://devnet.logianalytics.com/hc/en-us/articles/12528207082007-Export-Micro-Service-Reverse-Proxy) . The only difference is to setup a reverse proxy on web server.

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
   > 											sudo pm2 start app.js -- --port <port number>
   > 											sudo pm2 startup systemd
   > 											sudo pm2 save
   > 											sudo pm2 list
   > 										
   > ```
2. On successful completion of these commands, Export Service will start listening on specified port number.

   > [![../_images/service_started_linux.png](https://devnet.logianalytics.com/hc/article_attachments/12528146263319/service_started_linux_653x110.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146247191/service_started_linux.png)

## Deploying Export Micro Service on Windows

Export micro service does not required to be installed on same server as Izenda back-end or front-end. It can also run on any separate server. For installation on separate server, follow the steps mentioned here [Export Micro Service](https://devnet.logianalytics.com/hc/en-us/articles/12528207082007-Export-Micro-Service-Reverse-Proxy) . The only difference is to setup a reverse proxy on web server.

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

## BI Application changes

1. Export micro service can be enabled by setting `EnableExportService` to `1` in `IzendaSystemSetting` table.
2. Additionally, make an entry into `IzendaExportService` table specifying URL of Export Service. For example:

   > ```
   > INSERT INTO [IzendaExportService]([Id],[Url],[RequestCount]) VALUES ('9195E7BE-96A3-4529-985A-C4DC88646FFE','http://localhost:5775',0);
   > 									
   > ```

## Service Scalability

1. This is an optional step.
2. Export micro service is designed to scale out horizontally into multiple instances. A typical use case scenario would be a heavy load on export functionality. In such situations the load will be shared among multiple instances and multiple simultaneous exports will take relatively lesser time.
3. Deployment Steps

   > > 1. Navigate to the location where service is extracted and simply start the service on a different port.
   > > 2. Additionally, make an entry into IzendaExportService table specifying URL of Export Service. For example, if new service got started on <http://localhost:5776>, make an entry as following.
   > >
   > > ```
   > > INSERT INTO [IzendaExportService]([Id],[Url],[RequestCount]) VALUES ('5A93C3B8-56CF-409E-B45C-2F288732A53F','http://localhost:5776',0);
   > > 											
   > > ```
   >
   > [![../_images/micro-services-export-micro-services.png](https://devnet.logianalytics.com/hc/article_attachments/12528146305943/micro-services-export-micro-services_1024x608.png)](https://devnet.logianalytics.com/hc/article_attachments/12528146294423/micro-services-export-micro-services.png)
