#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# coded by Vikas Kundu https://github.com/vikas-kundu
# -------------------------------------------

import sys
import config
import importlib
from lib.core import util
from lib.core import wizard
from lib.core.parse import banner
from lib.core.parse import cmdline

def pre_checks():
    if(util.packages_check()==False):
        print("Looks like some modules have not been installed.\nTry again with: phonedict.py -i")
        sys.exit()

    if(config.wizard==True):
        wizard.guide()

    if(util.parameters_check()!=True):
        sys.exit()

def main():
    banner.logo()
    cmdline.options()
    pre_checks()
    
    if((config.str_task=="0") and (config.str_mode=="0")):
        generator_module = importlib.import_module("lib.country."+config.str_country+"_generator") ####https://stackoverflow.com/questions/8718885/
        args=generator_module.chooser(generator_module.offline())
        from lib.core.diskwrite import writer
        writer.dict_create(args)

    elif(config.str_task=="0" and config.str_mode=="1"):
        generator_module = importlib.import_module("lib.country."+config.str_country+"_generator")
        args=generator_module.chooser(generator_module.online())
        from lib.core.diskwrite import writer
        writer.dict_create(args)

    elif((config.str_task=="1") and (config.str_mode=="0")):
        generator_module = importlib.import_module("lib.country."+config.str_country+"_generator")
        search=importlib.import_module("lib.country."+config.str_country+"_search")
        search.find(generator_module.offline())

    elif((config.str_task=="1") and (config.str_mode=="1")):
        generator_module = importlib.import_module("lib.country."+config.str_country+"_generator")
        search=importlib.import_module("lib.country."+config.str_country+"_search")
        search.find(generator_module.online())
   
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nUser Quit!")
    except SystemExit:
        print("\nTermiated!")
        
