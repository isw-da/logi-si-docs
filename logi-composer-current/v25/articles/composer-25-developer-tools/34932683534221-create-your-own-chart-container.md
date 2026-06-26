---
title: "Create Your Own Chart Container"
id: 34932683534221
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932683534221-Create-Your-Own-Chart-Container
updated_at: 2026-05-26T22:06:20Z
---

# Create Your Own Chart Container

# Create Your Own Chart Container

Composer provides a reference to an HTML DIV element that developers can use as a container for their charts. This element is accessed via the `controller.element` property. Sometimes, it is useful to create an inner chart container inside the `controller.element` div to gain full control over its styling via the CSS chart components.

Example:

// In visualization.js
var chartContainer = document.createElement('div');
chartContainer.style.width = '100%';
chartContainer.style.height = '100%';
chartContainer.classList.add('chart-container');
controller.element.appendChild(chartContainer);

To add a border around the chart container:

/\* In GENERIC-TABLESTYLE.css \*/
div.chart-container {
border: 1px solid black;
}

Now you can use the div with the class `chart-container` to render your chart.
