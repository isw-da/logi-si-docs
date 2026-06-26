---
title: "PDF - Special Considerations for Java Apps"
id: 4406822317847
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822317847-PDF-Special-Considerations-for-Java-Apps
updated_at: 2022-04-06T06:06:02Z
---

# PDF - Special Considerations for Java Apps

# PDF - Special Considerations for Java Apps

Developers creating Logi apps that use the **Java** libraries and include less commonly-used fonts or special character sets may need to take steps to ensure that those character sets or fonts are also used in their PDF exports. This is done by adding the **Globalization** element in the \_Settings definition, and setting its **Java Font Folder** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583949719/javafontfolder1.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563305239/javafontfolder1a.png)

The value of this attribute identifies the folder where **TrueType** font files, for use with PDF exports, are located. These are required when PDF exports use fonts that contain characters that are not in the ISO 8859\_1 character set, such as Arabic, Cyrillic, and Korean language characters. Depending on your Java environment, you may even need to point the Logi application to the location of your regular fonts in order to ensure that they'll be used.

A typical value for a Windows installation might be something like C:\Windows\Fonts. For a Linux installation, the value might be something like /usr/local/share/fonts/ttfonts. This attribute is only functional when creating a Java application.

CSS classes are cached for Java application exports to PDF. If you need to stop this caching, add this case-sensitive constant in your \_Settings definition: rdJavaPdfClearCache = *True*.
