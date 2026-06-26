---
title: "Inline Frame or JavaScript API?"
id: 5281619698839
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281619698839-Inline-Frame-or-JavaScript-API
updated_at: 2022-05-03T22:08:19Z
---

# Inline Frame or JavaScript API?

# Inline Frame or JavaScript API?

Exago BI offers flexibility when integrating with a host application. This topic aims to describe the differences between using **inline frames** (also known as **iframes**) and the **JavaScript API**.

This topic details the pros and cons of each embedding method. As each application is unique, it is ultimately up to the developer to make the best decision for their own product. Exago BI has successfully been embedded exclusively with inline frames, exclusively the JavaScript API and a hybrid of the two together.

## Inline Frames

### Advantages

* **Security**
  + Exago BI code and host application code run in the context of their own pages. Exago BIJavaScript and host application do not interfere with each other.
* **Performance and User Experience**
  + The host application page can render separately from Exago BI, so one does not delay the other.
  + JavaScript failure in either the host application or in Exago BI does not prevent the other from loading.
* **Simple integration and testing**
  + Exago BI CSS and host application CSS run in their context and do not interfere with each other.
  + Utilizes a well-defined and widely-supported non-product specific HTML element.
  + Exago BI can be tested without having to build out the entirety of the host page first.

### Disadvantages

* **Performance**
  + The page’s `onLoad` event is delayed by the loading of iframes, so pages may appear to take longer to load than they actually do.
* **User Experience**
  + Creating a fully responsive design with iframes is possible but more complicated than doing so with JavaScript.
* **Only one API action permitted per session**, making it difficult to intermingle multiple reports, charts and non-Exago content on the same page.

## JavaScript API with <div>s

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> While neither an advantage or disadvantage per se, the JavaScript API works in conjunction with one of the server-side Exago APIs (that is .NET or REST Web Service) to create sessions.

### Advantages

* **Performance and User Experience**
  + A session is launched once per page load and multiple calls are allowed. This permits a “collage of BI elements” and more flexibility embedding Exago into the host app page.
  + Easy to integrate many reports, charts and non-Exago content seamlessly on the same page.
* **Integration**
  + Since each DOM is accessible to both applications, it may be easier to customize Exago’s styling with that of the host application and vice versa.
  + JavaScript available in the host application is available to Exago and vice versa. Custom scripting is possible without being limited to Action Events.
  + `OnLoad()` and `OnError()` callback functions in the `ExagoApi` object provide for simple and graceful event handling.

### Disadvantages

* **Integration**
  + Potential exists for CSS, JavaScript and library version conflict between host application and Exago.
  + The page that embeds Exago must be completely developed and functional during testing to ensure no conflicts exist between the two.
  + There is no concept of an Active Report or API Action; in-memory report changes are not supported. All report changes must be saved first.
* **Security**
  + Additional cross-domain CORS handling may be required.

## Additional Resources

The following materials were referenced in the drafting of this topic. Clients looking for additional resources to aid in their embedding decision are encouraged to review them.

* [JavaScript API](https://devnet.logianalytics.com/hc/en-us/articles/5281628892055-JavaScript-API)
* [JavaScript API](https://devnet.logianalytics.com/hc/en-us/articles/5281570668311-JavaScript-API) (video)
* [Cross-Origin Embedding of Exago BI](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI)
* [Third-Party Link: Blog of Krasimir Tsonev — iframe or not, that is the question](https://krasimirtsonev.com/blog/article/iframe-or-not-that-is-the-question)
