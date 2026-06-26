---
title: "Java Plug-in - Example: Modify a SQL Query with a Request Variable"
id: 4406822211351
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822211351-Java-Plug-in-Example-Modify-a-SQL-Query-with-a-Request-Variable
updated_at: 2022-04-06T06:04:44Z
---

# Java Plug-in - Example: Modify a SQL Query with a Request Variable

# Java Plug-in - Example: Modify a SQL Query with a Request Variable

The following are code examples for a plug-in that customizes a SQL query based on a request variable:

import org.w3c.dom.\*;  
import org.w3c.dom.Document;  
import javax.servlet.\*;  
import javax.servlet.http.\*;  
import java.util.\*;  
import java.util.Hashtable;  
import com.logixml.plugins.LogiPluginObjects10;import java.io.\*;  
import java.io.File;  
import javax.xml.transform.\*;  
import javax.xml.transform.dom.\*;  
import javax.xml.transform.stream.\*;  
import javax.xml.transform.OutputKeys;  
import com.sun.net.httpserver.HttpContext;  
public class myPlugin  
{  
 public void SetCustomerQuery(LogiPluginObjects10 rdObjects)  
{  
try  
 {  
DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();  
DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();  
byte b[] = rdObjects.getCurrentDefinition().getBytes();  
java.io.ByteArrayInputStream input = new java.io.ByteArrayInputStream(b);  
Document xmlDefinition = docBuilder.parse(input);  
NodeList nl = xmlDefinition.getElementsByTagName("DataLayer");  
if (nl.getLength() == 0)  
{  
throw new Exception("The report is missing the DataLayer element.");  
}//Use a Request variable to set set the SELECT query.  
int iPos = rdObjects.getRequestParameterNames().indexOf((Object)"Continent");  
if (iPos < 0)  
 {   
 throw new Exception("Continent Parameter name not found in SetCustomerQuery ");  
 }String sContinent = (String)rdObjects.getRequestParameterValues().get(iPos);  
String sSelect = new String();  
if (sContinent == null)  
{  
sSelect = "SELECT \* FROM Customers";  
}  
else  
{  
if (sContinent.equals("NA"))  
 {  
 sSelect = "SELECT \* FROM Customers WHERE Country IN('USA','Mexico','Canada')";   
 }  
else  
{  
if (sContinent.equals("SA"))  
 {   
 sSelect = "SELECT \* FROM Customers WHERE Country IN ('Argentina','Brazil','Venezuela')";  
 }  
else  
{  
if (sContinent.equals("EU"))  
 {   
 sSelect = "SELECT \* FROM Customers WHERE Country IN ('UK','Sweden','France','Spain','Switzerland','Austria',  
 'Portugal','Ireland','Belgium','Germany','Finland','Poland','Denmark')";  
 }  
 else  
 {  
sSelect = "SELECT \* FROM Customers";  
}  
}  
}  
}  
Node nodApp = nl.item(0);  
Element eleDataLayer = (Element)nodApp;  
eleDataLayer.setAttribute("Source", sSelect);  
rdObjects.setCurrentDefinition(getOuterXml(xmlDefinition));  
}  
catch (Exception ex)  
{  
ex.printStackTrace();  
System.out.println("SetCustomerQuery Error " + ex.getMessage());  
}  
}
