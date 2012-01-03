from sikuli import *
from com.criticalpath.seemonkey import SeeMonkey
import unittest
import globals



class test_foo(unittest.TestCase):
    def setUp(self):
        print("unlocking device")
        dir(globals.platform)
        globals.platform.unlockScreen(dev) # platform specific routine
                
    def tearDown(self):
        print("tearDown foo")
        
    def runTest(self):
        # shorthand reference
        dev = globals.device
        print("starting dialer app")
        globals.device.getMonkeyDevice().startActivity(
                component = "com.android.contacts/.TwelveKeyDialer")

        # here's an example of how to use the ui libraries

        # wait 30 seconds for the dialer app to appear
        dev.wait(globals.ui.SendCallButton, 30)
        
        dev.click(globals.ui.KeyPadButtons["5"])
        dev.click(globals.ui.KeyPadButtons["2"])
        dev.click(globals.ui.KeyPadButtons["5"])
        dev.click(globals.ui.KeyPadButtons["1"])
        dev.click(globals.ui.KeyPadButtons["3"])
