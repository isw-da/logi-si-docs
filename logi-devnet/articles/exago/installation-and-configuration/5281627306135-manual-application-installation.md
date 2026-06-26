---
title: "Manual Application Installation"
id: 5281627306135
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281627306135-Manual-Application-Installation
updated_at: 2023-04-03T17:52:19Z
---

# Manual Application Installation

# Manual Application Installation

If the host application is deployed on site it may prove convenient and advantageous to integrate the installation of Exago into the host’s installer. This topic details how to integrate the installation. To accomplish this task there must be an existing installation of the Exago Web Application, Exago Web Service API and Exago Scheduler Service from which to copy files and directories.

## Web Application and Web Service API Installer Integration

### Summary

The installer integration of the Exago Web Application and/or the Exago Web Service API has four steps:

1. Copy the Exago and/or the Exago Web Service API files to installation folders.
2. Create IIS Virtual Directory to point to Web Application/Web Service API.
3. Configure IIS as required for the Web Application/Web Service API setup.
4. [*Optional:* Modify the system registry.](#Windows)

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

### 1. Directory Structure

The directory structure should be preserved as follows:

#### Web Application

* `<WebApp>/`
  + /ApplicationThemes
  + /Bin
  + /Config
  + /Drivers
  + /Fonts
  + /Licenses v2019.2.39+v2020.1.21+v2021.1.9+
  + /MapCache
  + /Monitoring
  + /NetHelp
  + /Temp
  + /Themes

#### REST Web Service API

* `<WebSvc>/`
  + /Bin
  + /Config
  + /Drivers

### File Installation

The host application installer should create a copy of all the files that are initially created by the Web Application and/or Web Service API installer.

For *v2019.5+*, extract the Puppeteer library files from `chromium-win64.zip` into the bin directory for both the Web Application and the REST Web Service API (if applicable). This file can be found in the <WebApp>\bin directory of the ZIP installation package.

#### Configuration

The following configuration files are not part of the initial Exago/Exago Web Service API installation. Including the configuration files with the installation will help to minimize manual configuration. The files are stored in the following directory tree:

##### Web Application

* /Config/
  + xml and/or WebReports.xml.enc

##### Web Service API

* /Config/
  + xml

### 3. IIS Configuration

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Verify that the Virtual Directory does not exist before attempting to create the new one.

The following is a C# code sample of how to create a new IIS installation of Exago/Exago Web Service API, using *Microsoft.Web.Administration.dll*. The code requires the following input:

* **siteName** — Name of the IIS Web Site where it will be installed. (for example *Default Web Site*)
* **vDirName** — Name of Virtual Directory for the installation (for example *Exago* or *ExagoApi*)
* **physicalPath** — Physical installation path. (for example *C:Program FilesExagoExago*)

```
public new void CreateVDir(string siteName, string vDirName, string physicalPath)
{
try
{
ServerManager iisManager = new ServerManager();
string virtDirName = @"/" + vDirName;

// Check if Application/Virtual Directory exists
if (iisManager.Sites[siteName].Applications[virtDirName] != null)
{
iisManager.Sites[siteName].Applications[virtDirName].VirtualDirectories[@"/"].PhysicalPath =
	physicalPath;
}
// Create new Application/Virtual Directory
else
{
iisManager.Sites[siteName].Applications.Add(virtDirName, physicalPath);

Microsoft.Web.Administration.Application app =
iisManager.Sites[siteName].Applications[virtDirName];

app.ApplicationPoolName = "DefaultAppPool";
}

// Commit changes to the web server
iisManager.CommitChanges();
}
catch
{
throw;
}
}
```

### 4. Modify the Windows Registry

See [Windows Registry](#Windows).

## Scheduler Service Installer Integration

### Summary

The installer integration of the Scheduler Service has six steps:

1. Check to see if the Scheduler Service is running as a Windows Service. If yes, stop the service.
2. Copy the Scheduler Service files to installation folders.
3. [*Optional:* Modify the system registry](#Windows).
4. Modify the security settings on the Scheduler Service installation directory.
5. Create a new Windows Service for the Scheduler Service.
6. Enable the Scheduler Service’s Windows Service.

### 1. Check Windows Services

Before running the installation, the Windows Services should be checked to see if the Scheduler Service is currently installed and/or running as a service. If the Exago Scheduler is currently installed and/or running as a service it should be stopped.

The following C# code provides an example of how to stop the Scheduler Service if it is running.

```
ServiceState serviceSt = WindowsServiceInstaller.GetServiceStatus(“ExagoScheduler”);

// check to see if the Exago Scheduler service exists
if (serviceSt != ServiceState.NotFound && serviceSt != ServiceState.Unknown)
{
CreateServiceDelegate stDel = new CreateServiceDelegate(WindowsServiceInstaller.StopService);
stDel(“ExagoScheduler”);

for (int ProgCtr = 0; ProgCtr <= 120; ProgCtr++)
{
Thread.Sleep(1000);
serviceSt = WindowsServiceInstaller.GetServiceStatus(“ExagoScheduler”);

if (serviceSt == ServiceState.Stop)
break;

if (InvokeRequired)
Invoke(new Change(OnChange), ProgCtr);

(sender as BackgroundWorker).ReportProgress(ProgCtr);
}
}
```

### 2. File Installation

The host installer should then create a copy of all the files that are initially created by the Exago Scheduler Installer.

For *v2019.5+*, extract the Puppeteer library files from `chromium-win64.zip` into the Scheduler Service’s directory. This file can be found in the Scheduler directory of the ZIP installation package.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Overwrite the file ExagoScheduler.xml with a version configured for the host application.

### 3. Modify the Windows Registry

See [Windows Registry](#Windows)

### 4. Directory Security Settings

Changes to the security settings of the installation directory are required to enable Windows to run it as a Windows Service.

The following C# code provides an example of how to make the necessary security changes. It requires the following input.

* **dirName** – Physical installation path of Scheduler Service (for example *C:\Program Files\Exago\ExagoScheduler*)

```
private void SetDirSecurity(string dirName)
{
try
{
if (dirName == null)
return;

if (!Directory.Exists(dirName))
return;

DirectoryInfo dirInfo = new DirectoryInfo(dirName);

// get a DirectorySecurity object that represents the current
// security settings
DirectorySecurity dirSecurity = dirInfo.GetAccessControl();

// Add the FileSystemAccessRule to the security settings
dirSecurity.AddAccessRule(new FileSystemAccessRule("LOCAL SERVICE",
FileSystemRights.FullControl, AccessControlType.Allow));
dirSecurity.AddAccessRule(new FileSystemAccessRule("LOCAL SERVICE",
		FileSystemRights.FullControl,
InheritanceFlags.ContainerInherit | InheritanceFlags.ObjectInherit,
PropagationFlags.InheritOnly, AccessControlType.Allow));

// Set the new access settings
try
{
dirInfo.SetAccessControl(dirSecurity);
}
catch (Exception ex)
{
MessageBox.Show(ex.Message);
}
}
catch (Exception ex)
{
MessageBox.Show(this,"Unable to set privileges on install directory: " + dirName +
	".  Please set 'LOCAL SERVICE' privileges.nnException: " + ex.Message, "Error");
}
}
```

### 5 & 6. Windows Service Creation and Startup

Before installing the Scheduler Service as a new Service, verify that it is not installed and/or running. If the Exago Scheduler is not installed, install the software and make sure it is running.

The following C# code provides an example of how to make this check.

```
serviceSt = WindowsServiceInstaller.GetServiceStatus(“ExagoScheduler”);
// is Exago Scheduler already installed as a service
if (serviceSt == ServiceState.NotFound || serviceSt == ServiceState.Unknown)
{
// install Exago as a new Windows Service
WindowsServiceInstaller.Install(“ExagoScheduler”,“ExagoScheduler”,
filePath + “ExagoScheduler.exe”);


for (int timeCtr = 0; timeCtr <= 120; timeCtr++)
{
serviceSt = WindowsServiceInstaller.GetServiceStatus(“ExagoScheduler”);

if (serviceSt == ServiceState.Stop)
{
break;
}

if (InvokeRequired)
Invoke(new Change(OnChange), timeCtr);

(sender as BackgroundWorker).ReportProgress(timeCtr);
}

RegistryKey key = Registry.LocalMachine.OpenSubKey("SYSTEM\CurrentControlSet\Services\" +
	“ExagoScheduler”, true);

if (key != null)
{
key.SetValue("Description", "Exago Scheduler Windows Service");
}
}
// found service already installed, check to see if it is running
else
{
// if the service is not running, attempt to start it
if (this.initialStatus != ServiceState.Stop)
{
CreateServiceDelegate stDel = new CreateServiceDelegate(WindowsServiceInstaller.StartService);
stDel(“ExagoScheduler”);

for (int timeCtr = 0; timeCtr <= 120; timeCtr++)
{
serviceSt = WindowsServiceInstaller.GetServiceStatus(“ExagoScheduler”);

if (serviceSt == ServiceState.Starting || serviceSt == ServiceState.Run)
{
break;
}

if (InvokeRequired)
Invoke(new Change(OnChange), timeCtr);

(sender as BackgroundWorker).ReportProgress(timeCtr);
}
}
}
```

## Windows Registry

Windows Registry keys are written by the Exago Installer when installing the Web Application, the Web Service API and the Scheduler Service. The changes to the registry are documented in [Windows Registry Changes](https://devnet.logianalytics.com/hc/en-us/articles/5281616108439-Windows-Registry-Changes).

### Example of Registry

The following C# code provides an example of how to add items to the registry. It requires the following arguments:

* **application** — Set to *Exago*, *ExagoApi* or *ExagoScheduler*.
* **path** — Set to the installation path where the component is installed.
* **website** — Set to the IIS Web Site where Exago is installed. Leave blank for the Exago Scheduler.
* **vdir** — Set to the virtual directory that Exago is set up as. Leave blank for the Exago Scheduler.

```
public static void AddRegistryKey(string application, string path, string webSite, string vdir)
{
try
{
	string ExagoRegKey = application;
	if (application != “ExagoScheduler”)
{
	vdir = vdir.Replace(@””, @”/”);
		ExagoRegKey += @”” + webSite + @”/” + vdir;
	}

RegistryKey registryKey = Registry.LocalMachine.OpenSubKey(REGISTRY_KEY_ROOT +
		ExagoRegKey, true);
if (registryKey == null)
{
registryKey = Registry.LocalMachine.CreateSubKey(REGISTRY_KEY_ROOT
+ ExagoRegKey);
if (registryKey == null)
throw (new Exception("Error creating RegistryKey"));
else
registryKey.SetValue("CreateDate",
	System.DateTime.Now.ToString(CultureInfo.InvariantCulture));
}
using (registryKey)
{
registryKey.SetValue("DisplayName", ExagoRegKey);
registryKey.SetValue("UpdateDate",
System.DateTime.Now.ToString(CultureInfo.InvariantCulture));
registryKey.SetValue("Location", path);
registryKey.SetValue("Version",
System.Reflection.Assembly.GetExecutingAssembly().GetName().Version);
}

return;
}
catch
{
throw;
}
}
```
