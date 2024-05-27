# Copyright (C) @2022 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com

import re

re_cols = re.compile(r'select (.*) from.*')

def get_table_from_sql(sql):
    sql = sql.lower()
    table_start = sql.find("from")
    table_end = sql.find("where")

    if table_start == -1:
        return "unkown"

    if table_end != -1:
        table_end = table_end - 1

    table_start = table_start + len("from")
    return sql[table_start:table_end].strip()

def get_select_cols_ex(sql):
    head = sql.find("select") + len("select")
    tail = sql.find("from")
    cols = sql[head:tail]
    return [col.strip() for col in cols.split(',')]

def get_car_type(sql):
    head = sql.find("and car_type=")
    if head == -1:
        return "all"
    head_n = head + len("and car_type=")
    tail = sql.find(" ", head_n)
    if tail == -1:
        car_type = sql[head_n:]
        sql = sql[:head]
    else:
        car_type = sql[head_n:tail]
        sql = sql[:head] + sql[tail:]
    return car_type, sql

def get_select_cols(sql):
    groups = re.match(re_cols, sql)
    if groups is None:
        return []
    cols = groups.group(1)
    return [col.strip() for col in cols.split(',')]
