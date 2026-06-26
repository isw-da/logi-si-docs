---
title: "Configuring IIS Authentication"
id: 4419715175191
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715175191-Configuring-IIS-Authentication
updated_at: 2022-07-17T02:24:53Z
---

# Configuring IIS Authentication

# Configuring IIS Authentication

The following examples refer to IIS 7.5 but are also applicable to other
IIS versions.

Typically, integrated Windows security is used to connect to SSAS and your
Logi application's authentication method on IIS must be configured for
this. There are different configurations for four possible scenarios, as
follows:

**A. IIS and SSAS on the Same Server - Use Windows Login Account**

If IIS and SSAS are running on the *same* server and you want the
Logi application to use the user's Active Directory domain account to
access the database. In this case, individual users will need separate
logins for the database. To use this approach, configure your IIS
authentication for *impersonation*:

![](https://devnet.logianalytics.com/hc/article_attachments/7522847915287/connssas_01.png)

This is done in IIS Manager, as shown above, by configuring your
application's Authentication feature. In this example, one of the
authentication methods available is *ASP.NET Impersonation* - just
enable it. Its *Authenticated User* option (shown for completeness
here) is the default setting.

If *ASP.NET Impersonation* is not available in your list of methods,
you can manually make the change using these steps:

<?xml version="1.0" encoding="UTF-8"?>  
 <configuration>  
 <system.web>  
<identity impersonate="true"/>  
  
 <!-- DYNAMIC DEBUG COMPILATION  
 Set
compilation debug="true" to insert debugging symbols (.pdb
information)  
 into the
compiled page. Because this creates a larger file that executes...

  

1. In your Logi application folder, using Notepad or another text editor,
   edit the file
   Web.config.
2. Add the text highlighted above to the file. The user's Windows account
   credentials will be passed to SSAS.
3. Save and close the file.

**B. Use a Specific Database Login Account**

Another approach is to create a single login account for the database, one
that all Logi application sessions will use. This presumes appropriate
user security will be applied in the application. For this, configure your
IIS authentication for *impersonation*:

![](https://devnet.logianalytics.com/hc/article_attachments/7522832051607/connssas_02.png)

This is done in IIS Manager, as shown above, by configuring your
application's Authentication feature. One of the authentication methods
available is *ASP.NET Impersonation* - just enable it - then edit it
and select the *Specific User* option. Click **Set...** to supply
the database login ID and password you want to use.

When you click **OK**, if the application exists already, the program
will attempt a login using the supplied credentials in order to validate
them.

If *ASP.NET Impersonation* is not available in your list of methods,
you can manually make the change using these steps:

<?xml version="1.0" encoding="UTF-8"?>  
 <configuration>  
 <system.web>  
<identity impersonate="true"
userName="YourDBLoginID"
password="yourDBPassword"/>  
  
 <!-- DYNAMIC DEBUG COMPILATION  
 Set
compilation debug="true" to insert debugging symbols (.pdb
information)  
 into the
compiled page. Because this creates a larger file that executes...

  

1. In your Logi application folder, using Notepad or another text editor,
   edit the file
   Web.config.
2. Add the text highlighted above to the file. The account credentials
   entered here will be passed to SSAS.
3. Save and close the file.

**C. IIS and SSAS on the Different Servers - Use Windows Login Account**

If IIS and SSAS are running on *different* servers and you want the
Logi application to use the user's Active Directory domain account to
access the database, then configuration is more complicated. IIS can't
directly pass the account information to SSAS - this is known as a
dangerous authentication "double-hop" - so you'll need to
implement **Kerberos** authentication to help IIS safely pass the
account information to SSAS. That procedure is beyond the scope of this
document and is discussed in this
[Microsoft document](https://docs.microsoft.com/en-us/analysis-services/instances/configure-analysis-services-for-kerberos-constrained-delegation?redirectedfrom=MSDN&view=asallproducts-allversions&viewFallbackFrom=sql-server-ver15).

**D. Multi-Tenant Configurations**

A common "multi-tenant" service approach is to host multiple
instances of a Logi application on a single Web server, with separate
Application Pools for each instance (among other things, this allows
restarting one instance without affecting others). One way to secure
access to data while using a single Logi application connection is to
specify a unique identity for each Application Pool used. Each identity
corresponds to a special Active Directory domain account that has a
database login.

Configuring unique Application Pool identities is done in IIS Manager:

![](https://devnet.logianalytics.com/hc/article_attachments/7522847938839/connssas_03.png)

1. Open the Application Pools node in the Connections panel.
2. Select the application pool you want to configure and select its
   *Advanced Settings*.
3. Select the *Identity* property, as shown above, and click its
   browse button.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/7522847944727/connssas_04.png)

4. In the Application Pool Identity dialog box that appears, check
   *Custom Account* and click **Set...**
5. Enter the Active Directly domain account name and password to be used to
   access SSAS.
6. Click **OK** as needed to exit.

The Microsoft document
[*Specifying an Application Pool Identity (IIS7)*](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771170(v=ws.10)?redirectedfrom=MSDN)
provides more information about this process.

**Which Configuration Should You Use?**

Let's review the basic security terminology:
*authentication* identifies the user as valid, and
*authorization* determines which resources the authenticated user can
access. In production environments, it's not likely that IIS and SSAS will
be running on the same system, so scenarios B, C, and D above are the most
likely authentication options.

The most common approach used by Logi developers is B, which locates the
handling of authorization *in the Logi application*, using Logi
Security to control which reports and activities, and therefore data,
users can access. Using one specific login to access the database is
suitable for this and minimizes account maintenance headaches. This is
widely used by Logi customers for both OLAP and regular database access.
Each user has their own session on the web server and that translates into
their own connection to the database, so connection-related performance
constraints are not generally an issue.

Approaches C and D, which locate authorization
*in the database* itself, essentially recreate the accounts and/or
roles that appear in the application authentication mechanism in the
database as well. This requires additional administrative overhead (for
example, accounts must be maintained in *both* Active Directory and
in SQL Server) and connection complexity. Approach D is sometimes used in
multi-tenant database scenarios, but it's not a required approach.
Developers who choose to use these approaches will need extensive
expertise with Windows, IIS, and SSAS security configuration techniques in
order to succeed.
