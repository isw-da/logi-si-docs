---
title: "File System Interactions from a Task"
id: 4419723116567
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723116567-File-System-Interactions-from-a-Task
updated_at: 2022-07-17T01:39:57Z
---

# File System Interactions from a Task

# File System Interactions from a Task

Tasks can include Procedure elements that allow direct manipulation of files on the web server or on network-connected drives. To do this, of course, the account used by the web server to run your Logi application needs to have appropriate file access permissions.

Here are the elements available for file system interactions:

| Element | Description |
| --- | --- |
| Procedure.Compress File | Compresses the named file, using the .ZIP format. You must specify both the source and destination file names. Wild cards are allowed, see below. Specify a fully-qualified path and file name. |
| Procedure.Compress Folder | Compresses the named folder and its contents using the .ZIP format. Maintains the hierarchy of any sub-folders and files within it. You must specify both the source folder name and destination file name. Specify a fully-qualified path and folder name. |
| Procedure.Copy File | Copies a single file. You must specify both the source and destination file names. If it already exists, the destination file is overwritten without warning. Specify a fully-qualified path and file name. |
| Procedure.Create Folder | Creates a new file system folder. No error occurs if the folder already exists. Specify a fully-qualified path and folder name. |
| Procedure.Delete File | Deletes a file. No error occurs if the named file does not exist. Specify a fully-qualified path and file name. |
| Procedure.Delete Folder | Deletes a folder and its contents. No error occurs if the specified folder does not exist. Specify a fully-qualified path and folder name. |
| Procedure.File Exists | Returns *True* and executes its child elements if the named file is found in the web server file system. Specify a fully-qualified path and file name.  The token @Procedure.*<myProcedureElementID>*.rdReturnValue~ will return *True* or *False* depending on file existence. |
| Procedure.Folder Exists | Returns *True* and executes its child elements if the named folder is found in the web server file system. Specify a fully-qualified path and folder name.  The token @Procedure.*<myProcedureElementID>*.rdReturnValue~ will return *True* or *False* depending on folder existence. |
| Procedure.Run Shell Command | Executes an OS command-line command or application and optionally passes in parameters. See the section below for more information. |
| Procedure.Uncompress File | Expands a compressed .ZIP file. If no destination folder is specified, the files are written to the application's rdDataCache directory. Wild cards are allowed for selectively identifying files to be uncompressed, see below. You must specify a fully-qualified path and compressed file name. |
| Procedure.Uncompress Folder | Expands a compressed folder and its contents. Maintains the hierarchy of any sub-folders and files within it. You must specify both the source file name and the destination folder name and they must include a fully-qualified path. |
| Procedure.XML Modifier | Allows you to update an XML file from a Process Task. Information about using this element is available in [Procedure.XML Modifier](https://devnet.logianalytics.com/hc/en-us/articles/4419715437975-Procedure-XML-Modifier). |

You can use tokens, such as @Function.AppPhysicalPath~ and @Data.FileName~, to provide the part or all of the file or folder names required in these attributes. Valid characters that can be used in file and folder names are those allowed by the web server operating system.

The wildcards characters \* and ? can be used where mentioned in the descriptions above. For example, to compress all
files in a folder, leave the Files To Compress attribute *blank* or enter *\*.\** and to compress only XML files
that start with an S, enter *S\*.xml*.

## Using Procedure.Run Shell Command

The **Procedure.Run Shell Command** element allows you to run OS shell commands or applications from a task and handle their output.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Commands and applications launched using this element run *synchronously* and will *block* the processing of the rest of the task until they complete.

Here are the element's attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) Specifies a unique identifier for this element. |
| Error Output Filename | Specifies an method of handling error output from a shell command, as follows:   * Leave blank to have error output included in the return values, or * Specify a fully-qualified file path and file name to send error output to a file, or * Specify "NUL" to ignore error output   If left blank, the error output can be accessed using the token @Procedure.*<myProcedureID>*.ErrorOutput~. |
| Filename | Specifies the filename of a shell or application to execute, as follows:   * For Windows PowerShell, enter powershell and preface Shell Command Parameters with "/C". * For the Windows Command Line, enter cmd and preface Shell Command Parameters with "/C". * For Linux, enter the path to the command, such as /usr/bin/cp. * For applications, enter the fully-qualified path and filename of the executable file. If *not* located within your Logi application folder, then the account used by web server to run Logi app must have Read & Execute file access permissions for the executable file. * Tokens may be used here. |
| Shell Command Parameters | Specifies a string of parameters for the shell command. In a command line, this is the typically the part of the command that goes after the actual command name. Begin the string with "/C" if using the Windows Command line. Examples, with parameter string highlighted in yellow:    powershell /C Test-NetConnection cmd /C COPY \*.\* c:\temp /Y /usr/bin/ps -ef   Be sure to include any switches needed to suppress any prompts, such as "/Y" in the COPY example above. Otherwise, the task will "hang" indefinitely. |
| Standard Output Filename | Specifies a fully-qualified path and filename to be used to store the shell command's or application's "standard output". This is the output typically seen when running a shell command from a command prompt. Tokens may be used here.  If left blank, standard output can be accessed using @Procedure.*<myProcedureID>*.StandardOutput~. |
| Timeout | Specifies the length of time, in seconds, to wait for an action to complete before a timeout error occurs. If set to 0, then the task will wait indefinitely until the request completes. Entering a value here is a good idea, to protect against the task "hanging", but be sure to allow enough time for the shell to launch, interpret and execute the command and any parameters, and return a result. You may wish to experiment with different values and you can enter decimal values less than a whole second, such as 0.001, if appropriate. |
| Working Directory | Specifies the fully-qualified path to the folder to be used as the context of the shell command or application. Tokens may be used here. |

The following tokens are available for use with Procedure.Run Shell Command:

| Token | Description |
| --- | --- |
| @Procedure.*myProcedureID*.ErrorOutput~ | If the element's Error Output Filename attribute has been left blank, this token contains the shell command's or application's error output. If no error has occurred, this token will have no value. |
| @Procedure.*myProcedureID*.ExitCode~ | Contains the "exit" or "return" code from the shell command or application, often *0* for success. |
| @Procedure.*myProcedureID*.StandardOutput~ | If the element's Standard Output Filename attribute has been left blank, this token contains the shell command's or application's standard console output. If there is no standard output, this will have no value. |
| @Procedure.*myProcedureID*.TimedOut~ | Contains *True* if a timeout occurred; otherwise contains *False*. |

### USAGE EXAMPLE: RUN A WINDOWS BATCH FILE

In this example, we'll use Procedure.Run Shell Command to run a simple Windowsbatch file that will "ping" a web site and display some parameters. Here's the batch file contents:

ping %1  
echo %2 %3  
echo

As you can see, it expects three parameters.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707031447/workproctask_26.png)

