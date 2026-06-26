---
title: ".NET Plug-in - Writing Your Plug-in"
id: 4419707431703
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707431703--NET-Plug-in-Writing-Your-Plug-in
updated_at: 2022-07-17T01:56:03Z
---

# .NET Plug-in - Writing Your Plug-in

# .NET Plug-in - Writing Your Plug-in

Plug-ins written for Logi .NET applications are compiled into Dynamic Link Library (.DLL) files. In the code, the **System.Web** and **System.XML.Linq** .NET *namespaces* are referenced for interactions with Logi applications and report definitions. Namespaces are collections of classes with methods for doing things with specific kinds of data or objects. You import or include them in your plug-in project.

For example, System.Web is needed to access *HTTP Request* and *Session* objects, which are often useful in a plug-in.

Logi definitions and data are handled as XML streams during processing by the web server and therefore by your plug-in, too. Much of your code will be concerned with searching, parsing, and modifying this XML. The System.XML.Linq namespace provides useful methods for doing this. If you're familiar with XPath notation, you'll find that to be very helpful as well.

## Create your plug-in project in Visual Studio:

1. Create a new Class Library project, using C#, Visual Basic, or other language of your choice.
2. Configure the project to build the .DLL output in the \_Plugins folder of the Logi application (which you may need to create). The folder's name *must* be "\_Plugins", beginning with an underscore.
3. Add a reference to the System.Web and System.XML.Linq .NET namespaces. Both may not be needed, depending on what you do in the plug-in, but you can refine that later.
4. Add a reference to the file *yourLogiApp*/bin/rdPlugin.dll distributed with your Logi product.  A "strongly-signed" plug-in can be created by referencing *yourLogiApp*/bin/rdPluginSigned.dll *![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) Be sure* to use the file found in the bin folder of the Logi application that will use this plug-in. It's version-specific so don't refer to it in the bin folder of some other Logi application.

5. Write your plug-in code, starting with this prototype:

[Visual Basic]  
Imports System.Xml.Linq  
Imports System.Web Public Class Plugin  
 Public Sub yourMethodName(ByRef yourObjName As rdPlugin.rdServerObjects)  
' your method code goes here  
 End Sub  
End Class  
[C#]  
using System;  
 using System.Xml.Linq;  
using System.Web;  
 using rdPlugin;  
  
 namespace myPlugin  
{  
 public class Plugin  
 {  
 public void yourMethodName(ref rdPlugin.rdServerObjects yourObjName)  
 {  
 // your method code goes here  
 }  
 }  
 }

Add the methods and code you need to get the plug-in to do whatever it's supposed to do.
