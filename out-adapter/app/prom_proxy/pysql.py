# Copyright (C) @2022 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com

'''
CREATE TABLE perf_e2e(
   TIMESTAMP timestamp PRIMARY KEY     NOT NULL,
   lidar_ipc smallint,
   lidar_sched smallint,
   lidar_proc smallint,
   topdown_detections_ipc smallint,
   topdown_detections_sched smallint,
   topdown_detections_proc smallint,
   mot_tracks_ipc smallint,
   mot_tracks_sched smallint,
   mot_tracks_proc smallint,
   pred_obstacles_ipc smallint,
   pred_obstacles_sched smallint,
   pred_obstacles_proc smallint,
   planner_traj_ipc smallint,
   planner_traj_sched smallint,
   planner_traj_proc smallint,
   control_ipc smallint,
   control_sched smallint,
   contro_proc smallint,
   car_no integer NOT NULL
);
'''
import datetime
import time
import re
from collections import defaultdict, deque
import logging

#import psycopg2
#import numpy as np
import random


from .db_utils import get_select_cols, get_table_from_sql, get_select_cols_ex, get_car_type
from .utils import TripEvent

PROMETHEUS_TIME_OFFSET = 3600 * 8
TIMESTAMP_TO_MIN = 60
TIMESTAMP_TO_HOUR = 3600

logger = logging.getLogger('pysql')

con_re = re.compile(r'([\w]+)=([\w/\'\"]+)')
w_version_re = re.compile(r'version=([\w/]+)')
w_trip_re = re.compile(r"trip_id='([\w-]+)'")
w_and_version_re = re.compile(r'and version=([\w/]+)')
w_ad_re = re.compile(r'auto_drive=(\d+)')
w_and_ad_re = re.compile(r'and auto_drive=(\d+)')
s_ad_re = re.compile(r"auto_drive='(\w+)'")
s_and_ad_re = re.compile(r"and auto_drive='(\w+)'")

str_value_map = {
    'NORMAL': 0,
    'RR': 2
}

normal_table = ['perf_trip_item_info', 'task_failed', 'do_trip_bag']

