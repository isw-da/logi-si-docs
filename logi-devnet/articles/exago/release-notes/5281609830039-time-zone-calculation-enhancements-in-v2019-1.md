---
title: "Time Zone Calculation Enhancements in v2019.1"
id: 5281609830039
section: "Release Notes"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281609830039-Time-Zone-Calculation-Enhancements-in-v2019-1
updated_at: 2023-04-03T17:49:28Z
---

# Time Zone Calculation Enhancements in v2019.1

# Time Zone Calculation Enhancements in *v2019.1*

Geopolitical time zones present an inherent problem for scheduling and date calculations. Their UTC offset values may vary throughout the year based on if and when a user’s or server’s location observes daylight saving time (DST). For example, a user in California and server in England would enter and exit DST on different dates, necessitating different UTC offset values throughout the year. This displacement of the UTC offset may cause schedules to run ahead or behind their intended times or even be ignored entirely.

With the release of *v2019.1*, Exago BI now offers an easy way to accurately handle different users and server spread across different geopolitical time zones.

## What Changed

In previous versions of Exago BI, the client and server time offset would be compensated for based on the a static setting called **Server Time Zone Offset**, a specified number of +/- hours to calculate the difference in time between client and server. This setting, however, is incapable of considering the fluctuation in server time offset caused by the non-uniform observations of DST in different geopolitical regions.

To better handle this is issue Exago now has a new setting called **Client Time Zone Name** which works in conjunction with **Noda Time**, an advanced .NET library, to accurately consider geopolitical time zones through the year as schedules and calculations are done.

## Client Time Zone Name

To accurately handle time zones there is a new [Culture Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281607969943-Culture-Settings) field called **Client Time Zone Name** where the user’s geopolitical time zone may be specified.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Using **Client Time Zone Name** is highly recommended as a best practice. However, if **Client Time Zone Name** is not given a value then Exago BI will fall back on its *pre-v2019.1* behavior and use the **Server Time Zone Offset** setting. In general the **Server Time Zone Offset** setting should only be provided if a **Client Time Zone Name** cannot be determined.

### Adjusting the Client Time Zone Name

The **Client Time Zone Name** setting may be set in the following ways:

* Within the **Admin Console**
* Modifying the configuration file XML
* Via the .NET and REST APIs

#### Admin Console

Within **Culture Settings** in the **Admin Console**, the default **Client Time Zone Name** can be specified. Setting a default value is recommended if all or a majority of clients and users are located within the same geopolitical region. If clients and users are located in many different regions, then a default is not required as this information should be set dynamically through the use of Roles or via the API.

![screen.clienttimezonename.png](https://devnet.logianalytics.com/hc/article_attachments/5432236535319/screen.clienttimezonename.png)

The dropdown contains a complete list of official [IANA time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Expressed as locations rather than as deltas from UTC, each time zone in this list correlates to a specific geopolitical region and contains information on that region’s observations of DST.

#### Configuration XML

The **Client Time Zone Name** can be manually edited within the configuration file XML using the following tag:

```
<clienttimezonename>America/New_York</clienttimezonename>
```

#### .NET and REST APIs

To modify this setting via the .NET API, the following property may be used:

```
PageInfo.SetupData.General.ClientTimeZoneName
```

This setting may also be modified via the REST API:

```
curl http://{webservice}/rest/settings?sid={sid} -X PATCH ^
        -d "{
             'General':
              {
               'ClientTimeZoneName': 'America/New_York'
              }
            }"
```

## Noda Time Library

The standard .NET date and time library lacks important date/time concepts (for example, “a date and time in a *specific* geopolitical time zone”). Due to the inherent issues that arise for scheduling processes because of DST and other non-linear time zone conflicts, Exago has replaced this library with a more powerful date and time library: **Noda Time**, a .NET library specifically designed to resolve date and time issues associated with geopolitical time zones and DST.

The **Schedule** module now utilizes the *Instant* and *LocalDateTime* classes of the Noda Time library. The *Instant* class represents a global, linear time in seconds. It does not map onto any calendar system and does not consider DST. The *LocalDateTime* class represents a point in time of a particular [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). These values can be mapped onto a calendar system and can take DST into consideration. The system operates using *Instants* while users operate in the *LocalDateTime* of their legislative time zone of residence.

The Noda Time library is also available for use by developers via the .NET API. For in-depth information on the Noda Time library, please see the [Noda Time documentation](https://nodatime.org/).

### Updates to the Scheduler Queue

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If you have not implemented the **Scheduler Queue**, then the following information will not affect *v2019.1* upgrading process.

Certain DateTime values may have been assigned different meanings in the Scheduler Job XML following the implementation of Noda Time. Depending on the modifications made to the implementation of the **Scheduler Queue**, changes may have to be made to its code:

* If the implementation of the **Scheduler Queue** utilizes the QueueAPI object from WebReports.Api.Scheduler, then there should be no required for the **Scheduler Queue** to function properly after upgrading to *v2019.1*.
* If the implementation of the **Scheduler Queue** has been modified to directly parse the Job XML, then some DateTime values may have been assigned a different meaning and will need to be adjusted for. If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

## Additional Information

* Admin Support Lab — [Time Zone Handling](https://devnet.logianalytics.com/hc/en-us/articles/5281571285911-Time-Zone-Handling) (video)
