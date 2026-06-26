---
title: "Replace Characters in String (JAVA)"
id: 360047205694
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047205694-Replace-Characters-in-String-JAVA
updated_at: 2022-02-07T21:49:44Z
---

# Replace Characters in String (JAVA)

## **Plugin Description**

This Java plug-in is designed to provide a generic means to modify/replace sections of the resultant HTML using regular expressions and the FinishHTML event.

It was created to enable to the modification of Google Maps calls to support v3 of the Google Maps API in the current release of the Logi Info engine. However, its generic implementation will allow any string to be replaced within the resultant HTML. The download includes the .jar file, Java source code, and an example report definition.

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## **View Code Snippet**

```
import java.util.logging.Logger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Plugin {
	// Debug logger
	private final Logger logDebug = Logger.getLogger("ReplaceStringPlugin");

	public void StrReplace (LogiPluginObjects lgxobjects)
	{
		try {
			String html = lgxobjects.getResponseHtml();
			String currUrl = lgxobjects.getPluginParameters().get("current").toString();
			String replaceUrl = lgxobjects.getPluginParameters().get("replace").toString();
			
			Pattern p = Pattern.compile(currUrl, Pattern.CASE_INSENSITIVE);
			Matcher m = p.matcher(html);
			html = m.replaceAll(replaceUrl);
			//html.replaceAll(currUrl,replaceUrl);
			lgxobjects.setResponseHtml(html);
		}
		catch (Exception e ) {
			logDebug.severe(e.getMessage());
		}
	}
}
```

## 

## **Further Reading**

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
