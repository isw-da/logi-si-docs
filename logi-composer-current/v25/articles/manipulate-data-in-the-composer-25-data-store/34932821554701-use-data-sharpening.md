---
title: "Use Data Sharpening"
id: 34932821554701
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932821554701-Use-Data-Sharpening
updated_at: 2026-05-26T22:06:59Z
---

# Use Data Sharpening

# Use Data Sharpening

Data Sharpening™ is Composer's patented technique to deliver fast and responsive visuals for large volumes of data. Conceptually, Data Sharpening is similar to the way large image files or streaming video files display in a browser. When you start to load the image file, you see a blurry approximation of the image. But as the file loads in the background, the image sharpens until the entire image eventually comes into clear focus.

When you create or modify a visual for a large data set in Composer, Data Sharpening immediately displays a partial or approximate rendering of the data. It then continuously updates the visual with more and more data until the fully sharpened result is available.

While the visual sharpens, you can continue to interact with it, zooming into more detail or changing the Group By attribute without waiting for the entire query to return. Essentially, you can continue your big data exploration without waiting for long-running queries over billions of rows of data to complete. Composer adjusts on-the-fly based on your input. One thing to keep in mind—Data Sharpening may not always be needed when visualizing your data. If Composer is able to complete its query of the data quickly (within a few seconds), you will simply see the final result rendered in the visual. Data Sharpening is a tool that is leveraged when the visual may not render immediately due to the volume of the data being queried.

See the following topics:

* [Data Sharpening Prerequisites](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932836946061-Data-Sharpening-Prerequisites)
* [When Data Sharpening Occurs](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932849324685-When-Data-Sharpening-Occurs)
* [Enable Data Sharpening and Configure Its Defaults](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932836726541-Enable-Data-Sharpening-and-Configure-Its-Defaults)
* [Enable Data Sharpening for Cloudera Impala Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932735320461-Enable-Data-Sharpening-for-Cloudera-Impala-Data-Sources)
