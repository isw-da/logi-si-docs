---
title: "General Java Routines"
id: 360047205614
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047205614-General-Java-Routines
updated_at: 2022-02-07T21:50:24Z
---

# General Java Routines

## **Plugin Description**

This sample plug-in illustrates many of the techniques used with a Java plug-in, including:

* Setting an application caption
* Modifying a SQL query
* Adding a column of data to a datalayer
* Getting the system virtual memory size

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## **View Code Snippet**

```
import java.io.File;
import java.util.Hashtable;
import org.w3c.dom.Document;
import org.w3c.dom.*;

import javax.servlet.*;
import javax.servlet.http.*;
import java.util.*;

import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
import javax.xml.transform.*;
import javax.xml.transform.dom.*;
import javax.xml.transform.stream.*;
import java.io.*;
import com.sun.net.httpserver.HttpContext;
import javax.servlet.http.*;
import javax.xml.transform.OutputKeys;

/**   
 *  <B> Plugins for Logi Info Server Java </B>
 * 
 *   This sample plugin class is provided to assist customers in the creation of their own custom plugins.
 *   This works with the sample plugin reports provided with Logi Info Studio.These reports must have a 
 *   single parameter; LogiPluginObjects.  Return information back to a report by changing values in 
 *   LogiPluginObjects, such as the CurrentDefinition, or Session variables. The full list is documented 
 *   in LogiPluginObjects. All plugin classes must be installed in the application WEB-INF\classes 
 *   directory. Debugging is dependent on whatever Java application tools you have available. 
 */

public class SamplePlugin
{

	public void SetApplicationCaption(LogiPluginObjects rdObjects)
	{
		try
		{
			DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
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

	public void SetCustomerQuery(LogiPluginObjects rdObjects)
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
			}

			//Use a Request variable to set set the SELECT query.
			//javax.servlet.http.HttpServletRequest hsRequest = rdObjects.getRequest();
			//String sContinent = hsRequest.getParameter("Continent");
			int iPos = rdObjects.getRequestParameterNames().indexOf((Object)"Continent");
			if (iPos < 0) { throw new Exception("Continent Parameter name not found in SetCustomerQuery "); }
			String sContinent = (String)rdObjects.getRequestParameterValues().get(iPos);

			String sSelect = new String();
			if (sContinent == null)
			{
				sSelect = "SELECT * FROM Customers";
			}
			else
			{
				if (sContinent.equals("NA")) { sSelect = "SELECT * FROM Customers WHERE Country IN('USA','Mexico','Canada')"; }
				else
				{
					if (sContinent.equals("SA")) { sSelect = "SELECT * FROM Customers WHERE Country IN('Argentina','Brazil','Venezuela')"; }
					else
					{
						if (sContinent.equals("EU")) { sSelect = "SELECT * FROM Customers WHERE Country IN('UK','Sweden','France','Spain','Switzerland','Austria','Portugal','Ireland','Belgium','Germany','Finland','Poland','Denmark')"; }
						else
						{
							sSelect = "SELECT * FROM Customers";
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

	public void GetProducts(LogiPluginObjects rdObjects)
	{
		try
		{
			String sReturnFile = null;
			Document xmlData;
			if (rdObjects.getCurrentData() != null)
			{
				xmlData = rdObjects.getCurrentData();
			}
			else
			{
				if (rdObjects.getCurrentDataFile() != null)
				{
					File xmlFile = new File(rdObjects.getCurrentDataFile());
					if (xmlFile.exists())
					{
						DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
						DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
						xmlData = docBuilder.parse(xmlFile);
						sReturnFile = rdObjects.getReturnedDataFile();
					}
					else
					{
						throw new Exception("Referenced XML file does not exist in GetProducts plugin method. " + rdObjects.getCurrentDataFile());
					}
				}
				else
				{
					throw new Exception("No XML data was passed to the GetProducts plugin method.");
				}
			}

			//xmlData.getDocumentElement ().normalize ();
			Hashtable ht = rdObjects.getPluginParameters();
			String sDataLayerParentID = (String)ht.get("DataLayerParentID");

			Element eleMilk = xmlData.createElement(sDataLayerParentID);
			eleMilk.setAttribute("ProductName", "Milk");
			xmlData.getDocumentElement().appendChild((Node)eleMilk);

			Element eleBread = xmlData.createElement(sDataLayerParentID);
			eleBread.setAttribute("ProductName", "Bread");
			xmlData.getDocumentElement().appendChild((Node)eleBread);

			Element eleBeer = xmlData.createElement(sDataLayerParentID);
			eleBeer.setAttribute("ProductName", "Beer");
			xmlData.getDocumentElement().appendChild((Node)eleBeer);

			if (sReturnFile != null)
			{
				//If we got the data by filename, we need to return the updated file.
				File xmlOutFile = new File(sReturnFile);
				// Use a Transformer for output
				TransformerFactory tFactory = TransformerFactory.newInstance();
				Transformer transformer = tFactory.newTransformer();
				DOMSource source = new DOMSource(xmlData);
				StreamResult result = new StreamResult(xmlOutFile);
				transformer.transform(source, result);
			}

		}
		catch (TransformerConfigurationException tce)
		{
			tce.printStackTrace();
			System.out.println("Transformer Factory error in GetProducts " + tce.getMessage());
		}
		catch (TransformerException te)
		{
			te.printStackTrace();
			System.out.println("Transformation error in GetProducts " + te.getMessage());
		}
		catch (SAXParseException spe)
		{
			// Error generated by the parser
			spe.printStackTrace();
			System.out.println("SAX parsing error in GetProducts " + spe.getMessage());
		}
		catch (Exception ex)
		{
			ex.printStackTrace();
			System.out.println("GetProducts Error " + ex.getMessage());
		}
	}

	public void AddPriceColumn(LogiPluginObjects rdObjects)
	{
		try
		{
			String sReturnFile = null;
			Document xmlData;
			if (rdObjects.getCurrentData() != null)
			{
				xmlData = rdObjects.getCurrentData();
			}
			else
			{
				if (rdObjects.getCurrentDataFile() != null) {
					File xmlFile = new File(rdObjects.getCurrentDataFile());
					if (xmlFile.exists())
					{
						DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
						DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
						xmlData = docBuilder.parse(xmlFile);
						sReturnFile = rdObjects.getReturnedDataFile();
					}
					else
					{
						throw new Exception("Referenced XML file does not exist in AddPriceColumn plugin method. " + rdObjects.getCurrentDataFile());
					}
				}
				else
				{
					throw new Exception("No XML data was passed to the GetProducts plugin method.");
				}
			}

			Hashtable ht = rdObjects.getPluginParameters();
			String sColumnName = (String)ht.get("PriceColumnName");

			NodeList rdDataNodeList = xmlData.getElementsByTagName("rdData");
			for (int i = 0; i < rdDataNodeList.getLength(); i++)
			{
				Node nodeApp = rdDataNodeList.item(i);
				NodeList productsNodeList = xmlData.getElementsByTagName("dtProductsFromPlugin");
				for (int j = 0; j < productsNodeList.getLength(); j++)
				{
					Node prodApp = productsNodeList.item(j);
					Element eleRow = (Element)prodApp;
					//eleRow.get
					String sProductName = eleRow.getAttribute("ProductName");
					if (sProductName != null)
					{
						if (sProductName.equals("Milk")) { eleRow.setAttribute(sColumnName, "3.25"); }
						else
						{
							if (sProductName.equals("Bread")) { eleRow.setAttribute(sColumnName, "3.75"); }
							else
							{
								if (sProductName.equals("Beer")) { eleRow.setAttribute(sColumnName, "4.50"); }
								else
								{
									System.out.println("Product name not found " + sProductName);
								}
							}
						}
					}
				}
			}
			if (sReturnFile != null)
			{
				//If we got the data by filename, we need to return the updated file.
				File xmlOutFile = new File(sReturnFile);
				// Use a Transformer for output
				TransformerFactory tFactory = TransformerFactory.newInstance();
				Transformer transformer = tFactory.newTransformer();
				DOMSource source = new DOMSource(xmlData);
				StreamResult result = new StreamResult(xmlOutFile);
				transformer.transform(source, result);
			}
		}
		catch (TransformerConfigurationException tce)
		{
			tce.printStackTrace();
			System.out.println("Transformer Factory error in AddPriceColumn " + tce.getMessage());
		}
		catch (TransformerException te)
		{
			te.printStackTrace();
			System.out.println("Transformation error in AddPriceColumn " + te.getMessage());
		}
		catch (SAXParseException spe)
		{
			// Error generated by the parser
			spe.printStackTrace();
			System.out.println("SAX parsing error in AddPriceColumn " + spe.getMessage());
		}
		catch (Exception ex)
		{
			ex.printStackTrace();
			System.out.println("AddPriceColumns " + ex.getMessage());
		}
	}

	public void SetDataTableColumns(LogiPluginObjects rdObjects)
	{
		try
		{
			Hashtable ht = rdObjects.getPluginParameters();
			String sDataTableID = (String)ht.get("DataTableID");
			DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
			byte b[] = rdObjects.getCurrentDefinition().getBytes();
			java.io.ByteArrayInputStream input = new java.io.ByteArrayInputStream(b);
			Document xmlDefinition = docBuilder.parse(input);
			NodeList nlDataTableList = xmlDefinition.getElementsByTagName("DataTable");
			Element eleDataTable = (Element)nlDataTableList.item(0);
			if (!eleDataTable.getAttribute("ID").equals(sDataTableID))
			{
				for (int i = 1; i < nlDataTableList.getLength(); i++)
				{
					eleDataTable = (Element)nlDataTableList.item(i);
					if (eleDataTable.getAttribute("ID").equals(sDataTableID))
					{
						break;
					}
				}
			}

			String sReturnFile = null;
			Document xmlData;
			if (rdObjects.getCurrentData() != null)
			{
				xmlData = rdObjects.getCurrentData();
			}
			else
			{
				if (rdObjects.getCurrentDataFile() != null)
				{
					File xmlFile = new File(rdObjects.getCurrentDataFile());
					if (xmlFile.exists())
					{
						//DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
						//DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
						xmlData = docBuilder.parse(xmlFile);
						sReturnFile = rdObjects.getReturnedDataFile();
					}
					else
					{
						throw new Exception("Referenced XML file does not exist in SetDataTableColumns plugin method. " + rdObjects.getCurrentDataFile());
					}
				}
				else
				{
					throw new Exception("No XML data was passed to the GetProducts plugin method.");
				}
			}

			NodeList nlRdData = xmlData.getElementsByTagName("LocalData");
			if (nlRdData.getLength() > 0)
			{
				Node nodApp = nlRdData.item(0);
				NamedNodeMap nnm = nodApp.getAttributes();
				for (int i = 0; i < nnm.getLength(); i++)
				{
					Node atrNode = nnm.item(i);
					Attr atr = (Attr)atrNode;

					//Create a new DataTableColumn element under the DataTable.
					Element eleDataTableColumn = xmlDefinition.createElement("DataTableColumn");
					eleDataTableColumn.setAttribute("ID", "col" + atr.getName());
					eleDataTableColumn.setAttribute("Header", atr.getName());
					eleDataTable.appendChild((Node)eleDataTableColumn);

					//Create the Label element
					Element eleLabel = xmlDefinition.createElement("Label");
					eleLabel.setAttribute("ID", "lbl" + atr.getName());
					eleLabel.setAttribute("Caption", "@Data." + atr.getName() + "~");
					eleDataTableColumn.appendChild((Node)eleLabel);

				}
			}
			else
			{
				System.out.println("No rdData tag found in XML " + nlRdData.getLength());
			}
			rdObjects.setCurrentDefinition(getOuterXml(xmlDefinition));
			if (sReturnFile != null)
			{
				//If we got the data by filename, we need to return the updated file.
				File xmlOutFile = new File(sReturnFile);
				// Use a Transformer for output
				TransformerFactory tFactory = TransformerFactory.newInstance();
				Transformer transformer = tFactory.newTransformer();
				DOMSource source = new DOMSource(xmlData);
				StreamResult result = new StreamResult(xmlOutFile);
				transformer.transform(source, result);
			}
		}
		catch (TransformerConfigurationException tce)
		{
			tce.printStackTrace();
			System.out.println("Transformer Factory error in SetDataTableColumns " + tce.getMessage());
		}
		catch (TransformerException te)
		{
			te.printStackTrace();
			System.out.println("Transformation error in SetDataTableColumns " + te.getMessage());
		}
		catch (SAXParseException spe)
		{
			// Error generated by the parser
			spe.printStackTrace();
			System.out.println("SAX parsing error in SetDataTableColumns " + spe.getMessage());
		}
		catch (Exception ex)
		{
			ex.printStackTrace();
			System.out.println("SetDataTableColumns Error " + ex.getMessage());
		}
	}

	public void subHighlightText(LogiPluginObjects rdObjects)
	{
		try
		{
			Hashtable htElement = rdObjects.getPluginParameters();
			String sElementID = (String)htElement.get("ElementID");
			Hashtable htName = rdObjects.getPluginParameters();
			Object oFindInputName = htName.get("FindInputName");
			if (oFindInputName == null) {throw new Exception("FindInputName missing in subHighlight text"); }
			Hashtable htStyle = rdObjects.getPluginParameters();
			String sStyle = (String)htStyle.get("Style");
			//javax.servlet.http.HttpServletRequest hsRequest = rdObjects.getRequest();
			//String sFindValue = hsRequest.getParameter(sFindInputName);
			int iPos = rdObjects.getRequestParameterNames().indexOf(oFindInputName);

			if (iPos < 0) { throw new Exception("Parameter name not found in subHighlightText " + oFindInputName.toString()); }
			String sFindValue = (String)rdObjects.getRequestParameterValues().get(iPos);
			if ((sFindValue != null) && (sFindValue.trim().length() != 0))
			{
				//Load the ResponsesHtml string into an XmlDocument object.
				DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
				DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
				byte b[] = rdObjects.getResponseHtml().getBytes();
				java.io.ByteArrayInputStream input = new java.io.ByteArrayInputStream(b);
				Document xmlHtml = docBuilder.parse(input);
				xmlHtml.normalize();

				//Find all SPAN elements under the element with the specified ElementID.
				NodeList nl = xmlHtml.getElementsByTagName("*");
				for (int i = 0; i < nl.getLength(); i++)
				{
					Node nod = nl.item(i);
					String nname = nod.getNodeName();
					Element ele = (Element)nod;
					String eleAttr = ele.getAttribute("id");
					if (eleAttr == null)
					{
						eleAttr = ele.getAttribute("ID");
					}
					String elename = ele.getTagName();
					if (eleAttr.equals(sElementID))
					{
						NodeList nlSpans = ele.getElementsByTagName("SPAN");
						int totalSpans = nlSpans.getLength();
						int spanCounter = 0;
						while (spanCounter < totalSpans)
						{
							Element eleSpanText = (Element)nlSpans.item(spanCounter);
							//Split the SPAN into 3 SPANs to highlight the first match.
							int newSpanCounter = subSplitHighlightSpan(xmlHtml, eleSpanText, sFindValue, sStyle, true, spanCounter);
							totalSpans = totalSpans + (newSpanCounter - spanCounter);
							spanCounter = newSpanCounter;
							spanCounter++;
						}
						rdObjects.setResponseHtml(getOuterXml(xmlHtml));
					}
				}
			}
		}
		catch (Exception ex)
		{
			//ex.printStackTrace();
			//System.out.println("subHighlightText Error " + ex.getMessage());
		}
	}

	private int subSplitHighlightSpan(Document xmlHtml, Element eleSpanText, String sFindValue, String sStyle, boolean firstPass, int spanCount)
	{
		try
		{
			Node nod = (Node)eleSpanText;
			NodeList nl = nod.getChildNodes();
			if (nl.getLength() == 0) { return spanCount; }
			Text txt = (Text)nl.item(0);
			String sNodeValue = txt.getNodeValue();
			if ((!firstPass) && (sNodeValue.toLowerCase().equals(sFindValue.toLowerCase()))) { return spanCount; } //Prevent false hit on recursive call

			if ((sNodeValue == null) || (sNodeValue.trim().length() == 0)) { return spanCount; }
			int nFindLocation = sNodeValue.toLowerCase().indexOf(sFindValue.toLowerCase());
			if (nFindLocation != -1)
			{
				//The search string was found.  Break the SPAN into 3 SPANs.
				//Set the first SPAN element.
				String lastChar = sNodeValue.substring(nFindLocation - 1, nFindLocation);
				if (lastChar.equals(" ")) lastChar = " "; else lastChar = "";
				txt.setNodeValue(sNodeValue.substring(0, nFindLocation) + lastChar);  //setNodeValue strips the end space so it is restored here.
				//Make the highlighted SPAN element.
				Element eleNewSpan = xmlHtml.createElement("SPAN");
				Text highlightTxt = xmlHtml.createTextNode(sNodeValue.substring(nFindLocation, nFindLocation + sFindValue.length()));
				eleNewSpan.appendChild(highlightTxt);
				eleSpanText.getParentNode().appendChild(eleNewSpan);
				eleNewSpan.setAttribute("style", sStyle);
				//Make the final SPAN element.
				Element eleNewSpanFinal = xmlHtml.createElement("SPAN");
				Text finalTxt = xmlHtml.createTextNode(sNodeValue.substring(nFindLocation + sFindValue.length()));
				eleNewSpanFinal.appendChild(finalTxt);
				eleSpanText.getParentNode().appendChild(eleNewSpanFinal);
				//eleNewSpan = (Element)nodApp;
				//Recursively call again with this last SPAN.  There may be more matches.
				spanCount = spanCount + 2;
				subSplitHighlightSpan(xmlHtml, eleNewSpan, sFindValue, sStyle, false, spanCount);
			}
			return spanCount;
		}
		catch (Exception ex)
		{
			ex.printStackTrace();
			System.out.println("subHighlightSpan Error " + ex.getMessage());
			return spanCount;
		}
	}

	//This actually returns the amount of memory used,
	public Object GetVirtualMemorySize(LogiPluginObjects rdObjects)
	{
		return (Object)(Runtime.getRuntime().maxMemory());
	}

	private String getOuterXml(Node node)
	{
		try
		{
			Transformer transformer = TransformerFactory.newInstance().newTransformer();
			transformer.setOutputProperty("omit-xml-declaration", "yes");
			transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
			transformer.setOutputProperty(OutputKeys.METHOD, "xml");
			StringWriter writer = new StringWriter();
			transformer.transform(new DOMSource(node), new StreamResult(writer));
			String result = writer.toString();
			return result;
		}
		catch (Exception ex)
		{
			ex.printStackTrace();
			System.out.println("Transformer Error " + ex.getMessage());
			return "Transformer getOuterXml Error " + ex.getMessage();
		}
	}
}
```

## **Further Reading**

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
