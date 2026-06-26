---
title: "Analysis Grid Developers - Saving and Loading Analysis Grids"
id: 4406816984855
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816984855-Analysis-Grid-Developers-Saving-and-Loading-Analysis-Grids
updated_at: 2023-05-30T09:35:56Z
---

# Analysis Grid Developers - Saving and Loading Analysis Grids

# Analysis Grid Developers - Saving and Loading Analysis Grids

It may be important for users to be able to **save** their Analysis Grid configurations between sessions. Their configurations can be saved on the web server and made available to them during their next session. Developers can implement this behavior with a simple **Process** definition. The following examples illustrate how to save and manipulate grid settings.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584192279/workag_25.png)

The original Analysis Grid example definition is shown above with a set of **Label** and **Action** elements added, beneath their own Division. The **actSave** element attributes point to a Process definition task, **tskSaveAg**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584192919/workag_26.png)

To create the task:

1. In a Process definition, add a **Task** element ("tskSaveAg").
2. Below it, add a **Procedure.Set Session Vars** element ("getAgID").
3. Below that, add a **Session Parameters** element and set its attributes as shown above. The GUID token provides a random 48-character number for use as a unique identifier. Remember: the session parameter name is **case-sensitive**!

![](https://devnet.logianalytics.com/hc/article_attachments/4417591976983/workag_27.png)

4. Next, add to the task a **Procedure.Create Folder** element and set its attributes as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584193943/workag_28.png)

5. Add a **Procedure.Save Analysis Grid** element to the task and set its attributes as shown above. The full **Filename** value is:  
     
   @Function.AppPhysicalPath~\UserData\@Session.AgID~.xml  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The session variable created from the GUID token earlier is now being used as the file name; use of a session variable allowed us to "pass" the value through the task from an earlier procedure to this one.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584194199/workag_29.png)

6. Add a **Procedure.Set Cookie Vars** element to the task. Below it, add a **Cookie Parameters** element and set its attributes as shown above. This stores the name of the Analysis Grid settings file on the user's computer; the cookie will be used in future sessions to open the find and restore the settings.
7. Add a **Response.Report** and **Target.Report** element to the task to return processing to the report definition containing the Analysis Grid.

Cookies are useful when the user is unknown to the server and session information is unimportant. If authentication is integral to an application, developers can use strategies such as tying a saved Analysis Grid filename to a user ID and storing this information in a database. Developers
can also create a list of saved Analysis Grids that users can access from any workstation.
