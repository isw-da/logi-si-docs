> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Admin-Defined Functions

Self-Service Analytics provides a set of functions that you can use in expressions to build derived fields or custom metrics. However, you may want to use your own functions (for which there is no Self-Service Analytics equivalent) to extend your data analytics in Self-Service Analytics. Examples of this might be functions available within your data store either natively or as user-defined functions. In such situations, you can leverage administrator-defined functions to expose this capability throughout Self-Service Analytics.

Administrator-defined functions allow your organization to create functions at the connector level from SQL strings. These functions can be referenced later in [data source configurations](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) that use the connector.

Currently, the following limitations exist for administrator-defined functions.

1. They are only available for connectors that are SQL-based and that support row-level expressions in derived fields and custom metrics.
2. They are only available for functions that perform row-level operations, and not aggregation operations (for example, standard deviation or rank).

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **Y** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **N** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | **Y** |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **Y** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | **N** |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **Y** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | **N** |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **N** |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **N** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **Y** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **N** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **N** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | **N** |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **N** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | N/A |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **N** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **Y** |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **Y** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **Y** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **Y** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **Y** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | **Y** |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **Y** |

If a connector supports derived fields, it also supports row-level expressions.

For more information, see:

* [Activate Admin-Defined Functions](#activate-admin-defined-functions)
* [Admin-Defined Function JSON Files](#admin-defined-function-json-files)

<h2 id="activate-admin-defined-functions">
  Activate Admin-Defined Functions
</h2>

**Activate an admin-defined function in Self-Service Analytics**

1. Create a JSON file containing your admin-defined function definitions. This JSON file should reside on the same machine as the connector server. The recommended location for this JSON file is `/etc/zoomdata` (for example, `/etc/zoomdata/edc-impala-functions.json`). See [Admin-Defined Function JSON Files](#admin-defined-function-json-files) for more information about creating this JSON file.

2. Update the connector server configuration so the connector knows where to find the file containing the admin-defined functions you have created. Complete these steps:

   1. Locate and edit the properties file for the connector in the `/etc/zoomdata` directory. For example, the Impala properties file is called `edc-impala.properties`.

      ```bash theme={null}
      vi <property-file>
      ```

   2. Locate and update the `functions.template.json.path` property in the Functions section of the properties file. Supply the path to the JSON file containing your admin-defined functions in the property. In the following example, the path for the `edc-impala-functions.json` file is specified.

      ```properties theme={null}
      functions.template.json.path=/etc/zoomdata/edc-impala-functions.json
      ```

      All admin-defined functions for a connector should be defined in the same JSON file, so only one path is needed per data source.

   3. Save the properties file.

3. Restart the connector server.

The connector reads and validates the JSON file only at startup. When you restart the connector, it loads the admin-defined function JSON file and will validate the function definitions in the file. Errors are logged if they are found. If the function definitions are valid, the connector starts successfully and writes a list of the loaded admin-defined functions to the log.

<h2 id="admin-defined-function-json-files">
  Admin-Defined Function JSON Files
</h2>

Use a single JSON file to define all the admin-defined functions for a single connector. Store this JSON file in the appropriate location for your environment.

* Linux: `/etc/zoomdata`. As an example, `/etc/zoomdata/edc-impala-functions.json`.
* Windows: `<install-path>/conf-modify`. As an example, `<install-path>/conf-modify/edc-impala-functions.json`.

This topic covers the following information:

* [JSON File Structure](#json-file-structure)
* [Validating Your JSON File](#validating-your-json-file)
* [Example](#example)

<h3 id="json-file-structure">
  JSON File Structure
</h3>

The basic structure of an admin-defined function in the JSON file is shown below. Each section is described.

```json theme={null}
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
```

#### function

The function name is the identifier used for the row-level admin-defined function. This name is displayed in the UI. The function name must start with a letter or an underscore and can contain letters, underscores, numbers, and periods.

#### template

The template defines the SQL string that will be used in the SQL query to a data source. You are fully responsible for the validity of the template string. Self-Service Analytics cannot fully validate it.

The template references arguments defined later in the JSON file. The arguments are surrounded by braces (curly braces) and are replaced by their SQL representations at run time. Self-Service Analytics does validate missing arguments when the connector associated with this JSON file starts.

You can use a backslash (`\`) as an escape character. It can be used to escape the following three characters: `\ { }` anywhere in the SQL template string (including inside the argument placeholders).

Here is an example:

```yaml theme={null}
"template": "({arg_0}) + ({arg_1}) * interval '1 year'”
```

#### returnType

There are three possible returnTypes: `simple`, `generic`, and `array`. The returnType used for the whole function must be `simple` or `generic`; the `array` returnType is not supported for the whole function. However, all three returnTypes are supported in the arguments defined within an admin-defined function.

Each returnType in the JSON provides a type specification and a name.

simple returnTypes

Five simple returnTypes are supported : NUMBER, INTEGER, STRING, DATE, or BOOLEAN. Here is an example of a simple returnType:

```yaml theme={null}
"returnType": {
    "type": "simple",
    "name": "DATE"
}
```

generic returnTypes

A generic returnType is an abstract type that is given a name. Here is an example of a generic returnType:

```yaml theme={null}
"returnType": {
    "type": "generic",
    "name": "T"
}
```

The specified name is the name used for the returnType inference. The only restriction is that the function's generic returnType name must be the same as one of the argument types. This is required to infer a function returnType based on an argument type.

array returnTypes

An array returnType includes a baseType that can be used only for the last argument. The baseType can only be `simple` or `generic`. Here is an example:

```yaml theme={null}
"returnType": {
    "type": "array",
    "baseType": {
        "type": "simple",
        "name": "STRING"
    }
}
```

#### arguments

The arguments section defines the argument keys and definitions. You do not have to specify an arguments section if there are no arguments. The argument keys are used in the SQL template string at the beginning of the function definition.

An argument definition consists of a name, a returnType, and description. The name and description are used to display the argument in the UI. The returnType is used for argument type validation and function returnType inference. The argument returnType can be `simple`, `generic` or `array`.

#### description

The description is an optional string you can specify to describe a function or an argument in the JSON file and in the UI.

<h3 id="validating-your-json-file">
  Validating Your JSON File
</h3>

You can validate your JSON against a JSON schema file `functions-schema.json` that Self-Service Analytics provides in the appropriate directory for your environment.

* Linux: `/opt/zoomdata/docs/<edc-connector>`. For example, the Impala JSON schema is in `/opt/zoomdata/docs/edc-impala/functions-schema.json`.
* Windows: `<install-path>/docs/<edc-connector>`. For example, the Impala JSON schema is in `<install-path>/docs/edc-impala/functions-schema.json`.

**Validate your JSON file against the JSON schema**

1. Link to the JSON Schema Validator at [https://www.jsonschemavalidator.net/](https://www.jsonschemavalidator.net/).
2. Copy the schema found in the JSON schema file for your connector (see above) to the left side of the JSON Schema Validator screen.
3. Copy your JSON file admin-defined function definitions in the **Input JSON** section on the right side of the JSON Schema Validator screen.

Any schema errors will be identified immediately on the screen.

<h3 id="example">
  Example
</h3>

In the following JSON file, two admin-defined functions, `TEST_ADD` and `TEST_ADD_YEAR`, are defined.

<Note>
  Before using this example, be sure to remove the comments. Comments are not allowed in JSON.
</Note>

```json theme={null}
{

  "TEST_ADD": { //Function name
    "template": "{summand_1} + {summand_2}", //SQL template string
    "returnType": { //Return type of the function
	  "type": "simple",
	  "name": "NUMBER"
    },
    "arguments": { // List of arguments
	  "summand_1": { //Argument key used for lookup in SQL template string
	    "name": "Summand 1", //Argument name, will be displayed on Derived Field Editor
	    "returnType": { // Type of argument.
	      "type": "simple",
	      "name": "NUMBER"
        },
	    "description": "An expression evaluated to a numeric value." //Argument description
	  },
	  "summand_2": {
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
  "TEST_ADD_YEAR": {
    "template": "({0}) + ({1}) * interval '1 year'",
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
```
