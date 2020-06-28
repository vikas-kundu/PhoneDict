#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# coded by Vikas Kundu https://github.com/vikas-kundu
# -------------------------------------------

import sys
import urllib
from pkg_resources import resource_filename

import pandas as pd
pd.set_option('precision', 0)
pd.options.display.max_colwidth = 150

def chooser(*args):
    mobile_code=set()
    code_list=list()

    codes_table=args[0][0]
    area_info=args[0][1]

    print(area_info[['Circle name','Code']])
    more_info=input(str("\nNeed more info regarding circle name?(Y/N): "))

    if(more_info.lower()=='y'):
        print("\n",area_info[['Code','Geographic area(s) covered']])
    else:
        pass

    area = str(input("\n\nEnter your state code form above table i.e. DL \n\nMultiple states can be added separated by a comma i.e. jk,dl,hr\n\nTo select all the states, enter 0 : ")).split(",") 

    if('0' in area):
        code_list=codes_table[['code']].values.tolist()
    else:
        for i in area:
            matching_table=codes_table[ (codes_table['state'] == str(i).upper())]
            code_list=code_list+matching_table[['code']].values.tolist()

    if(len(code_list)==0):
        print("\nError No matching region found!")
        sys.exit()
    else:
        for i in code_list:
            for j in i:
                mobile_code.add(j)
    return mobile_code

def offline():    
    print('''

The offline data has been generated using an
online source. All the efforts have been made
to avoid errors. If you spot any please raise
an issue.



Please wait reading data...

    ''')
    open(resource_filename('data', 'india.html'), 'rb')
    option_table = pd.read_html(open(resource_filename('data', 'india.html'), 'rb'))[0]
    print("Generating Tables...")

    total= pd.read_html(open(resource_filename('data', 'india.html'), 'rb'))[1]
    total=total.drop('Unnamed: 0', axis=1)
    option_table=option_table.drop('Unnamed: 0', axis=1)
    #minor adjustment
    option_table=option_table.append({"Category[3]":'Metro',"Circle name":'Chennai',"Code":'CH',"Geographic area(s) covered":'refers to Chennai, which has been merged with Tamil Nadu circle.'},ignore_index=True)

    return (total,option_table)

def online():
    print("""

The source for these mobile codes is Wikipedia. Often the edits may be incorrect
which can tamper with the authenticity of data. So prefer the offline mode.
The last known correct edit by the author of this module is: https://w.wiki/V94
i.e. diff=963687820&oldid=959336425



Please be patient data scraping under process...

    """)
    link = "https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India"
    try:
        total = pd.DataFrame(columns = ['code', 'telecom','state']) 
        table_index=3

        while (table_index<=6):
            tables = pd.read_html(link)[table_index]
            base=tables.iloc[:, 0:3]
            base.columns = total.columns
            index=0
            while (index<=24):
                top=tables.iloc[:,(index+3):(index+6)]
                top.columns=base.columns
                base=base.append(top)
                index+=3
            total=base.append(total)
            table_index+=1
            print(round(((table_index-3)/4)*100,2),"% Done!")

        print("Generating Tables...")
        total = total[total['code'].notna()]
        option_table = pd.read_html(link)[0]
        #minor adjustment
        option_table=option_table.append({"Category[3]":'Metro',"Circle name":'Chennai',"Code":'CH',"Geographic area(s) covered":'refers to Chennai, which has been merged with Tamil Nadu circle.'},ignore_index=True)
        total.code=total.code.apply(int)
        return (total,option_table)

    except urllib.error.URLError as err:
        print(err)
