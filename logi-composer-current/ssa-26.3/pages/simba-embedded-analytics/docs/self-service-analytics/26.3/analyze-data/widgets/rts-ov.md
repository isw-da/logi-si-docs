> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Rich Text Snippets

Add rich text snippets to your Self-Service Analytics dashboards to round out your users' data experience.

Annotate your dashboard by:

* Describing the data on your dashboard in context
* Link external resources, such as user guides, or images
* Use Self-Service Analytics to generate a visual summary for one or more visuals in a dashboard

Update your dashboards with rich text snippets any time using the Self-Service Analytics UI, or the dashboard API. Each rich text snippet resides in its own widget; resize and adjust placement of snippets to complement your visuals.

<Note>
  When you create a rich text snippet, it is linked to the dashboard you have added it to. If you delete a dashboard, the snippet is deleted as well.
</Note>

For more information on creating and managing rich text snippets, see the following topics:

* [Add Rich Text Snippets to a Dashboard](#add-rich-text-snippets-to-a-dashboard)
* [Format Rich Text Snippets](#format-rich-text-snippets)
* [Edit Rich Text Snippets](#edit-rich-text-snippets)
* [Copy Rich Text Snippets](#copy-rich-text-snippets)
* [Export Rich Text Snippets](#export-rich-text-snippets)
* [Delete Rich Text Snippets](#delete-rich-text-snippets)
* [Use the Rich Text Snippet Menu](#use-the-rich-text-snippet-menu)

<h2 id="add-rich-text-snippets-to-a-dashboard">
  Add Rich Text Snippets to a Dashboard
</h2>

When you create a dashboard or edit an existing dashboard, you can add rich text snippets to provide context to the visuals for your users.

You can fully author your own rich text snippet, or have Self-Service Analytics generate visual description and add it to your dashboard in a rich text snippet.

<Note>
  When you create a rich text snippet, it is linked to the dashboard you have added it to. If you delete a dashboard, the snippet is deleted as well.
</Note>

### Blank Rich Text Snippet

**Create a** **blank rich text snippet**

1. [Create](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards) or [edit](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard) a dashboard.

   * To add a snippet to an existing dashboard, log in as a user with `READ` and `WRITE` permissions for the dashboard.
   * If you are creating a new dashboard, log in as a user with the **Create Dashboards** or **Administer Dashboards** [group privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/rts-add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=b69f086e70f0d10816d924ba9225dc95" alt="select to add a rich text snippet" width="28" height="28" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '28px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/rts-add.png" /> on the [dashboard icon bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons). A blank, new rich text snippet is added in a widget on the dashboard, ready to edit.

3. Add text or other information in the snippet, using the [snippet format tools](#format-rich-text-snippets) to adjust the look and layout of your text, or add images and links.

   As you add and update your text, use keyboard shortcuts to undo and redo formatting changes. If you employ custom attributes in your environment, incorporate them as needed.

4. When you have added the information you need, select the edit icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit3green.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=a1c340832a61f6658f2289ec95e7620c" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit3green.png" />) to hide the format tools and put the snippet in view mode.

5. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save) the dashboard.

<h4 id="describe-visual-generate-visual-summary-description">
  Describe Visual (Generate Visual Summary Description)
</h4>

**Generate and insert** **a rich text snippet with a visual summary description**

1. [Create](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards) or [edit](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard) a dashboard with one or more visuals.

   * To add a snippet to an existing dashboard, log in as a user with `READ` and `WRITE` permissions for the dashboard.
   * If you are creating a new dashboard, log in as a user with the **Create Dashboards** or **Administer Dashboards** [group privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#visual-drop-down-menu), and choose **Describe Visual > Create Snippet and Insert**. A new rich text snippet is added in a widget on the dashboard with the text of the visual summary description, ready to edit. Other options include:

   * **Describe Visual > Copy Visual Summary**: This copies the summary to your clipboard. You can add it to an existing rich text snippet, or use it outside of the Simba Self-Service Analytics environment as needed.

   * **Describe Visual > Create Snippet and insert**: This creates a new snippet for this visual summary description, or the first snippet for this dashboard.

   * **Describe Visual > Insert into \[Existing Snippet Name]**: This inserts the visual summary description into the selected snippet when a rich text snippet that exists is selected.

     <Note>
       If more than one rich text snippet widget exists, you can select the appropriate snippet from a list.
     </Note>

3. Add more text or other information in the snippet, using the [snippet format tools](#format-rich-text-snippets) to adjust the look and layout of your text, or add images and links.

   As you add and update your text, use keyboard shortcuts to undo and redo formatting changes. If you employ custom attributes in your environment, incorporate them as needed.

4. When you have added the information you need, select the edit icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit3green.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=a1c340832a61f6658f2289ec95e7620c" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit3green.png" />) to hide the format tools and put the snippet in view mode.

5. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save) the dashboard.

<Note>
  Visual Description is [a menu option](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#visual-drop-down-menu) available for most, but not all visuals.
</Note>

<Note>
  Any changes you make to a visual will be reflected in the generated visual summary description after you save your work with the updates.
</Note>

<h2 id="edit-rich-text-snippets">
  Edit Rich Text Snippets
</h2>

Edit rich text snippets quickly and easily in a dashboard. Update links, reformat text, or add images as needed.

**Edit a rich text snippet**

1. Select the snippet on the dashboard. A blue border appears around the snippet widget.
2. Select the edit pencil (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit3green.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=a1c340832a61f6658f2289ec95e7620c" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit3green.png" />) in the widget, or <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit4gry.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=87563143361325e376add708486db9b2" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit4gry.png" />**Edit** from the drop-down menu (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />). The rich text snippet opens for editing.
3. Make your content and [format](#format-rich-text-snippets) changes.
4. When you have finished making changes to the snippet, select the edit pencil (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit3green.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=a1c340832a61f6658f2289ec95e7620c" alt="" width="24" height="24" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '24px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit3green.png" />) to hide the format tools and put the snippet in view mode.
5. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-save) the dashboard.

<h2 id="copy-rich-text-snippets">
  Copy Rich Text Snippets
</h2>

Make a copy of a selected rich text snippet by selecting **Copy** on the [rich text snippet drop-down menu](#use-the-rich-text-snippet-menu). This creates a copy of the last saved version of the snippet on your dashboard.

**Copy a rich text snippet**

1. Select the snippet on a dashboard. A blue border appears around the widget.

2. Select **Copy** on the [rich text snippet drop-down menu](#use-the-rich-text-snippet-menu).

   A copy of the rich text snippet appears on the dashboard in its own widget. Its initial name is the same as the original snippet, with an incremented number added to the end of the name. For example, if the original name was **Sales Data Parameters**, the initial name of the first copied snippet is **Sales Data Parameters (1)**.

<Note>
  When you create a rich text snippet, it is linked to the dashboard you have added it to. If you delete a dashboard, the snippet is deleted as well.
</Note>

<h2 id="delete-rich-text-snippets">
  Delete Rich Text Snippets
</h2>

You can remove rich text snippets from dashboards if you no longer need it.

**Remove a rich text snippet from your dashboard**

1. Edit the dashboard. See [Edit a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#edit-a-dashboard).
2. Select the rich text snippet to be removed.
3. Select **Remove Widget** on the [rich text snippet drop-down menu](#use-the-rich-text-snippet-menu). A removal confirmation dialog opens.
4. Select **Delete** on the warning dialog to confirm the deletion.

<h2 id="export-rich-text-snippets">
  Export Rich Text Snippets
</h2>

You can export your rich text snippet as a screenshot or as a PDF to share with others.

Rich Text Snippets can be exported in the following formats:

* PNG Screenshot (as an image)
* PDF file (as an image)

**Export a rich text snippet**

1. Select **Export** from the [rich text snippet drop-down menu](#use-the-rich-text-snippet-menu). A submenu opens: select an export format.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/textsnippets/rts-export-menu-22-4.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=923fad65c623a7410678d3ea2ab7b15e" alt="select an option to export rich text snippets" width="288" height="197" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/textsnippets/rts-export-menu-22-4.png" />

2. Select a format on the submenu.

   * If you select **Screenshot (PNG)**, the screenshot is prepared and automatically downloaded.

   * If you select **PDF**, the Export as PDF dialog opens.

     <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/textsnippets/rts-export-pdf-22-4.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=a5da4c8d0dfa178fbaa918086d49ebea" alt="enter export options to export your rich text snippet" width="288" height="178" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/textsnippets/rts-export-pdf-22-4.png" />

3. Optionally, specify a header and footer for the PDF. Slide the **Add Username** switch on (to the right) to add a user name to the PDF. Slide the **Add Timestamp** switch on (to the right) to add a time stamp to the PDF. Then select **Export**. The PDF is prepared and automatically downloaded.

<h2 id="format-rich-text-snippets">
  Format Rich Text Snippets
</h2>

Use rich text snippets to enhance your users' dashboard experience by describing the data on your dashboard in context, linking external resources such as user guides, or adding images. Format rich text snippets to give your dashboard a smoothly integrated look and feel, using colors and images to complement your visual data.

As you add and update your text, use keyboard shortcuts to undo and redo formatting changes. If you employ custom attributes in your environment, incorporate them as needed.

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/textsnippets/rts-format-menu-22-4.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=cdf54be6093528e33b96b816d76ed12f" alt="use to format the look and feel of your rich text snippets" width="470" height="50" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/textsnippets/rts-format-menu-22-4.png" />

Format options include:

<table>
  <thead>
    <tr>
      <th>Formatting Option</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Text Style (Paragraph Level Format)</td>

      <td>
        Three text style options are available for formatting the text of your snippet at the paragraph level. After making a selection, you can apply additional format options as needed.

        <br />

        * **Body**: Default text format.
        * **Header 1**: A bold text format, larger than **Body** and **Header 2**.
        * **Header 2**: A bold text format, larger than **Body** and smaller than **Header 1**.
      </td>
    </tr>

    <tr>
      <td>Text Color</td>

      <td>
        Apply a color to selected text. There are five ways to select a color:

        <br />

        * Color Picker: Select a color; the **Hex** and **RGB** fields update to indicate color code information.
        * Color Slider: Select a color; the **Hex** and **RGB** fields update to indicate color code information.
        * **Hex**: Enter a color by hexadecimal color code number.
        * **RGB**: Enter a color by **R G B** color code number.
        * Color Presets: Select a preset color; the **Hex** and **RGB** fields update to indicate color code information.
      </td>
    </tr>

    <tr>
      <td>Background Color</td>

      <td>
        Apply a background color to selected text. There are five ways to select a background color:

        <br />

        * Color Picker: Select a color; the **Hex** and **RGB** fields update to indicate color code information.
        * Color Slider: Select a color; the **Hex** and **RGB** fields update to indicate color code information.
        * **Hex**: Enter a color by hexadecimal color code number.
        * **RGB**: Enter a color by **R G B** color code number.
        * Color Presets: Select a preset color; the **Hex** and **RGB** fields update to indicate color code information.
      </td>
    </tr>

    <tr>
      <td>Align</td>

      <td>
        Align your paragraphs. There are four alignment options:

        <br />

        * **Align Left**: Select to left align a paragraph.
        * **Align Center**: Select to center align a paragraph.
        * **Align Right**: Select to right align a paragraph.
        * **Align Justify**: Select to fully justify the alignment of a paragraph.
      </td>
    </tr>

    <tr>
      <td>Bold</td>
      <td>Apply bold formatting to selected text, if the default text style is not bold.</td>
    </tr>

    <tr>
      <td>Italic</td>
      <td>Apply italic formatting to selected text.</td>
    </tr>

    <tr>
      <td>Underline</td>
      <td>Underline the selected text.</td>
    </tr>

    <tr>
      <td>Bullet List</td>
      <td>Select to start a bulleted list. Alternatively, select text and convert it to a bulleted list of body text.</td>
    </tr>

    <tr>
      <td>Numbered List</td>
      <td>Select to start a numbered list. Alternatively, select text and convert it to a numbered list of body text.</td>
    </tr>

    <tr>
      <td>Add Link</td>

      <td>
        Select to insert a link to an external website. Opens the Add Link work area.

        <br />

        * Enter **Text** and a **Link** to an external URL to create a link.
        * If you're adding a link to selected text, that text is prefilled in the **Text** field.

        <br />

        <Note>
          Formatting applied to link text is converted to the browser's default link and visited link colors. On hover, an underline is shown under the link text.
        </Note>

        <br />

        To edit or remove the link, select the link while you are in edit mode and choose the **Edit** or **Remove** option.
      </td>
    </tr>

    <tr>
      <td>Add Image</td>

      <td>
        Select to insert an image. Opens the Add Image work area.

        <br />

        * Provide an **Image URL** to include an image; Self-Service Analytics imports the image into the rich text snippet.
        * If needed, provide **Alternative Text** for your image.
      </td>
    </tr>

    <tr>
      <td>Clear Formatting</td>
      <td>Select to clear color and font formatting (bold, italic, underline) from a paragraph.</td>
    </tr>
  </tbody>
</table>

<h2 id="use-the-rich-text-snippet-menu">
  Use the Rich Text Snippet Menu
</h2>

The rich text snippet menu includes options that help you modify and use rich text snippets in your dashboard. Access it by selecting<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> in the upper right corner of a rich text snippet widget.

The menu options are described in the following table.

<table>
  <thead>
    <tr>
      <th>Option</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Copy</td>

      <td>
        Select to make a copy of the saved version of the selected rich text snippet.

        <br />

        See [Copy Rich Text Snippets](#copy-rich-text-snippets).
      </td>
    </tr>

    <tr>
      <td>Edit</td>
      <td>Select to open the selected rich text snippet for editing, or if it is open for editing, put it in view mode.</td>
    </tr>

    <tr>
      <td>Export</td>

      <td>
        Export the selected rich text snippet.

        <br />

        See [Export Rich Text Snippets](#export-rich-text-snippets).
      </td>
    </tr>

    <tr>
      <td>Maximize</td>
      <td>Select to maximize the selected rich text snippet on the dashboard for optimal viewing.</td>
    </tr>

    <tr>
      <td>Minimize</td>
      <td>Select to minimize the selected rich text snippet so you can see other visuals and rich text snippets on the dashboard.</td>
    </tr>

    <tr>
      <td>Settings</td>

      <td>
        Open the sidebar menu for the selected rich text snippet. Edit the display name, optional description, and to define header behavior. The default Header setting is **Show**; this displays the header at all times.

        <br />

        **Show on Hover** hides the header in [Viewer mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-dashboard-view-mode) unless users perform a hover action over the widget where the header is temporarily hidden. **Hide** completely hides the header from visibility in Viewer mode.
      </td>
    </tr>

    <tr>
      <td>Remove Widget</td>

      <td>
        Remove the selected rich text snippet from the dashboard.

        <br />

        See [Delete Rich Text Snippets](#delete-rich-text-snippets).
      </td>
    </tr>
  </tbody>
</table>
