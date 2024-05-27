/*
 * Copyright 2022 Nightingale Team
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
/* eslint-disable react/require-default-props */
/* eslint-disable no-plusplus */
/* eslint-disable no-use-before-define */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Table, Input, Button, Modal, Tooltip } from 'antd';
import Color from 'color';
import _ from 'lodash';
import { SeriesType } from '../util/normalizeSeries';
import { replaceExpressionBracket } from '../util';
interface LegendProps {
  series: any;
  style: object;
  onSelectedChange: Function;
  rowSelection?: object;
  renderValue?: Function;
  comparisonOptions: any;
  graphConfig: any;
  columnsKey?: any;
}

interface LegendState {
  searchText: string;
  filterVal: string;
  filterDropdownVisible: boolean;
  contextMenuVisiable: boolean;
  contextMenuTop: number;
  contextMenuLeft: number;
  selectedKeys: string;
  highlightedKeys: string[];
  currentCounter?: number;
}

class Legend extends Component<LegendProps, LegendState> {
  constructor(props: LegendProps) {
    super(props);
    this.state = {
      searchText: '',
      filterVal: '',
      filterDropdownVisible: false,
      contextMenuVisiable: false,
      contextMenuTop: 0,
      contextMenuLeft: 0,
      selectedKeys: 'normal', // 默认全选, 已选的 keys
      highlightedKeys: [], // 高亮的 keys
    };
  }

  componentWillReceiveProps(nextProps) {
    const isEqualSeriesResult = isEqualSeries(this.props.series, nextProps.series);
    if (!isEqualSeriesResult) {
      this.setState({
        selectedKeys: 'normal',
        highlightedKeys: [],
      });
    }
  }

  handleInputChange = (e) => {
    this.setState({ searchText: e.target.value });
  };

  handleSearch = () => {
    const { searchText } = this.state;
    this.setState({
      filterDropdownVisible: false,
      filterVal: searchText,
    });
  };

  handleContextMenu = (e, counter) => {
    e.preventDefault();
    this.setState({
      currentCounter: counter,
      contextMenuVisiable: true,
      contextMenuLeft: e.clientX,
      contextMenuTop: e.clientY,
    });
  };

  handleClickCounter = (record) => {
    const { selectedKeys, highlightedKeys } = this.state;
    const highlightedKeysClone = _.clone(highlightedKeys);

    if (_.includes(highlightedKeysClone, record.id)) {
      _.remove(highlightedKeysClone, (o) => o === record.id);
    } else {
      highlightedKeysClone.push(record.id);
    }

    this.setState({ highlightedKeys: highlightedKeysClone }, () => {
      this.props.onSelectedChange(selectedKeys, highlightedKeysClone);
    });
  };

  filterData() {
    const { series } = this.props;
    const { filterVal } = this.state;
    const reg = new RegExp(filterVal, 'gi');
    const legendData = normalizeLegendData(series);
    return _.filter(legendData, (record) => {
      return (record.tags && record.tags.match(reg)) || (record.metricLabels && JSON.stringify(record.metricLabels).match(reg));
    });
  }

