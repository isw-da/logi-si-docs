---
title: "Process Tasks and Script Files"
id: 4406822620567
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822620567-Process-Tasks-and-Script-Files
updated_at: 2022-04-06T06:10:01Z
---

# Process Tasks and Script Files

# Process Tasks and Script Files

Scripting can also be used in Process definition tasks. Let's look at an example that uses scripting to read a text file on the web server:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575447063/scripting_11.png)  

1. In the example above, a **Procedure.Script** element has been added to a task, and its attribute values have been set to point to the script file and function to be called. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The Procedure.Script element throws an 'Unsafe class reference' error by default when accessing the file system object. To overcome this error when running a procedure, set the Unsafe Script Allowed attribute in the Process Element to '*True*'. For more information about Process Tasks and its associated elements, see [Process Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4406817796375-Process-Tasks).  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417562972183/scripting_12.png)
2. Next, a **Script Input Parameters** element is added beneath Procedure.Script. This is the element that passes arguments to the function and its attribute values have been set as shown.   
     
   The arbitrary parameter name "Filename" will become part of a special token we'll use in the actual function to access the passed value. Its value is set to the name of the text file to be read. This assumes that the file is in the same folder as the script file; the value could instead include a more
   complete path or a combination of the @Function.AppPhysicalPath~ token and other folder/filename information.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417562972439/scripting_13.png)
3. Next, a **Script Output Parameters** element is added and its attributes set to arbitrary values. This is the element that receives the value (the text from the text file) the function returns. The parameter name "result" will be the return variable in the function and we'll reference the value "outputText" later in the task to view the returned text.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583623703/scripting_14.png)
4. Finally, an element is added to do something with the returned text, in this case, a **Procedure.Send Mail** element. Its attributes are set as shown, and a token that incorporates the value from the Script Output Parameters, @Procedure.procReadTextFile.outputText~, is used to access the text returned from the function.

function ReadFile() {  
var forReading = 1;  
var fso = new ActiveXObject('Scripting.FileSystemObject');  
var tf = fso.OpenTextFile('@Input.Filename~', forReading);  
result = tf.ReadAll();  
tf.Close();  
}

An example of the JavaScript that might be used for this purpose is shown above. Note the way in which the @Input token and result variables are used.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The example above is for illustration purposes only. It uses a Logi Server Engine object now understood to expose substantial security vulnerabilites and is *not* available on Windows 64-bit or Java platforms.
