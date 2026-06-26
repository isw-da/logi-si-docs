---
title: "Flattener Usage Examples"
id: 4406822337687
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822337687-Flattener-Usage-Examples
updated_at: 2022-04-06T06:06:15Z
---

# Flattener Usage Examples

# Flattener Usage Examples

Here are some simple examples of the Flattener's effects.

<Library commonName="Library of Congress">  
 <Book ID="B1" />  
 <Book ID="B2">  
 <Category name="Fiction" />  
 <Category name="Mystery" />  
 <PublishDate year="1900" />  
 <Author>John
Doe</Author>  
 </Book>  
 <Book ID="3" >  
 <Category name="Nonfiction" />  
 </Book>  
 <Video ID="V1" />  
</Library>

The data shown above is the hierarchical input data for the following examples.

<dataLayer rdFlattenedElement="Book" ID="B1" />  
<dataLayer rdFlattenedElement="Book" ID="B2" Author="John Doe"/>  
<dataLayer rdFlattenedElement="Book" ID="B3" />

1. In this simple example, *no* Flattener element attributes are set and it transposes the data into the tabular layout shown above. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Text node elements are treated the same way as attributes.

<dataLayer rdFlattenedElement="Book" commonName="Library of Congress" ID="B1" />  
<dataLayer rdFlattenedElement="Book" commonName="Library of Congress" ID="B2" name="Mystery" year="1900" Author="John Doe" />  
<dataLayer rdFlattenedElement="Book" commonName="Library of Congress" ID="B3" name="Nonfiction" />

2. Using the same input data, the example above shows the flattened data created by specifying these Flattener element attributes:

Data Row Element Names = *Book*  
Top Level XPath = *//Library*

<dataLayer rdFlattenedElement="Book" Library\_commonName="Library of Congress" Book\_ID="B1" />  
<dataLayer rdFlattenedElement="Book" Library\_commonName="Library of Congress" Book\_ID="B2" Category\_name="Mystery" PublishDate\_year="1900" Book\_Author="John Doe" />  
<dataLayer rdFlattenedElement="Book" Library\_commonName="Library of Congress" Book\_ID="B3" Category\_name="Nonfiction" />  
<dataLayer rdFlattenedElement="Video" Library\_commonName="Library of Congress" Video\_ID="V1 />

3. Using the same input data, the example above shows the flattened data created by specifying these Flattener element attributes:   
Data Row Element Names = *Book,Video*  
Prepend Element Names = *True*  
Top Level XPath = *//Library*

<dataLayer rdFlattenedElement="Book" ID="B2" name="Fiction" Author="dave was here" />  
<dataLayer rdFlattenedElement="Book" ID="B2" name="Mystery" Author="dave was here" />  
<dataLayer rdFlattenedElement="Book" ID="B2" year="1900" Author="dave was here" />  
<dataLayer rdFlattenedElement="Book" ID="B3" name="Nonfiction" />

4. Using the same input data, the example above shows the flattened data created by specifying these Flattener element attributes:   
Data Row Element Names = *Category,PublishDate*  
Prepend Element Names = *True*  
Top Level XPath = *//Library*
