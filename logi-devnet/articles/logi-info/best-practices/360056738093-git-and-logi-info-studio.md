---
title: "Git and Logi Info Studio"
id: 360056738093
section: "Best Practices"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360056738093-Git-and-Logi-Info-Studio
updated_at: 2021-03-31T19:15:31Z
---

# Git and Logi Info Studio

Here is a step by step guide to ensuring your application built in Logi Info Studio can be used with Git as documented [here](https://documentation.logianalytics.com/logiinfov12/content/using-logi-studio-12.7-1.htm?Highlight=git#SourceControl).

Preparing an application for Git is as easy as:

1. Go to Tools > Options then select the option "Source Code Repository Friendly, for GIT and others.

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360094999833/mceclip0.png)

2. When asked if you want to convert your files to the new repository friendly format, select Yes.

Setting up Git Extensions

1. Download [Git](https://git-scm.com/downloads) for your appropriate system.

2. Install Git.

3. Download [Git Extensions](https://sourceforge.net/projects/gitextensions/).

4. Install Git Extensions.

5. Open Git Extensions

When you first open Git Extensions, you may need to configure the application further with your repository user name and other various options.

6. Select Create new repository.

8. Browse to the root folder of your application.

9. Click Create > OK.

10. Right-click Remotes and select Manage.

11. Enter the Name of your application and the URL in which to push/pull the files to.

Every instance has its way of creating a new repository. For these steps, we will assume that an empty repository has already been created.

12. Click Save Changes >Yes and close the dialog box once the connection has been established.

13. Click Commit

14. If this is your first time committing files, select all to Stage.

15. Add a comment and click Commit & push > OK > Yes > Yes

Depending on the size of your application and connection speed, this may take some time to fully commit. We suggest only committing files from the following folders:

\_Definitions

\_SupportFiles

\_Themes

\*Any other folders needed to run your application

\*\*Any modified files from the rdTemplate folder, however, as always we suggest that you keep a backup of these in the case that the application engine is upgraded.

\*\*\*All other loose files from the parent directory.

**Note: The following files and directories are automatically ignored in the gitignore file:**

**\*.lic  
\*.lgp  
TeamDevelopment/  
\_rdLivePreview\*.lgx  
rdDataCache/  
rdDownload/  
rdErrorLog/**

You can now click on the Git Extensions icon in the Tools tab of Logi Info Studio and it will open Git Extensions. From there you can commit any changes that you have made or use Git as you normally would.

Right-clicking on any file within your application will give you the following options:

-Git Repository History

--Allows you to see the history of the file.

-Git Repository Blame

--Allows you to assign blame to a portion of the file.

-Git Repository Differences

--Allows you to see the differences between the current file and the last file in the repository.
