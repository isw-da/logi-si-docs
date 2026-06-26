---
title: "Publish Custom Cross-Visual Filters"
id: 34933105142797
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933105142797-Publish-Custom-Cross-Visual-Filters
updated_at: 2026-05-26T22:07:46Z
---

# Publish Custom Cross-Visual Filters

# Publish Custom Cross-Visual Filters

You can build and enable your own custom cross-visual filters. An example is provided below.

**Note:** 
If you use date-time fields in your custom cross-visual filters, they must be in the format required by Composer. See [Date-Time Formats in Cross-Visual Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933066060429-Date-Time-Formats-in-Cross-Visual-Filters) for information on the required date-time format and an example for how to convert your data to the required format.

// START: PUB/SUB COMMON SECTION
// An embedding application should listen for the 'composer-dashboard-ready' event
// BEFORE attempting to publish or subscribe to cross-visual filters. The code below
// should be specified at the beginning of both publish and subscribe Javascript code.
const DASHBOARD\_READY\_EVENT = 'composer-dashboard-ready';
const pubSubReady = new Promise((resolve) => {
const resolvePubSubReady = (message, publisherId) => {
resolve();
document.removeEventListener(DASHBOARD\_READY\_EVENT, resolvePubSubReady);
}
document.addEventListener(DASHBOARD\_READY\_EVENT, resolvePubSubReady);
});
/\* END: Pub/Sub common section \*/
/\* START: Publish to Cross-Visual Filters \*/
// The following code represents the From and To date pickers on the
// embedding application's page that allow users to filter the data by
// a date range. The BETWEEN operator is used for the link name
// defined in the dashboard called 'LaunchedDate'. Note that the first part of
// this code converts the date-time data to the format expected by Composer.
const dateFromInput = document.getElementById('date-from');
const dateToInput = document.getElementById('date-to');
const formatDate = (date) => {
const d = new Date(date);
const year = `${d.getFullYear()}`;
let month = `${d.getMonth() + 1}`;
let day = `${d.getDate()}`;
if (month.length < 2) {
month = `0${month}`;
}
if (day.length < 2) {
day = `0${day}`;
}
return `${year}-${month}-${day}`;
}
const getEndOfDayString = dateString => `${dateString} 23:59:59.999`;
const getStartOfDayString = dateString => `${dateString} 00:00:00.000`;
const dateInputChangeHandler = (event) => {
const dateFromInputValue = dateFromInput.value;
const dateToInputValue = dateToInput.value;
const dateFrom = dateFromInputValue ? new Date(dateFromInput.value) : null;
const dateTo = dateToInputValue ? new Date(dateToInput.value) : null;
const dateFromString = dateFrom ? formatDate(dateFrom) : null;
const dateToString = dateTo ? formatDate(dateTo) : null;
const dateTimeFromString = dateFromString ? getEndOfDayString(dateFromString) : null;
const dateTimeToString = dateToString ? getStartOfDayString(dateToString) : null;
let operation = 'BETWEEN';
let value = [dateTimeFromString, dateTimeToString];
if (!dateTimeFromString) {
operation = 'LT';
value = dateTimeToString;
}
if (!dateTimeToString) {
operation = 'GT';
value = dateTimeFromString;
}
let publishObject = {
type: 'selection',
valueType: 'TIME',
ranges: [
{
operation: '<operation>',
value: '<value>'
}
]
}
if (!dateTimeFromString && !dateTimeToString) {
publishObject = null;
}
pubSubReady.then(() => embedManager.publish('LaunchedDate', publishObject));
}
dateFromInput.addEventListener('change', dateInputChangeHandler);
dateToInput.addEventListener('change', dateInputChangeHandler);
// This represents a drop-down field on the embedding application's page that
// lists a set of countries the user can filter by. After selecting a value,
// the embedding application calls its 'publishValue' function, defined
// below with the link name '<linkname> and the selected country value.
// The link name is defined in the dashboard. To clear the value filter,
// make sure you pass a null value as shown below.
const fieldSelect = document.getElementById('field-select');
fieldSelect.addEventListener('change', (event) => {
const value = event.target.value;
const publishObject = value !== 'null' ? {
type: 'selection',
valueType: 'ATTRIBUTE',
ranges: [
{
operation: 'IN',
value: '<value>'
}
]
} : null;
pubSubReady.then(() => embedManager.publish('Country', publishObject));
});
/\* END: Publish to Cross-Visual Filters \*/
