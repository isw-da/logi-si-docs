---
title: "See Full Error Details"
id: 5281647422487
section: "Troubleshooting"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281647422487-See-Full-Error-Details
updated_at: 2022-05-03T22:08:46Z
---

# See Full Error Details

# See Full Error Details

When an error occurs in Exago, a generic error message may be displayed. This generic message is meant to prevent end users from seeing the full stack trace of the error.

![pVvQHsBzgy.png](https://devnet.logianalytics.com/hc/article_attachments/5432173349271/pvvqhsbzgy.png)

Sample error message that could occur when executing a report with errors on it

There are two ways to see detailed error messages.

1. If you are accessing Exago directly in a browser:
   1. Append **?showerrordetail=true** to the URL.  
      Example: `/Exagohome.aspx?showerrordetail=true`
   2. Refresh the page and recreate the error.
2. If you are accessing Exago through one of the APIs:
   * With the .NET API call the method **GetUrlParamString** and set **showErrorDetail** to *True*.
   * With the REST Web Service API, set the **showErrorDetail** property of the **Session** object to *True* before starting the session.
3. Enter Exago through the API and recreate the error.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The status code on the generic error message corresponds to standard HTTP status codes. For example if the status code is 408 it means there was a request timeout. For status code 200 the request completed successfully and the error lies elsewhere.
