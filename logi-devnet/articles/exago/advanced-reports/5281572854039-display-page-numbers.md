---
title: "Display Page Numbers"
id: 5281572854039
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281572854039-Display-Page-Numbers
updated_at: 2023-06-14T13:32:48Z
---

# Display Page Numbers

# Display Page Numbers

1. Add a **Page Footer** or **Page Header** section, depending on where you’d prefer the page number to be located.
2. Select a cell and manually add this formula: `@pageNumber@`![btSC71ReZc.png](https://devnet.logianalytics.com/hc/article_attachments/5432365613591/btsc71rezc.png)

For more information on formulas, refer to the topic on [What are formulas?](https://devnet.logianalytics.com/hc/en-us/articles/5281600700183-What-are-formulas-). For more information on parameters, review [Internal Parameters](https://devnet.logianalytics.com/hc/en-us/articles/5281584619287-Internal-Parameters).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> To include the word “Page” with the page number, in step 2 above use the formula `=Concatenate("Page ",@pageNumber@)` instead.
>
> ![dC2r5CNLoS.png](https://devnet.logianalytics.com/hc/article_attachments/5432413801879/dc2r5cnlos.png)