class DBOper:
    def __init__(self, db_str, db_type="sqlite3"):
        self._db_str = db_str
        self._db_type = db_type

    def __enter__(self):
        if self._db_type=="postgres":
            try:
                import psycopg2
                self._conn = psycopg2.connect(self._db_str)
            except Exception as e:
                raise Exception('psycopg2 connect err:%s' % e)
        else:
            try:
                import sqlite3
                self._conn = sqlite3.connect(self._db_str)
            except Exception as e:
                raise Exception('sqlite3 connect err:%s' % e)

        return self

    def get_version_trips(self, version):
        trips = self.get_all_trips_by_version(version)
        return {"trips_num": [(1, len(trips))]}

    def sql_and_car_type(self, sql, car_type):
        if car_type == "all":
            return sql

        if car_type == "x86":
            sql += ' and car_no!=10010 and car_no!=10048 and car_no!=10011 and car_no!=10047'
            return sql

        if car_type == "orin":
            sql += ' and (car_no=10010 or car_no=10048 or car_no=10011 or car_no=10047)'
            return sql

        return sql

    def hz(self, sql):
        cols = get_select_cols(sql)
        sql = sql.replace("huizong,", "")

        car_type, sql = get_car_type(sql)
        datas = defaultdict(list)
        if 'p50' in cols:
            sql = sql.replace("p50,", "")
            p50 = self.get_hz_p(sql, 0.5, car_type)
            for k, v in p50.items():
                datas[k].append((1, v))
        elif 'p9999' in cols:
            sql = sql.replace("p9999,", "")
            p9999 = self.get_hz_p(sql, 0.9999, car_type)
            for k, v in p9999.items():
                datas[k].append((1, v))
        elif 'p99' in cols:
            sql = sql.replace("p99,", "")
            p99 = self.get_hz_p(sql, 0.99, car_type)
            for k, v in p99.items():
                datas[k].append((1, v))
        return datas

    def get_version_e2e(self, version, sql):
        cols = get_select_cols(sql)
        car_type, _ = get_car_type(sql)
        datas = defaultdict(list)
        if 'p50' in cols:
            p50 = self.get_version_e2e_p(version, 0.5, car_type)
            for k, v in p50.items():
                datas[k].append((1, v))
        elif 'p9999' in cols:
            p9999 = self.get_version_e2e_p(version, 0.9999, car_type)
            for k, v in p9999.items():
                datas[k].append((1, v))
        elif 'p99' in cols:
            p99 = self.get_version_e2e_p(version, 0.99, car_type)
            for k, v in p99.items():
                datas[k].append((1, v))
        return datas

    def get_hz_p(self, sql, p, car_type="all"):
        sql = self.sql_and_car_type(sql, car_type)
        cols = get_select_cols_ex(sql)
        cursor = self._conn.cursor()
        print('hz p sql', sql)
        cursor.execute(sql)
        items = cursor.fetchall()

        p_sums = defaultdict(list)
        p_val = defaultdict(float)
        for item in items:
            key, val = item[0], float(item[1])
            p_sums[key].append(float(val))

        for k, v in p_sums.items():
            n = len(v)
            if p == 0:
                pos = 0
            elif p == -1:
                pos = n - 1
            else:
                pos = min(int(n * p), n - 1)
            p_val[k] = (sorted(v))[pos]

        return p_val

    def get_version_e2e_p(self, version, p, car_type="all"):
        sql = "select total_latency, topdown_detections_ipc, topdown_detections_sched, topdown_detections_proc, \
                mot_tracks_ipc, mot_tracks_sched, mot_tracks_proc, \
                pred_obstacles_ipc, pred_obstacles_sched, pred_obstacles_proc, \
                planner_traj_ipc, planner_traj_sched, planner_traj_proc, \
                control_ipc, control_sched, control_proc from perf_e2e where trip_id in (select trip_id from trip_detail where git_branch=%s)" % version
        sql = self.sql_and_car_type(sql, car_type)
        cols = get_select_cols_ex(sql)
        cursor = self._conn.cursor()
        print('e2e sql', sql)
        cursor.execute(sql)
        items = cursor.fetchall()

        p_sums = defaultdict(list)
        p_val = defaultdict(float)
        for item in items:
            for i, val in enumerate(item):
                col = cols[i]
                p_sums[col].append(val)

        for k, v in p_sums.items():
            n = len(v)
            if p == 0:
                pos = 0
            elif p == -1:
                pos = n - 1
            else:
                pos = min(int(n * p), n - 1)
            p_val[k] = (sorted(v))[pos]

        return p_val

    def get_all_trips_by_version(self, version, start=-1, end=-1):
        if version[0] == "'":
            sql = "select distinct trip_id from trip_detail where git_branch=%s" % version
        else:
            sql = "select distinct trip_id from trip_detail where git_branch='%s'" % version

        filter = False
        if start != -1 and end != -1:
            filter = True

        cursor = self._conn.cursor()
        cursor.execute(sql)
        r = cursor.fetchall()
        trips = []
        for data in r:
            trip = data[0]
            if filter:
                if self.filter_trip_by_start_end(trip, start, end):
                    trips.append(trip)
            else:
                trips.append(trip)
        return trips

    def get_version_ad_time(self, version):
        datas = defaultdict(list)
        all_trips = self.get_all_trips_by_version(version)
        t_ad, t_dis = 0.0, 0.0
        for trip in all_trips:
            ad = self.get_trip_ad_time(trip)
            t_ad += ad[0]
            t_dis += ad[1]
        datas["ad_time"].append((1, t_ad))
        datas["total_time"].append((1, t_dis))
        print('ad time', datas)
        return datas

    def get_version_ad_distance(self, version):
        datas = defaultdict(list)
        all_trips = self.get_all_trips_by_version(version)
        t_ad, t_dis = 0.0, 0.0
        for trip in all_trips:
            ad = self.get_trip_ad_distance(trip)
            t_ad += ad[0]
            t_dis += ad[1]
        datas["ad_distance"].append((1, t_ad))
        datas["total_distance"].append((1, t_dis))
        print('ad distances', datas)
        return datas

    def get_trip_ad_time_ranges(self, trip):
        sql = "select * from trip_events where trip_id='%s' order by timestamp" % trip
        cursor = self._conn.cursor()
        cursor.execute(sql)
        r = cursor.fetchall()
        tes = []
        ad_time_ranges = []
        for ts in r:
            te = TripEvent._make(ts)
            tes.append(te)

        if not tes:
            return ad_time_ranges

        status, ad_begin, ad_end = 0, 0, 0
        ad_time = 0
        for te in tes:
            if te.event == "lat_start" or te.event == "long_start":
                if status == 0:
                    status = 1
                elif status == 1:
                    status = 2
                    ad_begin = te.ts.timestamp()
            elif te.event == "lat_stop" or te.event == "long_stop":
                if status == 2:
                    ad_end = te.ts.timestamp()
                    ad_time_ranges.append((ad_begin, ad_end))
                status = 0
        return ad_time_ranges

    def get_trip_ad_time(self, trip):
        sql = "select * from trip_events where trip_id='%s' order by timestamp" % trip
        cursor = self._conn.cursor()
        cursor.execute(sql)
        r = cursor.fetchall()
        tes = []
        for ts in r:
            te = TripEvent._make(ts)
            tes.append(te)

        if not tes:
            return (0.0, 0.0)

        status, ad_begin, ad_end = 0, 0, 0
        ad_time = 0
        for te in tes:
            if te.event == "lat_start" or te.event == "long_start":
                if status == 0:
                    status = 1
                elif status == 1:
                    status = 2
                    ad_begin = te.ts.timestamp()
            elif te.event == "lat_stop" or te.event == "long_stop":
                if status == 2:
                    ad_end = te.ts.timestamp()
                    ad_time += (ad_end - ad_begin) / TIMESTAMP_TO_HOUR
                status = 0
        total_time = (tes[-1].ts.timestamp() -
                      tes[0].ts.timestamp()) / TIMESTAMP_TO_HOUR
        if ad_time == 0:
            print('trip %s ad_time is 0' % trip)
            return 0, 0
        return (float(ad_time), float(total_time))

    def get_trip_ad_distance(self, trip):
        sql = "select * from trip_events where trip_id='%s' order by timestamp" % trip
        cursor = self._conn.cursor()
        cursor.execute(sql)
        r = cursor.fetchall()
        tes = []
        for ts in r:
            te = TripEvent._make(ts)
            tes.append(te)

        if not tes:
            return (0.0, 0.0)

        status, ad_begin, ad_end = 0, 0, 0
        ad_distance = 0
        for te in tes:
            if te.event == "lat_start" or te.event == "long_start":
                if status == 0:
                    status = 1
                elif status == 1:
                    status = 2
                    ad_begin = te.distance
            elif te.event == "lat_stop" or te.event == "long_stop":
                if status == 2:
                    ad_end = te.distance
                    ad_distance += (ad_end - ad_begin) / 1000
                status = 0
        total_distance = (tes[-1].distance - tes[0].distance) / 1000
        if ad_distance == 0:
            print('trip %s ad_distance is 0' % trip)
            return 0, 0
        return (float(ad_distance), float(total_distance))

    def filter_timestamp_by_range(self, timestamp, start, end):
        if start == -1 and end == -1:
            return True
        return start <= timestamp and timestamp <= end

    def query_trip_auto_drive_info(self, sql, start, end):
        datas = defaultdict(list)
        cursor = self._conn.cursor()
        cursor.execute(sql)
        r = cursor.fetchall()
        tes = []
        for ts in r:
            te = TripEvent._make(ts)
            tes.append(te)

        times = deque()
        for te in tes:
            timestamp = te.ts.timestamp() - PROMETHEUS_TIME_OFFSET
            if te.event == "begin" or te.event == "end" or te.event == "lat_stop":
                times.append((round(timestamp, 2), 0))
            elif te.event == "lat_start":
                times.append((round(timestamp, 2), 1))

        #logger.info('timestamp:%s', times)
        #logger.info('start-end:%s-%s', start, end)
        if times:
            head = times.popleft()
