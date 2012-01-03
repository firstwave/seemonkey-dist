from sikuli import *
from com.criticalpath.seemonkey import SeeMonkey
import unittest
import globals

class test_bar1(unittest.TestCase):
    def setUp(self):
        print("setUp bar1")
        
    def tearDown(self):
        print("tearDown bar1")
        
    def runTest(self):
        globals.device.press('menu')

class test_bar2(unittest.TestCase):
    def setUp(self):
        print("setUp bar2")
        
    def tearDown(self):
        print("tearDown bar2")
        
    def runTest(self):
        globals.device.press('home')