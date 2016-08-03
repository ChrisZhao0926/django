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
from dms import config


def rft_cav():
    dms = dms_manager.DMS(server=config.SERVER, user=config.USERNAME, pwd=config.PASSWORD, db=config.DB_NAME)
    result = dms.execute(sqlquery.RFT_CAV)

if __name__ == '__main__':
    rft_cav()
