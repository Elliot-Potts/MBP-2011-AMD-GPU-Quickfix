# Program to force Intel Integrated Graphics on Macbook Pro 2011, fixing the GPU issues temporarily
#   This is a short project, but I made it when I was attempting fixes for my Macbook Pro 2011 a couple years ago.
#       I saw the mockup on my wall and wanted to work on it. Have a good day.

import os
import sys
import time


def moveFunc():
    os.mkdir("Disabled_Ext")
    print("Disabled extensions directory created in {}".format(str(os.getcwd())+"\Disabled_Ext"))
    os.system("mount -uw")
    os.system("sudo mv /System/Library/Extensions/AMD*.* /Disabled_Ext/")
    os.system("sudo rm -rf /System/Library/Caches/com.apple.kext.caches/")
    os.system("sudo mkdir /System/Library/Caches/com.apple.kext.caches/")
    os.system("sudo touch /System/Library/Extensions/")
    os.system("sudo umount /")
    print("Files successfully moved. You should now be using Integrated Graphics.\nRebooting in 5 seconds.")
    time.sleep(5)
    os.system("sudo reboot")


if sys.argv[1] == "-move":
    moveFunc()
else:
    print("You have entered an incorrect parameter.\nUse python main.py -move")
