---
title: "White Labeling URLs"
id: 12528223421975
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528223421975-White-Labeling-URLs
updated_at: 2023-02-23T15:16:26Z
---

# White Labeling URLs

# White Labeling URLs

By default, the MVC Kit labels URLs with an Izenda namespace for you to modify.

When you navigate to your Report List for instance, your URL will look similar to the following:

> `http://localhost:14809/Home/Reports#?source=%2Fizenda%2Freport`

To modify this namespace, update the files below:

> In this example, we change ‘izenda’ to ‘reporting’.

* **Scripts\izenda.integrate.js:**

  ```
  "BaseUrl": "/reporting",
  ```

  ![../_images/Integrate.png](https://devnet.logianalytics.com/hc/article_attachments/12528163222167/integrate.png)
* **HomeController.cs:**

  *Update the appropriate routes in the controller*

  ```
  #region Izenda Actions[Route("reporting/settings")][Route("reporting/new")][Route("reporting/dashboard")][Route("reporting/report")][Route("reporting/reportviewer")][Route("reporting/reportviewerpopup")][Route("reporting")]publicActionResultIzenda(){returnView();}
  ```

  ![../_images/Home.png](https://devnet.logianalytics.com/hc/article_attachments/12528147172119/home.png)
