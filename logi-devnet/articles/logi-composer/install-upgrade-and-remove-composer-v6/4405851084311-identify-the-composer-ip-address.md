---
title: "Identify the Composer IP Address"
id: 4405851084311
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851084311-Identify-the-Composer-IP-Address
updated_at: 2021-09-21T01:28:48Z
---

# Identify the Composer IP Address

# Identify the Composer IP Address

After Composer is installed and the [firewall](https://devnet.logianalytics.com/hc/en-us/articles/4405859364759-Configure-the-Firewall) has been configured, you need to identify the Composer IP address so you can access Composer on your web browser. Record the IP address of the host where Composer is installed.

To
obtain the Composer IP address, enter the following command in a terminal window on the Composer server:

```
[zoomdata@localhost ~]$ hostname -I
```

Make note of this IP address. You will need it when you [access Composer](https://devnet.logianalytics.com/hc/en-us/articles/4405850867223-Access-Composer) from a web browser.
