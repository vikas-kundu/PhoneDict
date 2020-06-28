#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# coded by Vikas Kundu https://github.com/vikas-kundu
# -------------------------------------------

import os
import re
import config

def parameters_check():
	if(str(config.str_mode)!="0" and str(config.str_mode)!="1"):
        	print("\nError! Mode can be either 1 or 0\nWrong input exiting!")
    	
	elif(str(config.str_task)!="0" and str(config.str_task)!="1"):
	        print("\nError! Task value can be either 1 or 0\nWrong input exiting!")
    
	elif(str(config.str_country).lower() not in config.countries_supported):
	        print("\nSorry your country is not supported at the moment. These are the ones supported: \n",config.countries_supported)
    
	elif(str(config.str_task)=="0" and ".txt" not in str(config.str_output)):
        	print("\nNo valid output file name found! Make sure filename is of .txt type")
	
	elif(str(config.str_task)=="0" and os.path.isdir(os.path.dirname(str(config.str_output).strip('"\''))) == False):
			print("\nNo valid directory found!")
	
	elif(str(config.str_task)=="1" and (len(str(config.str_number))!=10 or len(re.findall("[0-9]", str(config.str_number)))!=10 or str(config.str_number)[:1]=="0") ):
		print("\nNot a valid number!")
	else:
        	return True

def packages_check():
        try:
                import pandas
                import psutil
                return True
        except(Exception):
                return False