#            datas["auto_drive_mode"].append(head)
            cur_time, cur_status = head[0], head[1]
            while times:
                next = times.popleft()
                next_time, next_status = next[0], next[1]
                while cur_time + 5 < next_time:
                    cur_time += 5
                    if self.filter_timestamp_by_range(cur_time, start, end):
                        datas["auto_drive_mode"].append((cur_time, cur_status))
                cur_time, cur_status = next_time, next_status
                if self.filter_timestamp_by_range(cur_time, start, end):
                    datas["auto_drive_mode"].append((cur_time, cur_status))

        return datas

    def query_p(self, sql):
        datas = defaultdict(list)
        cols = get_select_cols(sql)
        is_total = False
        if "total" in cols:
            is_total = True
            sql = sql.replace("total,", "")
        cursor = self._conn.cursor()
        cursor.execute(sql)
        items = cursor.fetchall()
        items = sorted(items, key=lambda x: x[0])
        for item in items:
            ts = item[0]
            #print(ts, time.mktime(ts.timetuple()), ts.timestamp())
            timestamp = ts.timestamp()
            total = 0
            for i, val in enumerate(item[1:], 1):
                if val > 500:
                    continue
                total += val
                datas[cols[i]].append([round(timestamp, 2), str(val)])
            datas["total"].append([round(timestamp, 2), str(total)])
            # prev_ts = timestamp
        return datas

    def sql_by_query(self, table, cols, conditions=None,
                     order_by=None, distinct=False):
        sql = "select "
        if distinct:
            sql += " distinct "

        for col in cols[:-1]:
            sql += ' %s,' % col

        sql += cols[-1]
        sql += " from %s" % table

        if conditions:
            sql += ' where %s' % conditions

        if order_by:
            sql += " " + order_by
        return sql

    def query_datas(self, table, cols, conditions=None,
                    order_by=None, distinct=False):
        datas = defaultdict(list)
        sql = self.sql_by_query(table, cols, conditions, order_by, distinct)

        cursor = self._conn.cursor()
        cursor.execute(sql)
        items = cursor.fetchall()
        for item in items:
            for i, val in enumerate(item):
                datas[cols[i]].append(val)

        return datas

    def get_query_conditions(self, sql):
        w_pos = sql.find("where")
        if w_pos == -1:
            return

        datas = {}
        w_str = sql[w_pos + len("where"):]
        condtions = con_re.findall(w_str)
        for k, v in condtions:
            datas[k] = v
        return datas

    def query_version(self, sql, start=None, end=None):
        cols = get_select_cols(sql)
        conditions = self.get_query_conditions(sql)
        if "version" in conditions:
            if "ad_distance" in cols:
                return self.get_version_ad_distance(conditions["version"])
            if "ad_time" in cols:
                return self.get_version_ad_time(conditions["version"])
            elif "trips" in cols:
                return self.get_version_trips(conditions["version"])
            elif "e2e" in cols:
                return self.get_version_e2e(conditions["version"], sql)
            elif "node_cpu" in cols:
                return self.get_version_node_cpu(conditions["version"], sql)
        return {}

    def sql_get_trip_start_end_ts(self, trip):
        if trip is None:
            return -1, -1
        sql = "select start_ts, end_ts from trip_detail where trip_id='%s'" % trip
        cursor = self._conn.cursor()
        cursor.execute(sql)
        items = cursor.fetchall()
        if items:
            item = items[0]
            return item[0], item[1]

        return -1, -1

    def sql_add_trip_ad_timerange(self, sql, trip, timerange):
        add_sql = " trip_id='%s' and ( " % trip

        i = 0
        for t_r in timerange:
            start, end = t_r
            if i == 0:
                add_sql += " timestamp between to_timestamp(%f) and to_timestamp(%f)" % (
                    start, end
                )
            else:
                add_sql += " or timestamp between to_timestamp(%f) and to_timestamp(%f)" % (
                    start, end
                )
            i += 1

        add_sql += " ) "

        w_index = sql.find("where")
        if w_index == -1:
            sql = sql + " where " + add_sql
        else:
            sql = sql[:w_index + len("where")] + add_sql + \
                " and " + sql[w_index + len("where"):]

        return sql

    def sql_add_ad(self, sql):
        trip_id = self.get_trip_id_from_sql(sql)
        if trip_id is None:
            return sql

        ad_times = self.get_trip_ad_time_ranges(trip_id)
        if not ad_times:
            logger.info('trip:%s no ad times' % trip_id)
            return sql

        s = 'trip:%s' % ad_times
        logger.info(s)

        add_sql = " and ("
        i = 0
        for ad_time in ad_times:
            start, end = ad_time
            if i == 0:
                add_sql += " timestamp between to_timestamp(%f) and to_timestamp(%f)" % (
                    start, end
                )
            else:
                add_sql += " or timestamp between to_timestamp(%f) and to_timestamp(%f)" % (
                    start, end
                )
            i += 1

        add_sql += " ) "

        if i > 0:
            sql += add_sql

        #logger.info('trip ad sql:%s' % sql)
        return sql

    def sql_add_timerange(self, sql, start, end, timeoffset=PROMETHEUS_TIME_OFFSET):
        add_sql = ""
        if "where" in sql:
            add_sql = " and timestamp between to_timestamp(%f) and to_timestamp(%f)" % (
                start + timeoffset, end + timeoffset)
        else:
            add_sql = " where timestamp between to_timestamp(%f) and to_timestamp(%f)" % (
                start + timeoffset, end + timeoffset)

        group_by_i = sql.find('group by')
        if group_by_i != -1:
            sql = sql[:group_by_i] + add_sql + " " + sql[group_by_i:]
            return sql

        return sql + add_sql

    def get_ad_status(self, sql):
        new_sql, ad_status = sql, "all"
        ad_match = s_ad_re.search(sql)
        and_ad_match = s_and_ad_re.search(sql)
        if ad_match:
            ad_status=ad_match.groups()[0]
            new_sql = sql.replace("auto_drive='%s'"%ad_status, "")

        if and_ad_match:
            ad_status=and_ad_match.groups()[0]
            new_sql = sql.replace("and auto_drive='%s'"%ad_status, "")

        return new_sql, ad_status

    def query(self, sql, time_offset=0, start=None, end=None):
        table = get_table_from_sql(sql)
        cols = get_select_cols(sql)
        #sql, ad_mode = self.get_ad_status(sql)

        #logger.info('ad sql:%s ad_mode:%s' %(sql, ad_mode))
        #ad_flag = 0
        #if ad_mode == "auto":
        #    ad_flag = 1

        if table != "perf_e2e":
            if table == 'trip_detail':
                return self.query_trip_detail(sql, start, end)
            #if table == 'trip_events':
            #    return self.query_trip_auto_drive_info(sql, start, end)
            if table == 'version':
                return self.query_version(sql, start, end)

            if table == 'trip_events':
                return self.query_trip_auto_drive_info(sql, -1, -1)

            if table == 'events_slice':
                sql = self.sql_add_timerange(sql, start, end)
                return self.query_cpu_core_info(sql, start, end, time_offset, ad_flag=0, fill_all_trip=False)

            if table in normal_table:
                return self.query_normal_table(sql)

            if table.find('report') != -1:
                logger.info('sql:%s cols:%s' %(sql, cols))
                if cols[0] == 'start_day' and cols[1] == 'end_day':
                    return self.query_report_trend(sql, start, end, time_offset)
                return self.query_report(sql, start, end, time_offset)

            if "huizong" in cols:
                return self.hz(sql)

            if cols[0] == 'timestamp':
                return self.query_cpu_core_info(sql, start, end, time_offset)
            elif cols[0] == 'start_time' and cols[1] == 'end_time':
                return self.query_start_end_table(sql, start, end, time_offset)
            else:
                return self.query_table(sql, start, end, time_offset)

        sql = self.sql_add_timerange(sql, start, end)
        logger.info('timerange sql:%s' % sql)
        datas = defaultdict(list)
        is_total = False
        if "total" in cols:
            is_total = True
            sql = sql.replace("total,", "")

        cursor = self._conn.cursor()
        cursor.execute(sql)
        items = cursor.fetchall()
        items = sorted(items, key=lambda x: x[0])

        for item in items:
            ts = item[0]
            timestamp = ts.timestamp()
            total = 0
            for i, val in enumerate(item[1:], 1):
                if val is None:
                    logger.info('val is None %s' % val)
                    continue

                if is_total:
                    total += val
                else:
                    datas[cols[i]].append([round(timestamp,2), str(val)])

            if is_total:
                datas["total"].append([round(timestamp,2), str(total)])

        return datas

    # print (random.uniform(10, 20))

    # 查看datas中的数据数目
    # for i in range(len(datas)):
    #    print ("datas_nums:", i, cols[i+1], len(datas[cols[i+1]]))

        #size = len(cols)          # 计算一维列表的长度
        #num = 1                   # 滑动窗口当前里面的数据数目
        #sum = list(range(size))   # 滑动窗口当前数据的总和
        #avg = list(range(size))   # 滑动窗口当前数据的的平均和
        #is_first = True           # 是否是第一次开启滑动窗口
