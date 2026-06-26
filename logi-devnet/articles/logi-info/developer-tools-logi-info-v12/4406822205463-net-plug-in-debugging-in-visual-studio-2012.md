---
title: ".NET Plug-in - Debugging in Visual Studio 2012"
id: 4406822205463
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822205463--NET-Plug-in-Debugging-in-Visual-Studio-2012
updated_at: 2022-04-06T06:04:40Z
---

# .NET Plug-in - Debugging in Visual Studio 2012

# .NET Plug-in - Debugging in Visual Studio 2012

You can debug your plug-in as it runs in your Logi application, using Visual Studio (VS). The examples in this topic show you how it's donein VS 2012. Ensure that you're running VS with a user account that has Administrator privileges.

![](https://devnet.logianalytics.com/hc/article_attachments/5263107671191/createpluginnet_01.png)

Open your plug-in solution in VS and, in the Solution Explorer, select and right-click the root node, then select **Add**![](https://devnet.logianalytics.com/hc/article_attachments/5263060093719/menuarrowrt.png)**Existing Web Site...** Click the **Local IIS** category and select your Logi application web site's virtual directory from the list, adding it to your solution.

![](https://devnet.logianalytics.com/hc/article_attachments/5263090132247/createpluginnet_02.png)

Right-click the Logi application web site in the Solution Explorer and select its **Property Pages** from the pop-up menu, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/5263090135319/createpluginnet_03.png)

In the Property Pages window, shown above, select the **Build** page in the left menu, and then:

1. Select **No Build** in the list of Start actions.
2. Ensure that the appropriate .NET Framework version for your Logi application is selected.

![](https://devnet.logianalytics.com/hc/article_attachments/5263090141463/createpluginnet_04.png)

Next, select the **Start Options** page in the left menu, as shown above, and then:

1. Select the **Start URL** radio button, and enter your Logi application's URL.
2. Ensure that the **Use default Web server** option is selected.
3. Ensure that the **ASP.NET** debugger option is checked. Click **OK** to save all your settings

![](https://devnet.logianalytics.com/hc/article_attachments/5263060129175/createpluginnet_05.png)

Finally, in the Solution Explorer, right-click your Logi application web site, and select the **Set as Startup Project** option.

You're now ready to press **F5** (or use the Debug menu) to run your solution and start debugging. The details of setting Watches, Breakpoints and other debugging-related activities are beyond the scope of this topic; refer to your Visual Studio documentation.

If you start debugging and receive the error "...Debugging failed because integrated Windows authentication is not enabled", read this [MSDN article](https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2012/x8a5axew(v=vs.110)?redirectedfrom=MSDN) for information about configuring the authentication for your Logi app virtual directory.

These settings are for a simple debugging example. Depending on the implementation of your Logi application, such as use of a remote web server, you may need to adjust some of the settings shown above.
