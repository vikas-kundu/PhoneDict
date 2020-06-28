#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# coded by Vikas Kundu https://github.com/vikas-kundu
# -------------------------------------------

import sys
import config
from lib.core.parse import cmdline
from lib.core import util

def guide():
    task=input("\nWhat do you wish to do?\n1. Create a dictionary \n2. Search a number\n")[:1]
    mode=input("\nHow do you wish to do it?\n1. Offline \n2. Online\n")[:1]
    country=input("\nPlease Enter the country of your choice i.e. india: ")
    try:
        if(int(task)==1):
            output=input("\nPlease enter the location and name (*.txt) of your output file i.e. C:\\Users\\home-pc\\Desktop\\dict.txt: ")
            config.str_output=str(output).strip('"\'')

        elif(int(task)==2):
            number=(input("\nPlease enter the number of your choice: "))
            config.str_number=str(number).strip('"\'')

        config.str_mode=str(int(mode)-1)
        config.str_task=str(int(task)-1)
        config.str_country=str(country).lower()
        
    except ValueError as err:
        print(err)
        sys.exit()
            
