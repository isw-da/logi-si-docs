---
title: "Fix Blank Visuals in the Home Page (for RPM Installations)"
id: 43701196098957
section: "Composer 26 Troubleshooting"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701196098957-Fix-Blank-Visuals-in-the-Home-Page-for-RPM-Installations
updated_at: 2026-05-29T14:09:34Z
---

# Fix Blank Visuals in the Home Page (for RPM Installations)

# Fix Blank Visuals in the Home Page (for RPM Installations)

## Symptom

If you successfully installed the RPM version of Composer and only see blank visuals on the dashboard, there may be a hostname mismatch in two specific Composer files:
`/etc/sysconfig/network` and `/etc/hosts`.

## Possible Cause

In the file `/etc/sysconfig/network`, the following setting is needed:

HOSTNAME=<servername>

Substitute any alphanumeric hostname for `<servername>`.

In the file `/etc/hosts`, the following should be listed:

<your\_server\_IP> <servername>

Substitute the IP address and hostname of your Composer instance for `<your_server_IP>` and `<servername>`.

## Resolution

To resolve this issue, open the two files and verify that the hostname references in both files match.

* If the hostname reference does not exist in the
  `/etc/sysconfig/network`
  file, then it must be added. The name must match the name in the
  `/etc/hosts`
  file.
* If the hostname reference exists in both files, then one of the references must be revised to match the other.

To correct this error:

1. Log out of Composer, if you are still in the program and close the browser.
2. From your terminal, open a command line session.
3. Change to the `zoomdata` directory. See [Configure Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700989620365-Configure-Composer) if you need guidance.
4. Edit the file `/etc/sysconfig/network`. Search for the term `HOSTNAME`. If the term is not in the file, add the following line:

   HOSTNAME=<servername>

   Substitute any alphanumeric hostname for `<servername>`.

   Save the file.
5. Edit the file `/etc/hosts`. Find or add the following line in the file.

   <your\_server\_IP> <servername>

   Substitute the IP address and hostname of your Composer instance for `<your_server_IP>` and `<servername>`. Verify that the `<servername>` specified in the `/etc/hosts` file matches the `<servername>` in the `/etc/sysconfig/network`file.

   Save the file.
6. Open a new browser session and log back into Composer to verify that the visuals are displaying in the gallery.

If this solution did not resolve the problem, contact Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support).
