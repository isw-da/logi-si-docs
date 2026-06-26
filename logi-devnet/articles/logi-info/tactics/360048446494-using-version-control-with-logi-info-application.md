---
title: "Using Version Control with Logi Info Application"
id: 360048446494
section: "Tactics"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360048446494-Using-Version-Control-with-Logi-Info-Application
updated_at: 2021-03-31T19:26:11Z
---

# Using Version Control with Logi Info Application

**When to use version control?**

The choice of a version control system is dependent on the complexity of the application requirements.

* For smaller and simpler applications, the use of version control system may not be necessary.
* For more sophisticated requirements, version control may be necessary, particularly for collaboration on a project

***Note****: Logi customers use a variety of version control systems, but this article discusses using Logi Info with Git*

**Logi Features for version control:**

Logi Studio v12+ includes features designed to make Logi definition source code easier to use with third party source code repository and control products such as Git.

**Git Extensions**is a plug-in that provides quick and easy access to Git, when it's being used as the application's source control repository. It is enabled when a Git Extensions installation is detected and when an application ancestor folder contains a .git file.

![image.PNG](https://devnet.logianalytics.com/hc/article_attachments/360072926133/image.PNG)

Git Extensions UI as shown below can be used to manage repositories and files

![image2.PNG](https://devnet.logianalytics.com/hc/article_attachments/360072926173/image2.PNG)

**What Logi Files are Subject to Change?**

A Logi application is made up of two major components

1. Developer generated content - these are xml configurations that a developer creates in Logi Info studio. These files are stored in the folders that begin with "\_".
2. The Logi engine.  For further breakdown of Logi engine's components, read more here: <https://documentation.logianalytics.com/inf/content/logi-info-app-overview/standard-logi-app-folders.htm>

Whereas the *"Logi Engine"* remains static other than on upgrades, *Developer generated content* updates as frequently as a report developer needs to introduce more features.![mceclip3.png](https://devnet.logianalytics.com/hc/article_attachments/360082606893/mceclip3.png)

Thus, a key decision when using source control with Logi Info is **whether or not to include** the Logi Info "engine files" in a Git repository.

Each method has pros and cons and should be evaluated for each situation on a case by case basis. The ultimate decision to either include or not include “engine files” depends on the requirements of that specific deployment.

|  |  |
| --- | --- |
| **Scenario 1: Include Engine Files** | **Scenario 2: Exclude Engine Files** |
| **Pros:** **Tightly controlled deployment and simplicity**  This scenario offers a more “tightly controlled deployment”, as a Logi Info engine upgrade would simply be another commit of changed files.  In order to deploy an app in this scenario, use Git’s “clone” feature to copy all files from the remote repository server to the desired web application folder.  Then the only additional step here will be to apply a license file.  **Cons:** **Large file size impacting deploy performance**  As Git includes a history of all files for each commit, every engine version will subsequently be added to the hidden “.git” folder, and may eventually reach into gigabyte range for each app (each engine file set is roughly 200MB). | **Pros:** **Allows independent Logi version manipulation and avoids tracking cached files**  If the requirements of the deployment allows that the engine files *not* be included, then it will take a few more steps for each deployment. However, this approach allows independent Logi version manipulation and avoids tracking cached files.  In this scenario, a “.gitignore” file is used to specify folders and files that should not be included.  **Cons:** **The engine files must be built and applied for each deployment**  In order to deploy an application in this scenario, the engine files must be applied on each new deployment. Deployment will require handling of logi's engine files and license file. |

**Recommended Scenario**

Scenario 2 [“Excluding engine files”] is the most adopted method. With a large number of constantly changing applications deployed to several locations (including servers and personal workstations), it's more flexible to allow each deployment to run on independent Logi engine versions with its own cache, while versioning only the definition/settings/support files that constitute the application.
