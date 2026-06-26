---
title: "Uninstall Composer"
id: 4405851102359
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851102359-Uninstall-Composer
updated_at: 2024-01-10T10:49:29Z
---

# Uninstall Composer

# Uninstall Composer

To remove the Composer server and associated microservices from your network environment:

* Remove the Composer server and associated microservices
* Remove Composer-related folders and files
* Remove the PostgreSQL metadata store used by Composer\*

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you connected Composer to an existing PostgreSQL in your network, then skip these steps.

## Uninstall Composer Server and All Associated Components

Select your server's operating system and follow those steps to completely remove all Composer-related components:

* [*In CentOS 7 or 8 Environments*](#Centos7-8)
* [*In Ubuntu 16 or 18 Environments*](#ubuntu16-18)

### In CentOS 7 or 8 Environments

1. Stop all Composer microservices:

   ```
   systemctl stop  $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
   ```
2. Remove Composer and associated components:

   ```
   yum remove 'zoomdata*'
   ```

   You are asked to verify the removal of the Composer components. Enter '**y** ' to confirm the removal.
3. Verify the removal of Composer components by running the following command. If all components have been successfully erased, the command returns no results.

   ```
   yum list installed | grep zoomdata
   ```
4. Remove all the Composer-specific folders:

   ```
   sudo rm -rf /etc/zoomdata     
   sudo rm -rf /opt/zoomdata					  
   sudo rm -rf /etc/yum.repos.d/zoomdata*
   ```

   The next steps are to remove the PostgreSQL metadata store and related files. However, skip these steps if you used your existing PostgreSQL as Composer's metadata store. In this case, you have completed the removal of all Composer-related components from your server.
5. Remove the PostgreSQL metadata store:

   ```
   systemctl stop postgresql-12  
   sudo yum remove 'postgresql*'
   ```
6. Remove the following PostgreSQL-related file:

   ```
   sudo yum remove 'pgdg*'
   ```
7. Remove the directories related to PostgreSQL:

   ```
   sudo rm -rf /var/lib/pgsql       
   sudo rm -rf /usr/pgsql-12
   ```

### In Ubuntu 16 or 18 Environments

1. Stop all Composer microservices:

   ```
   sudo systemctl stop $(systemctl list-unit-files | grep 'zoomdata' | awk '{print $1}')
   ```
2. Remove Composer and associated components:

   ```
   sudo apt-get 
   remove 'zoomdata*'
   ```

   You are asked to verify the removal of the Composer components. Enter '**y** ' to confirm the removal.
3. Verify the removal of Composer components by running the following command. If all components have been successfully erased, the command returns no results.

   ```
   sudo apt list --installed | grep zoomdata
   ```
4. Remove all the Composer-specific folders:

   ```
   sudo rm -rf /etc/zoomdata       
   sudo rm -rf /opt/zoomdata					  
   sudo rm -rf /etc/apt/sources.list.d/zoomdata*
   ```

   The next steps remove the PostgreSQL metadata store and related files. However, skip these steps if you used your existing PostgreSQL as Composer's metadata store. In this case, you have completed the removal of all Composer-related components from your server.
5. Remove the PostgreSQL metadata store:

   ```
   sudo systemctl stop postgresql-12  
   sudo apt-get remove 'postgresql*'
   ```
6. Remove the following PostgreSQL-related file:

   ```
   sudo apt-get
   remove 'pgdg*'
   ```
7. Remove the directories related to PostgreSQL:

   ```
   sudo rm -rf /etc/apt/sources.list.d/pg*       
   sudo rm -rf /var/lib/postgresql/					  
   sudo rm -rf /var/log/postgresql/					  
   sudo rm -rf /etc/postgresql					  
   sudo rm -rf /etc/postgresql-common/					  
   sudo rm -rf /var/run/postgresql
   ```

You have completed the removal of all Composer-related components from your server.
