---
title: "Uninstall Composer"
id: 43701120892685
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120892685-Uninstall-Composer
updated_at: 2026-05-29T14:08:51Z
---

# Uninstall Composer

# Uninstall Composer

To remove the Composer server and associated microservices from your network environment:

* Remove the Composer server and associated microservices
* Remove Composer-related folders and files
* Remove the PostgreSQL metadata store used by Composer

  **Note:** 
  If you connected Composer to an existing PostgreSQL in your network, then skip these steps.

## Uninstall Composer Server and All Associated Components

Select your server's operating system and follow those steps to completely remove all Composer-related components:

* [In CentOS Environments](#Centos7)
* [Uninstall Composer](#ubuntu18-20)
* [In Windows Environments](#Windows)

### In CentOS Environments

1. Stop all Composer microservices:

   systemctl stop $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
2. Remove Composer and associated components:

   yum remove 'zoomdata\*'

   You are asked to verify the removal of the Composer components. Enter '**y** ' to confirm the removal.
3. Verify the removal of Composer components by running the following command. If all components have been successfully erased, the command returns no results.

   yum list installed | grep zoomdata
4. Remove all the Composer-specific folders:

   sudo rm -rf /etc/zoomdata   
   sudo rm -rf /opt/zoomdata   
   sudo rm -rf /etc/yum.repos.d/zoomdata\*

   The next steps are to remove the PostgreSQL metadata store and related files. However, skip these steps if you used your existing PostgreSQL as Composer's metadata store. In this case, you have completed the removal of all Composer-related components from your server.
5. Remove the PostgreSQL metadata store:

   systemctl stop postgresql-12  
   sudo yum remove 'postgresql\*'
6. Remove the following PostgreSQL-related file:

   sudo yum remove 'pgdg\*'
7. Remove the directories related to PostgreSQL:

   sudo rm -rf /var/lib/pgsql   
   sudo rm -rf /usr/pgsql-12

### In Ubuntu Environments

1. Stop all Composer microservices:

   sudo systemctl stop $(systemctl list-unit-files | grep 'zoomdata' | awk '{print $1}')
2. Remove Composer and associated components:

   sudo apt-get
   remove 'zoomdata\*'

   You are asked to verify the removal of the Composer components. Enter '**y** ' to confirm the removal.
3. Verify the removal of Composer components by running the following command. If all components have been successfully erased, the command returns no results.

   sudo apt list --installed | grep zoomdata
4. Remove all the Composer-specific folders:

   sudo rm -rf /etc/zoomdata   
   sudo rm -rf /opt/zoomdata   
   sudo rm -rf /etc/apt/sources.list.d/zoomdata\*

   The next steps remove the PostgreSQL metadata store and related files. However, skip these steps if you used your existing PostgreSQL as Composer's metadata store. In this case, you have completed the removal of all Composer-related components from your server.
5. Remove the PostgreSQL metadata store:

   sudo systemctl stop postgresql-12  
   sudo apt-get remove 'postgresql\*'
6. Remove the following PostgreSQL-related file:

   sudo apt-get
   remove 'pgdg\*'
7. Remove the directories related to PostgreSQL:

   sudo rm -rf /etc/apt/sources.list.d/pg\*   
   sudo rm -rf /var/lib/postgresql/   
   sudo rm -rf /var/log/postgresql/   
   sudo rm -rf /etc/postgresql   
   sudo rm -rf /etc/postgresql-common/   
   sudo rm -rf /var/run/postgresql

### In Windows Environments

1. Stop all Composer microservices:

   ./bootstrap-composer.ps1 -ServicesAction stop
2. Create a binary PostgreSQL dump of Composer metadata to the `<install-path>/data/backups/` folder:

   ./bootstrap-composer.ps1 -DumpComposerMetadata

   **Important:** 
   Copy the information to a folder outside of the installation path or it will be deleted and unrecoverable after you uninstall Composer.
3. Remove Composer components by running the following command.

   ./bootstrap-composer.ps1 -DeinstallComposer

   See [Windows Bootstrap Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120362381-Windows-Bootstrap-Reference) for more information.

You have completed the removal of all Composer-related components from your server.
