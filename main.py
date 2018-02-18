# Program to force Intel Integrated Graphics on Macbook Pro 2011, fixing the GPU issues temporarily

import os
import sys


def moveFunc():
    os.mkdir("Disabled_Ext")
    print("Disabled extensions directory created in {}".format(str(os.getcwd())+"\Disabled_Ext"))
    os.system("mount -uw")
    os.system("sudo mv /System/Library/Extensions/AMD*.* /Disabled_Ext/")


if sys.argv[1] == "-move":
    moveFunc()
else:
    print("You have entered an incorrect parameter.\nEither use python main.py -move")
