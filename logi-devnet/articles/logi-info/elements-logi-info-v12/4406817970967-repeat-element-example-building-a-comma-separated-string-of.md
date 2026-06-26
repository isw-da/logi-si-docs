---
title: "Repeat Element Example: Building a Comma-Separated String of Values"
id: 4406817970967
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817970967-Repeat-Element-Example-Building-a-Comma-Separated-String-of-Values
updated_at: 2022-04-06T06:09:23Z
---

# Repeat Element Example: Building a Comma-Separated String of Values

# Repeat Element Example: Building a Comma-Separated String of Values

Have you ever needed to build a comma-separated string of values from data? With the Repeat Elements element, it's easy!

![](https://devnet.logianalytics.com/hc/article_attachments/4417583689495/repeatele_02.png)

In the definition fragment shown above, a Repeat Elements element is used to iterate through the data and an **Input Hidden** element is used as the repository of the comma-separated string of values.

The traditional difficulty when building comma-separated strings is avoiding having a trailing comma after the last item in the list. To do this, we need to know when we're processing the last data row. This is where the **Rank Column** element ("colRank") comes into play. It ranks the datalayer rows, based on the Category ID in this example, in *reverse* (set its **Reverse Rank** attribute to *True*), which means the *last* data row will have a rank of *1*.

With that ranking information in hand, we can use two **Division** elements, with their **Condition** attributes set to test the ranking, to control the JavaScript that builds the comma-separated string. Here's the Condition attribute for the divNotLastItem element above:

@Repeat.colRank~ <> 1

and the other division's Condition tests to see if the rank does equal 1. The two JavaScript scripts used to create the string either include a trailing comma, or not. Here's the script *with* the comma:

var myHidden = document.getElementById('inpHidden');  
myHidden.value += '@Repeat.CategoryName~,';

and the other script is exactly the same but omits that highlighted comma.

After the page is submitted, the completed comma-separated string of values will be available to the next definition as @Request.inpHidden~.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Ranking may not work as a test for the last datalayer row for all scenarios, but there are other ways to do it, including using a Sequence Column and a Aggregate Column (set to COUNT the rows) and comparing the two.