  render() {
    const { comparisonOptions, onSelectedChange, rowSelection, renderValue = (v) => v } = this.props;
    const { graphConfig } = this.props;

    if (!graphConfig) return null;

    const sortOrder = _.cloneDeep(_.get(graphConfig, 'sortOrder', {}));
    const { searchText, selectedKeys, highlightedKeys } = this.state;
    const counterSelectedKeys = highlightedKeys;
    const data = this.filterData();
    const firstData = data[0];
    let columns: any[] = [
      {
        title: <span> Series({data.length}) </span>,
        dataIndex: 'tags',
        width: 240,
        filterDropdown: (
          <div className='custom-filter-dropdown'>
            <Input placeholder='Input serie name' value={searchText} onChange={this.handleInputChange} onPressEnter={this.handleSearch} />
            <Button type='primary' onClick={this.handleSearch}>
              Search
            </Button>
          </div>
        ),
        ellipsis: true,
        filterDropdownVisible: this.state.filterDropdownVisible,
        onFilterDropdownVisibleChange: (visible) => this.setState({ filterDropdownVisible: visible }),
        render: (text, record) => {
          const { legendName, titleName } = getLengendName(record, comparisonOptions);
          return (
            <Tooltip title={titleName} getPopupContainer={() => document.body}>
              <span
                onClick={() => this.handleClickCounter(record)}
                onContextMenu={(e) => this.handleContextMenu(e, text)}
                style={{
                  cursor: 'pointer',
                  // eslint-disable-next-line no-nested-ternary
                  opacity: counterSelectedKeys.length ? (_.includes(counterSelectedKeys, record.id) ? 1 : 0.5) : 1,
                }}
              >
                <span style={{ color: record.color }}>● </span>
                {legendName}
              </span>
            </Tooltip>
          );
        },
      },
      {
        title: 'P50',
        dataIndex: 'p50',
        className: 'alignRight',
        width: 120,
        defaultSortOrder: sortOrder.columnKey === 'p50' ? sortOrder.order : undefined,
        render(text) {
          return <span style={{ paddingRight: 10 }}>{text !== null ? renderValue(text) : 'null'}</span>;
        },
        sorter: (a, b) => a.p50 - b.p50,
      },
      {
        title: 'P90',
        dataIndex: 'p90',
        className: 'alignRight',
        width: 120,
        defaultSortOrder: sortOrder.columnKey === 'p90' ? sortOrder.order : undefined,
        render(text) {
          return <span style={{ paddingRight: 10 }}>{text !== null ? renderValue(text) : 'null'}</span>;
        },
        sorter: (a, b) => a.p90 - b.p90,
      },
      {
        title: 'P99',
        dataIndex: 'p99',
        className: 'alignRight',
        width: 120,
        defaultSortOrder: sortOrder.columnKey === 'p99' ? sortOrder.order : undefined,
        render(text) {
          return <span style={{ paddingRight: 10 }}>{text !== null ? renderValue(text) : 'null'}</span>;
        },
        sorter: (a, b) => a.p99 - b.p99,
      },
      {
        title: 'P9999',
        dataIndex: 'p9999',
        className: 'alignRight',
        width: 120,
        defaultSortOrder: sortOrder.columnKey === 'p9999' ? sortOrder.order : undefined,
        render(text) {
          return <span style={{ paddingRight: 10 }}>{text !== null ? renderValue(text) : 'null'}</span>;
        },
        sorter: (a, b) => a.p9999 - b.p9999,
      },
      {
        title: 'Counts',
        dataIndex: 'num',
        className: 'alignRight',
        width: 120,
        defaultSortOrder: sortOrder.columnKey === 'num' ? sortOrder.order : undefined,
        render(text) {
          return <span style={{ paddingRight: 10 }}>{text !== null ? renderValue(text) : 'null'}</span>;
        },
        sorter: (a, b) => a.num - b.num,
      },
      {
        title: 'Avg',
        dataIndex: 'avg',
        className: 'alignRight',
        width: 120,
        defaultSortOrder: sortOrder.columnKey === 'avg' ? sortOrder.order : undefined,
        render(text) {
          return <span style={{ paddingRight: 10 }}>{text !== null ? renderValue(text) : 'null'}</span>;
        },
        sorter: (a, b) => a.avg - b.avg,
      },
      {
        title: 'Max',
        dataIndex: 'max',
        className: 'alignRight',
        width: 120,
        defaultSortOrder: sortOrder.columnKey === 'max' ? sortOrder.order : undefined,
        render(text) {
          return <span style={{ paddingRight: 10 }}>{text !== null ? renderValue(text) : 'null'}</span>;
        },
        sorter: (a, b) => a.max - b.max,
      },
      {
        title: 'Min',
        dataIndex: 'min',
        className: 'alignRight',
        width: 120,
        defaultSortOrder: sortOrder.columnKey === 'min' ? sortOrder.order : undefined,
        render(text) {
          return <span style={{ paddingRight: 10 }}>{text !== null ? renderValue(text) : 'null'}</span>;
        },
        sorter: (a, b) => a.min - b.min,
      },
    ];
    const newRowSelection = {
      selectedRowKeys: selectedKeys === 'normal' ? _.map(data, (o) => o.id) : selectedKeys,
      onChange: (selectedRowKeys) => {
        this.setState({ selectedKeys: selectedRowKeys }, () => {
          onSelectedChange(selectedRowKeys, highlightedKeys);
        });
      },
    };

    if (_.get(firstData, 'isSameMetric') === false) {
      columns.unshift({
        title: '指标',
        dataIndex: 'metric',
        width: 60,
      });
    }

    let scrollX = 650;

    if (this.props.columnsKey) {
      columns = _.filter(columns, (column) => {
        return _.includes([...this.props.columnsKey, 'metric', 'tags'], column.dataIndex);
      });
      scrollX = 150 + this.props.columnsKey.length * 100;
    }

    return (
      <div
        className='graph-legend'
        style={{
          ...this.props.style,
          height: '100%',
        }}
      >
        <Table
          className='auto-scroll-y'
          rowKey={({ id, comparison }) => `${id}${comparison}`}
          size='middle'
          // @ts-ignore
          rowSelection={false}
          columns={columns}
          dataSource={data}
          pagination={false}
          // @ts-ignore
          scroll={{ x: scrollX, y: true }}
          showSorterTooltip={false}
        />
      </div>
    );
  }
}

export default Legend;

