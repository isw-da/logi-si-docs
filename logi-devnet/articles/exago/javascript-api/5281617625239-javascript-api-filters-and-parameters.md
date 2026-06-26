---
title: "JavaScript API: Filters and Parameters"
id: 5281617625239
section: "JavaScript API"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281617625239-JavaScript-API-Filters-and-Parameters
updated_at: 2022-05-03T22:07:56Z
---

# JavaScript API: Filters and Parameters

# JavaScript API: Filters and Parameters

As of *v2019.1*, runtime filters and parameters can now be modified via the JavaScript API prior to a report’s execution. New behaviors have been defined for the for *ExecuteReport* function in order to allow the addition of new filters, the modification of existing filters, and the addition or modification of parameters. These modifications only apply at runtime and do not alter report definitions.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Review [JavaScript API](https://devnet.logianalytics.com/hc/en-us/articles/5281628892055-JavaScript-API) for in depth descriptions of the **Functions** and **Interfaces** utilized by these features.

For the code snippets in the following sections,  assume the following framework:

```
function executeReport() {
	var reportPath = document.getElementById('exagoReport').value;
	var exportSelector = document.getElementById('execSelection');
	var exportType = exportSelector.value;
	var containerId = document.getElementById('containerSelection').value;
	var container = document.getElementById('container' + containerId);
	
	var reportOptions =
	{
	Udf: null,
	UpdateCallback: updateCallback,
	ErrorCallback: errorCallback,
	
	//For adding new filters to a report
	NewFilters: filters,
	
	//For modifying prompting filters in Advanced Reports
	PromptingFilterValues: promptingFilters,
	
	//For modifying prompting filters Dashboards and Chained Reports
	//PromptingFilterValues: promptingCompositeFilters,
	
	//For adding or modifying the non-hidden parameters of a report
	Parameters: parameters
	};
	
	api.ExecuteReport(container, exportType, reportPath, reportOptions);
	}
```

## Adding a New Filter

To add runtime filters to a report via the JavaScript API:

1. Define the report filter objects by specifying their `FilterText`, `Operator`, `Values`, and other necessary information.
2. Add these definitions to an array of report filters.
3. Reference this array in the **NewFilters** property of the report options interface.
4. Call *ExecuteReport* referencing the report options parameter.

For a full list of properties and a description of this feature, see [wrJsApiExecuteReportFilter](https://devnet.logianalytics.com/hc/en-us/articles/5281628892055-JavaScript-API#wrJsApiE2).

Consider the following when adding a new filter via the JavaScript API:

* `FilterText` cannot be null
* `FilterText` must take one of the following forms:
  + a data field (for example `Employees.LastName`)
  + a function (for example `=Month({Employee.BirthDate})`)
  + a parameter (for example `@parameterNam@`)
* If the `Operator` type is `OneOf` or `NotOneOf`, then `Values` must be an array. If the type is `Between` or `NotBetween`, then the array may only be a length of two.
* Filter functions, like *DayAfterTomorrow()*, may not be used as a value.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Currently, runtime filters cannot be added to **Dashboards** or **Chained Reports** via the JavaScript API.

### Example

The following code sample creates two runtime filters on the *Employees* data category.

```
var filters = [];

	var filter =
	{
		FilterText: "Employees.EmployeeID",
		Operator: "Between",
		PromptFlag: true,
		AndFlag: true,
		GroupWithNextFlag: false,
		Values: [2, 5],
		Title: "Employee Id"
	};
	
	filters.push(filter);

	filter =
	{
		FilterText: "=Year({Employee.HireDate})", 
		Operator: "GreaterThanEqualTo",
		PromptFlag: false, 
		AndFlag: true, 
		GroupWithNextFlag: false, 
		Values: 2010, 
		Title: "Employee Hire Date"
	};
filters.push(filter);
```

## Modifying an Existing Prompting Filter

To modify and set the values for existing prompting filters on a report via the JavaScript API:

1. Define the prompting filter objects by specifying their `FilterText`, `Index`, and `Values`.
2. Add these definitions to a designated array of prompting filters.
3. Reference this array in the **PromptingFilterValues** property of the report options interface.
4. Call *ExecuteReport* referencing the report options parameter.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Only prompting filters may be modified prior to report execution. Non-prompting filters cannot currently be modified via the JavaScript API.

For a full list of properties and a description of this feature, please see [wrJsApiPromptingFilterValue](https://devnet.logianalytics.com/hc/en-us/articles/5281628892055-JavaScript-API#wrJsApiP) and [wrJsApiCompositePromptingFilterValue](https://devnet.logianalytics.com/hc/en-us/articles/5281628892055-JavaScript-API#wrJsApiC).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Any prompting filter with a value set via the JavaScript API will be treated as non-prompting and will not appear in the prompting **Filters** menu upon report execution.

### Examples

The following sections detail how to modify prompting filters on Advanced Reports and non-interactive filters on Dashboards and Chained Reports:

#### Modifying Prompting Filters on an Advanced Report

For the following example, assume that the following existing prompting filters on an Advanced Report:

```
Employees.LastName Starts With 'D' AND
Employees.ID Is Between '2' And '5' AND
Employees.LastName Is Not Equal To 'Dodsworth'
```

These filters are ordered as they appear in the Filters menu in the Report Designer. `FilterText` values are treated as the primary identifier of each filter. The `Index` value serves as a secondary identifier, increasing its value at each instance of identical `FilterText`. The following list details filter indexing for Advanced Reports:

```
Employees.LastName  [Index: 0]
Employees.ID        [Index: 0]
Employees.LastName  [Index: 1]

/*********** Continuing the example: ***************/
=MonthName({Employees.BirthDate}) [Index: 0]
Employees.ID        [Index: 1]
Employees.BirthDate [Index: 0]
Employees.LastName  [Index: 2]
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If the `Index` value is left null, the value of 0 (zero) will be passed by default.

The following code modifies and sets the values for two existing prompting parameters on a report prior to its execution. It sets the value of “Davolio” to the second instance of the `Employees.LastName` filter and modifies the `Operator` of the first instance of the `Employees.EmployeeID` filter.

```
	var promptingFilters = [];

	var promptingFilter =
	{
	FilterText: "Employees.LastName",
	Index: 1,
	Values: "Davolio"
	};
	promptingFilters.push(promptingFilter);

	promptingFilter =
	{
	FilterText: "Employees.EmployeeID",
	Index: 0,
	Values: [2, 5],
	Operator: "NotBetween"
	};
promptingFilters.push(promptingFilter);
```

#### Modifying Prompting Filters on a Dashboard or Chained Report

For the following example, assume the following existing prompting filters on the Dashboard or Chained Report:

```
=Year({Employees.HireDate}) = '1996' AND
Employees.FirstName Is Not Equal To 'Janet' AND
Employees.Title = 'Sales Representative'
```

These filters are ordered as they appear in the Filters menu on the composite report. However, within composite reports, `Index` values are the primary identifiers of each filter and are set on a global scale. The `Index` value increases for each new filter on a composite report. The following list details filter indexing for composite reports:

```
=Year({Employees.HireDate}) [Index: 0]
Employees.FirstName         [Index: 1]
Employees.Title             [Index: 2]
```

```
/************ Continuing the example **************/
Employees.ID                [Index: 3]
Employees.BirthDate         [Index: 4]
Employees.FirstName         [Index: 5]
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> `Index` values for composite reports do not default to 0 (zero) and are a required field for each prompting filter.

The following code modifies and sets the values for three existing prompting parameters on a composite report prior to its execution.

```
var promptingCompositeFilters = [];

	var promptingCompositeFilter =
	{
	Index: 0,
	Values: [1996, 2005],
	Operator: "Between"
	};
	promptingCompositeFilters.push(promptingCompositeFilter);

	promptingCompositeFilter =
	{
	Index: 1,
	Values: ["Nancy"],
	};
	promptingCompositeFilters.push(promptingCompositeFilter);

	promptingCompositeFilter =
	{
	Index: 2,
	Values: "Sales Manager"
	};
promptingCompositeFilters.push(promptingCompositeFilter);
```

## Adding Parameters and Modifying Parameter Values

New parameters may be added to a report and existing non-hidden parameter values may be modified prior to report execution via the JavaScript API. For a full list of properties and a description of this feature, see [wrJsApiExecuteReportParameter](https://devnet.logianalytics.com/hc/en-us/articles/5281628892055-JavaScript-API#wrJsApiE3).

With multi-value parameters introduced in *v2022.1.0*, the Value properties do support an array of values for those parameters that are already multi-value. Use the REST Web Service API or .NET API to change a Parameter between single or multi-value.

To add a new parameter to a report:

* The `Name` value must be unique and cannot be identical to the names assigned to existing non-hidden parameters or to reserved parameters. If the `Name` value is identical to an already existing non-hidden parameter, then this parameter’s value will be overwritten.
* The `Value` being assigned to the new parameter must be a number, string, or date. It may not be an array of multiple values *pre-v2022.1.0*.
* The `PromptText` value set represents the text that will display when prompting the user for a value. If `PromptText` is set to a null or empty string value, the parameter will be set to non-prompting. Otherwise, the parameter will prompt the user for input upon report execution.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> For more information on parameters and a list of reserved parameters, see [Parameters](https://devnet.logianalytics.com/hc/en-us/articles/5281625630615-Parameters).

To modify the value of an existing non-hidden parameter:

* The `Name` value must be identical to an existing non-hidden parameter on the report.
* The `Value` being assigned to the parameter must be a number, string, or date, and must match the existing parameter’s data type. It may not be an array of multiple values *pre-v2022.1.0*.
* The `PrompText` value set represents the text that will display when prompting the user for a value. If `PromptText` is set to a null or empty string value, the parameter will be set to non-prompting. Otherwise, the parameter will prompt the user for input upon report execution.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Modifying parameters via the JavaScript API will overwrite existing parameters at the application/system level for that specific report execution. For example, if an existing prompting parameter is modified to be non-prompting, it is equivalent to setting this parameter to be non-prompting within the **Admin Console**.

### Example

The following code will add two parameters. In this example, the first parameter, `@FirstName@` will prompt the user with the specified prompting text, while the second parameter, `@Id@` will be non-prompting.

```
var parameters = [];

var parameter = 
{
Name: "FirstName",
Value: "Anne", 
PromptText: "Enter your first name"
};
parameters.push(parameter);

parameter = 
{
Name: "Id",
Value: 9,
PromptText: ""
};
parameters.push(parameter);
```

## Additional Resources

* [Admin Support Lab — JavaScript API Filters](https://devnet.logianalytics.com/hc/en-us/articles/5281532084887-JavaScript-API-Filters) (video)
