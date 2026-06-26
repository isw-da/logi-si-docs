---
title: "Working with Source Control"
id: 4419723256855
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723256855-Working-with-Source-Control
updated_at: 2022-08-17T15:01:05Z
---

# Working with Source Control

# Working with Source Control

The choice of a source control system is highly dependent on the complexity of the source control functionality required. For smaller, simple applications, the use of the Team Development functionality within Logi Studio is often enough. Logi Team Development allows you to maintain version control, based on file saves, and provides file-locking/sharing capabilities for multiple developers.

If you require more sophisticated source control, then a third-party product will be necessary. Popular products include Git, Microsoft TFS, and Subversion. The files that make up a Logi Info application are used directly from the file system; they're not stored in, or controlled by, a database or other constraining mechanisms, so third-party source control products can be used directly on them without concern.

To benefit from a third-party product, however, you should keep your Logi application's source code folders (\_Definitions, \_SupportFiles, \_Templates, \_Scripts, \_Plugins), and all the root folder .aspx files under source control. Keeping the bin,
rdTemplate, and other "rd\*" system folders *outside* of source control will allow you to easily move between different versions of the Logi engine without interfering with your source control functionality.

### Basic Git Extensions Support

[Git Extensions](https://sourceforge.net/projects/gitextensions/) is a standalone UI tool for managing Git repositories. Logi Studio is now able to integrate Git Extensions, providing quick access to basic Git features when it's being used as the application's code repository.

Logi Studio's Git Extensions integration is enabled when a Git Extensions installation is detected and when an application ancestor folder contains a .git file (indicating that the application files are actually being managed in Git).

![](https://devnet.logianalytics.com/hc/article_attachments/4419714949655/usingstudio_80.png)

Once enabled, Git features can be accessed using the icon on Studio's Tools ribbon menu, shown above,

![](https://devnet.logianalytics.com/hc/article_attachments/4419707145239/usingstudio_81.png)

or by right-clicking any file in the Application Panel, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707145495/usingstudio_82.png)

In either case, the Git Extensions UI shown above will appear so that you can manage your repositories and files.
