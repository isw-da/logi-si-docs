---
title: "Upgrade Composer with Custom Applications"
id: 34933211615373
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933211615373-Upgrade-Composer-with-Custom-Applications
updated_at: 2026-05-26T22:08:29Z
---

# Upgrade Composer with Custom Applications

# Upgrade Composer with Custom Applications

Because Composer is installed software, your organization must decide whether and when to install any particular upgrade. The following considerations will help you understand what is involved in upgrading to any version of Composer.

## Did You White Label Composer with a Custom CSS?

The CSS in Composer evolves with the client application. Differences in the CSS should be considered before you upgrade. You should examine all existing CSS and modify it accordingly.

## Does Your Application Use REST APIs?

Composer’s REST API offerings change regularly. Be sure you review the [Release Notes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933150964493-Logi-Composer-25-Release-Notes-Overview) regularly for changes in API endpoints.

## Does Your Application Use an iFrame-Embedded Dashboard?

Any dashboard already embedded in a custom application using an iFrame will continue to work with newer versions of Composer. iFrame-embedded dashboards have additional capabilities that are invoked using parameters included with the embedding code.

## Does Your Application Use the JavaScript Client Library?

The JavaScript client library is used to embed visuals or data directly into a web application without using an iFrame. Before upgrading Composer, consider the following topics.

### Visual Variables

Visual variables are written in standard JSON and left unstringified.

### JSON Modifications

Some key-value pairs are now wrapped in objects. Review the documentation for updated JSON samples.

### Deprecated Objects and Methods

Deprecated objects are methods are mentioned in the [Release Notes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933150964493-Logi-Composer-25-Release-Notes-Overview).

## Have You Created a Custom Connector?

Custom connectors built to work with previous versions of Zoomdata or Composer should continue to function as expected with newer versions.
