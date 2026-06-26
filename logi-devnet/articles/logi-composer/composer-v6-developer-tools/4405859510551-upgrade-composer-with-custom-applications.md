---
title: "Upgrade Composer with Custom Applications"
id: 4405859510551
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859510551-Upgrade-Composer-with-Custom-Applications
updated_at: 2021-09-21T01:29:57Z
---

# Upgrade Composer with Custom Applications

# Upgrade Composer with Custom Applications

Because Composer is installed software, your organization must decide whether and when to install any particular upgrade. The following considerations will help you understand what is involved in upgrading to any version of Composer.

## Did You White Label Composer with a Custom CSS?

The CSS in Composer evolves with the client application. Differences in the CSS should be considered before you upgrade. You should examine all existing CSS and modify it accordingly.

## Does Your Application Use REST APIs?

Composer’s REST API offerings change regularly. Be sure you review the [Release Notes](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes) regularly for changes in API endpoints.

## Does Your Application Use an iFrame-Embedded Dashboard?

Any dashboard already embedded in a custom application using an iFrame will continue to work with newer versions of Composer. iFrame-embedded dashboards have additional capabilities that are invoked using parameters included with the embedding code.

## Does Your Application Use the JavaScript Client Library?

The JavaScript client library is used to embed visuals or data directly into a web application without using an iFrame. Before upgrading Composer, consider the following topics.

### Visual Variables

Visual variables are written in standard JSON and left unstringified.

### JSON Modifications

Some key-value pairs are now wrapped in objects. Review the documentation for updated JSON samples.

### Deprecated Objects and Methods

Deprecated objects are methods are mentioned in the [Release Notes](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes).

## Have You Created a Custom Connector?

Custom connectors built to work with previous versions of Zoomdata or Composer should continue to function as expected with newer versions.
