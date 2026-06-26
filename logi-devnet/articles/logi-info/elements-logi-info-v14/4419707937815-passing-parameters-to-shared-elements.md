---
title: "Passing Parameters to Shared Elements"
id: 4419707937815
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707937815-Passing-Parameters-to-Shared-Elements
updated_at: 2022-07-17T01:31:07Z
---

# Passing Parameters to Shared Elements

# Passing Parameters to Shared Elements

Shared elements can be made dynamic by passing them parameters. The passed values are then applied to the shared elements *before* they're included in the report definition. Here's an example:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707151511/shrelements_07.png)

Imagine that we want to make use of shared report header code, but we want to change the *location* displayed with the logo (highlighted above), depending on some variable. Shared element parameters are perfect for this situation.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714951447/shrelements_08.png)

In the example code above, in our Default report definition, we added an **Include Shared Element** element ("sharedHeader") beneath the Report Header element. As usual, the code from the shared element appears in Read-Only mode beneath it ("Rows").

Next, we added a child **Shared Element Params** element and created a single parameter, "OfficeLocation", and gave it a value. The value can be literal or derived from tokens, as shown. This parameter will tell the shared code which location text to use in the header.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714951703/shrelements_09.png)

In the shared element definition, shown above, we can see how the passed parameter is used. The **@Shared** token provides access to the passed parameter. In our example, it's used in a Condition attribute to control which column is displayed in the header.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) If tokens are used for parameter values, they are passed as intact tokens, *not* as the token *values*. The tokens will not be resolved in the shared element definition - instead, they'll be inserted with the shared elements into the calling report definition and will be resolved when the report definition is rendered.

<SharedElementParams   
 myParam1="Welcome to McLean"  
 myParam2=7900  
 myParamReq="@Request.myVal~"  
 myParamSes="@Session.myVal~"  
 myParamData="@Data.myColumnVal~"  
 myParamProc="@Procedure.myVal~"  
 myParamColName="myColumnName~"  
 />

To further clarify how they're used, theXML source code forsome examples of Shared Element Parameters isshown above.

<SharedElement ID="mySharedElement" >  
 <Label Caption="@Shared.myParam1~" />  
<Label Caption="@Shared.myParam2~" />  
<Label Caption="@Shared.myParamReq~" />  
<Label Caption="@Shared.myParamSes~" />  
<Label Caption="@Shared.myParamData~" />  
<Label Caption="@Shared.myParamProc~"/>  
<Label Caption="@Data.@Shared.myParamColName~~" />  
</SharedElement>

The XML source code above shows a Shared Element element and the passed parameters being used in Label elements via @Shared tokens. This is similar to the way you'd use @Request tokens to access the values of Link Params in a Process Task.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The last Label element above uses a nested token - when the calling report definition is rendered, the inner token (@Shared) will be resolved first, providing the literal column name, then outer token (@Data) will be resolved. For more information, see ["Nesting" Tokens](https://devnet.logianalytics.com/hc/en-us/articles/4419723178007--Nesting-Tokens).

<Label Caption="Welcome to McLean"/>  
<Label Caption="7900"/>  
<Label Caption="@Request.myVal~"/>  
<Label Caption="@Session.myVal~"/>  
<Label Caption="@Data.myColumnVal~"/>  
<Label Caption="@Procedure.myVal~"/>  
<Label Caption="@Data.myColumnName~"/>

When the calling report definition is processed and the shared element is inserted into it, the source code for the inserted Label elements would look like the examples above. Note how the Caption attributes relate to the original shared element parameters.
