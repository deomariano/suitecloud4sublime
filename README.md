# suitecloud4sublime

The unofficial SuiteCloud plugin for Sublime Text 3.

suitecloud4sublime is a Sublime Text 3 plugin for made to easily manage files for SuiteScript projects. Only supports Windows for now.

## Pre-requisites

The suitecloud4sublime plugin relies on a RESTlet residing in the target account's destination. Install the suitecloud4sublime Bundle in NetSuite (Bundle ID: 312535)

## Supported functionalities
* Generate SuiteScript 2.0 templates.
* Upload File to NetSuite
* Download File from NetSuite
* Compare local and server version of file

## Setup
1. Clone this repo to "C:/Users/*username*/AppData/Roaming/Sublime Text 3/Packages" where *username* is your PC's username.
2. Update config.sublime-settings with appropriate details from your account through any of the two ways: 1) Directly editing config.sublime-settings; or 2) Navigating to SuiteCloud > Configure...
	* email_address - NetSuite Email Address
	* password - NetSuite Password
	* role - NetSuite Role
	* account - NetSuite Account
	* consumer_key - Consumer Key from NetSuite (not needed for now)
	* consumer_secret - Consumer Secret from NetSuite (not needed for now)
	* token - Token from NetSuite (not needed for now)
	* token_secret - Token Secret from NetSuite (not needed for now)
	* application_id - Application ID from NetSuite (not needed for now)
	* restlet - RESTlet URL from bundle installation
	* folder - Kodella, LLC or any folder under SuiteScripts

3. Update suitecloud4sublime.py file references to config.sublime-settings from Packages/config.sublime-settings to Packages/suitecloud4sublime/config.sublime-settings.
4. Test Integration through any of two ways: 1) Under SuiteCloud Menu, click Test Integration; or 2) Right-click on any Sublime Text 3 view, select SuiteCloud and click Test Integration.

## What's not supported?
* Other platforms aside from Windows not supported.
* Token-Based Authentication not yet supported.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
