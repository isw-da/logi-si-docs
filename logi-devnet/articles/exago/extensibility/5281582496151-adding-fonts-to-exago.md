---
title: "Adding Fonts to Exago"
id: 5281582496151
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281582496151-Adding-Fonts-to-Exago
updated_at: 2022-05-03T22:08:17Z
---

# Adding Fonts to Exago

# Adding Fonts to Exago

Additional fonts may be added to Exago by installing them on the web server. Fonts must be available to the user account the web server is running under. The font must also be available on each user’s computer in order to appear in reports.

## Windows

Adding additional fonts to Azure App Services is not supported.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> This procedure requires restarting the web server which will terminate any user sessions in progress.

1. Right-click on the .ttf or .otf font file.
2. Click **Install for all users**.
3. Once all fonts are installed on the server, restart IIS.
4. Verify the font now appears in the Report Designer’s font list.

## Linux

1. As root, copy the .ttf or .otf font file to the font directory.
   * For CentOS, Debian, Fedora, Red Hat Enterprise: `usr/share/fonts/custom`
   * For Ubuntu: `/usr/local/share/fonts`
2. As root, re-build the font-cache by running `fc-cache -fv`.
3. Verify the font now appears in the Report Designer’s font list.
