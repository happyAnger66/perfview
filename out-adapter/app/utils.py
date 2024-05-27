# Copyright (C) @2023 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com
import logging

def log_init(logfile):
    fmt = '[%(asctime)s] %(filename)s:%(lineno)d %(threadName)s %(message)s'
    logging.basicConfig(
        filename=logfile,
        level=logging.INFO,
        format=fmt)
    logging.StreamHandler(stream=None)