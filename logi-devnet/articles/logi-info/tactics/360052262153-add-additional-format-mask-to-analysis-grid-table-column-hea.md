---
title: "Add Additional Format Mask to Analysis Grid Table Column Headers "
id: 360052262153
section: "Tactics"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360052262153-Add-Additional-Format-Mask-to-Analysis-Grid-Table-Column-Headers
updated_at: 2020-07-27T22:51:04Z
---

# Add Additional Format Mask to Analysis Grid Table Column Headers 

**Description**

The Analysis Grid only offers certain format masks for certain data types from the Analysis Grid Table Column Header menus as shown in the following devnet article section:

<https://documentation.logianalytics.com/logiinfov12/content/use-analysis-grid-1.htm?Highlight=analysis%20grid#Formatting>

![](https://documentation.logianalytics.com/logiinfov12/content/resources/images/usingag_20_226x515.png)

This affects web presentation, but especially should be considered for Excel export from the analysis grid table, as the format mask is applied to the export data.  For instance a numeric value may have many decimal places, but a format mask of ###,###,##0.00 will only export the first 2 decimal places to Excel  and this affects rounding.

**Implementation:**

These format masks are stored in the rdTemplate/rdAnalysisGrid/rdAg10Template.lgx template file for the analysis grid, so the change will have to be added via a Template Modifier File specified on the Analysis Grid element.

The following example will add a new format mask, $###,###,##0.000, directly after the ppo\_AddDollarSign PopupOption element which contains the $###,###,##0.00 format mask.  Add the following block between the <TemplateModifier> tags in your Template Modifier File in the \_SupportFiles directory.

```
<InsertAfterElement ID="ppo_AddDollarSign">   
 <NewElement>  
 <PopupOption Caption="$###,###,##0.000" ID="ppo_AddDollarSign2">  
 <Action ID="actAddDollarSign2" Type="Report">  
  <Target ID="tgtAddDollarSign2" KeepScrollPosition="True" Type="Report" />  
  <LinkParams rdAgColumnID="@Data.ID~" rdAgCommand="FormatAdd" rdAgCommandID="@Function.GUID~" rdAgFormat="$###,###,##0.000" />  
 </Action>  
 </PopupOption>  
 </NewElement>   
 </InsertAfterElement> 
```

This should add an extra decimal place that is retained for Excel export.

**Further Reading**

Template Modifier Files in Logi Info:

<https://documentation.logianalytics.com/logiinfov12/content/template-modifier-files.htm?Highlight=template%20modifier>
