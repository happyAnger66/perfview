# Copyright (C) @2023 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com

import  re

w_version_re = re.compile(r'version=(\w+)')
w_and_version_re = re.compile(r'and version=(\w+)')

w_ad_re = re.compile(r'auto_drive=(\d+)')
w_and_ad_re = re.compile(r'and auto_drive=(\d+)')

def get_con_in_where(sql, w_re, w_and_re):
    version = None
    a_version_r = w_and_re.search(sql)
    version_r = w_re.search(sql)
    if a_version_r:
        version = a_version_r.groups()[0]
        start, end = a_version_r.span()
        sql = sql[:start] + sql[end:]
        return version, sql

    if version_r:
        version = version_r.groups()[0]
        start, end = version_r.span()
        sql = sql[:start] + sql[end:]
        return version, sql

    return version, sql

if __name__ == "__main__":
    sql = "select sensor_name, status, count(*) from sensor_status_info where status != 1 group by sensor_name, status and version=release2023"
    print(get_con_in_where(sql, w_version_re, w_and_version_re))

    sql = "select sensor_name, status, count(*) from sensor_status_info where status != 1 group by sensor_name, status and version=dev "
    print(get_con_in_where(sql, w_version_re, w_and_version_re))

    sql = "select sensor_name, status, count(*) from sensor_status_info where status != 1 group by sensor_name, status and ver=dev "
    print(get_con_in_where(sql, w_version_re, w_and_version_re))

    sql = "select sensor_name, status, count(*) from sensor_status_info where status != 1 group by sensor_name, status"
    print(get_con_in_where(sql, w_version_re, w_and_version_re))

    sql = "select sensor_name, status, count(*) from sensor_status_info where status != 1 group by sensor_name, status and auto_drive=0"
    print(get_con_in_where(sql, w_ad_re, w_and_ad_re))

    sql = "select sensor_name, status, count(*) from sensor_status_info where status != 1 group by sensor_name, status and auto_drive=1 "
    print(get_con_in_where(sql, w_ad_re, w_and_ad_re))

    sql = "select sensor_name, status, count(*) from sensor_status_info where status != 1 group by sensor_name, status and version=dev and auto_drive=0"
    print(get_con_in_where(sql, w_ad_re, w_and_ad_re))

    sql = "select sensor_name, status, count(*) from sensor_status_info where status != 1 group by sensor_name, status"
    print(get_con_in_where(sql, w_ad_re, w_and_ad_re))
