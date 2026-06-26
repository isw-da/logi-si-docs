---
title: "Get App and Web Server Info"
id: 360047843793
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047843793-Get-App-and-Web-Server-Info
updated_at: 2022-02-07T21:52:59Z
---

# Get App and Web Server Info

## **Plugin Description**

This .NET plug-in demonstrates how information about a Logi v10 application and the IIS web server can be determined and provided to the application as Session variables. The VB.NET source code and compiled .dll are included. Information available as tokens includes:

* The version number of the Logi product used to create this app
* The Logi product name
* The name of the computer that the Logi v10 license has been assigned to
* The "friendly" name of the Windows OS on the web server.
* The major and minor service pack numbers of the Windows OS on the web server
* The application type, 32- or 64-bit, that the Logi application has been configured to run as
* The size, in bytes, of the Logi application root folder (including all sub-folders and files)

Plug-In Installation Instructions: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/360048172233)

## **View Code Snippet**

```
Imports System.Environment
Imports System.Management.ManagementObject
Imports System.IO
Imports System.Xml
Imports System.Web



Public Class Plugin

    Public Sub GetApplicationInfo(ByRef rdObjects As rdPlugin.rdServerObjects)
        Dim xmlSettings As New XmlDocument()

        '----- get product version number from _Settings definition ---------------
        '
        ' load _Settings definition into XML doc object
        xmlSettings.LoadXml(rdObjects.CurrentDefinition)
        ' load Setting node
        Dim eleSetting As XmlElement = xmlSettings.SelectSingleNode("//Setting")
        ' set session variable to version attribute value
        rdObjects.Session("lgxVersion") = eleSetting.GetAttribute("EngineVersion").ToString()
        eleSetting = Nothing

        '---- get product and machine name from license file ---------------
        '
        Dim licPath As String = AppDomain.CurrentDomain.BaseDirectory
        Dim foundFile As String = ""
        Dim licFile As String = ""

        ' iterate the license files in the app folder
        For Each foundFile In My.Computer.FileSystem.GetFiles(licPath, FileIO.SearchOption.SearchTopLevelOnly, "*.lic")
            If InStr(foundFile, "rdTrial.lic") = 0 Then
                licFile = foundFile
                Exit For
            End If
        Next

        'if no license file found, the check _settings def for custom license file location
        If licFile = "" Then
            ' load _Settings definition into XML doc object
            xmlSettings.LoadXml(rdObjects.CurrentDefinition)
            ' load General node
            Dim eleGeneral As XmlElement = xmlSettings.SelectSingleNode("//Setting/General")
            ' assign lic file location attribute value
            licPath = eleGeneral.GetAttribute("LicenseFileLocation").ToString()
            If licPath <> "" Then
                ' iterate the license files in the lic folder
                For Each foundFile In My.Computer.FileSystem.GetFiles(licPath, FileIO.SearchOption.SearchTopLevelOnly, "*.lic")
                    If InStr(foundFile, "rdTrial.lic") = 0 Then
                        licFile = foundFile
                        Exit For
                    End If
                Next
            End If
            eleGeneral = Nothing
        End If

        ' if we have a license file 
        If licFile <> "" Then
            xmlSettings.Load(licFile)
            Dim eleProduct As XmlElement = xmlSettings.SelectSingleNode("//LicenseFile/Product")
            ' set session variable to version attribute value
            rdObjects.Session("lgxProduct") = eleProduct.GetAttribute("Name").ToString()
            eleProduct = xmlSettings.SelectSingleNode("//LicenseFile/License")
            rdObjects.Session("lgxMachine") = eleProduct.GetAttribute("ComputerName").ToString()
            eleproduct = Nothing
        End If

        '---- get application folder size ---------------
        '
        Dim appPath As String = AppDomain.CurrentDomain.BaseDirectory
        Dim appSize As Long = 0

        For Each foundFile In My.Computer.FileSystem.GetFiles(appPath, FileIO.SearchOption.SearchAllSubDirectories, "*.*")
            Dim fInfo As New FileInfo(foundFile)
            appSize += fInfo.Length
        Next
        rdObjects.Session("lgxAppSize") = appSize.ToString("###,###,###")


        '---- get windows OS name and 32/64-bit ---------------
        '
        Try
            Dim objQuery As System.Management.ObjectQuery
            Dim objSearcher As System.Management.ManagementObjectSearcher
            Dim mgmtObj As System.Management.ManagementObject

            objQuery = New System.Management.WqlObjectQuery("SELECT * FROM Win32_OperatingSystem")
            objSearcher = New System.Management.ManagementObjectSearcher(objQuery)
            mgmtObj = New System.Management.ManagementObject
            For Each mgmtObj In objSearcher.Get()
                rdObjects.Session("lgxOSVersion") = mgmtObj("Caption")
                rdObjects.Session("lgxOSServicePack") = mgmtObj("ServicePackMajorVersion") & "." & mgmtObj("ServicePackMinorVersion")
            Next
            objQuery = Nothing
            objSearcher = Nothing
            mgmtObj = Nothing
        Catch e As Exception
        End Try

        ' determine whether app is running as a 32- or 64-bit app (not quite that same as the OS bits) 
        If IntPtr.Size = 4 Then
            rdObjects.Session("lgxAppBits") = "32"
        ElseIf IntPtr.Size = 8 Then
            rdObjects.Session("lgxAppBits") = "64"
        Else
            rdObjects.Session("lgxAppBits") = "undetermined"
        End If


        xmlSettings = Nothing
        rdObjects = Nothing

    End Sub
End Class
```

## **Further Reading**

How To Create a .NET Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722772759-Create-NET-Plug-in)

How To Create A Java Plug-In: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419715184151-Create-a-Java-Plug-in)

Logi Plug-Ins: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins)
