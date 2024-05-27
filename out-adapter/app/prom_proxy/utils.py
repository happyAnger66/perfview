# Copyright (C) @2023 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com

from collections import namedtuple

TripEvent = namedtuple('TripEvent', [
    'trip_id', 'event', 'ts', 'distance', 'gps_lat', 'gps_long', 'val'])