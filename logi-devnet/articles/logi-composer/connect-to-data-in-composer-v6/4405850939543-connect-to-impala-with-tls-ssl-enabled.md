---
title: "Connect to Impala with TLS (SSL) Enabled"
id: 4405850939543
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850939543-Connect-to-Impala-with-TLS-SSL-Enabled
updated_at: 2021-09-21T01:27:21Z
---

# Connect to Impala with TLS (SSL) Enabled

# Connect to Impala with TLS (SSL) Enabled

You can connect to the Impala data source with TLS/SSL network-level encryption to secure your data while working with your data source.

### Prerequisites

**For Impala:**

* Before you proceed, make sure that TLS is configured for Impala using either [Cloudera Manager](https://docs.cloudera.com/documentation/enterprise/5-4-x/topics/impala_ssl.html#concept_gnk_2tt_qp) or
  the [Command Line interface](https://docs.cloudera.com/documentation/enterprise/5-4-x/topics/impala_ssl.html#concept_q1p_j2d_rp).

* Impala's TLS configuration requires an x509 certificate that will identify the Impala daemon to clients during TLS connections. Production usage of TLS usually implies purchasing the necessary certificates from a commercial Certificate Authority (CA), while development environments can use self-signed certificates. If you have either a **rootCA** from the trusted CA
  or a **self-signed certificate** in PEM format you can verify your Impala TLS configuration using the `openssl` utility:

  ```
  openssl s_client -connect <impala_host>:port -CAfile <certificate.pem>
  ```

**For Composer Server/Impala Connector:**

* There is no particular configuration related to TLS from the point of view of Composer components. However, the client must have a
  [Java **truststore**](https://docs.oracle.com/cd/E19509-01/820-3503/ggffo/index.html)
  with a correct certificate (for example, a root certificate provided by some CA) installed. This means that the
  **truststore** must be accessible to the Composer Server/Impala connector.
* To list all the certificates installed in the Java truststore, use the `keytool` utility:

  ```
  keytool -v -list -keystore <path_to_truststore> -storetype jks -storepass <truststore_password>
  ```

After you have the Java truststore configured, enabling SSL from Composer’s perspective is a matter of composing the correct JDBC URL.

### Creating a JDBC URL with the TLS Parameters

To specify the TLS-related parameters, use the following template for a JDBC URL:

```
jdbc:hive2://<impala_host>:<port>/;ssl=true;sslTrustStore=<path_to_truststore>;
trustStorePassword=<truststore_password>;auth=noSasl
```

where:

* `ssl=true` is a required parameter for enabling TLS encryption.
* `path_to_truststore` is the path to a Java **truststore** which contains either a certificate issued by a trusted CA or a self-signed certificate (not recommended and shouldn’t be used in a production environment).

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Make sure that the Composer server/connector process has read access privileges to the **truststore** file.
* `truststore_password` is the password to access the **truststore**.
* `auth=noSasl` is a required parameter when no authentication or simple user/password authentication is used.

## Use TLS Encryption with Kerberos Authentication

See [*Connect to a Kerberized CDH Cluster*](https://devnet.logianalytics.com/hc/en-us/articles/4405859216407-Connect-to-a-Kerberized-CDH-Cluster)
for more details on enabling Kerberos authentication. The template for a JDBC URL containing both TLS and Kerberos parameters is as follows:

```
jdbc:hive2://<impala_host>:<port>/;principal=<impala_principal>;ssl=true;
sslTrustStore=<path_to_truststore>;trustStorePassword=<truststore_password>
```

You do not need to specify the `auth=noSasl` parameter when using Kerberos authentication.