#
#        for item in items:
#            ts = item[0]
#            timestamp = ts.timestamp() + time_offset
#            total = 0
#            print(item[1:])
#            # 如果是第一次开启滑动窗口，应该将数据全部加入datas中
#            if is_first:
#                is_first = False
#                for i, val in enumerate(item[1:], 1):
#                    if val is None or val > 600:
#                        continue
#                    datas[cols[i]].append([round(timestamp, 2), str(val)])
#                    num = 1
#                    avg[i] = val
#                    sum[i] = val
#
#                    # if is_total:
#                    #    total += val
#
#                # if is_total:
#                #    datas["total"].append([round(timestamp, 2), str(total)])
#                continue
#
#            # 如果不是第一次开启滑动窗口，应该考虑目前的数值是否超出滑动窗口中的数据平均值（阈值设置的50）
#            is_join = False
#            num += 1
#            for i, val in enumerate(item[1:], 1):
#                if is_join:
#                    break
#
#                val_n = 0
#                if val is None:
#                    val_n = 0
#
#                if (val_n - avg[i]) <= 50:
#                    if num % 5 == 0:
#                        is_join = True
#
#                    sum[i] += val_n
#                    avg[i] = sum[i] / num
#                else:
#                    is_join = True
#
            # is_join 为true 则应该加入datas中
