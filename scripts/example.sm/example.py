import unittest
import sys

from com.criticalpath.seemonkey import SeeMonkey
from com.android.monkeyrunner import MonkeyDevice
from org.sikuli.script import Settings

Settings.MoveMouseDelay = 0.01
Settings.AutoWaitTimeout = 10
Settings.DebugLogs = True

scr = SeeMonkey() # compatiable with Sikuli Screen/Region
print "Settling..."
sleep(10)

assert scr != None
dev = scr.getMonkeyDevice() # Android Monkey device
scr.autoDelay = 1000

class TestAndroidBasic(unittest.TestCase):
    def testA_Pass(self):
        scr.press('MENU')
        scr.press('MENU')
        scr.press('MENU')
        assert scr.exists("DOES NOT EXIST")
        
    def testB_Fail(self):
        assert scr.exists("DOES NOT EXIST")

    
                
if __name__ == '__main__':
    print "Executing test suite..."
    unittest.main()