---
title: "Configuring a Friendly Error Page in a Java Logi App"
id: 360048271494
section: "Tactics"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360048271494-Configuring-a-Friendly-Error-Page-in-a-Java-Logi-App
updated_at: 2020-07-28T20:01:08Z
---

# Configuring a Friendly Error Page in a Java Logi App

### Foreword

By default, Logi applications will present a Debug Page in the event of an error.  While this information is helpful in development and testing, production-ready Logi applications should send users to a friendly error page for best user experience.

The following guide walks through the implementation of a friendly error page for a java Logi application. While simple in application, it can be extended and expanded upon to meet a developer's needs.

The solution requires the following:

1. Access to a Logi Info application

2. A simple JSP or aspx page to show the friendly error message, saved in the application's root directory

### Implementation

**Step 1:** Add a Java Session Copying element to your \_Settings.lgx file.

Documentation: <https://documentation.logianalytics.com/logiinfov12/content/work-with-session-variables.htm>

Example (copy this directly into your \_Settings.lgx file):

```
<JavaSessionCopying CopyToJavaInclude="^" CopyToJavaExclude="DebugFile,-bUsesSort$,-tra$,-xmlDef$,-Xsl$,-rdDef$" CopyFromJavaInclude="^" CopyFromJavaExclude="^rd,^dt" />
```

**Step 2:** Set DebuggerStyle in the General element of your \_Settings.lgx file to "Redirect"

Read more about the options for DebuggerStyle here: <https://documentation.logianalytics.com/logiinfov12/content/settings-definition-12.7.htm?Highlight=debugger%20style#General>

**Step 3:** Specify a location to Redirect in the event of an error.  This should be a custom error page.  An example error page jsp is displayed below.

![mceclip1.png](https://devnet.logianalytics.com/hc/article_attachments/360072403193/mceclip1.png)

**Error.jsp page Body Example:**

```
<%@ page import="java.sql.*, java.util.*" %>  
  
<!DOCTYPE html>  
  
<html lang="en">  
  
  <head>  
  
                <meta charset="utf-8">  
  
                <meta http-equiv="X-UA-Compatible" content="IE=edge">  
  
  </head>  
  
   
  
                <body style="padding-top: 50px; padding-bottom: 0px;">  
  
                <div >  
  
<%  
  
                                String ErrorMessage = (String)session.getAttribute("rdLastErrorMessage");  
  
                                out.print("err=" + ErrorMessage);  
  
                                System.out.println("err=" + ErrorMessage);  
  
%>  
  
    </div>  
  
  </body>  
  
</html>
```

**Note:**The JSP provided displays the top level error message using the session variable rdLastErrorMessage and then pipes the value to the console using System.out.println(). This will pipe errors to console, but it's possible to extend the logic to write to a file or database as well.

if you’d like more robust logging features in addition to error logs (for instance when a query is run, or if there’s specific report being built) you may consider using Logi’s Event logger.

[https://documentation.logianalytics.com/logiinfov12/content/event-logging.htm](https://documentation.logianalytics.com/logiinfov12/content/event-logging.htm?Highlight=2198)
