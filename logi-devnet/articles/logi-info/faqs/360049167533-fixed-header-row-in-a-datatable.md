---
title: "Fixed Header Row in a DataTable"
id: 360049167533
section: "FAQs"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049167533-Fixed-Header-Row-in-a-DataTable
updated_at: 2023-08-02T14:08:56Z
---

# Fixed Header Row in a DataTable

**Question:**

How do I create a Fixed Header Row in a Logi Info DataTable?

**Answer:**

The easiest solution available is the CSS property "Position: Sticky;".

It currently has support in all major browser releases:  <https://caniuse.com/#feat=css-sticky>j

**Examples:**

To target all HTML tables:

```
table thead th {  
 position: sticky;   
 top: 0px;  
}
```

To target only Logi Info DataTable elements:

```
.rdThemeDataTable  thead th {  
 position: sticky;   
 top: 0px;  
}
```

To target a specific Logi Info DataTable:

First set the class attribute of the Datatable to "table-fixed-header"![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360072866753/mceclip0.png)

You can either add the following to a CSS file referenced within your application

```
.table-fixed-header thead th {  
 background-color: #ffffff !important;  
 position: sticky;   
 top: 0px;  
}
```

or add an IncludeHtml element to your report definition with the following Html:

```
<style>  
  
.table-fixed-header thead th {  
 position: sticky;   
 top: 0px;  
}  
   
</style>
```
