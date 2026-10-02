> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Errors and Exceptions

When working with the SDK, the Self-Service Analytics client might return one or more error messages. The following tables describe all the error messages the SDK might return, and some possible solutions.

### createQuery

<table>
  <thead>
    <tr>
      <th scope="col">Error</th>
      <th scope="col">Description</th>
      <th scope="col">Solution</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>metrics must be an array</td>
      <td>The metrics attribute of the query configuration object is not an array.</td>
      <td>Make sure metrics is an array, even if it's just an array of one.</td>
    </tr>

    <tr>
      <td>invalid metrics</td>
      <td>Metrics function, for example "avg" or "min", is not one of the expected values.</td>
      <td>The metrics function must be one of the following: 'min' , 'max' , 'avg' , 'sum' , 'calc' , 'distinct\_count' , 'last\_value' , 'percentiles'</td>
    </tr>

    <tr>
      <td>
        groups is not defined

        <br />

        fields is not defined
      </td>

      <td>The query configuration object has neither a groups attribute or a fields attribute.</td>
      <td>Either groups or fields must be defined. See the [query configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/api/application-framework/getting-started-with-the-application-framework#query-configuration-object) page for more information about the query configuration object.</td>
    </tr>

    <tr>
      <td>
        groups is not defined

        <br />

        fields must be an array of field names
      </td>

      <td>The query configuration object has a fields attribute that is not an array of field names, and does not define a groups attribute.</td>
      <td>Make sure your fields attribute is an array, or add a groups attribute to the query configuration object.</td>
    </tr>

    <tr>
      <td>
        groups must be an array of groups configurations

        <br />

        fields is not defined
      </td>

      <td>The query configuration object has a groups attribute that is not an array of groups configurations, and does not have a fields attribute.</td>
      <td>Make sure your groups attribute is an array. If you do not want a grouped query, add a fields attribute with an array of field names.</td>
    </tr>

    <tr>
      <td>filters must be an array</td>
      <td>The query configuration object has a filters attribute that is not an array of filter configurations.</td>
      <td>Make sure your filters attribute is an array, even if it's an empty array \[] or an array of just one configuration.</td>
    </tr>

    <tr>
      <td>element expected</td>
      <td>Configuration passed to visualize() does not have an 'element' attribute that is a webpage element.</td>
      <td>Check out the XYZ link to visualize sample.</td>
    </tr>

    <tr>
      <td>visualization does not exist</td>
      <td>Using visualize(), you tried to create a visualization that does not exist.</td>
      <td>Check the name of your visualization and make sure it is valid. If using a custom chart, make sure you copied the name exactly.</td>
    </tr>

    <tr>
      <td>data set empty</td>
      <td>The data set that you are trying to access is empty.</td>
      <td>This message will result if you have a non-live (static) data source and the query to access it contains `pauseAfterRead` set to `false` . A query to static data sources should have `pauseAfterRead` set to true, otherwise the query attempts to read and reread the source.</td>
    </tr>
  </tbody>
</table>
