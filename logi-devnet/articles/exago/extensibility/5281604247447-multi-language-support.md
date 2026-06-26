---
title: "Multi-Language Support"
id: 5281604247447
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support
updated_at: 2022-05-03T22:09:01Z
---

# Multi-Language Support

# Multi-Language Support

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

Any text in the application can be translated or modified. This can be accomplished by creating XML files in the `<WebApp>\Config\Language` directory. These files map IDs to strings. Any place within Exago that displays text has an associated ID. When a text element is required in the application, Exago will read the file(s) specified in the **Admin Console** > **General** > **Main Settings** > **Language File** setting and use the string that is mapped to the ID.

The language elements discussed in this topic do not include those created by users or administrators such as reports, folders, express report/CrossTab themes or Data Field names. To modify Data Field names, see [Column Metadata](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects#Column). To modify theme names please see [Chart, Map and Report Themes](https://devnet.logianalytics.com/hc/en-us/articles/5281604053911-Chart-Map-and-Report-Themes).

ExagoBI comes with both a standard English file `en-us.xml` and a Spanish translation `es-mx.xml`. Below is an example of the multi-language functionality. Notice that the prompt text in the **New Report Wizard** can be set by changing the string associated with the ID `NewReportLb1`.

```
en-us.xml

<NewReport>
	<element id="NewReportLbl">Complete the steps in the wizard below to create a new report</element>
</NewReport>
```

![](https://devnet.logianalytics.com/hc/article_attachments/5432249172375/image99.png)

Es-mx.xml:

```
es-mx.xml

<NewReport>
	<element id="NewReportLbl">Complete los pasos en el asistente para crear un nuevo informe</element>
</NewReport>
```

![](https://devnet.logianalytics.com/hc/article_attachments/5432284859159/image100.png)
> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Some language strings contain special place holders between curly brackets (ex. {0}).  These hold the place of elements that must be filled in dynamically by Exago. **Do not translate anything inside curly brackets**. The place holders may be moved within the string but do not delete them.

The example below demonstrates three place holders that will be replaced by dropdown menus in the Scheduling Wizard.

```
<element id="ScheduleRecurrenceRelativeMonthlyTxt">The {DayPosition} {DayOfWeek} of every {MonthNumber} month(s)</element>
```

![](https://devnet.logianalytics.com/hc/article_attachments/5432249232535/image101.png)

## Translating Exago

To translate the entire interface, make a copy of the file `en-us.xml` and give it a different name. Make sure this copy is in the folder `<WebApp>/Config/Languages`. Without changing the IDs translate the strings as desired (see example above). Then set the [Language File](https://devnet.logianalytics.com/hc/en-us/articles/5281644565527-Main-Settings#Language) setting in Admin Console > General > Main Settings. to point to the new file.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If you are using the Exago Scheduler Service be sure to copy all custom language XML files to the `<Sched>/Languages` folder of each Scheduler Service instance.

## Modifying Select Language Elements

To change specific language elements without copying the entire mapping you can use a base file and specify changes in separate language files. When you set the **Language File** setting, list the all of the files you want to load separated by commas or semicolons. Exago will load the files from left to right, meaning the first file listed will be used as a base and can be changed by the files loaded after it.

As an example you can create the file en-custom.xml which only contains the lines:

```
en-custom.xml

<?xml version="1.0" encoding="utf-8" ?>
	<element id="GettingStartedTab">Home</element>
```

Set the **Language File** setting to *en-us, en-custom* and the Getting Started tab will reflect the change made in the custom file.

![](https://devnet.logianalytics.com/hc/article_attachments/5432271243415/image102.png)
> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Begin all language XML files with the line `<?xml version="1.0" encoding="utf-8"?>`

### Text of Prompting Filters and Parameters on Dashboards

When adding a Report to a Dashboard a user can specify text for any prompting Filters or Parameters. By default this text will match the strings associated with the ids *CompositeReportOptionsFilterDefaultPromptText* and *CompositeReportOptionsParameterDefaultPromptText* respectively.

If a user changes the default and enters a different language Id then the associated text for that new Id will display when the Dashboard is executed.

If a user enters text that does not match any language Id the text will be displayed when the Dashboard is executed.

![](https://devnet.logianalytics.com/hc/article_attachments/5432249285911/image103.png)

### Theme Name

Names of custom chart, GeoChart, CrossTab, ExpressView and Express Report themes can also be translated. Review [Multi-Language Support for Theme Names](https://devnet.logianalytics.com/hc/en-us/articles/5281604053911-Chart-Map-and-Report-Themes#Multi-La).

### Filter Function Name and Description

Prefix the filter function's name or description with `_wrFunctionId`. If this ID matches the ID of any element in the language files, then the string of that language element will be displayed to the user instead of the function name/description in the Admin Console.
