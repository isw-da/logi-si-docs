---
title: "Design a Logi Report"
id: 4406822288535
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822288535-Design-a-Logi-Report
updated_at: 2023-10-10T10:24:19Z
---

# Design a Logi Report

# Design a Logi Report

The following topics introduce developers to the basic concepts involved in
designing a typical Logi report:

* [About HTML Containers](https://devnet.logianalytics.com/hc/en-us/articles/4406817368599-About-HTML-Containers#Containers)
* [Report Layout](https://devnet.logianalytics.com/hc/en-us/articles/4406822289431-Report-Layout#Layout)
* [Adding Live Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817369623-Adding-Live-Data#Data)
* [Finishing Up](https://devnet.logianalytics.com/hc/en-us/articles/4406817371031-Finishing-Up#Finishing)

## Purpose and Prerequisites

As mentioned above, the purpose of this topic is to give developers who
are new to Logi Analytics technology and "Elemental Development"
an introduction to designing a Logi report.

Ideally, developers who are going to work with Logi products should have a
good understanding of:

* HTMLand XML
* CSS
* SQL (or whatever it takes to access the datasource they're working with)
* JavaScript
* "Stateless" web application concepts and web server technology

The Logi Server Engine, running at the web server, combines page
definitions with data and returns the report as a complete web page to the
requesting browser. The returned page consists of HTML, XHMTL, and
JavaScript, which the browser processes and displays.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) For a developer, understanding the potential, and limitations, of
these technologies is the key to a satisfactory development experience
with Logi products.

### Standards? What Standards?

The HTML and browser paradigm was conceived with the idea of universal and
generic presentation of information. Despite the efforts of international
standards organizations, this lovely idea has morphed over time into
something a bit different and sometimes it seems as if there are
*no standards*. In reality, browsers vary by manufacturer and version
in their presentation of web pages, providing a challenge for those
developers whose target audience uses a variety of browsers.

Logi Info makes a serious effort to ensure that their page output is
generic XHTML, CSS, and JavaScript, in order to promote cross-browser
compatibility. However, there's no way to predict what changes the browser
manufacturers will uncork with their next release, so developers
*should**frequently**test* their Logi apps against the
range of browsers and browser versions that could be used to view their
applications to ensure compatibility.

There are a number of online testing sites that make it easy to see what
your Logi app will look like in different browsers. Some, like
[BrowserStack](https://www.browserstack.com),
display images of your app in different browser, while others, like
[Browserling](https://browserling.com/), show
your app in a specific browser in an iFrame.

### HTML5

The ever-evolving HMTL5 standard is another moving target for developers.
Different browsers support different sets of HTML5 features, and sites
like [HTML5 Test](http://html5test.com/) that
can help you discover the related capabilities of your specific browser
make and version. Another useful site,
[Can I Use](http://caniuse.com/), indicates
which HTML5 features are available in various browsers on an
feature-by-feature basis. Logi Analytics is working to include more HTML5
features in our products with each release.
