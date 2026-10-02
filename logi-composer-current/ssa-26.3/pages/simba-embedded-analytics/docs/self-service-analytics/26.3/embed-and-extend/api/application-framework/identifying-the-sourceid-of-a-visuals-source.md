> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Identify a Visual's sourceID

You can identify a Self-Service Analytics visual's `sourceID` while working with it. For example, to programmatically identify a visual's default settings using a REST API call, it is easiest to use the `sourceID` in the call to look at its source configuration.

**To identify the `sourceID` of a visual's source:**

1. Open the visual in its dashboard.

2. Find the number at the end of the URL in the address bar of your browser. The `sourceID` is the section of the number before the plus sign (+).

   <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/source-id.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=2f257453871bb9d12f7ce125c2c257ee" alt="" width="576" height="334" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/source-id.png" />

After you have identified the `sourceID` of a visual, you can use it in other steps such as calling REST API methods.
