---
title: "Use the Python Connector"
id: 43701044889485
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044889485-Use-the-Python-Connector
updated_at: 2026-05-29T14:07:53Z
---

# Use the Python Connector

# Use the Python Connector

You can use the Python connector using arbitrary Python scripts as connection parameter.

**Important:** 
The Python connector functions in raw data mode only and does not support push down of aggregations. Minimize the amount of data in your request using filter operations. This will increase performance speed and improve loading time for dashboards and visuals.

## Python Script Conventions

Data sources are resolved from Python script using the following conventions:

* Each function definition is a separate data source
* Private functions (that start with an underscore `_`) are not resolved as a data source

Conventions for return values of functions include:

* [Pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) dataframes.
* Dictionaries: The key is a string (column name) and values a list: `return {"column1": [1, 2, 3], "column2": ["one", "two", "three"]}`.
* List of dictionaries: return `[{"column1": 1, "column2": "one"}, {"column1": 2, "column2": "two"}]`.
* List of lists: `return [[1, 2], [3, 4]]`. Each enclosed list resolves as a row.
* List: `return [1, 2, 3, 4]`. Resolves as a single column with index 1.
* Single value of any of supported types: `return 1` OR `return decimal.Decimal("3.14")`

Regardless of return type, you must use uniform columns of the same size, containing the same value type, to prevent unexpected behavior.

### Conversion Values

The connector applies the following rules when reading values:

| Python Type | Connector Field Type |
| --- | --- |
| str | STRING |
| int | INTEGER |
| float | DOUBLE |
| decimal.Decimal | DOUBLE |
| datetime.date | DATE |
| datetime.datetime | DATE |
| arbitray object | STRING |

## Python Script Writing Tips

Avoid using top level statements

Top level statement are executed in a single thread for all users. You can add function calls in a top level statement to validate a connection, but don't call functions when you save your script. See [How the Connector Works](#How).

Avoid overriding internal names

Python is used within your environment to invoke data source functions and convert data. Since this code is executed in the same namespace as your scripts, if you try to override the names listed below, you may receive unexpected results. Avoid using the following names in your code:

* `__convert`
* `__convert_list_of_dicts_to_dict_of_lists`
* `f`
* `__fork`
* `__emulate`
* `all_functions`

To use this connector, we import these modules. Attempting to use these names for variables and functions may return unexpected results.

* `pandas`
* `numbers`
* `datetime`
* `multiprocessing`
* `queue`
* `inspect`
* `types`

Your python script has limited access to the file system; the container is run as a non-root user. Edit access is still available on the folders below:

Folders with write access include:

* `/opt/zoomdata/logs`
* `/opt/zoomdata/temp`
* `/opt/zoomdata/lib`
* `/opt/zoomdata/wrappers`

## How the Connector Works

Python code is executed using [JEP](https://github.com/ninia/jep) to interpret Python code in the same process where the Java app is running. To circumvent some Global Interpreter Lock issues in Python, some queries use [processed based parallelism](https://docs.python.org/3/library/multiprocessing.html). Based on the request type, the connector functions in one of two ways:

* Interpret the script in the same process for validation and describe requests.
* Interpret the script in the same process and invoke the function in a sub process for fetch data requests.

New sub processes are created by [forking](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods) the Java process. Each request starts a new Python interpreter. Scripts are always interpreted first in one parent process. Limit top level statements to imports and function definitions for optimal performance.

Function invocation happens in a separate process, so global variables aren't available. For example:

x = 40
def side\_effect():
x = x + 1
return {"result": [x]}

While the script is valid, using it as a connection parameter and attempting to set `side_effect` as an entity for the source will return an error such as:

UnboundLocalError: local variable 'x' referenced before assignment

## Logging

Outputs of your Python scripts are not preserved. Statements such as `print("Message")` to write data to `stdout` or `stderr` will not be retained.

## Python Script Conversion

Python script types conversion converts all values returned from public functions to [Pandas Dataframe](https://pandas.pydata.org/docs/reference/frame.html "Pandas dataframe link"). To resolve the type, the connector relies on [DataFrame.dtypes.kind](https://numpy.org/doc/stable/reference/generated/numpy.dtype.kind.html#numpy.dtype.kind "DataFrame.dtypes.kind link").

The following table includes the conversion rules used:

| Numpy kind (character code) | Numpy kind (type name) | Field Type |
| --- | --- | --- |
| b | boolean | STRING |
| i | signed integer | INTEGER |
| u | unsigned integer | INTEGER |
| f | floating-point | DOUBLE |
| c | complex floating-point | STRING |
| m | timedelta | STRING |
| M | datetime | DATE |
| O | object | STRING |
| S | (byte-)string | STRING |
| U | Unicode | STRING |
