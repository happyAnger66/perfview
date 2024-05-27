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
import _ from 'lodash';
import { Button, Space, Dropdown, Menu } from 'antd';
import { DownOutlined, EditOutlined } from '@ant-design/icons';
import Edit from './Edit';
import { ILink } from '../types';

interface IProps {
  editable?: boolean;
  value?: ILink[];
  onChange: (newValue: ILink[]) => void;
}

export default function index(props: IProps) {
  const { editable = true, value } = props;
  return (
    <Space align='baseline'>
      <Dropdown
        overlay={
          <Menu>
            {_.isEmpty(value) ? (
              <div style={{ textAlign: 'center' }}>暂无数据</div>
            ) : (
              _.map(value, (item, idx) => {
                return (
                  <Menu.Item key={idx}>
                    <a href={item.url} target={item.targetBlank ? '_blank' : '_self'}>
                      {item.title}
                    </a>
                  </Menu.Item>
                );
              })
            )}
          </Menu>
        }
      >
        <Button>
          大盘链接 <DownOutlined />
        </Button>
      </Dropdown>
      {editable && (
        <EditOutlined
          style={{ fontSize: 18 }}
          className='icon'
          onClick={() => {
            Edit({
              initialValues: value,
              onOk: (newValue) => {
                props.onChange(newValue);
              },
            });
          }}
        />
      )}
    </Space>
  );
}
