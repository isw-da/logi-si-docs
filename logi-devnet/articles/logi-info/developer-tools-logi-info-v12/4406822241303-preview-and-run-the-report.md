---
title: "Preview and Run the Report"
id: 4406822241303
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822241303-Preview-and-Run-the-Report
updated_at: 2022-04-06T06:05:04Z
---

# Preview and Run the Report

# Preview and Run the Report

This topic demonstrates how to preview and run the report in Logi Info.

You can preview the report right inside Studio:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575778327/datatableman_17.png)

In the Workspace panel, click the **Preview** tab at the bottom. Your report should appear in the panel. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Any changes to definitions (but not to support files, such as style sheets) are *automatically saved* when **Preview** is clicked. Click the column headers to see the sorting feature in action.
Let's clean up a few things before we move on. Let's rearrange the column order and set the column header titles.

  
![](https://devnet.logianalytics.com/hc/article_attachments/4417584034711/datatableman_18.png)  

1. Click the **Definition** tab to return to the definition editor.
2. In the MyDataTable2 definition, select the Data Table Column for the City data ("colCity").
3. Use the **Move Down** item in the main menu, or the **F8** key, to move the selected element down below the other data table column elements. Notice that its child elements (Label and Sort) move with it.
4. Repeat this process with the First Name ("colFirstName") data table column element so we wind up with a column order of EmployeeID, LastName, FirstName, and City. Preview the results to check the order.
5. Next, select each Data Table Column element in turn, and insert a space into its **Column Header** attribute value, separating the two words found there, so "FirstName" becomes "First Name", for example. Then preview the results again.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575778711/datatableman_19.png)

You can also view the results in your browser by right-clicking the **MyDataTable2** definition in the Application Panel and selecting *Run in Browser* from its context menu.
