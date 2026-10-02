> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Themes JSON File

<Warning>
  In this release, when you [enable the Enhanced Experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) user interface, users see changes to workflows and the user interface. The classic themes require updates to allow your users to see a consistent color scheme. For more information, see [Expand a Theme to Support the Enhanced Experience](#expand-a-theme-to-support-the-enhanced-experience) and [Themes and UI Updates](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#themes-and-ui-updates). If you're working in an earlier version of this analytics environment, see [JSON File Example Updates (Earlier Releases)](#json-file-example-updates-earlier-releases).
</Warning>

<h3 id="json-file-updates">
  JSON File Updates
</h3>

Work with an existing theme by downloading it, then updating a copy appropriately for your desired color scheme.

<table>
  <thead>
    <tr>
      <th>Theme Plan</th>
      <th>Actions Required</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>You want to design a new color theme, using an existing enhanced-experience theme as a template.</td>

      <td>
        * Download the `d+a_light` theme or other theme that supports the enhanced-experience interface. Edit as needed for your desired colors.

        <br />

        * Remove the `"system": true` and `"id": "<string>"` properties from the downloaded JSON file before you use it to create your new theme.

        <br />

        <Danger>
          If you don't remove these items, you may overwrite the system themes, and in turn, have your updates overwritten by subsequent software version updates. Self-Service Analytics automatically generates an ID for the theme and sets the value of the `"system"` property when the API request to create the theme is processed.
        </Danger>

        <br />

        * Make your changes. Optionally update specific objects in addition to your overall colors design. See [Update Specific Items in Your Theme](#update-specific-items-in-your-theme).

        <br />

        * Once complete, add to your environment and activate it. See [Activate a Theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#activate-a-theme).
      </td>
    </tr>

    <tr>
      <td>You want to update a standard or custom classic color theme, using an existing classic theme as a template.</td>

      <td>
        * Download your custom classic theme or standard classic theme.
        * Add the sample code provided in [JSON Updates to Support Enhanced Experience UI](#json-updates-to-support-enhanced-experience-ui).
        * Edit as needed for your desired colors. Update the content.customProperties.homePage and content.customProperties.navbar.sidebar sections.
        * Optionally update specific objects in addition to your overall colors design. See [Update Specific Items in Your Theme](#update-specific-items-in-your-theme).
        * Remove the `"system": true` and update the `"id": "<theme-id>"` and `"name": "<theme-name>"` properties to match the downloaded JSON file.
        * Make your changes, and follow the instructions to PATCH these updates to the theme you want to use in your environment and activate it. See [Patch a Theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#patch-a-theme).
      </td>
    </tr>
  </tbody>
</table>

First, find the `id` of your theme, then [download that theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#review-and-download-the-theme-json-code) from your environment. Use it as a template as described in the table above to make appropriate changes to deploy your color selections.

To find your currently active theme `id`, use the `/api/customization/themes/active` API endpoint with a `GET` call.

<Note>
  You can only tailor theme colors. Other tailoring properties (such as fonts or font sizes) should not be changed.
</Note>

<h4 id="expand-a-theme-to-support-the-enhanced-experience">
  Expand a Theme to Support the Enhanced Experience
</h4>

If you're upgrading from a previous environment to v26.2 or later, you can activate the `d+a_light` theme, or edit the `d+a_light` theme to suit your needs and use the enhanced experience UI.

Alternatively, you can take your existing classic theme and PATCH it by updating appropriate values for your existing theme using the sample below and adding it to your environment using a PATCH command to the themes API endpoint.

These updates are needed to support the new interface features that are a part of enabling the enhanced experience. See [Themes and UI Updates](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#themes-and-ui-updates).

<Danger>
  Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.2. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.
</Danger>

<h4 id="json-updates-to-support-enhanced-experience-ui">
  JSON Updates to Support Enhanced Experience UI
</h4>

Update this sample with your appropriate `id`, `name`, and other updates, then PATCH to your staging environment to test before deployment to production. See [Themes and UI Updates](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#themes-and-ui-updates).

```json theme={null}
{
  "id": "<theme-id>",
  "name": "<theme-name>",
  "content": {
    "customProperties": {
      "homePage": {
        "banner": {
          "background": "$colors.surface",
          "color": "$colors.onSurface",
          "mixBlendMode": "lighten"
        },
        "color": "$colors.onSurface",
        "menuCard": {
          "background": "$colors.surface",
          "color": "$colors.onSurface"
        },
        "title": "$colors.onSurface"
      },
      "navbar": {
        "sidebar": {
          "background": "$colors.primaryVariant",
          "iconColor": "$symphony.colors.white",
          "tabBg": "transparent",
          "tabBgActive": "$symphony.colors.slate.700",
          "tabBgHover": "$symphony.colors.slate.700"
         }
       }
     }
  }
}
```

<h4 id="update-specific-items-in-your-theme">
  Update Specific Items in Your Theme
</h4>

To change colors used for a specific visual type or a table, use the following substitutions.

| Substitution | Description |
| - | - |
| `<visual-type>` | Specify one of the following: `UBER_BARS`, `SCATTERPLOT`, `PIE`, `MULTI_METRIC_BARS`, `LINE_AND_BARS`, `HISTOGRAM`, `HEAT_MAP`, `FLOATING_BUBBLES`, `DONUT`, `BOX_PLOT`, or `LINE_CHART`. |
| `<table-type>` | Specify one of the following: `RAW_DATA_TABLE` or `PIVOT_TABLE`. |
| `<charts-color-parameter>` | Specify one of the base color parameters from the `"charts"` section of the JSON file to change for the selected `<visual-type>`. For example, `"axisLabelColor"`. |
| `<tables-color-parameter>` | Specify one of the base color parameters from the `"tables"` section of the JSON file to change for the selected `<table-type>`. For example, `"background"`. |
| `<newsetting>` | Specify the new color setting for the `<charts-color-parameter>` or the `<tables-color-parameter>`. |
| `<your-palette>` | Specify a name for your color palette, if you choose to add your own, personalized, palette to the environment. Palette names can be referenced in the `palette` property in the `customProperties` section of the JSON under `charts`. They can also be referenced in the `palette` property for individual visual types (`<visual-type>` sections) under `charts`. |
| `<hexcolorn>` | Specify the hexadecimal representation of up to 9 colors (where `n` ranges from 1 to 9) for your personalized color palette. |
| `<color-palette-name>` | Specify the name of a [supplied color palette](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors#supplied-color-palettes) or a color palette defined in this JSON file. |

You can specify color settings for more than one visual type or table type. You can also specify more than one color setting for each type.

| Substitution | Description |
| - | - |
| `<visual-type>` | Specify one of the following: `UBER_BARS`, `SCATTERPLOT`, `PIE`, `MULTI_METRIC_BARS`, `LINE_AND_BARS`, `HISTOGRAM`, `HEAT_MAP`, `FLOATING_BUBBLES`, `DONUT`, `BOX_PLOT`, or `LINE_CHART`. |
| `<table-type>` | Specify one of the following: `RAW_DATA_TABLE` or `PIVOT_TABLE`. |
| `<charts-color-parameter>` | Specify one of the base color parameters from the `"charts"` section of the JSON file to change for the selected `<visual-type>`. For example, `"axisLabelColor"`. |
| `<tables-color-parameter>` | Specify one of the base color parameters from the `"tables"` section of the JSON file to change for the selected `<table-type>`. For example, `"background"`. |
| `<newsetting>` | Specify the new color setting for the `<charts-color-parameter>` or the `<tables-color-parameter>`. |
| `<your-palette>` | Specify a name for your color palette, if you choose to add your own, personalized, palette to the environment. Palette names can be referenced in the `palette` property in the `customProperties` section of the JSON under `charts`. They can also be referenced in the `palette` property for individual visual types (`<visual-type>` sections) under `charts`. |
| `<hexcolorn>` | Specify the hexadecimal representation of up to 9 colors (where `n` ranges from 1 to 9) for your personalized color palette. |
| `<color-palette-name>` | Specify the name of a [supplied color palette](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors#supplied-color-palettes) or a color palette defined in this JSON file. |

You can specify color settings for more than one visual type or table type. You can also specify more than one color setting for each type. For more information on themes, see [Manage User Interface Themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).

```json theme={null}
{
"id": "<string>",
"masterThemeId": "<supplied-theme-name>",
"name": "mytheme",
"system": true,
"content": {
  "variables":{
     "colors":{
        "accentColor": "rgba(19, 124, 189, 0.5)",
        "background": "#f7f7f7",
        "backgroundVariant": "#dedede",
        "border": "#cccccc",
        "brandColor": "#182C44",
        "intentBase": "#f7f7f7",
        "intentBaseActive": "#dedede",
        "intentBaseDisabled": "#e8e8e8",
        "intentBaseHover": "#f0f0f0",
        "intentDanger": "#db3737",
        "intentDangerActive": "#c23030",
        "intentDangerDisabled": "#a82a2a",
        "intentDangerHover": "#f55656",
        "intentMinimal": "#5c7080",
        "intentMinimalActive": "rgba(115, 134, 148, 0.3)",
        "intentMinimalDisabled": "rgba(167, 182, 194, 0.6)",
	"intentMinimalHover": "rgba(167, 182, 194, 0.3)",
	"intentPrimary": "#137cbd",
	"intentPrimaryActive": "#0e5a8a",
	"intentPrimaryDisabled": "rgba(19, 124, 189, 0.5)",
	"intentPrimaryHover": "#106ba3",
	"intentSuccess": "#89bb40",
	"intentSuccessActive": "#15b371",
	"intentSuccessDisabled": "#0a6640",
	"intentSuccessHover": "#3dcc91",
	"intentWarning": "#d9822b",
	"intentWarningActive": "#bf7326",
	"intentWarningDisabled": "#a66321",
	"intentWarningHover": "#f29d49",
	"linkColor": "#106ba3",
	"muted": "#999999",
	"onBackground": "#1d384b",
	"onBackgroundVariant": "#4a4a4a",
	"onPrimary": "#fff",
	"onSurface": "#1d384b",
	"primary": "#1d384b",
	"primaryVariant": "#30404d",
	"secondary": "#89bb40",
	"surface": "#fff",
	"text": "#4a4a4a"
     },
     "breakpoints":[
        "320px",
        "568px",
        "768px",
        "1024px",
        "1200px"
     ],
     "space":[
        0,
        4,
        8,
        16,
        32,
        64,
        128,
        256,
        512
     ],
     "fonts":{
        "body":"\"Source Sans Pro\", system-ui, sans-serif",
        "heading":"\"Source Sans Pro\", system-ui, sans-serif",
        "monospace":"Monaco, Menlo, \"Ubuntu Mono\", Consolas, source-code-pro, monospace"
     },
     "fontSizes":[
        12,
        14,
        16,
        18,
        24,
        32,
        48,
        64,
        72
     ],
     "fontWeights":{
        "lightest":100,
        "normal":400,
        "heading":500,
        "bold":700
     },
     "lineHeights":{
        "body":1.25,
        "heading":1.125
     },
     "sizes":{
        "sm":288,
        "md":532,
        "lg":736,
        "xl":960,
        "xxl":1136
     },
     "shadows":{
     },
     "radii":{
        "none":0,
        "default":3,
        "sm":2.4,
        "lg":3.6,
        "pill":600
     },
     "links":{
        "primary":{
           "color":"intentPrimary"
        }
     }
     "palettes": {
        "DefaultSequential": {
           "2": ["#ffc65f", "#0096b6"],
           "3": ["#ffc65f", "#9eb778", "#0096b6"],
           "4": ["#ffd27c", "#ccbd67", "#7eb184", "#008db6"],
           "5": ["#ffd27c", "#ccbd67", "#7eb184", "#0096b6", "#0082b5"],
           "6": ["#ffd27c", "#efc15e", "#9eb778", "#7eb184", "#0096b6", "#0082b5"],
           "7": ["#ffd27c", "#efc15e", "#9eb778", "#7eb184", "#43a79b", "#008db6", "#097bb1"],
           "8": ["#ffdc9c", "#ffc65f", "#efc15e", "#9eb778", "#7eb184", "#43a79b", "#008db6", "#097bb1"],
           "9": ["#ffdc9c", "#ffc65f", "#efc15e", "#9eb778", "#7eb184", "#43a79b", "#008db6", "#0082b5", "#1473ac"]
        },
 "<your-palette>": {
           "2": ["<hexcolor1>", "<hexcolor2>"],
           "3": ["<hexcolor1>", "<hexcolor2>", "<hexcolor3>"],
           "4": ["<hexcolor1>", "<hexcolor2>", "<hexcolor3>", "<hexcolor4>"],
           "5": ["<hexcolor1>", "<hexcolor2>", "<hexcolor3>", "<hexcolor4>", "<hexcolor5>"],
           "6": ["<hexcolor1>", "<hexcolor2>", "<hexcolor3>", "<hexcolor4>", "<hexcolor5>", "<hexcolor6>"],
           "7": ["<hexcolor1>", "<hexcolor2>", "<hexcolor3>", "<hexcolor4>", "<hexcolor5>", "<hexcolor6>", "<hexcolor7>"],
           "8": ["<hexcolor1>", "<hexcolor2>", "<hexcolor3>", "<hexcolor4>", "<hexcolor5>", "<hexcolor6>", "<hexcolor7>", "<hexcolor8>"],
           "9": ["<hexcolor1>", "<hexcolor2>", "<hexcolor3>", "<hexcolor4>", "<hexcolor5>", "<hexcolor6>", "<hexcolor7>", "<hexcolor8>", "<hexcolor9>"]
        }
     }
  },
  "customProperties":{
     "navbar":{
        "background":"$colors.primary",
        "colorInactive":"$colors.muted",
        "tabFontActive":"$colors.onPrimary",
        "tabHover":"rgba(138, 155, 168, 0.15)",
        "tabActive":"rgba(138, 155, 168, 0.3)",
        "tabBorderActive":"$colors.secondary",
        "menu":{
           "background":"$colors.primaryVariant",
           "color":"$colors.onPrimary",
           "itemActive":"$colors.intentPrimary",
           "itemHover":"$colors.intentMinimalHover",
           "divider":"rgba(255, 255, 255, 0.15)"
        }
     },
     "homePage":{
        "title":"$colors.muted",
        "color":"$colors.text",
        "menuCard":{
           "background":"$colors.surface",
           "color":"$colors.onSurface"
        }
     },
     "dashboard":{
        "background":"$colors.background",
        "header":{
           "background":"$colors.background",
           "text":"$colors.onSurface",
           "unsavedText":"$colors.muted",
           "controls":{
              "filterIcon":"#939393",
              "filterIconHover":"#7a7a7a",
              "filterActiveIcon":"#68AD45",
              "filterActiveIconHover":"#59933b"
           }
        }
     },
     "dashboardList": {
	 "background": "$colors.background",
 	"linkColor": "$colors.linkColor",
	"preview": {
            "background": "$colors.surface",
            "border": "#E6E6E6",
            "color": "#595959",
            "description": {
		"color": "#939393"
            },
            "details": {
		"propertyColor": "#b2b2b2",
		"valueColor": "#323232"
            },
            "shadow": "rgba(0, 0, 0, 0.2) 2px 2px 10px 0px",
            "title": {
		"background": "#D2D2D2",
		"color": "#595959"
            }
     }
     "input":{
        "background":"$colors.surface",
        "text":"$colors.text",
        "label":"$colors.text",
        "border":"$colors.border",
        "placeholder":"$colors.muted",
        "disabled":{
           "background":"$colors.intentMinimalDisabled"
        }
     },
     "multiSelect":{
        "background":"$colors.background",
        "color":"$colors.text",
        "tagBackground":"$colors.backgroundVariant",
        "tagColor":"$colors.onBackgroundVariant"
     },
     "datePicker":{
        "background":"$colors.surface",
        "color":"$colors.onSurface",
        "hover":{
           "color":"$colors.onSurface",
           "background":"$colors.intentMinimalHover",
           "active":{
              "background":"$colors.intentPrimaryHover"
           }
        },
        "divider":{
           "color":"$colors.border"
        }
     },
     "tooltip":{
        "background":"$colors.primaryVariant",
        "color":"$colors.onPrimary"
     },
     "radio":{
        "background":"$colors.surface",
        "border":"$colors.border",
        "selected":{
           "background":"$colors.intentPrimary",
           "border":"$colors.intentPrimary",
           "innerBackground":"#fff"
        }
     },
     "buttons":{
        "base":{
           "bg":"$colors.intentBase",
           "color":"$colors.text",
           "hover":{
              "bg":"$colors.intentBaseHover"
           },
           "active":{
              "bg":"$colors.intentBaseActive"
           }
        },
        "primary":{
           "bg":"$colors.intentPrimary",
           "color":"$colors.onPrimary",
           "hover":{
              "bg":"$colors.intentPrimaryHover"
           },
           "active":{
              "bg":"$colors.intentPrimaryActive"
           },
           "disabled":{
              "bg":"$colors.intentPrimaryDisabled"
           }
        },
        "minimal":{
           "bg":"initial",
           "color":"$colors.onSurface",
           "hover":{
              "bg":"$colors.intentMinimalHover"
           },
           "active":{
              "bg":"$colors.intentMinimalActive"
           },
           "disabled":{
              "color":"$colors.intentMinimalDisabled"
           }
        }
     },
     "popup":{
        "color":"$colors.text",
        "background":"$colors.surface",
        "closeBtn":"#999999",
        "closeBtnHover":"#7a7a7a"
     },
     "resourcesTable": {
	  "active": {
		"background": "#2481bc",
		"color": "$colors.onPrimary"
	  },
	  "background": "$colors.surface",
	  "border": "$colors.border",
	  "color": "$colors.onSurface",
	  "header": {
		"background": "#e7e7e7 linear-gradient(180deg,#fafafa,#f0f0f0)",
		"backgroundImage": "linear-gradient(rgb(250, 250, 250), rgb(240, 240, 240))",
		"color": "$colors.text",
		"secondaryColor": "$colors.muted"
	  },
	  "hover": {
		"background": "$colors.background",
		"color": "$colors.text"
	  },
	  "linkColor": "$colors.linkColor",
	  "visualIconColor": "#5c7080"
     },
     "schedule":{
        "list":{
           "bg":"$colors.surface",
           "border":"$colors.border",
           "item":{
              "bg":"$colors.surface",
              "color":"$colors.text",
              "hover":{
                 "bg":"$colors.intentBaseHover"
              },
              "active":{
                 "bg":"$colors.intentPrimary",
                 "color":"$colors.onPrimary"
              }
           }
        }
     },
     "menu":{
        "color":"$colors.text",
        "bg":"$colors.surface",
        "hover":{
           "color":"$colors.onSurface",
           "bg":"$colors.intentBaseHover"
        },
        "active":{
           "color":"$colors.onPrimary",
           "bg":"$colors.intentBaseActive"
        },
        "disabled":"$colors.intentMinimalDisabled",
        "icon":{
           "color":"$colors.intentMinimal",
           "active":{
              "color":"$colors.intentSuccess",
              "hover":{
                 "color":"#59933b"
              }
           },
           "delete":{
              "hover":{
                 "color":"$colors.intentWarning"
              }
           },
           "hover":{
              "color":"$colors.onSurface"
           }
        },
        "divider":{
           "color":"$colors.border"
        }
     },
     "list":{
        "border":{
           "color":"$colors.intentBaseActive"
        }
     },
     "metaDataPicker":{
        "color":"$colors.text",
        "secondary":"$colors.muted",
        "background":"$colors.surface",
        "item":{
           "border":"#dedede",
           "aggrHover":"#dedede",
           "hover":{
              "bg":"$colors.intentBaseHover"
           }
        }
     },
     "radialMenu":{
        "bg":"rgba(0, 0, 0, 0.7)",
        "color":"$colors.onPrimary",
        "hover":{
            "bg":"#000"
        },
        "removeBtn":{
           "color":"$colors.onPrimary",
           "bg":"#939393",
           "hover":{
              "bg":"#E5683A"
           }
        }
     },
     "chartLegend":{
        "background":"$colors.background",
        "color":"$colors.text"
     },
     "chartTooltip":{
        "background":"$colors.background",
        "color":"$colors.text"
     },
     "widget":{
        "background":"$colors.surface",
        "borderColor":"$colors.surface",
        "selected":{
           "borderColor":"$colors.accentColor"
        },
        "titleColor":"$colors.text",
        "label":{
           "background":"$colors.background",
           "color":"#323232",
           "hover":{
              "background":"#d8d8d8"
           }
        },
        "iconColor":"$colors.muted"
     },
     "visualEditor":{
        "background":"$colors.background",
        "color":"$colors.text",
        "secondaryColor":"$colors.muted",
        "borderColor":"$colors.border"
     },
     "select":{
        "color":"$colors.text",
        "background":"$colors.surface",
        "border":"$colors.border",
        "disabled":{
           "background":"$colors.intentMinimalDisabled"
        }
     },
     "charts":{
        "base":{
           "axisLabelColor":"$colors.text",
           "axisLabelShadow":"rgba(255, 255, 255, 0.3)",
           "axisLineColor":"$colors.text",
           "color":"$colors.text",
           "palette":"<color-palette-name>",
           "pointerColor":"$colors.text",
           "splitLineColor":"$colors.text"
        },
        "<visual-type>":{
           "<charts-color-parameter>":"<newsetting>",
            ...
         },
     },
     "tables":{
        "base":{
           "color":"$colors.onSurface",
           "background":"$colors.surface",
           "backgroundOdd":"#fcfdfe",
           "border":"#BDC3C7",
           "borderSecondary":"#d9dcde",
           "hover":{
              "background":"#ecf0f1"
           },
           "heading":{
              "color":"$colors.text",
              "colorSecondary":"$colors.muted",
              "background":"$colors.background"
           }
        },
        "<table-type>":{
           "<tables-color-parameter>":"<newsetting>",
            ...
         },
     },
     "timebar":{
        "backgroundColor":"$colors.backgroundVariant",
        "backgroundColorHover":"rgba(167,182,194,0.3)",
        "border":"$colors.border",
        "textColorHover":"$colors.text",
        "textColor":"$colors.onBackgroundVariant",
        "scrubber":{
           "backgroundColor":"#b1bfd2",
           "backgroundColorHover":"rgba(167,182,194,0.3)",
           "splitterColor":"$colors.border",
           "splitterColorHover":"$colors.border",
           "tickColor":"$colors.intentPrimary",
           "tickColorHover":"#b1bfd2",
           "textColor":"#333333",
           "textColorHover":"#b1bfd2",
           "animatedTickColor":"#b1bfd2",
           "tooltipDatePickerColor":"#555555",
           "tooltipDatePickerBackgroundColor":"$colors.intentPrimary",
           "datePickerColorMaximized":"$colors.intentPrimary",
           "datePickerColorMinimized":"#ffffff",
           "datePickerBackgroundColorMaximized":"$colors.intentPrimary",
           "datePickerBackgroundColorMinimized":"#b1bfd2"
        }
     },
     "dialog":{
        "color":"$colors.onBackgroundVariant",
        "background":"$colors.background",
        "footerBackground":"$colors.backgroundVariant"
     },
     "colorPalette":{
        "background":"$colors.background",
        "borderColor":"$colors.border",
        "selected":{
           "background":"$colors.intentPrimary"
        },
        "hover":{
           "background":"$colors.intentBaseHover"
        },
        "iconColor":"$colors.muted",
        "activeIconColor":"$colors.text",
        "draggingBackgroundColor":"$colors.background"
     }
  }
}
}
```

<h3 id="json-file-example-updates-earlier-releases">
  JSON File Example Updates (Earlier Releases)
</h3>

To [create your own theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#create-a-theme), first find the `id` of your theme, then [download that theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#review-and-download-the-theme-json-code) from your environment. Use it as a template to make appropriate changes to deploy your color selections.

To find your currently active theme `id`, use the `/api/customization/themes/active` API endpoint with a `GET` call.

<Note>
  You can only tailor theme colors. Other tailoring properties (such as fonts or font sizes) should not be changed.
</Note>

Be sure to remove the `"system": true` and `"id": "<string>"` properties from the JSON file before you use it to create a theme. Self-Service Analytics automatically generates an ID for the theme and sets the value of the `"system"` property when the API request to create the theme is processed.

You can specify a master theme in the theme JSON using the `masterThemeID` property. Master themes are optional, but allow you to identify the Self-Service Analytics-supplied theme from which properties should be inherited by a custom theme, if the properties are not specified in the custom theme JSON. Master themes can only be Self-Service Analytics- supplied themes. See [Supplied Themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#user-interface-themes-v26-3-and-later-supplied-themes).

Finally, if you are changing the colors used for a specific visual type or a table, use the following substitutions.

| Substitution | Description |
| - | - |
| `<visual-type>` | Specify one of the following: `UBER_BARS`, `SCATTERPLOT`, `PIE`, `MULTI_METRIC_BARS`, `LINE_AND_BARS`, `HISTOGRAM`, `HEAT_MAP`, `FLOATING_BUBBLES`, `DONUT`, `BOX_PLOT`, or `LINE_CHART`. |
| `<table-type>` | Specify one of the following: `RAW_DATA_TABLE` or `PIVOT_TABLE`. |
| `<charts-color-parameter>` | Specify one of the base color parameters from the `"charts"` section of the JSON file to change for the selected `<visual-type>`. For example, `"axisLabelColor"`. |
| `<tables-color-parameter>` | Specify one of the base color parameters from the `"tables"` section of the JSON file to change for the selected `<table-type>`. For example, `"background"`. |
| `<newsetting>` | Specify the new color setting for the `<charts-color-parameter>` or the `<tables-color-parameter>`. |
| `<your-palette>` | Specify a name for your color palette, if you choose to add your own, personalized, palette to the environment. Palette names can be referenced in the `palette` property in the `customProperties` section of the JSON under `charts`. They can also be referenced in the `palette` property for individual visual types (`<visual-type>` sections) under `charts`. |
| `<hexcolorn>` | Specify the hexadecimal representation of up to 9 colors (where `n` ranges from 1 to 9) for your personalized color palette. |
| `<color-palette-name>` | Specify the name of a [supplied color palette](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/colors-and-axes/colors#supplied-color-palettes) or a color palette defined in this JSON file. |

You can specify color settings for more than one visual type or table type. You can also specify more than one color setting for each type. For more information on themes, see [Manage User Interface Themes](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov).
