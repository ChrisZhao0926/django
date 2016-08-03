#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Chris
@license:  
@file: dms_manager.py
@time: 8/3/16 3:04 PM
"""
import pymssql
from dms import config


class DMS:
    def __init__(self, server, user, pwd, db):
        self.server = server
        self.user = user
        self.pwd = pwd
        self.db = db

    def __get_connect(self):
        if not self.db:
            raise(NameError, 'db not exist!')
        self.conn = pymssql.connect(self.server, self.user, self.pwd, self.db)
        cursor = self.conn.cursor(as_dict=True)
        if not cursor:
            raise(NameError, 'connect server failed!')
        else:
            return cursor

    def execute(self,sql):
        cursor = self.__get_connect()
        cursor.execute(sql)
        for row in cursor:
            print('row = %r' % (row,))
        result = cursor.fetchall()
        self.conn.close()
        return result


def main():

    ms = DMS(server=config.SERVER, user=config.USERNAME, pwd=config.PASSWORD, db=config.DB_NAME)
    resList = ms.execute()
    for row in resList:
        print('row = %r' % (row,))


if __name__ == '__main__':
    main()
