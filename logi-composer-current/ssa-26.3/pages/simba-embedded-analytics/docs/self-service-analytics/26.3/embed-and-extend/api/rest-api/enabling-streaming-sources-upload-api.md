> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Upload API Source

Self-Service Analytics supports live streaming sources. This source uses PostgreSQL as a storage medium for the incoming data flow. By default, Self-Service Analytics uses PostgreSQL to store the data for Upload API. This PostgreSQL instance is separate from other PostgreSQL instances you may have in existence. You can elect to use another PostgreSQL instance that you may have by changing the configuration properties.

### Before You Begin

If you want to use an existing PostgreSQL instance in conjunction with the Upload API microservice, you need to find the above information in your `edc-postgresql.properties` file.

### Use Another PostgreSQL Instance for Upload API

1. Use the following command to access and open the properties file:

2. Add the following parameters to the file:

   ```properties theme={null}
   #  that are configured for Upload API
   upload.destination.params.user_name=yourusername
   upload.destination.params.password=yourpassword
   upload.destination.params.jdbc_url=jdbc:postgresql://yourlocalhost:yourport//zd_upload
   upload.batch-size=1000
   ```

3. Save and exit the configuration file.

4. Restart the Self-Service Analytics server.
