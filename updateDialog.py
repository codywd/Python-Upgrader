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
        upFile = "SET-YOUR-CURRENT-VERSION-FILE-HERE"
        #Example upgradeFile: https://raw.github.com/Seafire-Software/Seapad/master/SeaPad.py
        upgradeFile = "SET-YOUR-FILE-UPGRADING-WEB-PATH-HERE"
        
        # tempfile.gettempdir() is a cross-platform way to find the temporary directory of the current OS
        tempDir = tempfile.gettempdir()
        webFile = urllib.urlretrieve(upFile, tempDir + '/curVersion')
        basVer = open(tempDir + '/curVersion')
        ver = float(basVer.read())
        
        # Set your current Program Version as a float (ex: progVer = 1.00)
        if progVer < ver:
            dlg = wx.MessageDialog(None, "You must update. Your version is " + str(progVer) + ", and the latest version is " + str(ver) + ", Do you wish to update?", "Update Required.", wx.YES_NO | wx.ICON_INFORMATION)
           
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_YES:    
                urllib.urlretrieve(upgradeFile, os.path.join(sys.path[0], sys.argv[0]))
                dlg = wx.MessageBox("Update successful. Please restart the program!", "Restart manually.", wx.OK)
            else:
                wx.MessageBox("You chose not to upgrade. Please upgrade later!", "Upgrade later.", wx.OK)
        elif ver == progVer:
            wx.MessageBox("You do not need to update. Your version is " + str(progVer) + ", which is equal to the latest version of " + str(ver), "No Update Required.", wx.OK | wx.ICON_INFORMATION)
        elif progVer > ver: 
            wx.MessageBox("What happened here? Your version is " + str(progVer) + " which is greater than the latest version of " + str(ver), "Your version is greater than ours?", wx.OK | wx.ICON_QUESTION)
        else:
            wx.MessageBox("Something went wrong with the update. Please try again. If it happens again, file a bug report please.", "Error!", wx.OK | wx.ICON_ERROR)            
    except:
        ## The Error number (10152) is optional. You can remove if you don't add it on your site somewhere. ##
        wx.MessageBox("There was an error (Error 10152). Maybe you are not connected to the internet? Try again please.", "Try again.", wx.OK)
