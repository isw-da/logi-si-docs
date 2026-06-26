---
title: "Flattener Attributes "
id: 4419707594135
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707594135-Flattener-Attributes
updated_at: 2022-07-17T01:48:52Z
---

# Flattener Attributes 

# Flattener Attributes

The attributes of the Flattener element are described below:

| Attribute | Description |
| --- | --- |
| Bottom Level Element Names | Specifies one or more names of elements in the input data, in a comma-separated list, where the flattening operation should end. Any elements in this list will not have any of their children processed. The default (no value) causes flattening to end at the lowest child level. |
| Data Row Element Names | Specifies one or more names of elements in the input data, in a comma-separated list, which should generate output data rows. If left blank, an output data row is produced for each child element of the root element. |
| ID | Specifies a unique element ID. |
| Ignore Deep Attributes | Specifies whether all attributes of the elements that generate data rows will be added to the output, even attributes from lower-level child elements. When set to *True*, those lower-level attributes are *not* copied. The default (blank) value is *False*. |
| Ignore Text Elements | Specifies whether text nodes (elements) are moved into attributes of their parent element. When set to *True*, text nodes are *not* moved. The default (blank) value is *False*. |
| Prepend Element Names | Specifies whether the element name should be prepended to the attribute when it's flattened. For example, if set to *True* (the default value), <parent child="x" /> will be output as <datalayerid parent\_child="x" />. If set to *False*, it would be output as <datalayerid child="x" />. |
| Top Level XPath | Specifies an XPath query to be used to select the portion of the dataset to be flattened. The default value is *\**, which selects the entire dataset. |

The effects of some of these attributes on data are shown in [Flattener Usage Examples](https://devnet.logianalytics.com/hc/en-us/articles/4419715301015-Flattener-Usage-Examples).