#            if is_join:
#                for i, val in enumerate(item[1:], 1):
#                    val_n = 0
#                    if val is None or val > 600:
#                        continue
#                    datas[cols[i]].append([round(timestamp, 2), str(val)])

                    # if is_total:
#                    #    total += val
#                is_first = True
                # if is_total:
                #    datas["total"].append([round(timestamp, 2), str(total)])

    def get_con_in_where(self, sql, w_re, w_and_re):
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

    def get_version_in_where(self, sql):
        version = None
        a_version_r = w_and_version_re.search(sql)
        version_r = w_version_re.search(sql)
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

    def get_one_trip_datas(self, datas, trip, sql, timerange):
        sql = self.sql_add_trip_ad_timerange(sql, trip, timerange)
        logger.info('get_one_trip_datas %s' % sql)

        cursor = self._conn.cursor()
        cursor.execute(sql)
        items = cursor.fetchall()
        items = sorted(items, key=lambda x: x[0])

        timestamp = datetime.datetime.now().timestamp()
        for item in items:
            value = str(item[-1])
            if value in str_value_map:
                value = str_value_map[value]

            key = str(item[0])
            for v in item[1:-1]:
                key = key + ":" + str(v)
            datas[key].append([round(timestamp, 2), value])

    def filter_trip_by_start_end(self, trip, start, end):
        start_dt = datetime.datetime.fromtimestamp(
            start + PROMETHEUS_TIME_OFFSET)
        end_dt = datetime.datetime.fromtimestamp(end + PROMETHEUS_TIME_OFFSET)
        start_tp = '%s-%02d-%02d-%02d-%02d' % (start_dt.year,
                                               start_dt.month,
                                               start_dt.day,
                                               start_dt.hour,
                                               start_dt.minute)
        end_tp = '%s-%02d-%02d-%02d-%02d' % (end_dt.year,
                                             end_dt.month,
                                             end_dt.day,
                                             end_dt.hour,
                                             end_dt.minute)
        #logger.info('trip:%s start_tp :%s end_tp:%s %s' % (trip, start_tp, end_tp, start_tp < trip and trip < end_tp))
        return start_tp < trip and trip < end_tp

    def query_normal_table(self, sql, start=-1, end=-1, time_offset=0):
        datas = defaultdict(list)
        cursor = self._conn.cursor()
        cursor.execute(sql)
        items = cursor.fetchall()
        items = sorted(items, key=lambda x: x[0])

        timestamp = datetime.datetime.now().timestamp()
        for item in items:
            value = str(item[-1])
            if value in str_value_map:
                value = str_value_map[value]

            key = str(item[0])
            for v in item[1:-1]:
                key = key + ":" + str(v)
            datas[key].append([round(timestamp, 2), value])

        return datas

    def query_table(self, sql, start=-1, end=-1, time_offset=0):
        datas = defaultdict(list)
        old_sql = sql
        begintime = time.time()
        logger.info(
            'query_table sql: [%s] start-end:%s-%s begin:%s' %
            (old_sql, start, end, begintime))

        version, sql = self.get_con_in_where(
            sql, w_version_re, w_and_version_re)
        if version:
            all_trips = self.get_all_trips_by_version(version, start, end)
            logger.info(
                'version [%s] have [%d] trips !!!' %
                (version, len(all_trips)))

            if not all_trips:
                logger.warning('version [%s] have no trips !!!' % version)
                return datas

            ad, sql = self.get_con_in_where(sql, w_ad_re, w_and_ad_re)
            i = 0
            for trip in all_trips:
                ad_timerange = self.get_trip_ad_time_ranges(trip)
                if not ad_timerange:
                    #logger.warning('trip [%s] have no ad time' % trip)
                    continue

                i += 1
                self.get_one_trip_datas(datas, trip, sql, ad_timerange)

            endtime = time.time()
            logger.info(
                'query_table sql: [%s] trips:[%d] end:%ds' %
                (old_sql, i, endtime - begintime))
            return datas

        sql = self.sql_add_timerange(sql, start, end)
        cursor = self._conn.cursor()
        cursor.execute(sql)
        items = cursor.fetchall()
        items = sorted(items, key=lambda x: x[0])

        timestamp = datetime.datetime.now().timestamp()
        for item in items:
            value = str(item[-1])
            if value in str_value_map:
                value = str_value_map[value]

            key = str(item[0])
            for v in item[1:-1]:
                key = key + ":" + str(v)
            datas[key].append([round(timestamp, 2), value])

        # print(datas)
        endtime = time.time()
        logger.info(
            'query_table sql: [%s] end cost:[%d]s' %
            (old_sql, endtime - begintime))
        return datas

    def sql_add_timerange_trip(self, sql, start, end, time_offset):
        start_day, end_day = self.query_timerange_to_day(start, end, time_offset, end_offset=1)

        add_sql = ""
        if "where" in sql:
            add_sql = " and ( trip_id >= '%s' and trip_id <= '%s' )" % (start_day, end_day)

        else:
            add_sql = " where ( trip_id >= '%s' and trip_id <= '%s' )" % (start_day, end_day)

        return sql + add_sql

    def sql_add_day_trend(self, sql, start, end, time_offset):
        start_day, end_day = self.query_timerange_to_day(start, end, time_offset)

        add_sql = ""
        if "where" in sql:
            add_sql = " and ( start_day >= '%s' and end_day <= '%s' and start_day=end_day and start_day!='-1') order by start_day asc" % (start_day, end_day)

        else:
            add_sql = " where ( start_day >= '%s' and end_day <= '%s' and start_day=end_day and start_day!='-1') order by start_day asc" % (start_day, end_day)

        return sql + add_sql

    def sql_add_timerange_day(self, sql, start, end, time_offset):
        start_day, end_day = self.query_timerange_to_day(start, end, time_offset)

        add_sql = ""
        if "where" in sql:
            add_sql = " and ( start_day >= '%s' and end_day <= '%s' ) order by start_day asc, end_day desc" % (start_day, end_day)

        else:
            add_sql = " where ( start_day = '%s' and end_day = '%s' ) order by start_day asc , end_day desc" % (start_day, end_day)

        return sql + add_sql

    def query_timerange_to_day_offset(self, start, end, time_offset, offset=1):
        start_dt = datetime.datetime.fromtimestamp(start - time_offset) + datetime.timedelta(days=-offset)
        end_dt = datetime.datetime.fromtimestamp(end - time_offset) + datetime.timedelta(days=offset)
        start_day = '%s-%02d-%02d' % (start_dt.year, start_dt.month, start_dt.day)
        end_day = '%s-%02d-%02d' % (end_dt.year, end_dt.month, end_dt.day)
        return (start_day, end_day)

    def query_timerange_to_day(self, start, end, time_offset, end_offset=0):
        start_dt = datetime.datetime.fromtimestamp(start - time_offset)
        end_dt = datetime.datetime.fromtimestamp(end - time_offset) + datetime.timedelta(days=end_offset)
        start_day = '%s-%02d-%02d' % (start_dt.year, start_dt.month, start_dt.day)
        end_day = '%s-%02d-%02d' % (end_dt.year, end_dt.month, end_dt.day)
        return (start_day, end_day)

    def one_day_timestamp(self, day_str, offset):
        year, month, day = day_str.split('-')
        timestamps = []
        for i in range(1):