export function normalizeLegendData(series: SeriesType[] = []) {
  const tableData = _.map(series, (serie) => {
    const { id, metric, tags, data, comparison, metricLabels, legendTitleFormat } = serie;
    const { last, avg, max, min, sum, p50, p90, p99, p9999, len } = getLegendNums(data);
    return {
      id,
      metric,
      tags,
      comparison,
      metricLabels,
      last: _.isNumber(last) ? last.toFixed(3) : null,
      avg: _.isNumber(avg) ? avg.toFixed(3) : null,
      max: _.isNumber(max) ? max.toFixed(3) : null,
      min: _.isNumber(min) ? min.toFixed(3) : null,
      sum: _.isNumber(sum) ? sum.toFixed(3) : null,
      p50: _.isNumber(p50) ? p50.toFixed(3) : null,
      p90: _.isNumber(p90) ? p90.toFixed(3) : null,
      p99: _.isNumber(p99) ? p99.toFixed(3) : null,
      p9999: _.isNumber(p9999) ? p9999 : null,
      num: _.isNumber(len) ? len : null,
      color: serie.color,
      legendTitleFormat,
    };
  });
  return _.orderBy(tableData, 'counter');
}

export function getSerieVisible(serie, selectedKeys) {
  return selectedKeys === 'normal' ? true : _.includes(selectedKeys, _.get(serie, 'id'));
}

export function getSerieColor(serie, highlightedKeys, oldColor) {
  if (highlightedKeys.length && !_.includes(highlightedKeys, _.get(serie, 'id'))) {
    return Color(oldColor).lighten(0.5).desaturate(0.7).hex();
  }
  return oldColor;
}

export function getSerieIndex(serie, highlightedKeys, seriesLength, serieIndex) {
  return _.includes(highlightedKeys, _.get(serie, 'id')) ? seriesLength + serieIndex : serieIndex;
}

/**
 * 获取 legend 的 max min avg sum last
 * @param  {Array}  points 所有点列表
 * @param  {Number} smin   缩放后的最小值
 * @param  {Number} smax   缩放后的最大值
 * @return {Object}        {max,min,avg,sum,last}
 */
function getLegendNums(points) {
  let last = 0;
  let avg = 0;
  let max = -Infinity;
  let min = Infinity;
  let sum = 0;
  let p50 = 0;
  let p90 = 0;
  let p99 = 0;
  let p9999 = 0;
  let len = 0;

  if (!_.isArray(points)) {
    return { last, avg, max, min, sum, p50, p90, p99, p9999 };
  }

  let sorted_points = _.sortBy(points, (item) => _.toNumber(item[1]));
  const p50_index = _.toInteger(sorted_points.length * 0.50);
  const p90_index = _.toInteger(sorted_points.length * 0.90);
  const p99_index = _.toInteger(sorted_points.length * 0.99);
  var p9999_index = _.toInteger(sorted_points.length * 0.9999);
  if (p9999_index > sorted_points.length) {
    p9999_index = sorted_points.length - 1;
  }
  p50 = _.toNumber(sorted_points[p50_index][1]);
  p90 = _.toNumber(sorted_points[p90_index][1]);
  p99 = _.toNumber(sorted_points[p99_index][1]);
  p9999 = _.toNumber(sorted_points[p9999_index][1]);
  
  _.each(points, (point) => {
    const x = _.get(point, '[0]');
    const y = _.get(point, '[1]');
    if (_.isNumber(x) && _.isNumber(y)) {
      sum += y;

      if (max < y) {
        max = y;
      }

      if (min > y) {
        min = y;
      }

      last = y;
      len++;
    }
  });

  if (_.isNumber(sum)) {
    avg = sum / len;
  }

  return { last, avg, max, min, sum, p50, p90, p99, p9999, len};
}

/**
 * getLengendName
 * @param  {Object}  serie             [description]
 * @return {String}                   [description]
 */
function getLengendName(serie, comparisonOptions, locale = 'zh') {
  const { comparison, legendTitleFormat } = serie;
  let legendName = '',
    titleName;

  const serieMetricLabels = serie?.metricLabels || {};
  const metricName = serieMetricLabels.__name__;
  const labels = Object.keys(serieMetricLabels)
    .filter((ml) => ml !== '__name__')
    .map((label) => `${label}=${serieMetricLabels[label]}`);

  // display comparison
  // if (comparison && typeof comparison === 'number') {
  //   const currentComparison = _.find(comparisonOptions, { value: `${comparison}000` });
  //   if (currentComparison && currentComparison.label) {
  //     const enText = _.get(_.find(comparisonOptions, { value: String(Number(comparison) * 1000) }), 'labelEn');
  //     comparisonTxt = locale === 'zh' ? `环比${currentComparison.label}` : `(${enText} ago)`;
  //   }
  // }
  if (legendTitleFormat) {
    legendName = replaceExpressionBracket(legendTitleFormat, serieMetricLabels);
  } else {
    legendName = `${metricName || ''} ${comparison ? `offset ${comparison}` : ''} {${labels}}`;
  }
  titleName = (
    <div>
      <div>
        {metricName} {comparison ? `offset ${comparison}` : ''}
      </div>
      {labels.map((label, index) => (
        <div key={index}>{label}</div>
      ))}
    </div>
  );

  return { legendName, titleName };
}

export function isEqualSeries(series, nextSeries) {
  const pureSeries = _.map(series, (serie) => {
    return serie.id;
  });
  const pureNextSeries = _.map(nextSeries, (serie) => {
    return serie.id;
  });
  return _.isEqual(pureSeries, pureNextSeries);
}
