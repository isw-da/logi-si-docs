---
title: "List of REST Endpoints"
id: 5281669098391
section: "REST Web Service API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281669098391-List-of-REST-Endpoints
updated_at: 2022-05-03T22:07:51Z
---

# List of REST Endpoints

# List of REST Endpoints

The following REST Web Service API endpoint paths are available. All calls require the following headers:

```
Content-Type: application/json
Accept: application/json
Authorization: {type} {authstring}
```

For more information, review [REST — Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281660927895-REST-Introduction)

**/rest/Batch**v2018.1.1+

* POST

**/rest/Sessions**

* POST
* GET

**/rest/Sessions/{sid}**

* GET
* PATCH
* DELETE

All of the following calls require the Session ID URL parameter: `sid={sid}`

#### Example

```
GET /rest/Settings?sid={sid}
```

**/rest/DataSources**

* GET

**/rest/DataSources/{Id}**

* POST
* GET
* PATCH

**/rest/Entities**

* POST
* GET

**/rest/Entities/{Id}**

* GET
* PATCH
* DELETE

**/rest/Entities/{Id}/Fields**

* GET

**/rest/Entities/{Id}/Fields/{Field Id}**

* GET
* PATCH
* POST v2019.1.13+

**/rest/Folders/{Name}**

* POST
* DELETE

**/rest/Folders/Rename**

* POST

**/rest/Functions**

* POST
* GET

**/rest/Functions/{Id}**

* GET
* PATCH
* DELETE

**/rest/Joins**

* POST
* GET

**/rest/Joins/{Id}**

* GET
* PATCH
* DELETE

**/rest/Parameters**

* POST
* GET

**/rest/Parameters/{Id}**

* GET
* PATCH
* DELETE

**/rest/Reports/List**

* GET

**/rest/Reports/Execute/{Type}**

* POST

**/rest/Roles**

* POST
* GET

**/rest/Roles/{Id}**

* GET
* PATCH

**/rest/Roles/{Id}/DataObjectRows**

* GET
* PATCH

**/rest/Roles/{Id}/Entities**

* GET
* PATCH

**/rest/Roles/{Id}/Folders**

* GET
* PATCH

**/rest/Roles/{Id}/Settings**

* GET
* PATCH

**/rest/SchedulesV2**v2019.2.29+v2020.1.3+v2021.1.1+

* GET
* POST

**/rest/SchedulesV2/{ScheduleID}**v2019.2.29+v2020.1.3+v2021.1.1+

* GET
* PATCH
* DELETE

**/rest/SchedulesV2/Flush**v2019.2.29+v2020.1.3+v2021.1.1+

* POST

**/rest/SchedulesV2/{ScheduleID}/Filters**v2019.2.29+v2020.1.3+v2021.1.1+

* GET
* PATCH

**/rest/SchedulesV2/{ScheduleID}/Parameters**v2019.2.29+v2020.1.3+v2021.1.1+

* GET
* PATCH

**/rest/ServerEvents**

* GET

**/rest/ServerEvents/{Id}**

* GET
* DELETE

**/rest/Settings**

* GET
* PATCH

**/rest/StorageMgmt**v2020.1+

* GET
* PUT
* PATCH
