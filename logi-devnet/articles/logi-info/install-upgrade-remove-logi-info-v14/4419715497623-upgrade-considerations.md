---
title: "Upgrade Considerations"
id: 4419715497623
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715497623-Upgrade-Considerations
updated_at: 2022-07-17T01:36:33Z
---

# Upgrade Considerations

# Upgrade Considerations

SSRM upgrades are usually associated with a Logi Info upgrade and
*we highly recommend that you upgrade both of them**together*.
Upgrading just one or the other will usually result in undesirable
effects. See [Release Pairings](https://devnet.logianalytics.com/hc/en-us/articles/4419715356567-Release-Pairings) for more
information.

If you're upgrading to an early version (pre-v12.5), see
[Upgrading to Earlier Versions](https://devnet.logianalytics.com/hc/en-us/articles/4419715498519-Upgrading-to-Earlier-Versions) for important
details.

## Upgrading to v12.5+

If you're upgrading to the **SSRM v12.5+**, be aware of these important
considerations related to the included InfoGo application:

* Upgrading the SSRM will *overwrite* any edited InfoGo files,
  *except* those in the
  goCustomizations
  virtual folders under InfoGo![](https://devnet.logianalytics.com/hc/article_attachments/5163481069207/menuarrowrt.png)Definitions![](https://devnet.logianalytics.com/hc/article_attachments/5163481069207/menuarrowrt.png)Reports and InfoGo![](https://devnet.logianalytics.com/hc/article_attachments/5163481069207/menuarrowrt.png)\_SupportFiles. The file
  goCustomizations.goWebFooter.lgx
  will not be overwritten, for example.
* The application's
  \_Settings.lgx
  definition will not be overwritten; however, the new version may require
  new elements and/or attributes not found in older versions. You'll have
  to add these manually in the source code if they're missing. See [Configure InfoGo for Developers](https://devnet.logianalytics.com/hc/en-us/articles/4419722760343-Configure-InfoGo-for-Developers) for details.
* If you've used your own Definition or Template Modifier Files,
  identifiers used with them may change from one SSRM version to the next
  and you may need to adjust your modifier files accordingly.

Making backup copies of any InfoGo files you've edited, prior to applying
an upgrade, is always highly recommended.

## Upgrading to v12.7

InfoGo v12.7 provides enhanced content management. Visualizations are
stored as Bookmarks, which lets them be presented and manipulated in a way
consistent with other objects. This makes it easy to edit them, rename
them, and duplicate them, and eliminates the need for Gallery and Extra
Gallery files.

SSRM 12.7 provides an upgrade tool, the
**Gallery to Bookmarks Migration Utility**, for migrating
visualizations from gallery files to Bookmarks. When you launch InfoGo for
the first time after upgrading to it, you'll see a prompt to run the
tool:

![](https://devnet.logianalytics.com/hc/article_attachments/5163509132055/upgrssrm_08.png)

You can also run the utility independently by browsing:
/rdPage.aspx?rdReport=rdTemplate/rdGalleryMigration

You must have the "rdBookmarksAdmin" security right to be able to run the utility. Click the link to run it:

![](https://devnet.logianalytics.com/hc/article_attachments/5163504500887/upgrssrm_09.png)

The Migration Utility page is shown above and is fairly self-explanatory,
but here are a few key points:

* Make file or database backups *before* you run the utility!
* Gallery files that have been processed are retained in place, with
  .migrated added to their file names, and can be deleted after ensuring
  everything migrated properly.
* An asterisk (\*) wildcard is used in the input fields to represent the
  username parts of folder and file names.
* The migrated visualizations will appear in a new folder on the InfoGo
  Home page, called "My Visualizations".
* You have the option to output the migrated visualizations into a
  sub-folder of "My Visualizations".

After the migration completes, you'll see the results table appear at the
bottom of the page:

![](https://devnet.logianalytics.com/hc/article_attachments/5163509155991/upgrssrm_10.png)

As shown in the example above, the results will indicate whether or not
the visualizations were successfully migrated.

![](https://devnet.logianalytics.com/hc/article_attachments/5163479892119/criticalicon.png)
If your developers have customized gallery files to work with special
Dashboards, they will most likely need to rework the application to
accommodate this change.

After the migration, you may need to perform the following configuration tasks in your InfoGo application:

For Gallery files that have been processed and are retained in place, with .migrated and timestamp added to their file names, those files should be deleted after you are sure everything migrated properly.
