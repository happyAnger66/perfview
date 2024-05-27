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
import React, { useImperativeHandle, ReactNode } from 'react';
import { Form, Input } from 'antd';
import { layout } from '../../const';
import { UserAndPasswordFormProps } from '@/store/manageInterface';
import { useTranslation } from 'react-i18next';
const PasswordForm = React.forwardRef<ReactNode, UserAndPasswordFormProps>(
  (props, ref) => {
    const { t } = useTranslation();
    const [form] = Form.useForm();
    useImperativeHandle(ref, () => ({
      form: form,
    }));
    return (
      <Form {...layout} form={form}>
        <Form.Item
          name='password'
          label={t('密码')}
          rules={[
            {
              required: true,
              message: t('请输入密码!'),
            },
          ]}
          hasFeedback
        >
          <Input.Password />
        </Form.Item>

        <Form.Item
          name='confirm'
          label={t('确认密码')}
          dependencies={['password']}
          hasFeedback
          rules={[
            {
              required: true,
              message: t('请确认密码!'),
            },
            ({ getFieldValue }) => ({
              validator(_, value) {
                if (!value || getFieldValue('password') === value) {
                  return Promise.resolve();
                }

                return Promise.reject(new Error('密码不一致!'));
              },
            }),
          ]}
        >
          <Input.Password />
        </Form.Item>
      </Form>
    );
  },
);
export default PasswordForm;
