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
import _ from 'lodash';
import valueFormatter from './valueFormatter';
import { IValueMapping } from '../../types';

const getIndexValueAndToNumber = (value: any[], index: number) => {
  var p_index = _.toInteger(value.length * index);
  if (p_index > value.length) {
    p_index = value.length - 1;
  }

  if (p_index < 0) {
    p_index = 0;
  }
  return _.toNumber(value[p_index][1]);
};

const getValueAndToNumber = (value: any[]) => {
  return _.toNumber(_.get(value, 1, NaN));
};

export const getSerieTextObj = (value: number | string | null | undefined, standardOptions?: any, valueMappings?: IValueMapping[]) => {
  const { util, decimals } = standardOptions || {};
  const matchedValueMapping = _.find(valueMappings, (item) => {
    const { type, match } = item;
    if (value === null || value === '' || value === undefined) {
      if (type === 'specialValue') {
        if (match?.specialValue === 'empty') {
          return value === '';
        } else if (match?.specialValue === 'null') {
          return value === null || value === undefined;
        }
      }
      return false;
    } else {
      value = _.toNumber(value) as number;
      if (type === 'special') {
        return value === match?.special;
      } else if (type === 'range') {
        if (match?.from && match?.to) {
          return value >= match?.from && value <= match?.to;
        } else if (match?.from) {
          return value >= match?.from;
        } else if (match?.to) {
          return value <= match?.to;
        }
        return false;
      }
      return false;
    }
  });
  return {
    text: matchedValueMapping?.result?.text ? matchedValueMapping?.result?.text : valueFormatter({ util, decimals }, value),
    color: matchedValueMapping?.result?.color,
  };
};

const getCalculatedValuesBySeries = (series: any[], calc: string, { util, decimals }, valueMappings?: IValueMapping[]) => {
  const values = _.map(series, (serie) => {
    const results = {
      lastNotNull: () => _.get(_.last(_.filter(serie.data, (item) => item[1] !== null)), 1),
      last: () => _.get(_.last(serie.data), 1),
      firstNotNull: () => _.get(_.first(_.filter(serie.data, (item) => item[1] !== null)), 1),
      first: () => _.get(_.first(serie.data), 1),
      min: () => getValueAndToNumber(_.minBy(serie.data, (item) => _.toNumber(item[1]))),
      max: () => getValueAndToNumber(_.maxBy(serie.data, (item) => _.toNumber(item[1]))),
      avg: () => _.meanBy(serie.data, (item) => _.toNumber(item[1])),
      sum: () => _.sumBy(serie.data, (item) => _.toNumber(item[1])),
      count: () => _.size(serie.data),
    };
    const stat = results[calc] ? results[calc]() : NaN;
    return {
      id: serie.id,
      name: serie.name,
      metric: serie.metric,
      fields: {
        ...serie.metric,
        refId: serie.refId,
      },
      stat: _.toNumber(stat),
      ...getSerieTextObj(stat, { util, decimals }, valueMappings),
    };
  });
  return values;
};

export const getLegendValues = (series: any[], { util, decimals }, hexPalette: string[]) => {
  const values = _.map(series, (serie, idx) => {
    const results = {
      max: getValueAndToNumber(_.maxBy(serie.data, (item) => _.toNumber(item[1]))),
      min: getValueAndToNumber(_.minBy(serie.data, (item) => _.toNumber(item[1]))),
      avg: _.meanBy(serie.data, (item) => _.toNumber(item[1])),
      sum: _.sumBy(serie.data, (item) => _.toNumber(item[1])),
      last: getValueAndToNumber(_.last(serie.data)),
      p50: getIndexValueAndToNumber(_.sortBy(serie.data, (item) => _.toNumber(item[1])), 0.5),
      p90: getIndexValueAndToNumber(_.sortBy(serie.data, (item) => _.toNumber(item[1])), 0.9),
      p99: getIndexValueAndToNumber(_.sortBy(serie.data, (item) => _.toNumber(item[1])), 0.99),
      p9999: getIndexValueAndToNumber(_.sortBy(serie.data, (item) => _.toNumber(item[1])), 0.9999),
      num: serie.data.length
    };
    return {
      id: serie.id,
      name: serie.name,
      metric: serie.metric,
      offset: serie.offset,
      color: hexPalette[idx % hexPalette.length],
      disabled: serie.visible === false ? true : undefined,
      max: valueFormatter({ util, decimals }, results.max),
      min: valueFormatter({ util, decimals }, results.min),
      avg: valueFormatter({ util, decimals }, results.avg),
      sum: valueFormatter({ util, decimals }, results.sum),
      last: valueFormatter({ util, decimals }, results.last),
      p50: valueFormatter({ util, decimals }, results.p50),
      p90: valueFormatter({ util, decimals }, results.p90),
      p99: valueFormatter({ util, decimals }, results.p99),
      p9999: valueFormatter({ util, decimals }, results.p9999),
      num: results.num
    };
  });
  return values;
};

export default getCalculatedValuesBySeries;
