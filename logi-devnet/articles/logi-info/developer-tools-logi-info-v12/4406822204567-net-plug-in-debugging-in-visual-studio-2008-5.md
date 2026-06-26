---
title: ".NET Plug-in - Debugging in Visual Studio 2008/5"
id: 4406822204567
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822204567--NET-Plug-in-Debugging-in-Visual-Studio-2008-5
updated_at: 2022-04-06T06:04:41Z
---

# .NET Plug-in - Debugging in Visual Studio 2008/5

# .NET Plug-in - Debugging in Visual Studio 2008/5

You can debug your plug-in as it runs in your Logi app, using Visual Studio (VS). The technique is the same regardless of VS version, with minor differences as noted below. Ensure that you're running VS with a user account that has Administrator privileges.

![](https://devnet.logianalytics.com/hc/article_attachments/5263060137495/createpluginnet_06.png)

Open your plug-in solution in VS and, in the Solution Explorer, select and right-click the root node, then select **Add**![](https://devnet.logianalytics.com/hc/article_attachments/5263060146199/menuarrow.gif)**Existing Web Site...** Browse to and select your Logi application web site (its virtual directory), adding it to your solution.

![](https://devnet.logianalytics.com/hc/article_attachments/5263098110103/createpluginnet_07.png)

Right-click the Logi application site in the Solution Explorer and select its **Property Pages** from the pop-up menu, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/5263098132247/createpluginnet_08.png)

In the Property Pages window, shown above, select the **Build** page in the left menu, and then:

1. Select **No Build** in the list of Start actions.
2. Ensure that the appropriate .NET Framework version for your Logi application is selected.

![](https://devnet.logianalytics.com/hc/article_attachments/5263098138263/createpluginnet_09.png)

Next, select the **Start Options** page in the left menu, as shown above, and then:

1. Select the **Start URL** radio button, and enter your Logi application's URL.
2. To run your Logi app using the local IIS server:   
   VS 2008: Select the **Use default Web server** radio button.  
   VS 2005: Select the **Use custom server** radio button and enter the **Base URL**, as shown above.
3. Check the **ASP.NET** debugger check box; click **OK** to save all your settings

  

![](https://devnet.logianalytics.com/hc/article_attachments/5263098144919/createpluginnet_10.png)

Finally, in the Solution Explorer, right-click your Logi application web site, and select the **Set as Startup Project** option.

You're now ready to press **F5** (or use the Debug menu) to run your solution and start debugging. The details of setting Watches, Breakpoints and other debugging-related activities are beyond the scope of this topic; refer to your Visual Studio documentation.

If you start debugging and receive the error "...Debugging failed because integrated Windows authentication is not enabled", read this [MSDN article](https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2012/x8a5axew(v=vs.110)?redirectedfrom=MSDN) for information about configuring the authentication for your Logi app virtual directory.

These settings are for a simple debugging example. Depending on the implementation of your Logi application, such as use of a remote web server, you may need to adjust some of the settings shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/5263096722455/criticalicon.png) If you haven't done so already, you should read [Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/4406817734295-Logi-Plug-ins) for important supporting information before proceeding.
If you're developing a **Java** plug-in, see [Create a Java Plug-in](https://devnet.logianalytics.com/hc/en-us/articles/4406822210071-Create-a-Java-Plug-in) instead of this one.
