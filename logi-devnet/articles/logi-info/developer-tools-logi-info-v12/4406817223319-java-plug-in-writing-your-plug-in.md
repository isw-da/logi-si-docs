---
title: "Java Plug-in - Writing Your Plug-in"
id: 4406817223319
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817223319-Java-Plug-in-Writing-Your-Plug-in
updated_at: 2022-04-06T06:04:44Z
---

# Java Plug-in - Writing Your Plug-in

# Java Plug-in - Writing Your Plug-in

Plug-ins written for Logi applications on Java platforms are included as either standalone .class files, in the Logi application's WEB-INF/classes folder, or as a class file within a .jar file in the Logi application's WEB-INF/lib
folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Many copies of the files that define the LogiPluginObjects and LogiPluginObjects10 classes, LogiPluginObjects.java and LogiPluginObjects10.java, may exist on your hard drive if you're working with multiple Logi applications. To ensure version compatibility,
be sure to
use the
file found in the folders of the Logi application that will use the plug-in you're creating.

Logi definitions and data are handled as XML streams during processing by the web server and therefore by your plug-in, too. Much of your code will be concerned with searching, parsing, and modifying this XML. If you're familiar with XPath notation, you'll find that to be very helpful as well.

## Create your plug-in project in Eclipse

Here's an example of the steps needed to create a plug-in using the popular Eclipse IDE:

1. Create a standard Java Project. The Project Name is inconsequential if you're compiling to a single class file. The version of the JDK used in the plug-in project should match the JDK version used to run the Logi application on your web server.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417584072855/createpluginjava_04.png)
2. Add the necessary source code files and library references to your project. For example, to create our Plug-in (Java) sample application, we added the files shown above. You *must* include these two Logi files:

*yourLogiApp*/WEB-INF/lib/PluginCaller.jar  
*yourLogiApp*/WEB-INF/lib/rdPlugin.jar
We also had to include the other references to several .jar files to satisfy the requirements of our sample code.

3. Eclipse requires that the project output be placed within the project folder. Once created, you'll need to copy it to either:

yourLogiApp/WEB-INF/classes (.class file) - or -   
yourLogiApp/WEB-INF/lib (.jar file)  

4. Write your plug-in code, starting with this prototype:

import org.w3c.dom.\*;  
import org.w3c.dom.Document;  
import javax.servlet.\*;  
import javax.servlet.http.\*;  
import java.util.\*;  
import java.util.Hashtable;  
import com.logixml.plugins.LogiPluginObjects10;  
  
public class myPlugin  
{  
 public void yourMethodName(LogiPluginObjects10 rdObjects)  
{  
/\* your method code goes here \*/  
 }  
}

Add the methods and code you need to get the plug-in to do whatever it's supposed to do.
