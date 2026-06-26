---
title: "Setting Hidden Underlying Element Attributes"
id: 4406822532119
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822532119-Setting-Hidden-Underlying-Element-Attributes
updated_at: 2022-04-06T06:08:48Z
---

# Setting Hidden Underlying Element Attributes

# Setting Hidden Underlying Element Attributes

Some aspects of the appearance and behavior of a super-element can be configured using its *exposed* attributes (those that appear in Studio in the Attributes Panel). Further customization can occur by using a TMF to change its *hidden* attributes: the attributes of the underlying elements that make up the super-element.

The key to configuring hidden attributes is knowing the **ID** of the underlying elements.

The IDs of these underlying elements can be found by examining the special definition file that defines each super-element. These files are located in your application's rdTemplate folder. Here are a few of them:

| Super-Element | Template File |
| --- | --- |
| Analysis Chart | rdTemplate\rdAnalysisChart\rdAcTemplate.lgx |
| Analysis Filter | rdTemplate\rdAnalysisFilter\rdAfTemplate.lgx |
| Analysis Grid | rdTemplate\rdAnalysisGrid\rdAg10Template.lgx |
| Dashboard | rdTemplate\rdDashboard\rdDashboard2Template.lgx |
| Dimension Grid | rdTemplate\rdOlapGrid\rdDgTemplate.lgx |
| OLAP Grid | rdTemplate\rdOlapGrid\rdOgTemplate.lgx |
| Schedule | rdTemplate\rdSchedule\rdScheduleTemplate.lgx |
| Report Author | rdTemplate\ReportAuthorTemplate.lgx |

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Never edit these files directly; only examine them to determine element IDs!

Here's a simple example of how TMFs are used. Suppose we want to change the Layout "descriptive text" that appears in an Analysis Grid.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563085719/usingtmf_01.png)

When the **Filter** tab is clicked and the Filter configuration panel appears in an Analysis Grid, as shown above, the highlighted descriptive text is displayed.

To change this text to **French**, we first examine the Analysis Grid's definition file, rdAg10Template.lgx, with Notepad or a suitable text editor:

<Label ID="lblFilterDescription" Class="rdAgContentHeading" Caption="Filter rows by cell values." />

If we search the file for "filter rows", we'll find the code shown above. It contains a **Label** element, with an **ID** attribute of "lblFilterDescription", that sets the text we want to change. Note the ID of this element for use in our TMF.

<TemplateModifier>  
 <SetAttribute ID="lblFilterDescription" Caption="Filtrer par les valeurs des cellules." />  
 </TemplateModifier>

To cause the change, we create a TMF, as shown above, which we'll give the arbitrary filename AGFrenchTMF.xml.

This is a standard XML file, which starts and ends with the <TemplateModifier> tag. It uses a special TMF tag <SetAttribute> to make the change and the element to be changed is identified using its **ID** from the Analysis Grid's template definition file ("lblLayoutDescription"). The attribute to be changed is identified as the **Caption**
and is given its new French text value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563085847/usingtmf_01a.png)

Next we save the TMF file to the application's \_SupportFiles folder and, finally, enter its filename as the Analysis Grid's **Template Modifier File** attribute value, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563085975/usingtmf_02.png)

And the resulting change, shown above, can be seen when the report is run again.  
Now that you've seen the basic concept in action, here's a more complicated TMF example:

<ExampleTMF>  
<!-- These SetAttributes will change the Formula Column Panel Text -->  
<SetAttribute ID="lblFormulaColumnDescription" Caption="Formule de la colonne" />  
<SetAttribute ID="lblCalcHelp" Caption="Formule Aide" />  
 <SetAttribute ID="lblCalcName" Caption="Nom" />  
<SetAttribute ID="lblCalcInsertDataColumn" Caption="Inserer une colonne" />  
<SetAttribute ID="lblCalcInsertDataColumnNow" Caption="Inserer" />  
<SetAttribute ID="lblCalcFormula" Caption="Formule" />  
<SetAttribute ID="lblCalcDataType" Caption="Type de donnees" />  
<SetAttribute ID="lblCalcDisplayFormat" Caption="Format d'affichage" />  
<SetAttribute ID="lblCalcOk" Caption="Ajouter" />  
</ExampleTMF>

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Actual <TemplateModifier> tags are not required; any tags that properly open and close the XML are acceptable. Also note that **comments** can be embedded into the XML using the HTML <!-- ... --> comment syntax.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575540887/usingtmf_03.png)

The resulting changes are shown above. This example changed the section description, field captions, and button captions to French.

If a Security Right ID attribute is being set, the element is re-evaluated after the operation for security purposes.
