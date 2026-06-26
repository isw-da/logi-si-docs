---
title: "How to Reduce white-space in Headers and Footers when exporting to PDF (.Net)"
id: 360049163113
section: "FAQs"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049163113-How-to-Reduce-white-space-in-Headers-and-Footers-when-exporting-to-PDF-Net
updated_at: 2020-07-27T22:19:56Z
---

# How to Reduce white-space in Headers and Footers when exporting to PDF (.Net)

**Question:**

How do I reduce the white-space produced in the Header and Footer when exporting to PDF?

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360071663854/mceclip0.png)

**Answer:**

When Logi Info produces a PDF Export with a Page Header and / or Footer, each section is treated as a separate definition, rendered to HTML then stitched together during the export process.

By adding some inline CSS to both the Header and Footer sections, this white-space can be reduced significantly.

![mceclip1.png](https://devnet.logianalytics.com/hc/article_attachments/360071666494/mceclip1.png)

The attached sample includes IncludeHTML elements within the Page Header and Page Footer elements.  The IncludeHTML used targets the elements specific to the HTML document of the Header or Footer as follows:

```
<style>  
html, body, span, #rowsHeader td, #rowsHeader {  
 background-color: White;  
 padding-top: 0px !important;  
 padding-bottom: 0px !important;   
 margin-top: 0px !important;  
 margin-bottom: 0px !important;   
 font-size: 16px !important;  
 font-weight: bold !important;  
 line-height: 16px !important;  
}  
  
hr {  
 margin-top: 5px;  
 padding-bottom: 0px;  
 margin-bottom: 0px;  
}  
</style>
```
