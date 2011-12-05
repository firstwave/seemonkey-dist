# SeeMonkey API Guide #

The SeeMonkey object is how the Sikuli vision engine interacts with an Android device.
The API has been designed to closely resemble the Sikuli API where reasonable; method names maintain the same conventions,
i.e. `click` methods utilize the vision engine to drive touch-screen events, and the `press` methods drive hardware buttons/keyboard events.
Consult the documantation at http://sikuli.org/docx/index.html for a more in depth look at the Sikuli API.

### Fields ###

* `int autoDelay`

    Sets the default delay in milliseconds for the `sleep()` method, which is called automatically after every UI event.
    Used to prevent overloading the vision engine and adb queue.
    Default 500
    
`int longPressDelay`

    Delay in miliseconds for a long press.
    Default 1000

### Methods ###

#### SeeMonkey(), SeeMonkey(long, String)

To use the SeeMonkey API in a Sikuli script, you must first initialize a SeeMonkey object:

``` python
from com.criticalpath.seemonkey import SeeMonkey

dev = SeeMonkey()
```

Alternately, you can specify a timeout in miliseconds and/or a specific device/emulator by serial number:

``` python
dev = SeeMonkey(10000, null) # connect to default device with a timeout of 10 seconds
dev = SeeMonkey(-1, 'emulator-5554') # connect to specified device with default timeout
```


#### ScreenImage capture(), capture(int, int, int, int), capture(Rectangle), capture(Region)

_IScreen_ interface method, used by Sikuli.


#### Rectangle getBounds()

_IScreen_ interface method, used by Sikuli.


#### IRobot getRobot()

_IScreen_ interface method, used by Sikuli.


#### Region newRegion(Rectangle)

_IScreen_ interface method, used by Sikuli.


#### void showMove(Location), void showClick(Location), void showTarget(Location), void showDropTarget(Location)

_IScreen_ interface methods. No implementation on Android.


#### MonkeyDevice getMonkeyDevice()

Returns a com.android.monkeyrunner.MonkeyDevice.
See the documentation at http://developer.android.com/guide/developing/tools/MonkeyDevice.html for full details.


#### String getArgs(String)

Used to get System properties through Java's System.getProperty() method.
This is useful when passsing data at invocation via the run-script command using the --set-property argument.
For instance, using this command to run a SeeMonkey script:
    
    $ ./run-script --set-property "test_output=/foo/bar"
    
Then `getArgs("test_output");` would return `"/foo/bar"`


#### void press(String), void press(String, int), void press(String, String)

Trigger a hardware key-press event.
See http://developer.android.com/reference/android/view/KeyEvent.html for information on valid keycodes.
Note that it is not necessary to use the full keycode name, such as `KEYCODE_HOME`.
This method automagically determines the correct keycode, so:

``` python
press("KEYCODE_HOME")
press("HOME")
press("home")
```

all perform the same action.
The second argument is used to indicate a type:

``` python
press("home", "down") # press key down
press("home", "up") # release key
press("home", "down_and_up") # default, not required
```


#### void longPress(String)

Trigger a long press of a hardware button.
The keycode is handled the same as in `press()`, and the duration can be adjusted with the `SeeMonkey.longPressDelay` field.    


#### int type(String)

Send a sequence of hardware-keyboard keystrokes.
    
    
#### sequence(String)

This method is deprecated.


#### int click(PSMRL), click(PSMRL, int),

This method accepts a `<PSMRL>`` object and triggers a touch event after successfully located.
More on the `<PSMRL>` object below.
Throws a FindFailed exception if `<PSMRL>` cannot be found.


#### int rightClick(PSMRL), rightClick(PSMRL, int), int longClick(PSRML), longCLicl(PSMRL, int)

This method accepts a `<PSMRL>` object and triggers a long-press event after successfully located.
The `rightClick()` methods exist only as defined by the IScreen interface and should not be used;
instead use `longClick()`.
More on the `<PSMRL>` object below.
Throws a `FindFailed` exception if `<PSMRL>` cannot be found.


#### Boolean exists(String)

Accepts a string literal to be searched for with OCR, or a path to a filename to be located with the vision engine.
Returns `True` if target is found, `False` otherwise.

#### Finder find(String)

Accepts a string literal to be searched for with OCR, or a path to a filename to be located with the vision engine.
More about the Finder object can be found here: http://sikuli.org/docx/finder.html


#### wake()

Wakes the device.


#### void sleep(), sleep(long)

Pauses execution for the specified number of milliseconds.
The default can be adjusted with the `SeeMonkey.autoDelay` field.


### PSMRL Object ###

_PSMRL_ in this context can mean any one of the following types of objects, though generally you will only be using Patterns and Strings:

* Pattern

Pattern objects can be handled by the IDE by clicking on a target image and adjusting parameters in the given dialog.
Read more about the Pattern object here: http://sikuli.org/docx/pattern.html

* String

If a string ends in ".png" it is assumed to be a path to an image file to be used.
If the image is not found, or the string does not end in ".png", then the OCR engine will attempt to locate the text on-screen.

* Match - See http://sikuli.org/docx/match.html for details
* Region - See http://sikuli.org/docx/region.html for details
* Location - A Java-style Location object, with x and y fields.

### Sikuli Settings object ###

This object can be made available with this import statement:

    from org.sikuli.script import Settings
    
Use the `Settings` object to configure the Sikuli interpereter.
Full usage information can be found at http://sikuli.org/docx/globals.html#Settings
There are some inconsistencies with how SeeMonkey uses these values; this will be fixed in a future update.
-----
* Author: Oliver Bartley
* Date: 5 DEC 2011
* Version: 0.1