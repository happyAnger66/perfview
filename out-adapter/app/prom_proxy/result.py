# Copyright (C) @2022 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com

class Result:
    def __init__(self ):
        self._result = []

    def add_metric(self, metric):
        self._result.append(metric.result())

    def data(self):
        data = {"status": "success",
                      "data": {
                          "resultType": "matrix",
                          "result": self._result
                      }}
        return data

class Metric:
    def __init__(self, name, labels):
        self._name = name
        self._labels = labels
        self._metric = {}
        self._values = []

    def set_values(self, values):
        self._values = values

    def add_value(self, ts, val):
        self._values.append([ts, val])

    def result(self):
        labels = {"__name__": self._name}
        labels.update(self._labels)
        self._result = {"metric": labels,
                        "values": self._values}
        return self._result