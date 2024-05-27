# Copyright (C) @2024 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com

configs_table_create_sql = """
CREATE TABLE configs (
    id bigint primary key,
    ckey TEXT NOT NULL,
    cval TEXT NOT NULL
);
"""

users_table_create_sql = """
CREATE TABLE users (
    id bigint primary key,
    username TEXT,
    nickname TEXT,
    password TEXT,
    phone TEXT,
    email TEXT,
    portrait TEXT,
    roles TEXT,
    contacts TEXT,
    maintainer SMALLINT,
    create_at BIGINT,
    create_by TEXT,
    update_at BIGINT,
    update_by TEXT
);
"""

busi_group_table_create_sql = """
CREATE TABLE busi_group (
    id bigint primary key,
    name TEXT,
    label_enable SMALLINT,
    label_value TEXT,
    create_at BIGINT,
    create_by TEXT,
    update_at BIGINT,
    update_by TEXT
);
"""

board_table_create_sql = """
CREATE TABLE board (
    id INTEGER primary key AUTOINCREMENT,
    group_id bigint,
    name TEXT,
    ident TEXT,
    tags TEXT,
    create_at BIGINT,
    create_by TEXT,
    update_at BIGINT,
    update_by TEXT,
    public bigint
);
"""

board_payload_table_create_sql="""
CREATE TABLE board_payload (
    id INTEGER primary key AUTOINCREMENT,
    payload TEXT
);
"""

cpu_board='{"var":[{"definition":"label_values(trip)","name":"trip"},{"definition":"label_values(hostname)","name":"hostname"}],"panels":[{"targets":[{"refId":"A","expr":' +  \
'"select timestamp,name,pid,cpu_total from node_info where trip_id=' + "''$trip''" + " and hostname=''$hostname''" + " and name!=''cargo_monitor_n'' and cpu_total > 5" + '"' + \
   ',"legend":"{{ident}}"}],"name":"cpu","options":{"tooltip":{"mode":"all","sort":"desc"},"legend":{"displayMode":"list"},"standardOptions":{},"thresholds":{}},"custom":{"drawStyle":"lines","lineInterpolation":"smooth","fillOpacity":0.5,"stack":"off"},"version":"2.0.0","type":"timeseries","layout":{"h":20,"w":24,"x":0,"y":0,"i":"11b59086-6491-43e6-a96d-dd161b144af9","isResizable":true},"id":"11b59086-6491-43e6-a96d-dd161b144af9"}],"version":"2.0.0"}'

import sqlite3

def board_init(db, cur):
    try:
        cur.execute("insert into board VALUES (1, 1, 'node cpu info all', \
                    1, NULL, \
                    1678340861, 'root', 1678340861, 'root', 0)")
        db.commit()
    except Exception as e:
        print('boards datas init failed:%s' % e)

    try:
        cur.execute("insert into board VALUES (2, 1, 'report cpu', \
                    1, NULL, \
                    1678340861, 'root', 1678340861, 'root', 0)")
        db.commit()
    except Exception as e:
        print('boards datas init failed:%s' % e)

if __name__ == "__main__":
    db = sqlite3.connect('/tmp/admin_db.sqlite3')
    cur = db.cursor()

    try:
        cur.execute(configs_table_create_sql)
        db.commit()
    except Exception as e:
        print('configs table create failed:%s' % e)

    try:
        cur.execute(users_table_create_sql)
        db.commit()
    except Exception as e:
        print('users table create failed:%s' % e)

    try:
        cur.execute(busi_group_table_create_sql)
        db.commit()
    except Exception as e:
        print('busi_group table create failed:%s' % e)

    try:
        cur.execute(board_table_create_sql)
        db.commit()
    except Exception as e:
        print('board table create failed:%s' % e)

    try:
        cur.execute(board_payload_table_create_sql)
        db.commit()
    except Exception as e:
        print('board_payload table create failed:%s' % e)

    try:
        cur.execute("insert into configs VALUES (1, 'salt', '83a9f75eb87cff57394fbbe25a664c06')")
        db.commit()
    except Exception as e:
        print('configs datas init failed:%s' % e)

    try:
        cur.execute("insert into users VALUES (1, 'root', 'xiaoan', '123456', \
                    '', '', '', 'Admin', NULL, 0, \
                    1678340861, 'system', 1678340861, 'system')")
        db.commit()
    except Exception as e:
        print('users datas init failed:%s' % e)

    try:
        cur.execute("insert into busi_group VALUES (1, 'perf', 0, \
                    NULL, \
                    1678340861, 'root', 1678340861, 'root')")
        db.commit()
    except Exception as e:
        print('busi_group datas init failed:%s' % e)


    board_init(db, cur)

    try:
        cur.execute(f"insert into board_payload VALUES (1, '{cpu_board}')")
        db.commit()
    except Exception as e:
        print('board_payload init failed:%s' % e)
