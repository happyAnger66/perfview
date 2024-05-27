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
import React from 'react';
import { Form, Radio, Row, Col } from 'antd';
import _ from 'lodash';
import { Panel } from '../../Components/Collapse';

export default function index() {
  const namePrefix = ['options', 'tooltip'];

  return (
    <Panel header='Tooltip'>
      <Row gutter={10}>
        <Col span={12}>
          <Form.Item label='模式' name={[...namePrefix, 'mode']}>
            <Radio.Group buttonStyle='solid'>
              <Radio.Button value='single'>single</Radio.Button>
              <Radio.Button value='all'>all</Radio.Button>
            </Radio.Group>
          </Form.Item>
        </Col>
        <Col span={12}>
          <Form.Item noStyle shouldUpdate={(prevValues, curValues) => _.get(prevValues, [...namePrefix, 'mode']) !== _.get(curValues, [...namePrefix, 'mode'])}>
            {({ getFieldValue }) => {
              if (getFieldValue([...namePrefix, 'mode']) === 'all') {
                return (
                  <Form.Item label='排序' name={[...namePrefix, 'sort']}>
                    <Radio.Group buttonStyle='solid'>
                      <Radio.Button value='none'>none</Radio.Button>
                      <Radio.Button value='asc'>asc</Radio.Button>
                      <Radio.Button value='desc'>desc</Radio.Button>
                    </Radio.Group>
                  </Form.Item>
                );
              }
              return null;
            }}
          </Form.Item>
        </Col>
      </Row>
    </Panel>
  );
}
