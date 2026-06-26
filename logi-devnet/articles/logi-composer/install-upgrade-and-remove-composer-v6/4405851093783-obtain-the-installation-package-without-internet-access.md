---
title: "Obtain the Installation Package  Without Internet Access"
id: 4405851093783
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851093783-Obtain-the-Installation-Package-Without-Internet-Access
updated_at: 2021-09-21T01:28:54Z
---

# Obtain the Installation Package  Without Internet Access

# Obtain the Installation Package Without Internet Access

If the target server for your Composer installation does not have Internet access, you can download the PostgreSQL repo package from another source and then transfer the files to the target server. Take the following steps to obtain the PostgreSQL repo package:

1. Access the PostgreSQL website, navigate to the PostgreSQL 12 section, and locate the correct repo package for your target server.

   ```
        https://yum.postgresql.org/repopackages.php#pg12
   ```
2. Copy the link address of the PostgreSQL repo package. For example, right-click on the link and select the **Copy Link Address** option.
3. Paste the copied link address into the following command line and execute it:

   ```
   yum install -y <copied_link_URL>
   ```

   This command needs to be run from a server containing the same OS version as the target server for the Composer installation.
4. Run the following command line to download the dependencies for your selected PostgreSQL repo package:

   ```
   yum install --enablerepo=pgdg12 -y postgresql12-server --downloadonly --downloaddir=/<your_target_directory>
   ```
5. Transfer the PostgreSQL repo package to the target server.
6. Run the PostgreSQL repo package from the target server.
