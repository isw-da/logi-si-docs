---
title: "Manually Install OpenJDK\u00a011"
id: 4405851089815
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851089815-Manually-Install-OpenJDK-11
updated_at: 2021-09-21T01:28:51Z
---

# Manually Install OpenJDK 11

# Manually Install OpenJDK 11

Composer 5.8 and later versions require Java 11.0.5. All supported Zoomdata versions and earlier versions of Composer 5 use Java 8.

To manually install OpenJDK 11:

1. Stop all Composer components (if any are running) before you install OpenJDK 11. See [*Stop Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851101463-Stop-Composer-Microservices).
2. Run the following command on the installation machine.

   ```
   sudo mkdir -p /opt/zoomdata/jre && curl -sL https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.tar.gz | sudo tar zx -C /opt/zoomdata/jre --strip-components=1
   ```
3. Restart all Composer components. See [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices).

For information on how Composer validates the version of Java used in an environment, see [*How Composer Validates an Environment's Java Version*](https://devnet.logianalytics.com/hc/en-us/articles/4405859375767-How-Composer-Validates-an-Environment-s-Java-Version).
