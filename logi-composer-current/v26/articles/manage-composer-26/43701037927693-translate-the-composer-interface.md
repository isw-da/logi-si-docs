---
title: "Translate the Composer Interface"
id: 43701037927693
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701037927693-Translate-the-Composer-Interface
updated_at: 2026-05-29T14:11:35Z
---

# Translate the Composer Interface

# Translate the Composer Interface

You can translate the Composer interface into other languages. Composer supports standard i18n languages. See <https://perldoc.perl.org/I18N::LangTags::List#LIST-OF-LANGUAGES>.

**Note:** 
To translate the interface, you must have a specific advanced setting switched on. Please contact technical support for information about this setting.

Translation files in the format `vocabulary-<xx>_<YY>.json` are used in the translation. The English translation file is provided and is named `vocabulary-en_US.json`.

* Linux Environments: Located in the `/opt/zoomdata/client/i18n` folder.
* Windows Environments: Located in the `<install-path>/client/i18n` folder.

**Translate the** Composer **interface:**

1. Locate and copy the provided English translation file `vocabulary-en_US.json` in the appropriate `/client/i18n` folder.
2. Rename the copy of the file. Be sure to name it in the format `vocabulary-<xx>_<YY>.json`, where `<xx>` is a two-character code representing the language you want to use and `<YY>` is the dialect. See <https://perldoc.perl.org/I18N::LangTags::List#LIST-OF-LANGUAGES>.
3. Translate the JSON values to the right of the JSON keys (after the colon) in the file. All values should be specified in quotes. The JSON keys should not be translated because the keys are used by the Composer code.

   Here is an example of part of a translated translation file:

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242757999245)

   This file is CSS-friendly. For example, `<b>` and `</b>` around a JSON value or part of a value indicate that the value should be bold.

   Finally, placeholders (variables) are used throughout the file and should not be changed or removed, although they can be relocated within a JSON value, as needed for your translation. Placeholders appear surrounded by `%` symbols (for example, `%name%`) in the translation file. Composer code inserts a value for these placeholders, based on where the JSON key is used in the product. For example, a dashboard name might be inserted for the placeholder `%name%` for one JSON key, but a visual name might be inserted for a different JSON key that also uses the `%name%` placeholder.
4. Save your translated file.
5. Contact your insightsoftware [technical support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) representative for additional steps.

**Note:** 
If you import an exported source that has an associated translation file, you must re-upload the translation for that source.