#            for j in range(3):
            dt = datetime.datetime(year=int(year), month=int(month), day=int(day)+offset, hour=i)
            timestamps.append(dt.timestamp())

        return timestamps

    def day_to_timestamp(self, day_str):
        year, month, day = day_str.split('-')
        timestamps = []
        for i in range(24):
            for j in range(3):
                dt = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=i, minute=j*20)
                timestamps.append(dt.timestamp())
        return timestamps

    def query_notimestamp_withday(self, sql, timeoffset):
        datas = defaultdict(list)
        cursor = self._conn.cursor()
        cursor.execute(sql)

        items = cursor.fetchall()
        head_day, end_day = None, None
        first = True
        for item in items:
            value = str(item[-1])
            start_day = item[0]
            end_day = item[1]


            key = str(item[2])
            for v in item[3:-1]:
                key = key + ":" + str(v)

            if first:
                head_day = start_day
                first = False

            for ts in self.day_to_timestamp(start_day):
                timestamp = ts + timeoffset
                value_with_time = [round(timestamp, 2), value]
                datas[key].append(value_with_time)

        for key, values in datas.items():
            for ts in self.one_day_timestamp(end_day, 1):
                timestamp = ts + timeoffset
                value_with_time = [round(timestamp, 2), 0]
                datas[key].append(value_with_time)

        #logger.info(str(datas))
        return datas

    def query_notimestamp(self, sql, unique_flag=False):
        datas = defaultdict(list)
        cursor = self._conn.cursor()
        cursor.execute(sql)

        items = cursor.fetchall()
        timestamp = datetime.datetime.now().timestamp()
        for item in items:
            value = str(item[-1])
            if value in str_value_map:
                value = str_value_map[value]

            key = str(item[0])
            for v in item[1:-1]:
                key = key + ":" + str(v)

            value_with_time = [round(timestamp, 2), value]
            if unique_flag and  value_with_time in datas[key]:
                continue

            datas[key].append(value_with_time)

        # print(datas)
        return datas

    def query_with_trip_timestamp(self, sql, start=-1, end=-1, time_offset=0):
        new_sql = self.sql_add_timerange_trip(sql, start, end, time_offset)
        logger.info('query_trip_timestamp new_sql:%s' % new_sql)
        return self.query_notimestamp(new_sql)

    def query_report_trend(self, sql, start=-1, end=-1, time_offset=0):
        new_sql = self.sql_add_day_trend(sql, start, end, time_offset)
        logger.info('query_report_trend new_sql:%s' % new_sql)

        return self.query_notimestamp_withday(new_sql, time_offset)

    def query_report(self, sql, start=-1, end=-1, time_offset=0):
        new_sql = self.sql_add_timerange_day(sql, start, end, time_offset)
        logger.info('query_report new_sql:%s' % new_sql)

        return self.query_notimestamp(new_sql, unique_flag=True)

    def get_trip_id_from_sql(self, sql):
        result = w_trip_re.search(sql)
        if result is None:
            return

        return result.groups()[0]

    def start_end_to_timestamps(self, start, end):
        dt_start = start.timestamp()
        dt_end = end.timestamp()
        timestamps = []
        for t in range(int(dt_start), int(dt_end)):
            timestamps.append(t)
        return timestamps

    def query_start_end_table(self, sql, start=-1, end=-1, time_offset=0):
        datas = defaultdict(list)
        sql = self.sql_add_timerange_trip(sql, start, end, time_offset)
        sql += " order by start_time asc"

        cursor = self._conn.cursor()
        cursor.execute(sql)
        items = cursor.fetchall()
        for item in items:
            start_ts = item[0]
            end_ts = item[1]
            value = str(item[-1])

            key = str(item[2])
            for v in item[3:-1]:
                key = key + ":" + str(v)

            for ts in self.start_end_to_timestamps(start_ts, end_ts):
                timestamp = ts + time_offset
                datas[key].append([round(timestamp, 2), value])

        #for k, v in datas.items():
        #    logger.info('start_end key:%s v:%s'%(k, v))
        return datas

    def query_cpu_core_info(self, sql, start=-1, end=-1, time_offset=0, ad_flag=0, fill_all_trip=False):
        datas = defaultdict(list)
