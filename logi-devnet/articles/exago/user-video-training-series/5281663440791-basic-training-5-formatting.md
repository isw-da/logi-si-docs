---
title: "Basic Training 5. Formatting"
id: 5281663440791
section: "User Video Training Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281663440791-Basic-Training-5-Formatting
updated_at: 2022-05-03T22:07:35Z
---

# Basic Training 5. Formatting

# Basic Training 5. Formatting

[Previous: Sections](https://devnet.logianalytics.com/hc/en-us/articles/5281640445591-Basic-Training-4-Sections)

[Next: Formulas](https://devnet.logianalytics.com/hc/en-us/articles/5281640504087-Basic-Training-6-Formulas)

## Transcript

Welcome back to the Exago Video Training Series. Today’s video will focus on formatting in the advanced report designer.

We’re currently looking at an advanced report that will display order information grouped by employee last names, with revenue being totaled for each employee, and once across the entire report. Let’s hop over to our editor tab and apply some formatting this report.

We can select any existing cell to format by left clicking, and we’ll see the cell is now highlighted blue. Our formatting bar will allow us to bold, italicize, or underline the cell’s contents. Let’s bold our last name header so it’s a clear label for the detail rows it precedes. We can bold our revenue sums so they stand out a bit as well.

We have the ability to change our cell’s foreground and background colors, so let’s give our column labels a soft turquoise background, and a white foreground. After I’ve modified one cell’s formatting, I can select the format paintbrush, then select another cell to copy my formatting changes over. Additionally, if I select a cell, hold shift, and select another cell, Exago will highlight all cells in between. Now we can apply formatting changes to all the selected cells.

We can change the font we use for any given cell, and change the font size as well. Let’s bump up the font of our last name headers and our revenue sums. We can hold control and click to select multiple disjoint cells, and now our font size changes will be applied to both our headers and our sums.

Our format cells icon dictates how a cell’s actual contents will be formatted. General will automatically apply default formatting, number allows us to modify how numeric values will appear, date allows us to format dates in any .NET standard format, and finally text will not apply any formatting to the cell contents. Since we’re showing revenue and unit price, both of which are numeric dollar amounts, let’s select the appropriate cells, and set the cell format to number, use a currency symbol, and verify we have 2 decimal places.

The format cells icon also allows us to apply borders to any selected cell. Let’s add some borders to our revenue totals to help them stand out.

The last piece of the format cells menu is conditional formatting, where modifications will be made only if a certain condition is met  – check out our segment on conditional formatting for more info there.

Next we can modify how our cell contents are aligned, both horizontally and vertically. Let’s center align our detail information so it appears directly beneath the column headers here.

We have our merge cells icon here which takes the cells we’ve selected and combines them into one larger cell. Let’s merge the cells on row 4 so our last name header has more room. We can do the same to our revenue totals as well. After cells have been merged, we can break them up again using our split cells icon here.

Finally, let’s add alternate row shading to our detail information. As you may recall from our discussion on sections, we’ll accomplish this by clicking the section, selecting ‘section shading’, and specifying the colors we’d like to use.

Executing our report, we can see the final formatted result. Comparing this back to our initial report execution, we can see our formatting changes improve both the report’s clarity and aesthetics.

This concludes our discussion on formatting. Be sure to check out our segment on conditional formatting, and as always, Happy Reporting!
