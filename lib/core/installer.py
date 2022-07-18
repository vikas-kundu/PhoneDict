#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# coded by Vikas Kundu https://github.com/vikas-kundu
# -------------------------------------------

import os
import sys
import time

def start_install():
    if(os.name=='posix' ):
        if(os.system('python3 --version')!=0 or os.system('pip3 --version')!=0 ):
            print("\nUnable to find python3 or pip3. Make sure they are installed!")
            time.sleep(2)
            sys.exit()
        else:
            print("Installing Pandas and Psutil, please wait...")
            if(os.system('pip3 install pandas')!=0):
                print("\nPandas Installation Failed!")
                time.sleep(2)
                sys.exit()
            elif(os.system('pip3 install psutil')!=0):
                print("\nPsutil Installation Failed!")
                time.sleep(2)
                sys.exit()
            else:
                print("\nThe necessary python packages have been installed, you can now use the tool")
                time.sleep(2)
                sys.exit()

    elif(os.name=='nt'):
        default_dir="C:/Python38-32/"

        while(not os.path.isdir(default_dir)):
            default_dir=input("The default location for Python3 in windows is C:/Python38-32\nLooks like this directory does not exist.\nPlease manually enter the location of your Python3 installation folder: ")

        if(not os.path.isfile(default_dir+"/scripts/pip3.exe")):
            print("pip3 not found at the given location on your system! \n1. Either install pip3. \n2. Or Upgrade pip to pip3 \n3 Or enter correct folder.\nCannot Proceed Exiting!")
            time.sleep(2)
            sys.exit()

        else:
            print("Installing Pandas and Psutil, please wait...")
            if(os.system(str(default_dir+"/scripts/pip3.exe install pandas"))!=0):
                print("\nPandas Installation Failed!")
                time.sleep(2)
                sys.exit()
            elif(os.system(str(default_dir+"/scripts/pip3.exe install psutil"))!=0):
                print("\nPsutil Installation Failed!")
                time.sleep(2)
                sys.exit()
            else:
                print("\nThe necessary python packages have been installed, you can now use the tool")
                time.sleep(2)
                sys.exit()
