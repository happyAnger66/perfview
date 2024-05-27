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
import React, { FC } from 'react';

export interface QueryStats {
  loadTime: number;
  resolution?: number;
  resultSeries: number;
}

const QueryStatsView: FC<QueryStats> = (props) => {
  const { loadTime, resolution, resultSeries } = props;

  return (
    <div className="query-stats">
      <span>
        Load time: {loadTime}ms &ensp;{resolution && `Resolution: ${resolution}s `}&ensp;Result series: {resultSeries}
      </span>
    </div>
  );
};

export default QueryStatsView;
