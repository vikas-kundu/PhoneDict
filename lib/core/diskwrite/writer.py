#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# coded by Vikas Kundu https://github.com/vikas-kundu
# -------------------------------------------

import sys
import time
import os
import psutil
import config

def space_check(*args):
        print("Calculating the dictionary size and disk free space...")
        suffix_len=10-len(str(args[0]))
        estimated_len=( ( (args[1])*12 ) * ( 10**suffix_len ) )/(1024**2)
        obj_Disk = psutil.disk_usage(str(os.path.split(config.str_output)[0]))
        
        if(int(obj_Disk.free / (1024 ** 2))>int(estimated_len)):
                print("\n Estimated file size: ",round(estimated_len,2),"MB")
        else:
           print("\nNot enough free space on this disk!")
           time.sleep(1)
           sys.exit()

def dict_create(mobile_code):
        space_check(list(mobile_code)[0],len(mobile_code))
        #Method 1: (Fast and easy to understand but takes more resources)
        t0 = time.time()
        index=1 
        suffix_len=10-len(str(list(mobile_code)[0]))
        f = open(config.str_output, "w")
        print("\nPlease be patient. Now writing to the disk!")
        for i in mobile_code:
                progress=(index/(len(mobile_code)))*100
                print("...",round(progress,2),"% Completed...")
                index+=1
                for j in range (0,10**suffix_len):
                    j=str(j).zfill(suffix_len)  
                    f.write(str(i)+str(j)+"\n")

        f.close()
        d = time.time() - t0
        print ("\nTime taken: %.2f s. \n\nSuccess! Exiting!" % d)
        
def dict_create2(mobile_code):
        space_check(list(mobile_code)[0],len(mobile_code))
        #Method 2: (Low on memory and Disk but takes more time than method 1)
        t0 = time.time()
        f = open(config.str_output, "w")        
        f.writelines(str(x) + str(y)+"\n" for x in mobile_code for y in {str(i).zfill(6) for i in range(0,1000000)})
        d = time.time() - t0
        print ("Time taken: %.2f s." % d)
        print("Sucess!")


