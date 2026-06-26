---
title: "Cloudera and Kerberos Authentication "
id: 4419715321111
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715321111-Cloudera-and-Kerberos-Authentication
updated_at: 2022-07-17T02:24:17Z
---

# Cloudera and Kerberos Authentication 

# Cloudera and Kerberos Authentication

Logi Info has been certified with Cloudera's CDH4 using Kerberos as a
method to authenticate database access.
*Hortonworks is not certified at this time*.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Hadoop drivers were deprecated from Info Java. The following libraries were removed: hadoop-core-0.20.2.jar,
hive-exec-0.13.0.jar,
hive-jdbc-0.13.0.jar,
hive-service-0.13.0.jar,
libfb303-0.9.1.jar, and
libthrift-0.9.1.jar.

Kerberos security should be enabled at the cluster server by following the
[instructions](https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/sg_how_tos_intro.html)
on the Cloudera web site. MIT's
kfw-4.0.1-amd64.msi
must be installed on the Logi application web server, and then the file
 krb5.conf
should copied from the Kerberos server to the web server. Save it to the
following folder and *change its file extension* as shown:
C:\ProgramData\MIT\Kerberos5\krb5.ini.

![](https://devnet.logianalytics.com/hc/article_attachments/7522809959319/workhadoop_08_333x453.png)

A typical DSN setup is shown above. ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Kerberos will
*not* work with IP addresses in place of a **Host** name.

For this example, a Hadoop account was created for "logixml" and
added to the Kerberos domain ("CLOUDERA"). Then this account is
used in the Impala configuration to allow access as the Kerberos principal
user.

![](https://devnet.logianalytics.com/hc/article_attachments/7522828187543/workhadoop_09_585x247.png)

The MIT Kerberos Ticket Manager utility, which is part of the
kfw-4.0.1-amd64.msi
installation and shown above, is used to get a Kerberos ticket.

![](https://devnet.logianalytics.com/hc/article_attachments/7522809979415/workhadoop_10_477x342.png)

On the server, the MIT Kerberos Get Ticket application is used to obtain
the correct credentials from the Kerberos domain controller.

![](https://devnet.logianalytics.com/hc/article_attachments/7522799064599/workhadoop_11_533x218.png)

Once the credentials are obtained, they appear in the Ticket Manager, as
shown above.
