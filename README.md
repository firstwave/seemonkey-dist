SeeMonkey
=====
SeeMonkey is a [Sikuli](http://sikuli.org/) extension which enables running image-driven UI scripts on Android devices and emulators.

Requirements and Installation
-----
Installation of the [Sikuli IDE](http://sikuli.org/download.shtml) (currently Sikuli X 1.0rc3) is recommended if you plan on writing SeeMonkey scripts. The Sikuli IDE is avalable in Windows, Mac OS X, and GNU/Linux flavors.
Currently, SeeMonkey has only been tested only Mac OS X 10.6/10.7. Please send feedback about what works and what doesn't on various other platforms.

The [Android SDK](http://developer.android.com/sdk/index.html) (currently revision 15) is also required.
It is recommended that you set the environment variable `ANDROID_SDK` to contain the path to your SDK installation.

If you only plan on running SeeMonkey scripts (such as on a build server for continuous integration) you do not need to install the Sikuli IDE, 
but you do need to take extra care to ensure that Sikuli can locate the native [OpenCV](http://opencv.willowgarage.com/wiki/) libraries.
Due to the way Sikuli searches for these libraries, if you do not have the Sikuli IDE installed in the default location you must do one of the following:

* `cd` into the installation root before invoking `run-script`
* manually set the `--seemonkey-root` option when invoking `run-script` 
	* **NOTE** this has the effect of changing the working dir, so ensure you give relative paths that are relative to this path, not your original working directory.

This lets Sikuli find libraries which it assumes to be located in `libs\`.

The distruibution package is organized like so:

* `/` _installation root_
    * `run-script` _Python wrapper used to properly configure a JVM and invoke the Sikuli interpereter. Use the `-h` option for usage._
    * `scripts/` _Scripts can be located anywhere, this directory is provided as a convenient way to redistribute scripts within the distribution package._
    	* `sanity.sikuli` _Simple script that can be run to confirm that the environment is correctly configured and that you are able to successfully connect to a device/emulator._
    * `libs/`
    	* `python/` _This directory is for Python modules and packages that can in turn be imported into SeeMonkey scripts_
    		* `xmlrunner/` _Python module that runs unit tests ond generates JUnit-style XML output_
    	* `seemonkey.jar`
    	* `sikuli-script.jar`
	* _opencv libraries_

SeeMonkey scripts are Sikuli scripts written to take advantage of the custom SeeMonkey api provided by seemonkey.jar.
A Sikuli script is organized in a .sikuli package, similar to a OS X .app package. 
This package contains a Python script executed by the Sikuli interpereter and may contain an HTML file which tells the Sikuli IDE how to display the script.
Both .py and .html files have the same name as the .sikuli package, e.g. example.sikuli contains example.py.
The .sikuli package can also contain a number of .png files which are referenced in the Python script.