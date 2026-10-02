> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Visuals Using Visualization Variables

When a visual is embedded into a custom application, it uses the default settings determined by the metrics and fields or groups present in the data query that supplies the visual with data. For more information about configuring and creating a data query, see [Query Configuration Object](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#query-configuration-object) or [Use a Data Query](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#use-a-data-query).

When embedding a visual, you also have the option of overriding default configurations by modifying the configuration of visual settings. You modify the default settings with the `variables` key in the parameter passed to the `visualize()` method.

Before you can encode settings into an embedded visual, you must identify every required setting as well as any optional settings that you wish to use. Visual settings can be identified using an internal REST API method.

The REST API method used in these steps is considered internal to the Self-Service Analytics application. Internal APIs should not be used except as directed. For more information about using internal APIs, see [Cautionary Note About Internal APIs](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/rest-api/restapi-overview2#cautionary-note-about-internal-apis).
