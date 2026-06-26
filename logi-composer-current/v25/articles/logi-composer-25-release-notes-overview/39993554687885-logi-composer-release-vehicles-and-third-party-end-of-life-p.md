---
title: "Logi Composer Release Vehicles and Third Party End of Life Policy"
id: 39993554687885
section: "Logi Composer  25 Release Notes Overview"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39993554687885-Logi-Composer-Release-Vehicles-and-Third-Party-End-of-Life-Policy
updated_at: 2026-05-26T22:06:01Z
---

# Logi Composer Release Vehicles and Third Party End of Life Policy

# Logi Composer Release Vehicles and Third Party End of Life Policy

## Important Notices

Composer is offered on a quarterly release schedule, and our version numbering system reflects this. The current major release of Composer is v25.4.

For information about Composer's end-of-life policy for third-party software, see [Third Party End of Life Policy](#Third).

**Important:**  Older license keys are not compatible with Composer. If you are upgrading from any older Composer or Zoomdata release, a new license must be requested. See [Request and Apply a New License Key](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933040878349-Request-and-Apply-a-New-License-Key).

## Current Releases

Each quarterly release is supported using service packs to address any issues until the next quarterly release is available. Subsequent fixes for a non-current quarterly release are limited to the most severe issues for the next three quarters. Upgrade to the most current quarterly release for the most up to date support and features.

| Release | Support Cycle |
| --- | --- |
| Q1 Release | * Service packs for all issues throughout Q2 * Service packs for severe issues only throughout Q3 and Q4 * End of life for Q1 release at next Q1 release |
| Q2 Release | * Service packs for all issues throughout Q3 * Service packs for severe issues only throughout Q4 and Q1 * End of life for Q2 release at next Q2 release |
| Q3 Release | * Service packs for all issues throughout Q4 * Service packs for severe issues only throughout Q1 and Q2 * End of life for Q3 release at next Q3 release |
| Q4 Release | * Service packs for all issues throughout Q1 * Service packs for severe issues only throughout Q2 and Q3 * End of life for Q4 release at next Q4 release |

See [Request and Apply a New License Key](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933040878349-Request-and-Apply-a-New-License-Key) to obtain a license appropriate for your release of choice from our support team. For information about retired releases, see [Retired Releases](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933122979213-Retired-Releases).

#### Upgrade and Migration Considerations

* Windows Server 2012R2 is not compatible with both Java17 binaries and the latest releases of Composer (23.2 and later). We recommend you use Windows 2016 or later to run Composer 23.2 and later.
* In general, you can upgrade directly to the latest version of Composer from a prior version.
* If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Change the Encryption Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933139088269-Change-the-Encryption-Mode).

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

**Important:** If you are upgrading to a newer version of Composer and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932887294349-Timezone-Conversion-for-Users#Upgrade) for more information about preparing your environment for the upgrade process.

## Previous Releases / Retired Releases

If you are using an earlier version of Logi Composer , you should contact Sales and upgrade to the most current release. We no longer publish documentation for any Logi Composer products prior to version v24. Contact [Customer Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) if you need content for an unsupported release.

## Third Party End of Life Policy

As third-party software (such as operating system, database engine, and cluster environment software) ages, it becomes increasingly difficult for insightsoftware to provide the support and level of functionality that our customers expect. To ease this difficulty, insightsoftware has established the following end-of-life (EOL) policy for third-party software. An EOL policy describes when Composer will cease to provide support for a version of third-party software.

Third-party software vendors set the EOL for its software versions. This is the period of time during which the vendor provides patches, fixes, and other updates for a given software version.

When a vendor no longer provides updates and patches or declares an EOL for their software,insightsoftware will remove support for that third-party software version.

When a third-party software version reaches EOL, it continues to function normally. Existing Composer installations using that third-party software version will also continue to function normally. However, you will be unable to perform:

* **Fresh installations of Composer** — Composer prevents new installations after the third-party software reaches EOL.
* **Upgrades to new versions of Composer** — Composer prevents upgrades after the third-party software reaches EOL.
* **Third-party-specific fixes** — Composer does not provide fixes, security or otherwise, after the third-party software reaches EOL.

**Caution:** If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Composer and operating system to a later version. For more information, see [Operating System Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39993525943181-Operating-System-Support).
