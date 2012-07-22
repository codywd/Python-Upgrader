## Importing Std Libraries ##
import urllib
import os
import sys
import tempfile

## Importing 3rd-Party Libraries ##
import wx


class updateDialog():
    
    try:
        #Example upFile: https://raw.github.com/Seafire-Software/Seapad/master/curVersion
        upFile = "SET-YOUR-CURVERSION-HERE"
        tempDir = tempfile.gettempdir()
        webFile = urllib.urlretrieve(upFile, tempDir + '/curVersion')
        basVer = open(tempDir + '/curVersion')
        ver = float(basVer.read())
                
        if progVer < ver:
            #You have to set a variable as progVer somewhere.
            dlg = wx.MessageDialog(None, "You must update. Your version is " + str(progVer) + ", and the latest version is " + str(ver) + ", Do you wish to update?", "Update Required.", wx.YES_NO | wx.ICON_INFORMATION)
                   
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_YES:
		#Check if the currently running operating system is linux
                if sys.platform == "linux2":
                    #Example upgradeFile: https://raw.github.com/Seafire-Software/Seapad/master/SeaPad.py
                    upgradeFile = "SET-YOUR-UPGRADE-FILE-HERE"
                #Check if the currently running operating system is Windows
		elif sys.platform == "win32":
                    #Example upgradeFile: https://raw.github.com/Seafire-Software/Seapad/master/SeaPad.exe
                    upgradeFile = "https://github.com/Seafire-Software/Anansi-CalcPad/blob/master/Binary/Anansi-CalcPad-Setup.exe?raw=true"
                   
                urllib.urlretrieve(upgradeFile, os.path.join(os.getcwd(), sys.argv[0]))
                dlg = wx.MessageDialog(None, "Update successful. Please restart the program!", "Restart manually.", wx.YES_NO)
            else:
                wx.MessageBox("You chose not to upgrade. Please upgrade later!", "Upgrade later.", wx.OK)
        elif ver == progVer:
            wx.MessageBox("You do not need to update. Your version is " + str(progVer) + ", which is equal to the latest version of " + str(ver), "No Update Required.", wx.OK | wx.ICON_INFORMATION)
        elif progVer > ver: 
            wx.MessageBox("What happened here? Your version is " + str(progVer) + " which is greater than the latest version of " + str(ver), "Your version is greater than ours?", wx.OK | wx.ICON_QUESTION)
        else:
            wx.MessageBox("Something went wrong with the update. Please try again. If it happens again, file a bug report please.", "Error!", wx.OK | wx.ICON_ERROR)            
        except:
            wx.MessageBox("There was an error (Error 10152). Maybe you are not connected to the internet? Try again please.", "Try again.", wx.OK)
