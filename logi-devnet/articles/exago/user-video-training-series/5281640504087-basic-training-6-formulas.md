---
title: "Basic Training 6. Formulas"
id: 5281640504087
section: "User Video Training Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281640504087-Basic-Training-6-Formulas
updated_at: 2022-05-03T22:07:35Z
---

# Basic Training 6. Formulas

# Basic Training 6. Formulas

[Previous: Formatting](https://devnet.logianalytics.com/hc/en-us/articles/5281663440791-Basic-Training-5-Formatting)

[Next: CrossTabs](https://devnet.logianalytics.com/hc/en-us/articles/5281633248791-Basic-Training-7-CrossTab-Reports)

## Transcript

Welcome back to the Exago Video Training Series! Today we’ll be exploring formulas which allow us to modify a given cell’s contents. We’re currently looking at a report displaying product sales grouped by their order number.

The ‘discontinued’ field will display a 1 if a product is discontinued, and a 0 otherwise. 1’s and 0’s won’t look great on our report output, so we can use a formula to display it in a more clear manner. Let’s select the cell under the discontinued header, then open our formula editor by clicking the F of X icon.

The formula editor gives access to data fields on the left pane, and on the right we can see various categories of functions. Functions will take a specified number of input values, and give back a new value based off the input. We can click into any category to see a list of functions, or use the search bar. In this case, I’ll search for the ‘if’ function. Notice we’re provided with a description of the function here to let us know what input it needs, as well as what the function will output. Our ‘if’ function needs three inputs. The first is a condition that must become either true or false – in this case, we’ll check if our ‘discontinued’ field is equal to 1. We can drag fields from the left menu, or begin typing and let the editor auto-complete the field for us. If our first condition is true – if our discontinued field is equal to 1 – our cell will show the second input. So if the product has been discontinued, let’s output a simple ‘yes’. Since our output is static text, we’ll need to surround it with quotes like so. Finally, our third input will be displayed if the first condition is false. So if the product hasn’t been discontinued, we’ll output ‘no’, again wrapped in quotes.

Now that our if() function is completed, hitting okay will exit the formula editor. We can see the formula we just built now displays in our editor.

For each product sale we’ll generate some revenue, however to see the final revenue per product, we need to subtract any discount we provide from the revenue per product. We’ll go into our formula editor here add the revenue field, and then subtract the discount field with the subtraction operator like so.

Next let’s add a count of the number of products per order, and the final revenue summed per order as well. We’ll highlight an available cell in our group footer on order number, open our formula editor, and dig into the aggregate category. I’ll add the AggCount function, and call it on my product name field. Because we’re in a group footer on order number, this will count the number of products per order. Hitting okay, we can now use another cell in our group footer to add an aggsum function. We want to sum the final revenue, which is revenue minus discount. We’ve already calculated final revenue per product in cell D6. Navigating into our formula editor, we can add our aggsum, and reference the revenue cell in our formula using a capital D and a 6, surrounded by square brackets. This cell will now show us the total revenue per order.

We’ve got a product count and revenue sum for each order, but we might want to see those values across the entire report as well. Holding control, I can click and drag to copy both my AggCount and aggsum formulas down to my report footer. Formulas know what section they’re being called from. This means the aggcount/sum in our group footer will get order totals, while the aggcount/sum in the report footer will get report wide totals, despite the two sets of formulas being identical. This highlights the importance of sections we mentioned earlier in this series. As we now have the calculations we need, we can also use formulas to join and format both date and text fields.

We can add each customer’s name and title so we know who each order is going to. I’ll highlight this cell and open my formula editor, and add the contact name field. Next I’d like to concatenate, or join together, the contact name with contact title, and include a comma in between. The & acts as a concatenate operator and will combine whatever is directly to the left with whatever is directly to the right, so I’ll add an &, and then a comma in quotes as its static text. I can then add another &, and now I’ll add my contact title field. This formula will now display the contact name, a comma, and then the contact title.

Finally let’s add the month of each order to the header on order number. We’ll go into our formula editor, and dig into our date functions category. We’ll first add the monthname function, which outputs the month given an input date. We’ll give the function the order date field. We can now hit okay, and execute our report.

Looking at the output, we can see the order month displayed in the top right of each order. For each product in an order, we can see whether or not that product has been discontinued, and the final revenue after subtracting the discount. We can see the number of products and total revenue per order, the customer contact and title, and the overall total products and revenue at the bottom of our report.

This concludes our discussion on formulas. Be sure to check out our segments on charting and CrossTabs, and as always, Happy Reporting!
