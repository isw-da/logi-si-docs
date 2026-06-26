---
title: "Data Entry in Pop-up Panels"
id: 4406817780759
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817780759-Data-Entry-in-Pop-up-Panels
updated_at: 2022-04-06T06:08:10Z
---

# Data Entry in Pop-up Panels

# Data Entry in Pop-up Panels

One common use of pop-up panels is to provide a data entry form for data
tables, like this:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575573143/poppanel_16.png)

Typically, you'd use a Process task to update the data when the Save
button is clicked. You'd expect that the user input values would be passed
to the task as Request variables, as usual.

However, it's important to realize that the @Request token IDs will
automatically have a row designator ("\_Row1") appended to them,
because the Input controls are within a data table row. This presents a
complication: how will the task "know" which row these values
refer to and therefore which tokens to use? For example,

@Request.inpPropertyNo\_Row**1**~, or
@Request.inpPropertyNo\_Row**2**~, or ?

The recommended technique for handling this is to use
**Input Hidden** elements, one for each user input element in the
pop-up panel, placed *outside* the data table. When the Save button
is clicked, an *onMouseDown* Event Handler is used with
Action.JavaScript to call code that assigns the values from the pop-up
panel's Input elements to the Input Hidden elements. An additional
Action.Process element under the Save button then calls the Process task,
which uses the @Request tokens for the Input Hidden elements to update the
data.

You can see this in action and view sample definitions in the
[Samples page](https://devnet.logianalytics.com/hc/en-us/articles/360050374433-Update-Table-Sample-Application)
on DevNet.
