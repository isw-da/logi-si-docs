---
title: "Logi Composer 26.1 Feature Enhancements"
id: 43701146985741
section: "Logi Composer  26 Release Notes Overview"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements
updated_at: 2026-05-29T14:09:19Z
---

# Logi Composer 26.1 Feature Enhancements

# Logi Composer 26.1 Feature Enhancements

This topic provides details about the enhancements in Composer 26.1.

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

* [Source Creation Updates](#Source)
* [Tenant Management Updates](#Tenant)
* [Interactivity Overrides](#Interact)
* [Mapbox Style & Satellite Mode](#Mapbox)
* [Numeric Ratios](#Numeric)
* [PDF Generation](#PDF)
* [UI Improvements](#UI)
* [Dependency & Tooling Upgrades](#Dependen)
* [Spring Boot Updates](#Spring)

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

## Source Creation Updates

Source creation work area updates make it easier for you to add derived fields, hierarchies, upload translation files, and update field capabilities. Select an output node in the Source Creation canvas, and expand the Options menu to select and perform your task.

## Tenant Management Updates

The workflow for tenant creation and updates has been expanded and extended for easy management and maintenance.

Set up the **Reply-To Email** and **Sender Display Name** in this expanded work area as a tenant attribute if needed for sharing dashboard reports and self service reports.

Additionally, you can return reserved tenant attributes using the new endpoint, `api/account-attributes/reserved/`.

## Interactivity Overrides

Interactivity overrides have been updated to accommodate the updated source creation workflow.

## Mapbox Style & Satellite Mode

You can now enter a [supported style ID](https://docs.mapbox.com/api/maps/styles/ "supported style ID") when you define MapBox as a Tile Provider in a source for map visuals.

An additional option for display of map visuals, satellite mode, is available for supported map tile providers.

## Numeric Ratios

A new Ratio format is now available in the numeric format selector. Decimal values are expressed as a normalized ratio against one. For example, 0.5 renders as 1:2, 0.3333… as 1:3. This format is supported across all visuals that accept a numeric field.

## PDF Generation

The underlying component we use to generate PDFs, jspdf, has been updated from 2.5.2 to 3.0.1. This upgrade is compatible with most current browsers, excluding Internet Explorer.

## UI Improvements

Adjust your columns of truncated fields in the Visual Gallery, the dashboards Library, and the Sources work areas. Select to drag and resize the width of the Name, Tags, and Data Source columns as you navigate among your resources.

## Dependency & Tooling Upgrades

Upgraded core dependencies for improved performance and security:

* Node.js to 20.12.0
* Yarn to 4.9.2 (Berry/Corepack)
* npm to10.5.0
* TypeScript to 5.4.0
* Jest-circus to 29.7.0 (replaces deprecated Jasmine)

## Spring Boot Updates

We have upgraded the underlying Spring Boot framework to 3.5.5 across the platform. This infrastructure update provides enhanced security compliance and compatibility with modern development standards.
