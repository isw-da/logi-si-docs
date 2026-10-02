> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Uninstall Self-Service Analytics

To remove the Self-Service Analytics server and associated microservices from your network environment:

* Remove the Self-Service Analytics server and associated microservices

* Remove Self-Service Analytics-related folders and files

* Remove the PostgreSQL metadata store used by Self-Service Analytics

  <Note>
    If you connected Self-Service Analytics to an existing PostgreSQL in your network, then skip these steps.
  </Note>

<h2 id="uninstall-self-service-analytics-server-and-all-associated">
  Uninstall Self-Service Analytics Server and All Associated Components
</h2>

Select your server's operating system and follow those steps to completely remove all Self-Service Analytics-related components:

* [In CentOS Environments](#in-centos-environments)
* [In Ubuntu Environments](#in-ubuntu-environments)
* [In Windows Environments](#in-windows-environments)

<h3 id="in-centos-environments">
  In CentOS Environments
</h3>

1. Stop all Self-Service Analytics microservices:

   ```bash theme={null}
   systemctl stop $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
   ```

2. Remove Self-Service Analytics and associated components:

   ```bash theme={null}
   yum remove 'zoomdata*'
   ```

   You are asked to verify the removal of the Self-Service Analytics components. Enter '**y** ' to confirm the removal.

3. Verify the removal of Self-Service Analytics components by running the following command. If all components have been successfully erased, the command returns no results.

   ```bash theme={null}
   yum list installed | grep zoomdata
   ```

4. Remove all the Self-Service Analytics-specific folders:

   ```bash theme={null}
   sudo rm -rf /etc/zoomdata
   sudo rm -rf /opt/zoomdata
   sudo rm -rf /etc/yum.repos.d/zoomdata*
   ```

   The next steps are to remove the PostgreSQL metadata store and related files. However, skip these steps if you used your existing PostgreSQL as Self-Service Analytics's metadata store. In this case, you have completed the removal of all Self-Service Analytics-related components from your server.

5. Remove the PostgreSQL metadata store:

   ```bash theme={null}
   systemctl stop postgresql-12
   sudo yum remove 'postgresql*'
   ```

6. Remove the following PostgreSQL-related file:

   ```bash theme={null}
   sudo yum remove 'pgdg*'
   ```

7. Remove the directories related to PostgreSQL:

   ```bash theme={null}
   sudo rm -rf /var/lib/pgsql
   sudo rm -rf /usr/pgsql-12
   ```

<h3 id="in-ubuntu-environments">
  In Ubuntu Environments
</h3>

1. Stop all Self-Service Analytics microservices:

   ```bash theme={null}
   sudo systemctl stop $(systemctl list-unit-files | grep 'zoomdata' | awk '{print $1}')
   ```

2. Remove Self-Service Analytics and associated components:

   ```bash theme={null}
   sudo apt-get remove 'zoomdata*'
   ```

   You are asked to verify the removal of the Self-Service Analytics components. Enter '**y** ' to confirm the removal.

3. Verify the removal of Self-Service Analytics components by running the following command. If all components have been successfully erased, the command returns no results.

   ```bash theme={null}
   sudo apt list --installed | grep zoomdata
   ```

4. Remove all the Self-Service Analytics-specific folders:

   ```bash theme={null}
   sudo rm -rf /etc/zoomdata
   sudo rm -rf /opt/zoomdata
   sudo rm -rf /etc/apt/sources.list.d/zoomdata*
   ```

   The next steps remove the PostgreSQL metadata store and related files. However, skip these steps if you used your existing PostgreSQL as Self-Service Analytics's metadata store. In this case, you have completed the removal of all Self-Service Analytics-related components from your server.

5. Remove the PostgreSQL metadata store:

   ```bash theme={null}
   sudo systemctl stop postgresql-12
   sudo apt-get remove 'postgresql*'
   ```

6. Remove the following PostgreSQL-related file:

   ```bash theme={null}
   sudo apt-get remove 'pgdg*'
   ```

7. Remove the directories related to PostgreSQL:

   ```bash theme={null}
   sudo rm -rf /etc/apt/sources.list.d/pg*
   sudo rm -rf /var/lib/postgresql/
   sudo rm -rf /var/log/postgresql/
   sudo rm -rf /etc/postgresql
   sudo rm -rf /etc/postgresql-common/
   sudo rm -rf /var/run/postgresql
   ```

<h3 id="in-windows-environments">
  In Windows Environments
</h3>

1. Stop all Self-Service Analytics microservices:

   ```bash theme={null}
   ./bootstrap-composer.ps1 -ServicesAction stop
   ```

2. Create a binary PostgreSQL dump of Self-Service Analytics metadata to the `<install-path>/data/backups/` folder:

   ```bash theme={null}
   ./bootstrap-composer.ps1 -DumpComposerMetadata
   ```

   <Warning>
     Copy the information to a folder outside of the installation path or it will be deleted and unrecoverable after you uninstall Self-Service Analytics.
   </Warning>

3. Remove Self-Service Analytics components by running the following command.

   ```bash theme={null}
   ./bootstrap-composer.ps1 -DeinstallComposer
   ```

   See [Windows Bootstrap Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows#windows-bootstrap-reference) for more information.

You have completed the removal of all Self-Service Analytics-related components from your server.
