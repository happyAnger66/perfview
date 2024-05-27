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
import React, { useEffect, useState, useImperativeHandle, ReactNode, useCallback } from 'react';
import { Form, Input, Select, Switch, Row, Tag, Space, Button } from 'antd';
import { layout } from '../../const';
import { MinusCircleOutlined, PlusOutlined, CaretDownOutlined } from '@ant-design/icons';
import { getBusinessTeamInfo, getTeamInfoList } from '@/services/manage';
import { TeamProps, Team, TeamInfo, ActionType } from '@/store/manageInterface';
import { useTranslation } from 'react-i18next';
import { debounce } from 'lodash';

const { Option } = Select;
const TeamForm = React.forwardRef<ReactNode, TeamProps>((props, ref) => {
  const { t } = useTranslation();
  const { businessId, action } = props;
  const [form] = Form.useForm();
  const [userTeam, setUserTeam] = useState<Team[]>([]);
  const [initialValues, setInitialValues] = useState({
    label_enable: false,
    label_value: '',
    members: [{ perm_flag: true }],
    name: '',
  });
  const [loading, setLoading] = useState<boolean>(true);
  const [refresh, setRefresh] = useState(true);
  useImperativeHandle(ref, () => ({
    form: form,
  }));

  useEffect(() => {
    if (businessId && action === ActionType.EditBusiness) {
      getTeamInfoDetail(businessId);
    } else {
      setLoading(false);
    }
  }, []);

  const getTeamInfoDetail = (id: string) => {
    getBusinessTeamInfo(id).then((data: { name: string; label_enable: number; label_value: string; user_groups: { perm_flag: string; user_group: { id: number } }[] }) => {
      setInitialValues({
        name: data.name,
        label_enable: data.label_enable === 1,
        label_value: data.label_value,
        members: data.user_groups.map((item) => ({
          perm_flag: item.perm_flag === 'rw',
          user_group_id: item.user_group.id,
        })),
      });
      setLoading(false);
    });
  };

  useEffect(() => {
    getList('');
  }, []);

  const getList = (str: string) => {
    getTeamInfoList({ query: str }).then((res) => {
      setUserTeam(res.dat);
    });
  };

  const debounceFetcher = useCallback(debounce(getList, 800), []);

  return !loading ? (
    <Form {...layout} form={form} initialValues={initialValues} preserve={false} layout={refresh ? 'horizontal' : 'horizontal'}>
      {action !== ActionType.AddBusinessMember && (
        <>
          <Form.Item
            label={t('业务组名称')}
            name='name'
            rules={[
              {
                required: true,
                message: t('业务组名称不能为空！'),
              },
            ]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label={t('作为标签使用')}
            name='label_enable'
            valuePropName='checked'
            tooltip={{ title: '系统会自动把业务组的英文标识作为标签附到该业务组下辖监控对象的时序数据上', getPopupContainer: () => document.body }}
          >
            <Switch />
          </Form.Item>

          <Form.Item noStyle shouldUpdate={(prevValues, curValues) => prevValues.label_enable !== curValues.label_enable}>
            {({ getFieldValue }) => {
              return (
                getFieldValue('label_enable') && (
                  <Form.Item
                    label={t('英文标识')}
                    name='label_value'
                    rules={[
                      {
                        required: true,
                      },
                    ]}
                    tooltip={{
                      title: (
                        <span>
                          尽量用英文，不能与其他业务组标识重复，系统会自动生成 <Tag color='blue'>busigroup={form.getFieldValue('label_value')}</Tag> 的标签
                        </span>
                      ),
                      getPopupContainer: () => document.body,
                    }}
                  >
                    <Input
                      onChange={(val) => {
                        setRefresh(!refresh);
                      }}
                    />
                  </Form.Item>
                )
              );
            }}
          </Form.Item>
        </>
      )}

      {(action === ActionType.CreateBusiness || action === ActionType.AddBusinessMember) && (
        <Form.Item
          label={t('团队')}
          required
          // tooltip={{
          //   title: '默认可读勾选可写',
          // }}
        >
          <Form.List name='members'>
            {(fields, { add, remove }) => (
              <>
                {fields.map(({ key, name, fieldKey, ...restField }) => (
                  <Space key={key} style={{ display: 'flex', marginBottom: 8 }} align='baseline'>
                    <Form.Item
                      style={{ width: 450 }}
                      {...restField}
                      name={[name, 'user_group_id']}
                      fieldKey={[fieldKey, 'user_group_id']}
                      rules={[{ required: true, message: t('业务组团队不能为空！') }]}
                    >
                      <Select
                        suffixIcon={<CaretDownOutlined />}
                        style={{ width: '100%' }}
                        filterOption={false}
                        onSearch={(e) => debounceFetcher(e)}
                        showSearch
                        onBlur={() => getList('')}
                      >
                        {userTeam.map((team) => (
                          <Option key={team.id} value={team.id}>
                            {team.name}
                          </Option>
                        ))}
                      </Select>
                    </Form.Item>
                    <Form.Item {...restField} name={[name, 'perm_flag']} fieldKey={[fieldKey, 'perm_flag']} valuePropName='checked'>
                      <Switch checkedChildren='读写' unCheckedChildren='只读' />
                    </Form.Item>
                    <MinusCircleOutlined onClick={() => remove(name)} />
                  </Space>
                ))}
                <Form.Item>
                  <Button type='dashed' onClick={() => add()} block icon={<PlusOutlined />}>
                    添加团队
                  </Button>
                </Form.Item>
              </>
            )}
          </Form.List>
        </Form.Item>
      )}
    </Form>
  ) : null;
});
export default TeamForm;
