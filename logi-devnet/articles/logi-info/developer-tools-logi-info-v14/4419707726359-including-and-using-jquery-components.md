---
title: "Including and Using jQuery Components"
id: 4419707726359
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707726359-Including-and-Using-jQuery-Components
updated_at: 2022-07-17T02:23:58Z
---

# Including and Using jQuery Components

# Including and Using jQuery Components

Here are two examples that illustrate how to include the jQuery libraries and jQuery code. The first one displays the "date picker" UI component.

First, we configure our report definition's **Style** element to use a jQuery style sheet hosted online by Google:

http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css  

The jQuery versions used here are representative and other versions will work as well.

![](https://devnet.logianalytics.com/hc/article_attachments/7522797219607/jquery_02.png)

Then we add two **Include Script File** elements to our definition, as shown above, and configure their attributes to include the jQuery libraries hosted online:

http://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js  
http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js  

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The Google API hosting page suggests using these URLs with the "https:" protocol. However, if your Logi application is not specifically configured for SSL, then using "https:" URLs to include these libraries will *not* work. Use "http:" instead, as shown.

You could, of course, use local copies of the jQuery style sheet libraries, downloaded into \_SupportFiles, by just selecting their filenames instead.

![](https://devnet.logianalytics.com/hc/article_attachments/7522797231639/jquery_03.png)

Next we add an **Include Script** element and enter our jQuery code in its **Included Script** attribute, as shown above. The full code is:

$(document).ready(function() {  
$("#divDatePicker").datepicker();  
});

And finally, we need to add a container (a **Division** element) for the date picker,

![](https://devnet.logianalytics.com/hc/article_attachments/7522797241111/jquery_04.png)

as shown above. The **Output HTML Div Tag** attribute must be set to *True* and notice that the **ID** of the division is used in the jQuery code, which is case-sensitive.

![](https://devnet.logianalytics.com/hc/article_attachments/7522839011351/jquery_05.png)

When you run the report, you should see a fully-operational date picker calendar similar to the one shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The date picker highlights the current date (default), as well as the selected date.

## The jQuery News Ticker

The next example demonstrates a little more integration with standard Logi elements. It uses a datalayer as the source for "news headlines", one of which is displayed for a fixed interval before being replaced by the next headline, a classic "news ticker".
Begin by adding the following two style classes to a local style sheet:

#ticker {   
 height: 20px;  
 width: 500px;   
 overflow: hidden;  
 border: 2px Green Solid;  
 padding: 5px;  
}   
  
#ticker li {   
 height: 30px;   
 font-family: Verdana, Arial, sans-serif;  
 font-size: 12pt;  
 color: orange;  
}

Then assign that style sheet to your report definition, using a **Style** element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522811859223/jquery_06.png)

Use the same two jQuery libraries from the previous example. Add an **Include Script** element, as shown above and use the following jQuery code for its **Included Script** attribute value:

function tick(){   
 $('#ticker li:first').animate({'opacity':0}, 200, function () { $(this).appendTo($('#ticker')).css('opacity', 1); });   
}   
setInterval(function(){ tick () }, 4000)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) There is only one long line of code in the function tick( ) but it may have wrapped to look like two lines in your browser.

![](https://devnet.logianalytics.com/hc/article_attachments/7522811877015/jquery_07.png)

Now, add a **Data List** element in the report Body, as shown above. Its ID, "ticker", matches identifiers in the jQuery code and CSS, so you need to enter it exactly as shown.

![](https://devnet.logianalytics.com/hc/article_attachments/7522811885975/jquery_08.png)

Next, add a **DataLayer.Static** element and four **Static Data Row** elements. This, of course, could be any type of datalayer. Set the four data row elements to each have a single column called "ItemName" and enter one of the four headlines for each element, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522793237015/jquery_09.png)

Finally, add a **List Item** element and, beneath it, a **Label** element. Set the Label element's **Caption** attribute as shown above.

So - what you've created is a datalayer-driven, HTML un-ordered list and the jQuery code will display one line of the list at a time.

![](https://devnet.logianalytics.com/hc/article_attachments/7522822491415/jquery_10.png)

Run the application and you should see something like the example above, with each headline rotating through it.

Now you can begin to see how the jQuery code can interact with other HTML components created by Logi elements, with CSS, and with data from a datalayer. The next sections look at data manipulation in more detail.
