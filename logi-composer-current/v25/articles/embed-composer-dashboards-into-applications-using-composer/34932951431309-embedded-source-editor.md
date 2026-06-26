---
title: "Embedded Source Editor"
id: 34932951431309
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932951431309-Embedded-Source-Editor
updated_at: 2026-05-26T22:07:20Z
---

# Embedded Source Editor

# Embedded Source Editor

Use Composer to embed a source editor for your users, enabling them to view, edit, or configure data sources directly in your application. Define the editor for users as needed for your custom solution.

You can embed the complete source editor, or limit what your users can access and use.

* [Step 1. Define a Connection to Create a Source](#Step1)
* [Step 2. Create a Component for the Source Editor](#Step2)
* [Step 3. Define Interactivity Settings](#Step3)
* [Step 4. Define Breadcrumbs Configuration](#Step4)

## Step 1. Define a Connection to Create a Source

Define a connection users can access to create a source. See [Embed Source Editor Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932982468749-Embed-Source-Editor-Properties) for more information on the properties for creating a source.

{
create: {
visible: true,
connections: {
ids: ["6347eca23d231b5c3c2a2f79", "633d6ef33d27115c3c2a2e45"],
defaultId: "6347eca22d271b5c3c2a2f79"
}
},
fields: {
visible: true
},
caching: {
visible: true
},
settings: {
visible: true
}
}

## Step 2. Create a Component for the Source Editor

// First initialize embed manager
const sourceEditor = await embedManager.createComponent('source-editor', {
sourceId: "633167d188f857721d2f70dd", // existing Source ID
activeTab: "fields",
theme: "composer",
tabs: { ... },
breadcrumbs: { ... },
interactivityOverrides: { ... },
notificationSettings: { ... },
});

## Step 3. Define Interactivity Settings

interactivityOverrides: {
create: {
ADD\_FROM\_CONNECTION: false,
UPLOAD\_NEW\_FILE: 'false' // value can be string as well
},
fields: {
ADD\_DERIVED\_FIELD: false,
ADD\_HIERARCHY\_FIELD: 'false' // value can be string as well
},
caching: {
STATISTICS\_CACHE: false,
SCHEDULE\_REFRESH: 'false' // value can be string as well
}
}

## Step 4. Define Breadcrumbs Configuration

{
title: "Back to Sources",
href: "https://company.com/sources",
target: "\_blank",
onClick: () => {
console.log("do action");
}
}
