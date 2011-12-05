# SeeMonkey #

SeeMonkey is a [Sikuli](http://sikuli.org/) extension which enables running image-driven UI scripts on Android devices and emulators.
It uses the Android Debug Bridge to communicate with Android devices and emulators.
SeeMonkey scripts are written in the Python programming language.
It is recommended that you fork this repository into one dedicated to your project, and add this as a remote:

    git remote add upstream giot@github.com:SeeMonkey/seemonkey-dist
    
To update your distribution, issue `git pull upstream master.`

### Requirements and Installation ###

Installation of the [Sikuli IDE](http://sikuli.org/download.shtml) (currently Sikuli X 1.0rc3) is recommended if you plan on writing SeeMonkey scripts. The Sikuli IDE is avalable in Windows, Mac OS X, and GNU/Linux flavors.
Currently, SeeMonkey has only been tested only Mac OS X 10.6/10.7. Please send feedback about what works and what doesn't on various other platforms.
If you only plan on running SeeMonkey scripts (such as on a build server for continuous integration) you do not need to install the Sikuli IDE.
**NOTE** It is not possible to execute SeeMonkey scripts from within the Sikuli IDE -- you must instead use the `run-script` command, which is outlined below.

The [Android SDK](http://developer.android.com/sdk/index.html) (currently revision 15) is required;
it is recommended that you set the environment variable `$ANDROID_SDK` to contain the path to your SDK installation.

This lets Sikuli find libraries which it assumes to be located in `libs\`.

The distruibution package is organized like so:

* `/` _installation root_
    * `run-script` _Python wrapper used to properly configure a JVM and invoke the Sikuli interpereter._
    * `scripts/` _Scripts can be located anywhere, this directory is provided as a convenient way to redistribute scripts within the distribution package._
    	* `sanity.sikuli` _Simple script that can be run to confirm that the environment is correctly configured and that you are able to successfully connect to a device/emulator._
    * `libs/`
    	* `python/` _This directory is for Python modules and packages that can in turn be imported into SeeMonkey scripts_
    		* `xmlrunner/` _Python module that runs unit tests ond generates JUnit-style XML output_
    	* `seemonkey.jar`
    	* `sikuli-script.jar`
        * _opencv libraries_
    * `docs/`
        * _API documentation_

### SeeMonkey Scripts ###

SeeMonkey scripts are Sikuli scripts written to take advantage of the SeeMonkey API.
A Sikuli script is organized in a .sikuli package, similar to a OS X .app package.
This package contains a Python script executed by the Sikuli interpereter and may contain an HTML file which tells the Sikuli IDE how to display the script;
Both .py and .html files have the same name as the .sikuli package, e.g. example.sikuli contains example.py.
The .sikuli package can also contain a number of .png files which can then be referenced in the .py script.

To run a SeeMonkey script, use the `run-script` copmmand and supply a list of .sikuli packages as arguments.

If the environment variable `$ANDROID_SDK` is not set, you must specify its location with the `--android-sdk` option.

Due to the way Sikuli searches for the native [OpenCV](http://opencv.willowgarage.com/wiki/) libraries you must do one of the following:

* `cd` into the installation root before invoking `run-script`
* manually set the `--seemonkey-root` option when invoking `run-script` 
	* **NOTE** this has the effect of changing the working dir, so ensure you give relative paths that are relative to this path, not your original working directory.

For more usage information, see `run-script -h`.

----
* Author: Oliver Bartley (obartley@ebay.com)
* Date: 30 NOV 2011
* Version: 0.1
