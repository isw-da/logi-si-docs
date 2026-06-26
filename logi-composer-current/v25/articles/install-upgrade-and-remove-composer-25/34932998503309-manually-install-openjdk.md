---
title: "Manually Install OpenJDK"
id: 34932998503309
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932998503309-Manually-Install-OpenJDK
updated_at: 2026-05-26T22:07:23Z
---

# Manually Install OpenJDK

# Manually Install OpenJDK

Composer v23.2 and later runs on Java 17.
When you perform a straightforward upgrade to this release, Java is updated automatically.

Composer v23.1 and earlier continue to run on Java 11.

**Manually install OpenJDK**

1. Stop all Composer components (if any are running) before you install OpenJDK. See  [Stop Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Stop).
2. Run the following command on the installation machine.

   For JDK 17:

   sudo mkdir -p /opt/zoomdata/jre && curl -sL https://corretto.aws/downloads/latest/amazon-corretto-17-x64-linux-jdk.tar.gz | sudo tar zx -C /opt/zoomdata/jre --strip-components=1

   For JDK 11:

   sudo mkdir -p /opt/zoomdata/jre && curl -sL https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.tar.gz | sudo tar zx -C /opt/zoomdata/jre --strip-components=1
3. Restart all Composer components. See  [Start Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Start).

**Note:** 
In Windows environments, Composer installs a compatible JDK as part of the bootstrap installation. To install a system wide Java distribution, see <https://www.java.com/en/download/help/windows_manual_download.html>.

For information on how Composer validates the version of Java used in an environment, see [How Composer Validates an Environment's Java Version](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932998659341-How-Composer-Validates-an-Environment-s-Java-Version).
