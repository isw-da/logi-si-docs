---
title: "Create Your Own Chart Container"
id: 43700989151885
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700989151885-Create-Your-Own-Chart-Container
updated_at: 2026-05-29T14:07:14Z
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
