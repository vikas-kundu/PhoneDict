#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# coded by Vikas Kundu https://github.com/vikas-kundu
# -------------------------------------------

import sys
import getopt
import time
import config
from lib.core.parse import banner
from lib.core import util
from lib.core import installer


def options():
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'm:t:c:o:n:whi', ['mode','task','country','output','number','wizard','help','install'])
        if((len(sys.argv)==9) or (len(sys.argv)==2)):
            pass
        else:
            print("Error! Some parameter is missing please check!")
            time.sleep(2)
            banner.usage()
            sys.exit()
        
    except getopt.GetoptError as err:
        print(err)
        banner.usage()
        sys.exit(2)

    for (o, a) in opts:
        if(o in('-i','--install')):
            if(util.packages_check()==False):
                installer.start_install()
            else:
                print("Packages already installed!")
                sys.exit()

        elif (o in ('-w', '--wizard')):
            config.wizard=True

        elif o in ('-h','--help'):
            banner.usage()
            sys.exit()

        elif o in ('-m','--mode'):
            config.str_mode=str(a)
            
        elif o in ('-t','--task'):
            config.str_task=str(a)
            
        elif o in ('-c','--country'):
            config.str_country=str(a.lower().strip('"\''))
            
        elif o in ('-o','--output'):
            config.str_output=str(a.strip('"\''))
            
        elif o in ('-n','--number'):
            config.str_number=str(a.strip('"\''))

        else:
            print("Something went wrong with argument parsing!")
            time.sleep(2)
            banner.usage()
            sys.exit()
