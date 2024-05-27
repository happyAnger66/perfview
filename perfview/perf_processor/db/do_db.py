# Copyright (C) @2024 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com
import logging
import sqlite3

class DataBase:
    def __init__(self, url):
        self._url = url
        self._conn = sqlite3.connect(url)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()

    def close(self):
        self._conn.close()

    def execute_many(self, sql, datas):
        try:
            cursor = self._conn.cursor()
            cursor.executemany(sql, datas)
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()
            logging.error('execute many sql:%s failed:%s' % (sql, e))

    def execute(self, sql):
        try:
            cursor = self._conn.cursor()
            cursor.execute(sql)
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()
            logging.error('execute sql:%s failed:%s' % (sql, e))



