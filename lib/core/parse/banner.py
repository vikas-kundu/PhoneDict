#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# coded by Vikas Kundu https://github.com/vikas-kundu
# -------------------------------------------



def logo():
    print('''                                                                                  
            ,,                                                 ,,                 
`7MM"""Mq.`7MM                                  `7MM"""Yb.     db           mm    
  MM   `MM. MM                                    MM    `Yb.                MM    
  MM   ,M9  MMpMMMb.  ,pW"Wq.`7MMpMMMb.  .gP"Ya   MM     `Mb `7MM  ,p6"bo mmMMmm  
  MMmmdM9   MM    MM 6W'   `Wb MM    MM ,M'   Yb  MM      MM   MM 6M'  OO   MM    
  MM        MM    MM 8M     M8 MM    MM 8M""""""  MM     ,MP   MM 8M        MM    
  MM        MM    MM YA.   ,A9 MM    MM YM.    ,  MM    ,dP'   MM YM.    ,  MM    
.JMML.    .JMML  JMML.`Ybmd9'.JMML  JMML.`Mbmmd'.JMMmmmdP'   .JMML.YMbmd'   `Mbmo 
                                                                                                                                                                    
    ''')

def usage():
    print('''
-m,--mode ##The mode to work in(offline=0 or online=1)

-t,--task ##Task to be done i.e.
    Create a dictionary or search a number.
    -t 0(write) = To create a dictionary.
    -t 1(search)= To search a number.

-c,--country ##The country of your choice.

-o,--output ##Location and name of output file. Only .txt format is accepted.
            ##i.e. C:\\Users\\home-pc\\Desktop\\dict.txt
	    ##i.e. /home/homepc/Desktop/dict.txt

-n,--number ##The number for which to search info like location, telecom etc. Used with -t 1

-w,--wizard ##User friendly interface to guide through the process.

-h,--help ##Prints help info to the screen.

-i,--install ##Checks for Python version 3 and pip3. Installs the necessary packages.(Pandas and Psutil)

Usage Example: phonedict.py -m 1 -t 0 -c india -o C:\\Users\\home-pc\\Desktop\\dict.txt
Usage Example: phonedict.py -m 0 -t 1 -c india -n 1234567890
Usage Example: phonedict.py --wizard
Usage Example: phonedict.py -h
    ''')

