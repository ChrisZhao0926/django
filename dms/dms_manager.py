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
    def __init__(self):
        self.server = config.SERVER
        self.user = config.USERNAME
        self.pwd = config.PASSWORD
        self.db = config.DB_NAME

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
        total = cursor.rowcount
        print('total count %r' % (total,))
        self.conn.close()
        return result


def main():

    ms = DMS()
    resList = ms.execute()
    for row in resList:
        print('row = %r' % (row,))


if __name__ == '__main__':
    main()
