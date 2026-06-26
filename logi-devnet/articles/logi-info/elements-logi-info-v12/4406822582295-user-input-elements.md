---
title: "User Input Elements"
id: 4406822582295
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822582295-User-Input-Elements
updated_at: 2022-04-06T06:09:32Z
---

# User Input Elements

# User Input Elements

**User Input** elements produce input controls, which allow users to interact with applications at runtime. They're often used to often to provide data selection and filtering criteria.

The following topics discuss each of the Logi Info Input elements:

* [Input Hidden](https://devnet.logianalytics.com/hc/en-us/articles/4406817987735-Input-Hidden#Hidden)
* [Input Text](https://devnet.logianalytics.com/hc/en-us/articles/4406822580119-Input-Text#Text)
* [Input Password](https://devnet.logianalytics.com/hc/en-us/articles/4406822576279-Input-Password#Password)
* [Input Date](https://devnet.logianalytics.com/hc/en-us/articles/4406822574231-Input-Date#Date)
* [Date Picker](https://devnet.logianalytics.com/hc/en-us/articles/4406817980951-Date-Picker#DatePicker)
* [Input Email](https://devnet.logianalytics.com/hc/en-us/articles/4406817986583-Input-Email#Email)
* [Input Number](https://devnet.logianalytics.com/hc/en-us/articles/4406817988759-Input-Number-Mobile-Only-#Number) (Mobile Only)

* [Input Telephone](https://devnet.logianalytics.com/hc/en-us/articles/4406822578071-Input-Telephone-Mobile-Only-#Telephone) (Mobile Only)
* [Input Time](https://devnet.logianalytics.com/hc/en-us/articles/4406822581399-Input-Time#Time)
* [Input File Upload](https://devnet.logianalytics.com/hc/en-us/articles/4406822575255-Input-File-Upload#Upload)
* [Input Text Area](https://devnet.logianalytics.com/hc/en-us/articles/4406822578967-Input-Text-Area#Area)
* [Input Check Box](https://devnet.logianalytics.com/hc/en-us/articles/4406822572439-Input-Check-Box#check%20box)
* [Input Select List](https://devnet.logianalytics.com/hc/en-us/articles/4406817990935-Input-Select-List#List)
* [Input Check Box List](https://devnet.logianalytics.com/hc/en-us/articles/4406817984151-Input-Check-Box-List#check%20boxList)
* [Input Combo List](https://devnet.logianalytics.com/hc/en-us/articles/4406822573335-Input-Combo-List#ComboList)

* [Input Radio Buttons](https://devnet.logianalytics.com/hc/en-us/articles/4406817989911-Input-Radio-Buttons#radio%20buttons)
* [Input Slider](https://devnet.logianalytics.com/hc/en-us/articles/4406817992087-Input-Slider#Slider)
* [Input Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/4406817985303-Input-Color-Picker#Picker)
* [Input Chart.List](https://devnet.logianalytics.com/hc/en-us/articles/4406817981975-Input-Chart-List#ChartList)
* [Input Chart.Range](https://devnet.logianalytics.com/hc/en-us/articles/4406817983127-Input-Chart-Range#ChartRange)
* [Input Selection Point & Range](https://devnet.logianalytics.com/hc/en-us/articles/4406822577175-Input-Selection-Point-and-Range#InpSelection)

## About Input Elements

Logi Info Input elements are based on the standard HTML input control types and provide useful interactivity. They can be used to gather user input at runtime in order to login to an application, to filter or restrict data, to modify the style or appearance of a report, to insert new or update existing data, and more.

When you include Input elements in a report definition, a ;<FORM> tag is automatically added to the HTML page generated. Following standard HTML behavior, when a user clicks links or buttons that reload the report or pass control to another definition, the form is submitted, along with all of the input control values that have been entered.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) When an report page is submitted, the values of *all* of its Input elements are *automatically* passed to the next Report or Process definition. DO NOT use **Link Parameters** to try to pass the entered values - they'll become null.

In the *next* Report or Process definition, you can access the entered values using Request tokens. For example, if an Input Text element has an element ID of *inpLastName*, its value is available in the token @Request.inpLastName~.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Because the values are passed using HTTP POST, they will *not* appear in the URL. They are clearly shown, however, in the Debugger Trace Page when you turn debugging on, and this is a great tool for determining what's happening with user input values.

Due to the stateless nature of HTML pages, you generally have to submit (or refresh) a page before its value is usable in its own report definition. There are some exceptions to this; it's possible to use JavaScript to get and set the values of Input elements without submitting the page. This, and many other useful techniques, are described in [Working with User Input Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406818159767-Working-with-User-Input-Elements).

Our [Sample Center](https://sampleapps.logianalytics.com/LambdaExV2/rdPage.aspx?rdReport=GettingStarted) is also an good resource. Special mobile input elements are discussed in [Logi Mobile Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406822416407-Logi-Mobile-Reports).

Now let's examine the available Input elements.
