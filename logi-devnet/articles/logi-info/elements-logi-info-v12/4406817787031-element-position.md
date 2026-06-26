---
title: "Element Position"
id: 4406817787031
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817787031-Element-Position
updated_at: 2022-04-06T06:08:12Z
---

# Element Position

# Element Position

Logi Info can use two methods for positioning elements on the report page: **Flow** positioning and **Absolute** positioning**.**

The following topics introduce you to these positioning schemes:

* [Selecting the Positioning Scheme](https://devnet.logianalytics.com/hc/en-us/articles/4406822475415-Selecting-the-Positioning-Scheme#Selecting)
* [Using the Layout Editor](https://devnet.logianalytics.com/hc/en-us/articles/4406822476439-Using-the-Layout-Editor#useLayout)

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Do not switch layout modes, even just as an experiment, without reading the section Switching Back from Absolute to Flow [Selecting the Positioning Scheme](https://devnet.logianalytics.com/hc/en-us/articles/4406822475415-Selecting-the-Positioning-Scheme) first. Absolute positioning is retained in Logi Analytics products primarily for *backward compatibility* with earlier versions and we highly recommend that you *do not use it* for any new development work.

## About Flow and Absolute Positioning

Logi application report definitions are developed in Studio using the Element Tree, which is a hierarchical arrangement of elements. **Flow positioning** determines the layout of the elements on the report page by order of appearance in the tree and each element's position is based on the previous element's position.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563121431/positionele_01.png)

For example, as shown above, most report definitions contain elements in the element tree grouped beneath **Report Header**, **Body** and **Report Footer** elements, which are arranged from top to bottom. On the actual report page, elements in the Report Header will appear above elements in the Body and elements in the Body will appear above elements in Report Footer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583770647/positionele_02.png)

Flow positioning is the default layout for report definitions created in Logi Studio and works well with multiple browser types and mobile devices. The use of HTML tables (**Row**, **Rows**, and **Column Cell** elements in Logi definitions), responsive elements, and the careful application of style classes can achieve very accurate alignment of elements on the report page under Flow positioning and, for most situations, it's the best approach.

**Absolute** **positioning**, however, determines the location of the elements on the report page by assigning groups of elements exact pixel offsets from the top and left side of the browser window.

When Absolute positioning is in use, Studio's Layout editor enables you to place elements in absolute positions on the screen by dragging and dropping them (it's not completely WYSIWYG, but it's close).

![](https://devnet.logianalytics.com/hc/article_attachments/4417575569431/positionele_03.png)

The example above shows the previous report after Absolute positioning has been enabled and elements have been positioned as desired.
