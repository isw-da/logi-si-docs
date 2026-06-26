---
title: "Enable FIPS Compliant Encryption on Windows"
id: 5281581323927
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281581323927-Enable-FIPS-Compliant-Encryption-on-Windows
updated_at: 2022-05-03T22:09:08Z
---

# Enable FIPS Compliant Encryption on Windows

# Enable FIPS Compliant Encryption on Windows

Exago is [FIPS (Federal Information Processing Standard) 140-2](https://technet.microsoft.com/en-us/library/cc750357.aspx) compliant. FIPS is a United States and Canadian government standard which defines a minimum set of security requirements for cryptographic systems. This standard is designed for products to secure sensitive but unclassified information.

Exago is compliant with FIPS Level 2 (140-2) which is the current active version of the standard. Before enabling FIPS, please be aware that you may lose access to certain websites which use SSL 1.0 via Internet Explorer. For more details, see the following Microsoft support topics:

* [“System cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing” security setting effects in Windows XP and in later versions of Windows](https://support.microsoft.com/en-us/kb/811833)
* [PRB: Cannot visit SSL sites after you enable FIPS compliant cryptography](https://support.microsoft.com/en-us/kb/811834)

## Enabling FIPS

FIPS compliant encryption on Windows can be enabled using a local group policy setting or by editing a registry key.

### Group Policy

Log in with an account that has administrative credentials. To open the Group Policy editor, press Start, press Run, type **gpedit.msc**, and press Enter.

Navigate to the following setting:

*Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options*

![](https://devnet.logianalytics.com/hc/article_attachments/5432348024087/group_policy_setting.png)

Windows Local Group Policy Editor window

In the Details pane, double-click *System cryptography: Use FIPS-compliant algorithms for encryption, hashing, and signing.*

![](https://devnet.logianalytics.com/hc/article_attachments/5432297117463/fips_setting_on.png)

Enabling the System cryptography: Use FIPS compliant algorithm for encryption policy

Select *Enabled*, and press OK or Apply. Then restart the web server.

### Windows Registry

Log in with an account that has administrative credentials. To open the Registry editor, press Start, press Run, type **regedit**, and press Enter.

Navigate to the following key:

HKEY\_LOCAL\_MACHINESystemCurrentControlSetControlLsaFipsAlgorithmPolicy

![](https://devnet.logianalytics.com/hc/article_attachments/5432297136919/registry_setting.png)

Windows Registry editor

Double-click on *Enabled*.

![](https://devnet.logianalytics.com/hc/article_attachments/5432224011287/fips_registry_setting_on.png)

Enter 1 in Value data, then press OK. Then restart the web server.
