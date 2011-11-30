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
but you do need to take extra care to ensure that the Sikuli interpereter can locate the native [OpenCV](http://opencv.willowgarage.com/wiki/) libraries.

The distruibution package is organized like so:
* / _installation root_
    * run-script _Python wrapper used to properly configure a JVM and invoke the Sikuli interpereter._
    * scripts/ _Scripts can be located anywhere, this directory is provided as a convenient way to redistribute scripts within the distribution package._
        * example.sikuli/
            * example.py
            * example.html
            * sample-image.png
    * libs/
    	* python/ _This directory is for Python modules and packages that can in turn be `import`ed into SeeMonkey scripts_
    		* xmlrunner/ _Python module that runs unit tests ond generates JUnit-style XML output_
    	* seemonkey.jar
    	* sikuli-script.jar
		* _opencv libraries_

