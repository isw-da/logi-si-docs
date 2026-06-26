---
title: "JavaScript Manage UI Components, Libraries and Unit Tests"
id: 4415504588183
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504588183-JavaScript-Manage-UI-Components-Libraries-and-Unit-Tests
updated_at: 2021-12-10T15:40:07Z
---

# JavaScript Manage UI Components, Libraries and Unit Tests

# JavaScript Manage UI Components, Libraries and Unit Tests

Unit testing raises the need to organize code into separate components.
Other reasons include code re-use and better management of various
JavaScript libraries.

In this sample we will re-write the [ReactJS to manage the list of categories](https://devnet.logianalytics.com/hc/en-us/articles/4415492662679-ReactJS-to-Manage-the-List-of-Categories) sample in
a commonly recommended way that allows for code re-use, unit test,
deployment and automatic management of third-party JavaScript packages
together with their specific versions.

## Folders and Tools Preparation

We will use [npm](https://www.npmjs.com/) as the central place to
manage the libraries, run the web server and unit tests.

1. npm is packaged inside Node.js so firstly we need to download Node
   installer from <https://nodejs.org>.
2. Install npm

   Run the installer and include npm in the setup.

   ![../_images/Node.js_Setup_Including_npm.png](https://devnet.logianalytics.com/hc/article_attachments/4415504314903/node.js_setup_including_npm_306x62.png)
3. Test that npm is installed successfully by running `npm--version`
   in the command-line to see the version number.
4. Create a folder named “ui\_react\_samples\_2” anywhere available.
5. Inside it, create a folder named “src”. This is where we will put our
   code, with each component in a separate file.

   > Because of this structure, we now must use a web server even for
   > testing. For details, please see [same-origin
   > policy](https://en.wikipedia.org/wiki/Same-origin_policy).
6. Inside “src” folder, create a folder named “\_\_tests\_\_”. This is
   where we will put the unit tests.
7. In command-line, go to “ui\_react\_samples\_2” folder and run
   `npminit` to create npm configuration file “package.json”.
8. Accept default values by pressing Enter.
9. The content of “ui\_react\_samples\_2/package.json” will be as
   following:

```
{"name":"ui_react_samples_2","version":"1.0.0","description":"","main":"index.js","scripts":{"test":"echo \"Error: no test specified\" && exit 1"},"author":"","license":"ISC"}
```

## Install the Packages

We need the following packages:

* In both production and development:
  + [react](https://www.npmjs.com/package/react) and
    [react-dom](https://www.npmjs.com/package/react-dom) for the
    UI.
  + [babel-loader](https://www.npmjs.com/package/babel-loader)[babel-core](https://www.npmjs.com/package/babel-core)[babel-preset-es2015](https://www.npmjs.com/package/babel-preset-es2015)[babel-preset-react](https://www.npmjs.com/package/babel-preset-react)
    to transpile JSX.
  + [request](https://www.npmjs.com/package/request) for REST API
    calls (to replace JQuery that [needs
    tweaking](https://www.npmjs.com/package/jquery) to work in
    Node.js).
  + [webpack](https://www.npmjs.com/package/webpack) to bundle the
    source files together
  + [json-loader](https://www.npmjs.com/package/json-loader) for
    webpack.
* In development only:
  + [webpack-dev-server](https://www.npmjs.com/package/webpack-dev-server)
    to serve the bundle.
  + [http-server](https://www.npmjs.com/package/http-server) to
    serve HTML files.
  + [react-addons-test-utils](https://www.npmjs.com/package/react-addons-test-utils)
    for unit testing.
  + [mocha](https://www.npmjs.com/package/mocha) for the test
    framework.
  + [karma](https://www.npmjs.com/package/karma)[karma-cli](https://www.npmjs.com/package/karma-cli),
    [karma-mocha](https://www.npmjs.com/package/karma-mocha),
    [karma-webpack](https://www.npmjs.com/package/karma-webpack),
    [karma-chrome-launcher](https://www.npmjs.com/package/karma-chrome-launcher)
    for the test runner.
  + [karma-sinon](https://www.npmjs.com/package/karma-sinon) to
    stub out API calls in unit tests.
  + [expect](https://www.npmjs.com/package/expect) to write
    assertions in unit tests.

Install the packages and save to “package.json”:

1. In command-line, go to “ui\_react\_samples\_2” folder.
2. `npminstallreactreact-dom--save`
3. `npminstallbabel-loaderbabel-corebabel-preset-es2015babel-preset-react--save`
4. `npminstallrequest@2.65.0--save`

   > (Use request at 2.65.0 because higher versions are having an
   > issue with webpack.)
5. `npminstallwebpackjson-loader--save`
6. `npminstallwebpackwebpack-dev-serverhttp-serverreact-addons-test-utilsmocha`  
   `karmakarma-clikarma-mochakarma-webpackkarma-chrome-launcherkarma-sinonexpect--save-dev`

   > (Packages only needed for development use `--save-dev` so that
   > they are excluded when deployed for production)

## Configure Unit Test

1. Create a text file named “tests.webpack.js” in “ui\_react\_samples\_2” folder.

   ```
   varcontext=require.context('./src',true,/-test\.jsx$/);context.keys().forEach(context);
   ```

   The code tells webpack to bundle all files ending in `-test.jsx` (test cases) below “ui\_react\_samples\_2/src” folder into this “tests.webpack.js” file.
2. Create a text file named “karma.conf.js” in “ui\_react\_samples\_2” folder.

   ```
   varwebpack=require('webpack');module.exports=function(config){config.set({browsers:['Chrome'],client:{captureConsole:true},singleRun:true,frameworks:['mocha','sinon'],files:['tests.webpack.js'],preprocessors:{'tests.webpack.js':['webpack']},reporters:['dots'],webpack:{module:{loaders:[{test:/\.jsx$/,loader:'babel-loader',query:{presets:['react','es2015']}},{test:/\.json$/,loader:'json-loader'}]},watch:true,node:{console:true,fs:'empty',net:'empty',tls:'empty'}},webpackServer:{noInfo:true}});};
   ```

   `files` section says that `tests.webpack.js` should be used to test, and `preprocessors` section tells webpack to process this file in advance (which bundles all test cases into the file).

   Also, the `loaders` section inside `webpack` tells webpack to use babel loader for JSX and json loader for json files.
3. Finally, edit “package.json” to change the npm test command to call karma:

```
"scripts": {
						"test": "karma start"
						},
					
```

## Implement an Empty Component

Create a text file named “CategoryList.jsx” in
“ui\_react\_samples\_2/src”.

```
var React = require('react');
						module.exports = React.createClass({
						render: function() {
						return <div></div>
						}
						});
					
```

## Write the Unit Test

1. Create a text file named “CategoryList-test.jsx” in
   “ui\_react\_samples\_2/src/\_\_tests\_\_”.

   |  |  |
   | --- | --- |
   | ```  1 											2 											3 											4 											5 											6 											7 											8 											9 											10 											11 											12 											13 											14 											15 											16 											17 											18 											19 											20 											21 											22 											23 											24 											25 											26 											27 											28 											29 											30 											31 											32 											33 											34 											35 											36 											37 											38 											39 										40 ``` | ``` varReact=require('react');varTestUtils=require('react-addons-test-utils');varexpect=require('expect');varrequest=require('request');varCategoryList=require('../CategoryList.jsx');describe('CategoryList',function(){before(function(done){sinon.stub(request,'get').yields(null,{statusCode:200},JSON.stringify([{id:"192a433a-383e-4093-a21c-266b9a3031c2",name:"Category_1"},{id:"3c55a8ac-5763-4dfd-9e1e-788e0e741400",name:"Category_2"},{id:"3c55a8ac-5763-4dfd-9e1e-788e0e741401",name:"Category_3"}]));done();});it("renders an ul with lis",function(){varcategoryList=TestUtils.renderIntoDocument(<CategoryListrootUrl={"foo"}/>);varul=TestUtils.findRenderedDOMComponentWithTag(categoryList,'ul');expect(ul).toExist();varlis=TestUtils.scryRenderedDOMComponentsWithTag(categoryList,'li');expect(lis.length).toBe(3);});after(function(done){request.get.restore();done();});}); ``` |
2. In `before`, we use sinon to stub any GET request to return successfully by statusCode 200 with a mock array of 3 categories as response. (See [GET advancedSetting/category/(tenant\_id)](https://devnet.logianalytics.com/hc/en-us/articles/4415492699031-Advanced-Settings-APIs#_bm9) for sample of actual response.)
3. In `"rendersanulwithlis"`, we use React TestUtils to render the component with a dummy url, then use TestUtils functions to find and assert the UI elements.
4. In `after`, we restore the original request.

## Run the Unit Test

1. In command-line, go to “ui\_react\_samples\_2” folder and run
   `npmrun--silenttest`.
2. `karmastart` should be called and after a while, open a Chrome
   browser window, then fail as expected with the messages
   `CategoryListrendersanulwithlisFAILED` and
   `Executed1of1(1FAILED)ERROR`.

In next sections we will work on CategoryList code to make the unit test
succeed, as well as more tests to make use of React TestUtils’
`Simulate`.

## Run the Component in Server

To run the component, we render it in a starting page, then use webpack
to bundle the page together with the libraries, then use
webpack-dev-server to serve the JavaScript bundle. This bundle will be
included in an HTML page served by the http-server.

1. Create the starting page named “index.jsx” in “ui\_react\_samples\_2”
   folder.

   ```
   varReactDOM=require('react-dom');varCategoryList=require('./src/CategoryList');ReactDOM.render(<CategoryListrootUrl={"http://127.0.0.1:8888/api/"}/>,document.getElementById('app'));
   ```
2. Create the default webpack configuration file named “webpack.config.js” in “ui\_react\_samples\_2” folder.

   ```
   module.exports={entry:'./index.jsx',output:{filename:'bundle.js',publicPath:'http://localhost:8090/assets'// url to include the bundle in HTML page will be http://localhost:8090/assets/bundle.js},module:{loaders:[{test:/\.jsx$/,loader:'babel-loader',query:{presets:['react','es2015']}},{test:/\.json$/,loader:'json'}]},externals:{//don't bundle the 'react' npm package with our bundle.js//but get it from a global 'React' variable'react':'React'},resolve:{extensions:['','.js','.jsx']},node:{console:true,fs:'empty',net:'empty',tls:'empty'}}
   ```
3. Create the HTML page named “index.html” in “ui\_react\_samples\_2” folder.

   ```
   <!DOCTYPE html><html><head><!-- include react --><scriptsrc="./node_modules/react/dist/react-with-addons.js"></script></head><body><divid="app"><!-- id="app" is where the react component will be rendered --></div><!-- include the webpack-dev-server script so changes are automatically reloaded --><scriptsrc="http://localhost:8090/webpack-dev-server.js"></script><!-- include the bundle from webpack --><scripttype="text/javascript"src="http://localhost:8090/assets/bundle.js"></script></body></html>
   ```
4. Add commands to “package.json” to start the server

   ```
   "scripts": {
   								"test": "karma start",
   								"start": "npm run serve | npm run dev",
   								"serve": "./node_modules/.bin/http-server -p 8080",
   								"dev": "webpack-dev-server --progress --colors --port 8090"
   								},
   							
   ```
5. Start the server by running `npmrunstart`.
6. Open browser and go to <http://localhost:8080/> to see a blank page.

## Implement CategoryList Component

The JavaScript code is nearly the same as [ReactJS to manage the list of categories](https://devnet.logianalytics.com/hc/en-us/articles/4415492662679-ReactJS-to-Manage-the-List-of-Categories), but without the HTML code.

```
var React = require('react');
						var request = require('request');
						module.exports = React.createClass({
						getInitialState: function() {
						return {
						categoryArray: new Array()
						};
						},
						componentDidMount: function() {
						this.fetchData();
						},
						render: function() {
						var lines = this.state.categoryArray.map(function(category) {
						return (
						<li key={category.id}>
						<input type="text" id={category.id} value={category.name} onChange={this.reflectChangedData.bind(this,category.id)} />&nbsp;
						<button onClick={this.removeCategory.bind(this,category.id)}>Remove</button>
						</li>
						)
						}.bind(this));
						return (
						<div style={{"border": "1px solid black", "width": "400px"}}>
						<button onClick={this.addCategory}>Add</button>
						<ul> {lines} </ul>
						<button onClick={this.pushData}>Save</button>
						</div>
						)
						},
						fetchData: function() {
						// TODO
						},
						reflectChangedData: function(id, event) {
						var categories = this.state.categoryArray;
						var pos = categories.map(function(x) {return x.id; }).indexOf(id);
						categories[pos].name = event.target.value;
						this.setState({categoryArray : categories});
						},
						pushData: function() {
						// TODO
						},
						addCategory: function(e) {
						e.preventDefault();
						var categories = this.state.categoryArray;
						var newId = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
						var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
						return v.toString(16);
						});
						categories.push({id: newId, name: null});
						this.setState({categoryArray : categories});
						},
						removeCategory: function(id, event) {
						// TODO
						}
						});
					
```

The fetchData, pushData and removeCategory functions are now implemented using [request](https://www.npmjs.com/package/request) library:

```
fetchData:function(){request.get({url:this.props.rootUrl+"advancedSetting/category/",headers:{"Content-Type":"application/json"},withCredentials:false},function(err,res,body){if(!err&&res.statusCode===200){this.setState({categoryArray:JSON.parse(body)});}else{console.log("Error in fetchData: "+JSON.stringify(res));}}.bind(this));},pushData:function(){request.post({url:this.props.rootUrl+"advancedSetting/category/",headers:{"Content-Type":"application/json"},withCredentials:false,body:JSON.stringify(this.state.categoryArray)},function(err,res,body){varparsed_body=JSON.parse(body);if(!err&&res.statusCode===200){if(!parsed_body.success){console.log(JSON.stringify(res));}this.fetchData();}else{console.log(JSON.stringify(res));this.fetchData();}}.bind(this));},removeCategory:function(id,event){request.delete({url:this.props.rootUrl+"advancedSetting/category/"+id,headers:{"Content-Type":"application/json"},withCredentials:false},function(err,res,body){varparsed_body=JSON.parse(body);if(!err&&res.statusCode===200){if(!parsed_body.success){console.log(JSON.stringify(res));}this.fetchData();}else{console.log(JSON.stringify(res));this.fetchData();}}.bind(this));}
```

The page at <http://localhost:8080/> will automatically be refreshed each
time the code is updated.

## Test Behaviors with React TestUtils

React TestUtils allow us to simulate mouse and keyboard events,
therefore provides a way to test the event handler code. Here we will
test that a new <li> tag is inserted when the Add button is clicked.

Between the functions `"rendersanulwithlis"` and `after`, add
the following function:

|  |  |
| --- | --- |
| ```  1 									2 									3 									4 									5 									6 									7 									8 									9 									10 									11 									12 									13 									14 									15 									16 									17 									18 									19 									20 									21 									22 								23 ``` | ``` it("renders one more li when Add button is clicked",function(){varcategoryList=TestUtils.renderIntoDocument(<CategoryListrootUrl={"foo"}/>);varul=TestUtils.findRenderedDOMComponentWithTag(categoryList,'ul');expect(ul).toExist();varbuttons=TestUtils.scryRenderedDOMComponentsWithTag(categoryList,'button');varaddButton=buttons[0];TestUtils.Simulate.click(addButton);varlis=TestUtils.scryRenderedDOMComponentsWithTag(categoryList,'li');expect(lis.length).toBe(4);}); ``` |
