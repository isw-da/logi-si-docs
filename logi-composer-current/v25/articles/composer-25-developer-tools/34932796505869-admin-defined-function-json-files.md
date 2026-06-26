---
title: "Admin-Defined Function JSON Files"
id: 34932796505869
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932796505869-Admin-Defined-Function-JSON-Files
updated_at: 2026-05-26T22:06:56Z
---

# Admin-Defined Function JSON Files

# Admin-Defined Function JSON Files

Use a single JSON file to define all the admin-defined functions for a single connector. Store this JSON file in the appropriate location for your Composer environment.

* Linux: `/etc/zoomdata`. As an example, `/etc/zoomdata/edc-impala-functions.json`.
* Windows: `<install-path>/conf-modify`. As an example, `<install-path>/conf-modify/edc-impala-functions.json`.

This topic covers the following information:

* [JSON File Structure](#JSON)
* [Validating Your JSON File](#Validati)
* [Example](#Example)

## JSON File Structure

The basic structure of an admin-defined function in the JSON file is shown below. Each section is described.

{
"<function>": {
"template": "<SQL template string>",
"returnType": {
"type": "<type>",
"name": "<name>"
},
"arguments": {
"<arg1-key>": {
"name": "<arg1-name>",
"returnType": {
"type": "<type>",
"name": "<name>"
},
"description": "<arg1-description>"
},
"<arg2-key>": {
"name": "<arg2-name>",
"returnType": {
"type": "<type>",
"name": "<name>"
},
"description": "<arg2-description>"
}
},
"description": "<function-description>"
}
}

### function

The function name is the identifier used for the row-level admin-defined function. This name is displayed in the Composer UI. The function name must start with a letter or an underscore and can contain letters, underscores, numbers, and periods.

### template

The template defines the SQL string that will be used in the SQL query to a data source. You are fully responsible for the validity of the template string. Composer cannot fully validate it.

The template references arguments defined later in the JSON file. The arguments are surrounded by braces (curly braces) and are replaced by their SQL representations at run time. Composer does validate missing arguments when the connector associated with this JSON file starts.

You can use a backslash (`\`) as an escape character. It can be used to escape the following three characters:  `\ { }` anywhere in the SQL template string (including inside the argument placeholders).

Here is an example:

"template": "({arg\_0}) + ({arg\_1}) \* interval '1 year'”

### returnType

There are three possible returnTypes: `simple`, `generic`, and `array`. The returnType used for the whole function must be `simple` or `generic`; the `array` returnType is not supported for the whole function. However, all three returnTypes are supported in the arguments defined within an admin-defined function.

Each returnType in the JSON provides a type specification and a name.

simple returnTypes

Five simple returnTypes are supported : NUMBER, INTEGER, STRING, DATE, or BOOLEAN. Here is an example of a simple returnType:

"returnType": {
"type": "simple",
"name": "DATE"
}

generic returnTypes

A generic returnType is an abstract type that is given a name. Here is an example of a generic returnType:

"returnType": {
"type": "generic",
"name": "T"
}

The specified name is the name used for the returnType inference. The only restriction is that the function's generic returnType name must be the same as one of the argument types. This is required to infer a function returnType based on an argument type.

array returnTypes

An array returnType includes a baseType that can be used only for the last argument. The baseType can only be `simple` or `generic`. Here is an example:

"returnType": {
"type": "array",
"baseType": {
"type": "simple",
"name": "STRING"
}
}

### arguments

The arguments section defines the argument keys and definitions. You do not have to specify an arguments section if there are no arguments. The argument keys are used in the SQL template string at the beginning of the function definition.

An argument definition consists of a name, a returnType, and description. The name and description are used to display the argument in the Composer UI. The returnType is used for argument type validation and function returnType inference. The argument returnType can be `simple`, `generic` or `array`.

### description

The description is an optional string you can specify to describe a function or an argument in the JSON file and in the Composer UI.

## Validating Your JSON File

You can validate your JSON against a JSON schema file `functions-schema.json` that Composer provides in the appropriate directory for your environment.

* Linux: `/opt/zoomdata/docs/<edc-connector>`. For example, the Impala JSON schema is in `/opt/zoomdata/docs/edc-impala/functions-schema.json`.
* Windows: `<install-path>/docs/<edc-connector>`. For example, the Impala JSON schema is in `<install-path>/docs/edc-impala/functions-schema.json`.

**Validate your JSON file against the JSON schema**

1. Link to the JSON Schema Validator at <https://www.jsonschemavalidator.net/>.
2. Copy the schema found in the JSON schema file for your connector (see above) to the left side of the JSON Schema Validator screen.
3. Copy your JSON file admin-defined function definitions in the **Input JSON** section on the right side of the JSON Schema Validator screen.

Any schema errors will be identified immediately on the screen.

## Example

In the following JSON file, two admin-defined functions, `TEST_ADD` and `TEST_ADD_YEAR`, are defined.

**Note:** 
Before using this example, be sure to remove the comments. Comments are not allowed in JSON.

{
"TEST\_ADD": { //Function name
"template": "{summand\_1} + {summand\_2}", //SQL template string
"returnType": { //Return type of the function
"type": "simple",
"name": "NUMBER"
},
"arguments": { // List of arguments
"summand\_1": { //Argument key used for lookup in SQL template string
"name": "Summand 1", //Argument name, will be displayed on Derived Field Editor
"returnType": { // Type of argument.
"type": "simple",
"name": "NUMBER"
},
"description": "An expression evaluated to a numeric value." //Argument description
},
"summand\_2": {
"name": "Summand 2",
"returnType": {
"type": "simple",
"name": "NUMBER"
},
"description": "An expression evaluated to a numeric value."
}
},
"description": "Addition: add two numbers." //Function description
},
"TEST\_ADD\_YEAR": {
"template": "({0}) + ({1}) \* interval '1 year'",
"returnType": {
"type": "simple",
"name": "DATE"
},
"arguments": {
"0": {
"name": "Date",
"returnType": {
"type": "simple",
"name": "DATE"
},
"description": "An expression 1"
},
"1": {
"name": "Year",
"returnType": {
"type": "simple",
"name": "INTEGER"
},
"description": "An expression 2"
}
},
"description": "Add year."
}
}
