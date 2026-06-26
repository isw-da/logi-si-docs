---
title: "Oracle Policy Changes"
id: 4419723054359
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723054359-Oracle-Policy-Changes
updated_at: 2022-07-17T02:07:03Z
---

# Oracle Policy Changes

# Oracle Policy Changes

Starting in January 2019, Oracle discontinued its free, long-term support
of the **Oracle Java Development Kit** (JDK) for enterprises. All
Oracle JDK releases now require a Support Agreement with Oracle. Going
forward, there are two new types of support available:

* The Long Term Support (LTS) release includes support and security
  updates for *several years*. The current LTS releases are Oracle
  JDK 8 and Oracle JDK 11.
* The Non-LTS release includes support and security updates for
  *six months*. Each Non-LTS release will be superseded by the next
  one, i.e. there will be no further support or security updates provided
  for previous releases. For example, the latest non-LTS release was
  Oracle JDK 12, released in March 2019, and it will be superseded by the
  next non-LTS release, in September 2019.

Organizations may choose instead to *not* use the Oracle JDK and to
use the free **OpenJDK** (also maintained by Oracle) instead. OpenJDK
details include:

* OpenJDK release frequency matches the Oracle JDK non-LTS release
  frequency, every six months, with each superseding the previous release.
* OpenJDK release numbers correspond to Oracle JDK release numbers, e.g.
  OpenJDK 11 corresponds to Oracle JDK 11.
* OpenJDK and Oracle JDK releases will include similar functionality, with
  Oracle JDK expected to have some additional proprietary features that
  won't impact Logi products.
* While there is no cost for using OpenJDK, it's released under a
  [GPL 2 license](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html), with ClassPath Exception, which may matter to some Logi customers.
