---
title: "Admin Console Password Encryption"
id: 5281617339287
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281617339287-Admin-Console-Password-Encryption
updated_at: 2023-04-03T17:52:19Z
---

# Admin Console Password Encryption

# Admin Console Password Encryption

Beginning with *v2017.3*, the **Admin Console** password is now encrypted by default when entered into the Admin Console or when set through an API call. This is done to increase the security of credential storage by preventing plain text passwords from being saved to disk in the unencrypted version of the configuration file.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> If updating from an older version, existing passwords will not be encrypted automatically.

There are two ways to set an encrypted Admin Console password: Using the **Admin Console** or the **API**.

### Using the Admin Console

1. Browse to the Admin Console
2. Navigate to ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Other Settings**.
3. Enter the desired password into the **Password** and **Confirm Password** fields  
   ![pass.png](https://devnet.logianalytics.com/hc/article_attachments/5432124771735/pass.png)
4. Click **Apply** or **Okay**

To verify that the configuration contains the encrypted password, open the XML config file in a text or XML editor and locate the <password> node.

![enc_pw.png](https://devnet.logianalytics.com/hc/article_attachments/5432258481687/enc_pw.png)

The value should be an encrypted string surrounded by brackets [ ].

### Using the API

To add an encrypted password to a programmatically generated config file:

```
 api.General.Password = api.General.EncryptPassword("mypassword");
 api.SaveConfigToFile(); // Save the configuration file to disk
```

For versions *pre-2019.2*:

```
api.General.Password = api.General.EncryptPassword("mypassword");
api.SaveData(); // Save the configuration file to disk
```

To verify whether two passwords match:

```
bool IsMatch = api.General.CheckPassword("mypassword", api.General.Password);
```

To verify if an existing password is encrypted:

```
bool IsEncrypted = api.General.IsHashedPassword(api.General.Password);
```

### Additional information

Password encryption is one-way. An encrypted password cannot be decrypted into plain text.

The encryption algorithm used is **[SHA-256](https://en.wikipedia.org/wiki/SHA-2)**. Passwords are **[salted](https://en.wikipedia.org/wiki/Salt_(cryptography))**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> We still recommend that the plain text config file (for example *WebReports.xml*) is removed in favor of the encrypted config file (for example *WebReports.xml.**enc***) in a production environment. See **[Security Checklist](https://devnet.logianalytics.com/hc/en-us/articles/5281588834455-Security-Checklist)** for more information.
