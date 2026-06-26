---
title: "Configure and Start the Configuration Microservice"
id: 43701128284045
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128284045-Configure-and-Start-the-Configuration-Microservice
updated_at: 2026-05-29T14:09:26Z
---

# Configure and Start the Configuration Microservice

# Configure and Start the Configuration Microservice

**Install, configure, and start the** Composer **configuration microservice**

1. Verify that you have set up a PostgreSQL metastore or a GitHub repository to store the property metadata. See [Set Up the Configuration Microservice Metadata Store or Repository](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175948429-Set-Up-the-Configuration-Microservice-Metadata-Store-or-Repository).
2. Open the SSH client associated with your instance.
3. Configure all installed and enabled microservices to use the configuration microservice. Run the following script:

   for i in $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}'|sed -e 's/\.service/.properties/g' -e 's/zoomdata\-//g');  
   do  
   echo "config-server.enabled=true">>/etc/zoomdata/$i;  
   done
4. Each microservice supports two configuration properties related to the configuration microservice:

   * `config-server.enabled`: Enables or disables integration with the configuration microservice. Valid values are `true` (enable integration) and `false` (disable integration). The default is `true`.
   * `config-client.retry.max-attempts`: Sets the maximum number of attempts that should be made to connect to the configuration microservice. The default is 20. The microservice will fail if the number of attempts to connect to the configuration microservice exceeds this value. This property is useful in situations where the configuration microservice starts with a delay. If your microservice fails while waiting for the configuration microservice and you want to give it more time, increase this value.

   Update these properties, as appropriate, for each microservice.
5. Install, enable and start the configuration microservice. Enter the following commands:

   sudo yum install zoomdata-config-server \  
   && systemctl enable zoomdata-config-server \  
   && systemctl start zoomdata-config-server

   **Note:** 
   After starting the configuration microservice with a valid database configuration, the microservice should connect to the database and create a properties table.
6. Restart all the other microservices. Enter the following command:

   sudo systemctl restart $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}')

   See also  [Restart Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Restart).
