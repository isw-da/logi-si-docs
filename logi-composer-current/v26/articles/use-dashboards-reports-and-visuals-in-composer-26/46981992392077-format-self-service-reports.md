---
title: "Format Self Service Reports"
id: 46981992392077
section: "Use Dashboards, Reports  and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46981992392077-Format-Self-Service-Reports
updated_at: 2026-08-26T07:12:52Z
---

# Format Self Service Reports

# Format Self Service Reports

## Header and Footer Formatting

Format the header and footer rich text snippet widgets of your self service report to provide information about the report data. Provide context, link external resources, or add images.

As you add and update your text, use keyboard shortcuts to undo and redo formatting changes. If you employ custom attributes in your environment, incorporate them as needed.

![use to format the look and feel of this widget](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48417946772237 "Format Menu")

Format options include:

| Formatting Option | Description |
| --- | --- |
| Text Style (Paragraph Level Format) | Three text style options are available for formatting the text of your snippet at the paragraph level. After making a selection, you can apply additional format options as needed.   * **Body**: Default text format. * **Header 1**: A bold text format, larger than **Body** and **Header 2**. * **Header 2**: A bold text format, larger than **Body** and smaller than **Header 1**. |
| Align | Align your paragraphs. There are four alignment options:   * **Align Left**: Select to left align a paragraph. * **Align Center**: Select to center align a paragraph. * **Align Right**: Select to right align a paragraph. |
| Bold | Apply bold formatting to selected text, if the default text style is not bold. |
| Italic | Apply italic formatting to selected text. |
| Underline | Underline the selected text. |
| Bullet List | Select to start a bulleted list. Alternatively, select text and convert it to a bulleted list of body text. |
| Numbered List | Select to start a numbered list. Alternatively, select text and convert it to a numbered list of body text. |
| Add Image | Select to insert an image. Opens the Add Image work area.   * Provide an **Image URL** to include an image; Composer imports the image into the rich text snippet (header or footer). * If needed, provide **Alternative Text** for your image.   **Note:** Keep your header and footer image sized between 200kb and 500kb for [optimal rendering](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#File) performance. |
| Clear Formatting | Select to clear color and font formatting (bold, italic, underline) from a paragraph. |

## Conditional Formatting

[Conditional formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting) increases report generation time significantly. A report with conditional formatting can take from twice as long to significantly longer than an equivalent report without it. Conditional formatting in complex reports exported to PDF format place a higher load on your environment, resulting in a percentage of error rates.

Self service reports support conditional formatting on reports with and without [grouped data](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183802381-Group-and-Ungroup-Table-Data). You can apply conditional formatting rules as you would for a table visual. See [Configure Conditional Formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183616525-Configure-Conditional-Formatting).

![Use the conditional formatting sidebar menu to apply conditional formatting to data and grouped data](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48417965423373 "Self Service Report work area, with conditional formatting example")
