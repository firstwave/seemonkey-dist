from sikuli import *

print('aosp library loaded')

def unlockScreen(device):
    # this function can safely be used even if
    # it is unknown if the device is locked or not
        device.wake()
        if device.exists("1321469716016.png"):
            if device.exists("1321472659750.png"):
                device.dragDrop(Pattern("1321469716016.png").similar(0.73),"1321472659750.png")
            else:    
                device.dragDrop(Pattern("1321469716016.png").similar(0.73),"1321469736786.png")
def dismissSoftKeyboard(device):
    if device.exists("1323908723908.png"):
        device.press('back')
        
def clearAppData(device, package):
        # start the 'clear app data' activity for the provided 
        # package name
        device.getMonkeyDevice().startActivity(
                action = "android.settings.APPLICATION_DETAILS_SETTINGS",
                data = "package:%s" % package,
                component = "com.android.settings/.applications.InstalledAppDetails")
        device.sleep(3000)
        if device.exists(Pattern("Cleardata.png").similar(0.93)):
            device.click(Pattern("Cleardata.png").similar(0.93))
            device.sleep(250)
            device.click(Pattern("OK-1.png").similar(0.80))
        device.press('back')
