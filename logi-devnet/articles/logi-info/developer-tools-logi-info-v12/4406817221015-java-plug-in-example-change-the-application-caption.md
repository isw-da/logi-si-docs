---
title: "Java Plug-in - Example: Change the Application Caption"
id: 4406817221015
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817221015-Java-Plug-in-Example-Change-the-Application-Caption
updated_at: 2022-04-06T06:04:43Z
---

# Java Plug-in - Example: Change the Application Caption

# Java Plug-in - Example: Change the Application Caption

The following are code examples for a plug-in that alters the caption of the Logi application at runtime:

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
 public void SetApplicationCaption(LogiPluginObjects10 rdObjects)  
{  
 try  
{  
 DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();  
DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder);  
byte b[] = rdObjects.getCurrentDefinition().getBytes();  
java.io.ByteArrayInputStream input = new java.io.ByteArrayInputStream(b);  
Document xmlSettings = docBuilder.parse(input);  
NodeList nl = xmlSettings.getElementsByTagName("Application");  
if (nl.getLength() > 0)  
 {  
 Node nodApp = nl.item(0);  
Element eleApp = (Element)nodApp;  
eleApp.setAttribute("Caption", "Greetings from the Sample Plugin!");  
rdObjects.setCurrentDefinition(getOuterXml(xmlSettings));  
 }  
}  
catch (Exception ex)  
{  
ex.printStackTrace();  
System.out.println("SetApplicationCaption Error " + ex.getMessage());  
}  
 }  
}
