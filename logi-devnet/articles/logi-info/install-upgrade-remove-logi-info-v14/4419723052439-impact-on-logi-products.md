---
title: "Impact on Logi Products"
id: 4419723052439
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723052439-Impact-on-Logi-Products
updated_at: 2022-07-17T01:42:46Z
---

# Impact on Logi Products

# Impact on Logi Products

The impact of Oracle's new Java release and maintenance policy varies by
Logi product, as follows.

## Logi Info and Logi SSRM

Logi Info Java applications currently work with Oracle JDK 8 and OpenJDK
8. Logi Info 12.6 SP2+ applications now work with Oracle Java 11, 12, 13,
and 14 and OpenJDK 11, 12, 13, and 14.

| Logi Info and SSRM Version | OpenJDK Version |
| --- | --- |
| v12.5-v12.6 SP1 | Open JDK 8 |
| v12.6 SP2-v12.6 SP6 | Open JDK 11 |
| v12.7-v12.7 SP1 | Open JDK 12 and 13 |
| v12.7 SP2-v12.7 SP5 | Open JDK 13 |
| v12.7 SP5- v12.7 SP7 | Open JDK 14 |

Going forward, Logi Info will be certified on the latest OpenJDK releases,
within three weeks of those releases becoming available. In the event that
changes are required in Logi Info itself as a result of a JDK upgrade,
Logi will provide them as a new Service Pack for the latest Logi Info
major release.

Logi customers who choose to stay on one of Oracle's LTS releases (e.g.
Oracle JDK 8, 11, or 12) can continue to do so. If issues are found by
those customers as a result of an update to the Oracle LTS release, or due
to a new Logi Info release, Logi will attempt to resolve those issues.
Customers should generally expect resolution via Service Packs in the two
latest major releases.

## Discovery Module and Logi Platform Services

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) We will no longer bundle Java into our product installers. Customers
are expected to get, install, and maintain the latest OpenJDK versions on
their own.

The Logi Discovery Module (DM) v3.2+ and Logi Platform Services (LPS)
v3.4+ will work with the latest version of OpenJDK. Future releases will
typically be supported within three weeks of release of a new OpenJDK
version.

If you have questions regarding Oracle's policy changes, please visit
[Oracle's support roadmap page](https://www.oracle.com/technetwork/java/java-se-support-roadmap.html). For questions regarding impacts on Logi products and applications,
please contact Logi Customer Support.
