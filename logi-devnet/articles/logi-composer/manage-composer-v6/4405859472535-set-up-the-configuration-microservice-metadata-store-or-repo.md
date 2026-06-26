---
title: "Set Up the Configuration Microservice Metadata Store or Repository"
id: 4405859472535
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859472535-Set-Up-the-Configuration-Microservice-Metadata-Store-or-Repository
updated_at: 2021-09-21T01:29:39Z
---

# Set Up the Configuration Microservice Metadata Store or Repository

# Set Up the Configuration Microservice Metadata Store or Repository

Before you can install and start Composer's configuration microservice, you must set up a PostgreSQL metastore or a GitHub repository to store Composer property metadata. A separate PostgreSQL database or a separate GitHub repository must be configured.

See the following sections:

* [*PostgreSQL Database Setup Notes*](#PostgreS)
* [*GitHub Repository Setup Notes*](#GitHub)

## PostgreSQL Database Setup Notes

If you elect to persist property metadata to a PostgreSQL metastore:

1. Configure a separate database and make it accessible to the connection user account:

   ```
   CREATE DATABASE <composer-config> WITH OWNER <db_username>;
   ```

   where `<composer-config>` is the name of the PostgreSQL database and `<db_username>` is the connection user account name.
2. Add the following properties to the Composer`config-server.properties` file, located in the `/etc/zoomdata` directory:

   ```
   # metadata storage settings  
   spring.datasource.url=jdbc:postgresql://localhost:5432/<composer-config>  
   spring.datasource.username=<db_username>  
   spring.datasource.password=<db_password>
   ```

   Substitute the connection user account name and password you set up in Step 1 for `<db_username>` and `<db_password>`. Substitute the name of the PostgreSQL database for `<composer-config>`.
3. Save the properties file. You will restart the configuration microservice when you configure it. See [*Configure and Start the Configuration Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405859471255-Configure-and-Start-the-Configuration-Microservice).

## GitHub Repository Setup Notes

If you elect to persist property metadata to a GitHub repository:

1. Add the following properties to the Composer`config-server.properties` file, located in the `/etc/zoomdata` directory:

   ```
   # metadata storage settings  
   spring.cloud.config.server.git.uri=<repo_uri>
     
   spring.cloud.config.server.git.skipSslValidation=true
     
   spring.cloud.config.server.git.username=<repo_username>
     
   spring.cloud.config.server.git.password=<repo_password>
   ```

   Substitute the repository user account name and password for `<repo_username>` and `<repo_password>`. Substitute the URI of the repository for `<repo_uri>` (for example, `https://example.com/my/repo`).

   Additional and advanced configuration information can be found in [Spring.io's documentation](https://cloud.spring.io/spring-cloud-config/multi/multi__spring_cloud_config_server.html#_git_backend).
2. Save the properties file. You will restart the configuration microservice when you configure it. See [*Configure and Start the Configuration Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405859471255-Configure-and-Start-the-Configuration-Microservice).