#        sql = self.sql_add_timerange(sql, start, end)

        if ad_flag:
            logger.info('ad before sql:%s'%sql)
            sql = self.sql_add_ad(sql)
            logger.info('ad sql:%s'%sql)

        trip_id = self.get_trip_id_from_sql(sql)
#        start_ts, end_ts = self.sql_get_trip_start_end_ts(trip_id)

#        sql="select timestamp,name,pid,cpu_total from node_info where trip_id='2024-04-19-15-58-36' and hostname='orin_0' and name!='cargo_monitor_n' and cpu_total > 5 "
        logger.info('sql exec :%s' % sql)
        cursor = self._conn.cursor()
        cursor.execute(sql)
        items = cursor.fetchall()
        items = sorted(items, key=lambda x: x[0])
        last_timestamp = -1
        print("items:%d" % len(items))
        for item in items:
            ts = int(int(item[0]) / 1000000000)
            timestamp = ts
            value = str(item[-1])
            if value in str_value_map:
                value = str_value_map[value]

            key = str(item[1])
            for v in item[2:-1]:
                key = key + ":" + str(v)
            datas[key].append([round(timestamp, 2), value])

#        end_ts = end_ts / 1000 - time_offset
#        logger.info('last_timestamp:%s end_ts:%s' % (last_timestamp, end_ts))

#        if last_timestamp != -1 and fill_all_trip:
#            while last_timestamp + 100 < end_ts:
#                last_timestamp += 100
#                for k, v in datas.items():
#                    datas[k].append([round(last_timestamp + time_offset, 2), 0])

        print("datas")
        for k, v in datas.items():
            logger.info('key:%s nums:%d'%(k, len(v)))
        return datas

    def query_trip_detail(self, sql, start=None, end=None):
        datas = defaultdict(list)

        cursor = self._conn.cursor()
        cursor.execute(sql)
        items = cursor.fetchall()
        items = sorted(items, key=lambda x: x[0])
        for item in items:
            datas[item[0]].append([end, str(item[1])])

#        print("trip_details:", datas)
        return datas

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()


if __name__ == "__main__":
    db = DBOper("")

    sql = "select sensor_name, status, count(*) from sensor_status_info where status != 1 group by sensor_name, status and version=release2023"
    print(db.get_version_in_where(sql))

    sql = "select sensor_name, status, count(*) from sensor_status_info where status != 1 group by sensor_name, status and version=dev "
    print(db.get_version_in_where(sql))
