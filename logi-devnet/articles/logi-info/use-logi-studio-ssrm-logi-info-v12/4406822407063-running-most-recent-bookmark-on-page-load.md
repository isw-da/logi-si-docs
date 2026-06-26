---
title: "Running Most-Recent Bookmark on Page Load"
id: 4406822407063
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822407063-Running-Most-Recent-Bookmark-on-Page-Load
updated_at: 2022-04-06T06:07:05Z
---

# Running Most-Recent Bookmark on Page Load

# Running Most-Recent Bookmark on Page Load

Some developers may want their users to run a report and have their most-recently saved bookmark applied by default.

There are two steps required to make this happen: 1) run the report to get the ID for the most-recently saved bookmark, and 2) run that bookmark. Here's how to do this:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575632023/introbm_35.png)

The elements shown above will let you reduce the data in the datalayer to the single row for the most-recently saved bookmark.

1. **Local Data** - This is used to get the bookmark. We'll control when it runs by setting its **Condition** attribute to the special token "@Request.rdBookmarkID~" = "".
2. **DataLayer.Bookmarks** - Configure with the name of your bookmark collection or leave blank if a default collection has been specified in \_Settings. A token can also be used here.
3. **Sort Filter** - Sort the bookmarks on the SaveTime column (*Date* type data), into *Descending* order.
4. **Sequence Column** - This adds a "row number" column to each row of sorted data and the most recent bookmark will wind up as Row #1.
5. **Condition Filter** - Configure its Condition attribute to @Data.mySequenceColumn~ = 1 which will remove all rows except Row #1, the most recent bookmark.

Now that you've retrieved and isolated the most-recently saved bookmark data, you need to run the bookmark:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563203991/introbm_36.png)

The elements shown above will reload the report with the appropriate request variables.

1. **Division** - This container is used to prevent endless recursive reloading of the report; set its **Condition** attribute to "@Request.rdBookmarkID~" = "".
2. **Image** - Create and use a 1-pixel x 1-pixel transparent image (which will not be visible in the report).
3. **Event Handler** - Set this to handle the DHTML onLoad event.
4. **Action.Run Bookmark** attributes:   
   - **Bookmark Collection** = leave this blank if you configured it in \_Settings > General.  
   - **Bookmark ID** = @Local.BookmarkID~.  
   - **Report Definition File** = the name of this report definition (do not select *Current Report*).
5. **Target.Run Bookmark -**  No attribute settings.

When run, your report will load, then immediately reload itself with the most-recently saved bookmark applied to it.
