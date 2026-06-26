---
title: "Configure and Start the Configuration Microservice"
id: 4405859471255
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859471255-Configure-and-Start-the-Configuration-Microservice
updated_at: 2021-09-21T01:29:38Z
---

# Configure and Start the Configuration Microservice

# Configure and Start the Configuration Microservice

To install, configure, and start the Composer configuration microservice:

1. Verify that you have set up a PostgreSQL metastore or a GitHub repository to store the property metadata. See [*Set Up the Configuration Microservice Metadata Store or Repository*](https://devnet.logianalytics.com/hc/en-us/articles/4405859472535-Set-Up-the-Configuration-Microservice-Metadata-Store-or-Repository).
2. Open the SSH client associated with your Composer instance.
3. Configure all installed and enabled Composer microservices to use the Composer configuration microservice. Run the following script:

   ```
   for i in $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}'|sed -e 's/\.service/.properties/g' -e 's/zoomdata\-//g');  
   do  
   echo "config-server.enabled=true">>/etc/zoomdata/$i;  
   done
   ```
4. Install, enable and start the Composer configuration microservice. Enter the following commands:

   ```
   sudo yum install zoomdata-config-server \  
   && systemctl enable zoomdata-config-server \  
   && systemctl start zoomdata-config-server
   ```

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) After starting the configuration microservice with a valid database configuration, the microservice should connect to the database and create a properties table.
5. Restart all the other Composer microservices. Enter the following command:

   ```
   sudo systemctl restart $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}')
   ```

   See also [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).
