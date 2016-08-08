#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Chris
@license:  
@file: execute.py
@time: 8/3/16 2:44 PM
"""

from dms import dms_manager
from dms import sqlquery
import datetime.time


def rft_cav():
    dms = dms_manager.DMS()
    dms.execute(sqlquery.RFT_CAV)


def qualify_cav():
    dms = dms_manager.DMS()
    dms.execute(sqlquery.QUALIFY_CAV)


def rft_lv():
    dms = dms_manager.DMS()
    dms.execute(sqlquery.RFT_LV)


def qualify_lv():
    dms = dms_manager.DMS()
    dms.execute(sqlquery.QUALIFY_LV)


def lr_lv():
    dms = dms_manager.DMS()
    dms.execute(sqlquery.LR_LV)

if __name__ == '__main__':
    datetime.datetime.now()
    lr_lv()
