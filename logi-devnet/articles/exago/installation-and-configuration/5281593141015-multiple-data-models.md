---
title: "Multiple Data Models"
id: 5281593141015
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281593141015-Multiple-Data-Models
updated_at: 2023-04-03T17:52:19Z
---

# Multiple Data Models

# Multiple Data Models

In some cases the same Data Objects may need to be joined together differently. To accomplish this, Data Objects and Joins can be placed into Categories/Folders to create **multiple data models**. When an end user selects a Data Object from a Category/Folder it indicates which joins to use.

The following steps detail how to create multiple data models:

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

1. *Optional:* To limit a report to using fields from a single Data Object, set **Admin Console** > **General** > **Other Settings** > **Limit Reports and Visualizations to One Object** to *True*.
2. Open the XML configuration file (by default this file is located at `<WebApp>\Config\WebReports.xml`) in a text editor.
3. In the `<webreports>` section, begin by creating a `<category>` for each unique data model.  
   > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
   >
   > Each XML tag must be closed (for example `<category>` must be closed with `</category>`).
4. Inside the `<category>` specify an ID with a `<category_id>` node. The ID should be a unique identifier for the data model and will be utilized by the Data Objects and Joins.
5. Give the model a name that will be displayed to the end user using the `<category_name>` node.  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
   >
   > The `<category_name>` node creates a folder structure to group Data Objects. Child folders can be created by entering the parent , a backslash, then the then the child folder name. (for example `<category_name>Sales\Clients</category_name>`)

   **Example:**

   ```
   <category>
      <category_name>Exago University\Advisors</category_name>
      <category_id>advisorModel</category_id>
   </category>
   ```
6. For each Data Object (`<entity>` node):
   1. Within the `<category>` node, create a comma separated list of IDs for each data model in which you want the Object to be available. In the example below two data models are specified by their IDs (advisorModel & classesModel).  
      **Example:**  

      ```
      <entity>
         <entity_name>Professors</entity_name>
         <db_name>Professor</db_name>
         <category>advisorModel,classesMode</category>
         <datasource_id>7</datasource_id>
         <object_type>xmltable</object_type>
         <key>
            <col_name>ID</col_name>
         </key>
      </entity>
      ```
7. For each Join (`<join>` node):
   1. Within the `<category>` node, create a comma separated list of IDs for each data model in which you want the Join to be utilized. In the example below a Join between two Data Objects is being set to one data model (advisorModel).  
      **Example:**  

      ```
      <join>
         <entity_from_name>Professor</entity_from_name> 
         <entity_to_name>Student</entity_to_name> 
         <join_type>rightouter</join_type> 
         <relation_type>1M</relation_type> 
         <weight>0</weight>   
         <category>advisorModel</category>  
         <joincol>      
            <col_from_name>ID</col_from_name>      
            <col_to_name>Advisor</col_to_name>     
         </joincol>
      </join>
      ```

## Example

The following configuration example demonstrates how three Data Objects are made available in two different relational models. In the advisor Model model Students are joined directly to Professors, while in the classes Model model Students are joined to Professors indirectly through Classes.

### Models

```
<category>
   <category_name>Exago University\Advisors</category_name>
   <category_id>advisorModel</category_id>
</category>
<category>
   <category_name>Exago University\Classes</category_name>
   <category_id>classesModel</category_id>
</category>
```

### Data Objects

```
<entity>
   <entity_name>Classes</entity_name>
   <db_name>Class</db_name>
   <category>advisorModel,classesModel</category>
   <datasource_id>7</datasource_id>
   <object_type>xmltable</object_type>
   <key>
      <col_name>ID</col_name>
   </key>
</entity>
<entity>
   <entity_name>Students</entity_name>
   <db_name>Student</db_name>
   <category> advisorModel,classesModel </category>
   <datasource_id>7</datasource_id>
   <object_type>xmltable</object_type>
   <key>
      <col_name>ID</col_name>
   </key>
</entity>
```

### Joins

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> The Professors => Classes join is utilized by both Data Models because no `<category>` is set.

```
<join>
   <entity_from_name>Professor</entity_from_name>
   <entity_to_name>Student</entity_to_name>
   <join_type>rightouter</join_type>
   <relation_type>1M</relation_type>
   <weight>0</weight>
   <category>advisorModel</category>
   <joincol>
      <col_from_name>ID</col_from_name>
      <col_to_name>Advisor</col_to_name>
   </joincol>
</join>
<join>
   <entity_from_name>Professor</entity_from_name>
   <entity_to_name>Class</entity_to_name>
   <join_type>inner</join_type>
   <relation_type>1M</relation_type>
   <weight>0</weight>
   <joincol>
      <col_from_name>ID</col_from_name>
      <col_to_name>ID</col_to_name>
   </joincol>
</join>
```

## Additional Resources

* [Admin Support Lab — Multiple Data Models, Cloned Data Objects & Vertical Tables](https://devnet.logianalytics.com/hc/en-us/articles/5281554024983-Multiple-Data-Models-Cloned-Data-Objects-Vertical-Tables) (video)
