#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# coded by Vikas Kundu https://github.com/vikas-kundu
# -------------------------------------------

import config

operators={
    "AT":"Airtel India",
    "CG":"BSNL Mobile",
    "DP":"MTNL (DOLPHIN)",
    "AV":"AEROVOCE",
    "RJ":"Reliance Jio",
    "VF":"Vodafone India-Merged with Idea Cellular-Vodafone Idea Ltd",
    "ID":"Idea Cellular-Merged with Vodafone India-Vodafone Idea Ltd",
    "ET":"Etisalat India",
    "SR":"Subrin Rintel",
    "ST":"S Tel",
    "LM":"Loop Mobile",
    "RC":"Reliance Mobile CDMA",
    "VD":"Videocon Telecom",
    "MT":"MTS India",
    "RG":"Reliance Mobile GSM",
    "AC":"AIRCEL",
    "TD":"TATA DOCOMO",
    "TN":"telenor"
    }

def find(*args):
    total_table=args[0][0]
    operator_table=args[0][1]
    code=str(config.str_number)[:4]
    matching_table=total_table[ (total_table['code'] == int(code))]
    if(len(matching_table)==0):
        print("\nSorry nothing found please recheck number!")
    else:
        lst=matching_table.values.tolist()
        more_info=operator_table[(operator_table['Code'] == str(lst[0][2]))]
        lst2=more_info.values.tolist()
        try:
            print("\nTelecom operator:",operators[str(lst[0][1])])
            print("Area:",lst2[0][0],"\nType:",lst2[0][2],"\nDetails:",lst2[0][3])
        except KeyError:
            print("\nNo entry for this record found. Most probably this number has not been alloted!")