In the task definition shown above, you can see how the Procedure.Run Shell Command element's attributes are configured. Note the use of a token in the **Filename** value, and that there are three separate parameters, separated by a space, in the **Shell Command Parameters**.

**Link Parameters** are used in our example to pass the four related Procedure tokens to the response report.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707031831/workproctask_27.png)

The results are displayed in the response report as shown above.

### USAGE EXAMPLE: TEST A NETWORK CONNECTION

In this example, we'll use a Windows PowerShell command to retrieve information about the network:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707032087/workproctask_28.png)

In the task definition shown above, you can see how the Procedure.Run Shell Command element's attributes are configured. Note the use of the shell invocation in the **Filename** value, and that "/C" is added before the shell command in the **Shell Command Parameters**.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714876183/workproctask_29.png)

The results are displayed in the response report as shown above.

For purposes of illustration, let's make the command invalid by adding "x" to it, so the Shell Command Parameters value is "/C Test-NetConnectionx", and re-run the task:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707032343/workproctask_30.png)

Now we can see that the Exit Code, Standard Output, and Error Output values have changed.

### USAGE EXAMPLE: RUN A LINUX COMMAND

In this example, we'll use the Linux "ps" command to display a formattedlist of active processes:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714876439/workproctask_31.png)

In the task definition shown above, you can see how the Procedure.Run Shell Command element's attributes are configured. Note the use of the Linux "ps" command in the **Filename** value, and the "-ef" flags in the **Shell Command Parameters**.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699865879/workproctask_32.png)

The results are displayed in the response report as shown above.

### USAGE EXAMPLE: RUN A LINUX COMMAND USING TOKENS

In this example, we'll use the Linux "cp" command to copy a file:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714876695/workproctask_33.png)

In the task definition shown above, you can see how the Procedure.Run Shell Command element's attributes are configured. Note the use tokens in the **Shell Command Parameters** value, which in its entirety is:

@Function.AppPhysicalPath~/test.txt @Function.AppPhysicalPath~/test.out -f

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) The ability to run shell commands can be dangerous, so use this element with care.
