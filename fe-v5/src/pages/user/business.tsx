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
import React, { useEffect, useState, useRef } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import PageLayout from '@/components/pageLayout';
import { Button, Table, Input, Switch, message, List, Row, Col, Pagination, Modal } from 'antd';
import { DeleteTwoTone, EditOutlined, DeleteOutlined, SearchOutlined, UserOutlined, InfoCircleOutlined } from '@ant-design/icons';
import UserInfoModal from './component/createModal';
import { RootState, accountStoreState } from '@/store/accountInterface';
import { changeStatus, deleteBusinessTeamMember, getBusinessTeamList, getBusinessTeamInfo, deleteBusinessTeam } from '@/services/manage';
import { User, Team, UserType, ActionType, TeamInfo } from '@/store/manageInterface';
import './index.less';
import { ColumnsType } from 'antd/lib/table';
import '@/components/BlankBusinessPlaceholder/index.less';
import { useTranslation } from 'react-i18next';
const { confirm } = Modal;
import { useQuery } from '@/utils';

export const PAGE_SIZE = 200;

const Resource: React.FC = () => {
  const { t } = useTranslation();
  const urlQuery = useQuery();
  const id = urlQuery.get('id');
  const [visible, setVisible] = useState<boolean>(false);
  const [action, setAction] = useState<ActionType>();
  const [teamId, setTeamId] = useState<string>(id || '');
  const [memberId, setMemberId] = useState<string>('');
  const [memberList, setMemberList] = useState<{ user_group: any }[]>([]);
  const [memberTotal, setMemberTotal] = useState<number>(0);
  const [allMemberList, setAllMemberList] = useState<User[]>([]);
  const [teamInfo, setTeamInfo] = useState<{ name: string; id: number }>();
  const [teamList, setTeamList] = useState<Team[]>([]);
  const [query, setQuery] = useState<string>('');
  const [memberLoading, setMemberLoading] = useState<boolean>(false);
  const [searchValue, setSearchValue] = useState<string>('');
  const [searchMemberValue, setSearchMemberValue] = useState<string>('');
  const userRef = useRef(null as any);
  let { profile } = useSelector<RootState, accountStoreState>((state) => state.account);
  const dispatch = useDispatch();
  const teamMemberColumns: ColumnsType<any> = [
    {
      title: t('团队名称'),
      dataIndex: ['user_group', 'name'],
      ellipsis: true,
    },
    {
      title: t('团队备注'),
      dataIndex: ['user_group', 'note'],
      ellipsis: true,
      render: (text: string, record) => record['user_group'].note || '-',
    },
    {
      title: t('权限'),
      dataIndex: 'perm_flag',
    },
    {
      title: t('操作'),
      width: '100px',
      render: (text: string, record) => (
        <a
          style={{
            color: memberList.length > 1 ? 'red' : '#00000040',
          }}
          onClick={() => {
            if (memberList.length <= 1) return;

            let params = [
              {
                user_group_id: record['user_group'].id,
                busi_group_id: teamId,
              },
            ];
            confirm({
              title: t('是否删除该团队'),
              onOk: () => {
                deleteBusinessTeamMember(teamId, params).then((_) => {
                  message.success(t('团队删除成功'));
                  handleClose('deleteMember');
                });
              },
              onCancel: () => {},
            });
          }}
        >
          {t('删除')}
        </a>
      ),
    },
  ];

  useEffect(() => {
    teamId && getTeamInfoDetail(teamId);
  }, [teamId]);

  useEffect(() => {
    getTeamList();
  }, []);

  const getList = (action) => {
    getTeamList(undefined, action === 'delete');
  };

  // 获取业务组列表
  const getTeamList = (search?: string, isDelete?: boolean) => {
    let params = {
      query: search === undefined ? searchValue : search,
      limit: PAGE_SIZE,
    };
    getBusinessTeamList(params).then((data) => {
      setTeamList(data.dat || []);
      if ((!teamId || isDelete) && data.dat.length > 0) {
        setTeamId(data.dat[0].id);
      }
    });
  };

  // 获取业务组详情
  const getTeamInfoDetail = (id: string) => {
    setMemberLoading(true);
    getBusinessTeamInfo(id).then((data) => {
      dispatch({
        type: 'common/saveData',
        prop: 'curBusiItem',
        data: data,
      });
      setTeamInfo(data);
      setMemberList(data.user_groups);
      setMemberLoading(false);
    });
  };

  const handleClick = (type: ActionType, id?: string, memberId?: string) => {
    if (memberId) {
      setMemberId(memberId);
    } else {
      setMemberId('');
    }

    setAction(type);
    setVisible(true);
  };

  // 弹窗关闭回调
  const handleClose = (action) => {
    setVisible(false);
    if (['create', 'delete', 'update'].includes(action)) {
      getList(action);
      dispatch({ type: 'common/getBusiGroups' });
    }
    if (teamId && ['update', 'addMember', 'deleteMember'].includes(action)) {
      getTeamInfoDetail(teamId);
    }
  };

  return (
    <PageLayout title={t('业务组管理')} icon={<UserOutlined />} hideCluster>
      <div className='user-manage-content'>
        <div style={{ display: 'flex', height: '100%' }}>
          <div className='left-tree-area'>
            <div className='sub-title'>
              {t('业务组列表')}
              <Button
                style={{
                  height: '30px',
                }}
                size='small'
                type='link'
                onClick={() => {
                  handleClick(ActionType.CreateBusiness);
                }}
              >
                {t('新建业务组')}
              </Button>
            </div>
            <div style={{ display: 'flex', margin: '5px 0px 12px' }}>
              <Input
                prefix={<SearchOutlined />}
                placeholder={t('搜索业务组名称')}
                onPressEnter={(e) => {
                  // @ts-ignore
                  getTeamList(e.target.value);
                }}
                onBlur={(e) => {
                  // @ts-ignore
                  getTeamList(e.target.value);
                }}
              />
            </div>

            <List
              style={{
                marginBottom: '12px',
                flex: 1,
                overflow: 'auto',
              }}
              dataSource={teamList}
              size='small'
              renderItem={(item) => (
                <List.Item key={item.id} className={teamId == item.id ? 'is-active' : ''} onClick={() => setTeamId(item.id)}>
                  {item.name}
                </List.Item>
              )}
            />
          </div>
          {teamList.length > 0 ? (
            <div className='resource-table-content'>
              <Row className='team-info'>
                <Col
                  span='24'
                  style={{
                    color: '#000',
                    fontSize: '14px',
                    fontWeight: 'bold',
                    display: 'inline',
                  }}
                >
                  {teamInfo && teamInfo.name}
                  <EditOutlined
                    title={t('刷新')}
                    style={{
                      marginLeft: '8px',
                      fontSize: '14px',
                    }}
                    onClick={() => handleClick(ActionType.EditBusiness, teamId)}
                  ></EditOutlined>
                  <DeleteOutlined
                    style={{
                      marginLeft: '8px',
                      fontSize: '14px',
                    }}
                    onClick={() => {
                      confirm({
                        title: t('是否删除该业务组'),
                        onOk: () => {
                          deleteBusinessTeam(teamId).then((_) => {
                            message.success(t('业务组删除成功'));
                            handleClose('delete');
                          });
                        },
                        onCancel: () => {},
                      });
                    }}
                  />
                </Col>
                <Col
                  style={{
                    marginTop: '8px',
                    color: '#666',
                  }}
                >
                  {t('备注')}：{t('告警规则，告警事件，监控对象，自愈脚本等都归属业务组，是一个在系统里可以自闭环的组织')}
                </Col>
              </Row>
              <Row justify='space-between' align='middle'>
                <Col span='12'>
                  <Input
                    prefix={<SearchOutlined />}
                    value={searchMemberValue}
                    className={'searchInput'}
                    onChange={(e) => setSearchMemberValue(e.target.value)}
                    placeholder={t('搜索团队名称')}
                  />
                </Col>
                <Button
                  type='primary'
                  ghost
                  onClick={() => {
                    handleClick(ActionType.AddBusinessMember, teamId);
                  }}
                >
                  {t('添加团队')}
                </Button>
              </Row>

              <Table
                rowKey='id'
                columns={teamMemberColumns}
                dataSource={memberList && memberList.length > 0 ? memberList.filter((item) => item.user_group && item.user_group.name.indexOf(searchMemberValue) !== -1) : []}
                loading={memberLoading}
              />
            </div>
          ) : (
            <div className='blank-busi-holder'>
              <p style={{ textAlign: 'left', fontWeight: 'bold' }}>
                <InfoCircleOutlined style={{ color: '#1473ff' }} /> {t('提示信息')}
              </p>
              <p>
                业务组（监控对象、监控大盘、告警规则、自愈脚本都要归属某个业务组）为空，请先&nbsp;
                <a onClick={() => handleClick(ActionType.CreateBusiness)}>创建业务组</a>
              </p>
            </div>
          )}
        </div>
      </div>
      <UserInfoModal
        visible={visible}
        action={action as ActionType}
        userType={'business'}
        onClose={handleClose}
        teamId={teamId}
        onSearch={(val) => {
          setTeamId(val);
        }}
      />
    </PageLayout>
  );
};

export default Resource;
