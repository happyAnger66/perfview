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
import { Modal, Form, Select, message } from 'antd';
import _ from 'lodash';
import { useTranslation } from 'react-i18next';
import ModalControl from '@/components/BaseModal/modalControl';
import request from '@/utils/request';
import api from '@/utils/api';

const FormItem = Form.Item;
const { Option } = Select;

const UnBindTags = (props) => {
  const { t } = useTranslation();
  const [form] = Form.useForm();
  const handleOk = () => {
    const { selectedIds } = props;
    form.validateFields().then((values: any) => {
      request(`${api.tasktpl(props.busiId)}s/tags`, {
        method: 'DELETE',
        body: JSON.stringify({
          tags: values.tags,
          ids: selectedIds,
        }),
      }).then(() => {
        message.success(t('tpl.tag.unbind.success'));
        props.onOk();
        props.destroy();
      });
    });
  }

  const handleCancel = () => {
    props.destroy();
  }

  const { visible, uniqueTags } = props;

  return (
    <Modal
      title={t('tpl.tag.unbind.title')}
      visible={visible}
      onOk={handleOk}
      onCancel={handleCancel}
    >
      <Form form={form}>
        <FormItem
          label={t('tpl.tag.unbind.field')}
          required
          name="tags"
          rules={[{ required: true }]}
        >
          <Select mode="tags">
            {
              _.map(uniqueTags, (tag) => {
                return <Option key={tag} value={tag}>{tag}</Option>;
              })
            }
          </Select>
        </FormItem>
      </Form>
    </Modal>
  );
}

UnBindTags.defaultProps = {
  visible: true,
  onOk: _.noop,
  destroy: _.noop,
};

export default ModalControl(UnBindTags as any);
