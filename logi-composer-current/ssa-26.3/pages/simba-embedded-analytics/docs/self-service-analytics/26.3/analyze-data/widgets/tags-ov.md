> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Tags to Group and Categorize Content

Categorize your object inventory and create themed groups of content by associating tags with dashboards, self service reports, data sources, and visual gallery visuals. Create an overarching themed content structure for your users, or use tagging to improve your object migration flow. Tag content to create groupings for everyone in the organization for ease of use. Filter content or [search results](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#filter-lists-and-search-results-using-tags) for dashboards and reports in the Library, data sources in Sources, and visuals in the Visual Gallery to view content associated with specific tags.

<Note>
  All tags added to your environment are visible to all users within the tenant.
</Note>

Users who can add, and in some cases, remove tags, include:

* Users who belong to a group with the [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Administer Tags** can add tags and delete tags added by any user, as needed.
* Users who belong to a group with the [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Create Tags** can create new tags but can only delete their own tags.
* Users with [Editor access](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-share-withinacct#shared-access-editors) to a dashboard, self service report, data source, or visual gallery visuals), which is equivalent to READ + WRITE permissions can assign or remove an existing tag to the resource.

When you export or import dashboards, data sources, or visuals the associated tags are exported and can be imported as well.

For more information on using content tags in your environment:

* [Add Tags](#add-tags)
* [Remove Tags](#remove-tags)
* [Remove Tags](#remove-tags)

You can also manage tags in embedded environments, or using the API.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<h2 id="add-tags">
  Add Tags
</h2>

Users with the [privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Administer Tags**, **Create Tags** or who have READ + WRITE permissions to dashboards, data sources, and visual gallery visuals can add tags to these resources. Once tags are added to a resource within an environment or tenant, users can filter dashboards, data sources, and visuals they see by content tag.

<Note>
  All tags added to your environment are visible to all users within the tenant.
</Note>

<Note>
  Only users with the [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Administer Tags** can delete other users' tags.
</Note>

**Add a tag to a dashboard**

1. Open a dashboard you have permissions to access and edit, then select the manage tags icon <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/tags/manage-tags-cmp-23-3.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=d3a5dde7e6648bd5809eb12e6f623a2d" alt="manage tags icon" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/tags/manage-tags-cmp-23-3.png" />. The Manage Tags work area opens.

2. Select the **Tags** Search field. Any tags available in your environment or tenant appear as a list: select tags to add from the list.

3. Enter a few characters: a shorter list of matching tags is returned. Select an existing tag to add it to this dashboard.

4. If a matching tag does not exist, and you have appropriate privileges, you can select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> to add the tag to the dashboard. Your software returns a success message.

5. When you have added the tags you need, select **Save** to save your tags with this dashboard.

   <Note>
     You can also add a new or existing tag to a dashboard when you save the dashboard: select an existing tag or add a new one.
   </Note>

**Add a tag to a** **data source**

1. Open a data source you have permissions to access and edit, then expand the **Source Definition** work area.
2. Select the **Tags** Search field. Any tags available in your environment or tenant appear as a list: select tags to add from the list.
3. Enter a few characters: a shorter list of matching tags is returned. Select an existing tag to add it to this data source.
4. If a matching tag does not exist, and you have appropriate privileges, you can select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> to add the tag to the data source. Your software returns a success message.
5. When you have added the tags you need, select **Save Source** to save your tags with this data source.

**Add a tag to a** **visual gallery visual**

1. Open a visual gallery visual you have permissions to access and edit, or create a new visual in the visual gallery.

2. Select the **Tags** icon in the upper left corner of the visual. The **Manage Tags** work area opens.

3. Select the **Tags** Search field. Any tags available in your environment or tenant appear as a list: select tags to add from the list.

4. Enter a few characters: a list of matching tags is returned if the tags exist. Select an existing tag to add it to this visual.

5. If a matching tag does not exist, and you have appropriate privileges, you can select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> to add the tag to the visual. Your software returns a success message.

6. When you have added the tags you need, select the save icon to save your tags with this visual.

   <Note>
     You can also add a new or existing tag to a visual gallery visual when you save the visual: select an existing tag or add a new one.
   </Note>

<h2 id="remove-tags">
  Remove Tags
</h2>

Some users can remove tags associated with your content when no longer needed for that item.

Users with the [privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Administer Tags**, **Create Tags** or who have READ + WRITE permissions to dashboards, data sources, and visual gallery visuals can remove tags from these resources.

**Remove a tag from a** **dashboard**

1. Open a dashboard you have permissions to access and edit, then select the manage tags icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/tags/manage-tags-cmp-23-3.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=d3a5dde7e6648bd5809eb12e6f623a2d" alt="manage tags icon" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/tags/manage-tags-cmp-23-3.png" />). The Manage Tags work area opens.

2. Select a tag in the **Tags** field; select the **x** icon to remove the tag.

3. Make any other changes to the tags associated with this dashboard.

4. Select **Save** to save your changes to this dashboard.

   <Note>
     You can also remove a tag from a dashboard when you save the dashboard: select the **x** icon to remove the tag.
   </Note>

**Remove a tag from a** **data source**

1. Open a data source you have permissions to access and edit, then expand the **Source Definition** work area.
2. Select a tag in the **Tags** field; select the **x** icon to remove the tag.
3. Make any other changes to the tags associated with this data source.
4. Select **Save Source** to save your tags with this data source.

**Remove a tag from a** **visual gallery visual**

1. Open a visual you have permissions to access and edit, then select the manage tags icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/tags/manage-tags-cmp-23-3.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=d3a5dde7e6648bd5809eb12e6f623a2d" alt="manage tags icon" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/tags/manage-tags-cmp-23-3.png" />). The Manage Tags work area opens.
2. Select a tag in the **Tags** field; select the **x** icon to remove the tag.
3. Make any other changes to the tags associated with this visual.
4. Select the save icon to save your tags for this visual.

## Delete Tags

Users with the **Administer Tags** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can delete tags associated with your content when no longer needed in your software environment. If you belong to a group with the **Create Tags** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), you can delete your own tags.

When you delete a tag from your environment, it is removed from all resources in your tenant or environment.

**Delete a tag**

1. Open a dashboard, data source, or visual gallery visual.

   * Dashboards: Open a dashboard and then select the manage tags icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/tags/manage-tags-cmp-23-3.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=d3a5dde7e6648bd5809eb12e6f623a2d" alt="manage tags icon" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/tags/manage-tags-cmp-23-3.png" />) to open the Manage Tags work area.
   * Data sources: Open a data source and expand the Source Definition work area.
   * Visual gallery visuals: Open a visual gallery visual and select the manage tags icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/tags/manage-tags-cmp-23-3.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=d3a5dde7e6648bd5809eb12e6f623a2d" alt="manage tags icon" width="20" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/tags/manage-tags-cmp-23-3.png" />) to open the Manage Tags work area.

2. Select the **Tags** field. A list of tags appears you can add, remove, or delete.

3. Select the delete icon (<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=2f005e6454f4553621ce9f5926d15d6a" alt="" width="17" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/trashcan.png" />) for the tag you want to delete. A success message indicates the tag was deleted from your environment.

4. Optionally, **Save** your dashboard, data source, or visual gallery visual.

   <Warning>
     Even if you close your work area without saving after you make this change, the tag is deleted and no longer associated with any content in your environment.
   </Warning>
