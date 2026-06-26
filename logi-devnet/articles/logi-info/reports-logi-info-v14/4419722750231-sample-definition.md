---
title: "Sample Definition"
id: 4419722750231
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722750231-Sample-Definition
updated_at: 2022-07-17T01:57:01Z
---

# Sample Definition

# Sample Definition

The following is a **sample definition** you can experiment with. Just select all the text, copy and paste it into Notepad, then save it with an .LGX extension in the \_Definitions\\_Reports folder of a test application. If the application is already open in Studio, right-click the Reports folder in the Application panel and select "Refresh Application" to make the sample definition appear in the list of report definitions.

The sample definition you have a connection to the Northwind database and that it's thefirst Connection in the application's \_Settings definition. The blue.css style sheet, included with your Logi product installation, is also used.

>/Report<
  
> /"" myLastName=""ideTestParams myFirstName=<
  
>ReportFooter /<
  
>/Body<
  
> /"lblName" ID="@Request.myFirstName~ @Request.myLastName~"Label Caption=<
  
>LineBreak /<
  
> /"lblInstruction4" ID="4. This label concatenates two text values from request tokens."Label Caption=<
  
>LineBreak /<
  
>/DataTable<
  
>/DataTableColumn<
  
> /"lblName" ID="@Data.FirstName~ @Data.LastName~"Label Caption=<
  
>"cell" Class="Employee Name" Header="colName3"DataTableColumn ID=<
  
>/DataTableColumn<
  
> /"lblEmpID" ID="@Data.EmployeeID~"Label Caption=<
  
>"cell" Class="Employee ID" Header="colEmpID3"DataTableColumn ID=<
  
> /"Collapsed" IdeDisplayStatus="Select \* From Employees" Source="dlEmployees3" ID="SQL"DataLayer Type=<
  
>"Collapsed" IdeDisplayStatus="tableheader" ColumnHeaderClass="table" Class="dtEmployees3"DataTable ID=<
  
> /"lblInstructionTable3" ID="3. This table uses @Data tokens to display the First Name and Last Name together."Label Caption=<
  
>LineBreak /<
  
>/DataTable<
  
>/DataTableColumn<
  
> /"lblName" ID="@Data.calcName~"Label Caption=<
  
>"cell" Class="Employee Name" Header="colName2"DataTableColumn ID=<
  
>/DataTableColumn<
  
> /"lblEmpID" ID="@Data.EmployeeID~"Label Caption=<
  
>"cell" Class="Employee ID" Header="colEmpID2"DataTableColumn ID=<
  
>/DataLayer<
  
> /"calcName" ID="quot;&quot;@Data.LastName~&quot; + &quot; &quot;+ &quot;@Data.FirstName~&"CalculatedColumn Formula=<
  
>"Select FirstName, LastName, EmployeeID From Employees" Source="dlEmployees2" ID="SQL"DataLayer Type=<
  
>"Collapsed" IdeDisplayStatus="tableheader" ColumnHeaderClass="table" Class="dtEmployees2"DataTable ID=<
  
> /"lblInstruction2" ID="2. This table uses a calculated column to concatenate the First Name and Last Name together."Label Caption=<
  
>LineBreak /<
  
>/DataTable<
  
>/DataTableColumn<
  
> /"lblName" ID="@Data.Name~"Label Caption=<
  
>"cell" Class="Employee Name" Header="colName"DataTableColumn ID=<
  
>/DataTableColumn<
  
> /"lblEmpID" ID="@Data.EmployeeID~"Label Caption=<
  
>"cell" Class="Employee ID" Header="colEmpID"DataTableColumn ID=<
  
> /"Collapsed" IdeDisplayStatus="Select FirstName + ' ' + LastName As Name, EmployeeID From Employees" Source="dlEmployees1" ID="SQL"DataLayer Type=<
  
>"Collapsed" IdeDisplayStatus="tableheader" ColumnHeaderClass="table" Class="dtEmployees1"DataTable ID=<
  
> /"lblInstruction1" ID="1. This table uses SQL to concatenate the First Name and Last Name together."Label Caption=<
  
>Body<
  
>ReportHeader /<
  
> /"blue.css"StyleSheet StyleSheet=<
  
> /"Walton" myLastName="Sam"DefaultRequestParams myFirstName=<
  
>"11.4.046" EngineVersion="4/4/2008 1:30 PM" SavedAt="Sam" SavedBy="CombinedText"Report ID=<
