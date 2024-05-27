# Copyright (C) @2022 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com

from collections import namedtuple

METRICS = [
    "prom_proxy",
    "e2e_lidar_ipc", "e2e_lidar_sched", "e2e_lidar_proc",
    "e2e_topdown_ipc", "e2e_topdown_sched", "e2e_topdown_proc", "perf_e2e"
]

metrics_to_sql = namedtuple('metrics_to_sql', ['table_name', 'col_name', 'label_cols'])
