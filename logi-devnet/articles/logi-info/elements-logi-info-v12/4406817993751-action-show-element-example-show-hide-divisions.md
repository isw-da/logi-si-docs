---
title: "Action.Show Element Example: Show/Hide Divisions"
id: 4406817993751
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817993751-Action-Show-Element-Example-Show-Hide-Divisions
updated_at: 2022-04-06T06:09:31Z
---

# Action.Show Element Example: Show/Hide Divisions

# Action.Show Element Example: Show/Hide Divisions

This example provides the functionality shown in [Action.Show Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822584343-Action-Show-Element): showing and hiding links in the DevNet Developer Library Index. The example actually includes three links that can be clicked to activate the Action.Show Element element: a"right arrow" image, a"down arrow" image, and the A-E text link itself.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563025687/showelement_02.png)

1. Add a **Division** element to contain the "right arrow", as shown above. Set its **Show Modes** attribute to *All.*
2. Beneath it, add the actual right arrow image and beneath it, an **Action.Show Element** element.
3. We'll have three divisions that are affected by the Action.Show Element element, so all of their element IDs are entered, as a comma-separated list, into the **Element ID** attribute, as shown above.
4. The **Display** attribute is set to *Toggle* so that we get alternating show/hide behavior.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575498903/showelement_03.png)

5. Add a **Division** for the "down arrow" and repeat the previous steps, as shown above. Set the new division's Show Modes attribute to *None.* Be sure to give the new division an Element ID that is in the comma-separated list of element IDs for the Action.Show Element element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583674519/showelement_04.png)

6. Add **Space** and **Label** elements, as shown above.
7. The Label will become the A-E text link, so add an Action.Show Element element beneath it and set its attributes as shown. Be sure to specify the IDs of the three divisions in a comma-separated list in the Element ID attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575499287/showelement_05.png)

8. Finally, add the last **Division** element, as shown above, and beneath it add the detail text to be shown and hidden. Set the new division's **Show Modes** attribute to *None.* Be sure to give the new division an Element ID that is in the comma-separated list of element IDs for the Action.Show Element elements.

By setting the Show Modes attributes to *All* or *None*, you determine which divisions will be initially shown and which hidden. The Action.Show Element element works by overriding these Show Modes settings. The values *All* and *None* are just arbitrary text, so you can use whatever values make sense in the specific situation.

Preview the report and you'll see how the divisions are shown or hidden when the images or link are clicked.
