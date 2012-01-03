from sikuli import *
from com.criticalpath.seemonkey import SeeMonkey
import unittest
import sys
import xmlrunner
import component_tests

# globals is a namespace used to pass global configuration 
# and a single device reference
# around to various unittests, instead of reconnecting for every test
import globals

print("loading ui libraries")
import resources.app_mdpi as ui
import resources.platforms.aosp_mdpi as platform
globals.ui = ui
globals.platform = platform

print("setting up android connection")
globals.device = SeeMonkey()

print("building test suite...")
suite = unittest.TestSuite()

# this method allows you to specify which tests and in which order the
# test suite will run
#testNames = ["test_foo",
#        "test_bar1",
#        "test_bar2"]
#suite.addTests(unittest.TestLoader().loadTestsFromNames(testNames, BAT))

# this method automatically finds all unittest derived classes in a module
suite.addTests(unittest.TestLoader().loadTestsFromModule(component_tests))

print("running test suite...")
# use the xmlrunner to generate reports in JUnit-style XML
xmlrunner.XMLTestRunner(output='test-reports').run(suite)
exit(0)

