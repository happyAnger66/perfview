from datetime import datetime

import requests
import json

from flask import (
    Blueprint, current_app, request
)

bp = Blueprint('dchat', __name__, url_prefix='/dchat')


def convert_timestamp(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    return str(dt)


def send_one_user(user, text):
    cfg = current_app.config
    url = 'https://%s/%s' % (cfg["DCHAT_DOMAIN"],
                             cfg["DCHAT_MSG_CREATE_ROUTE"])
    r = requests.post(url,
                      auth=(cfg["DCHAT_USER"], cfg["DCHAT_PASS"]),
                      data={'bot_id': cfg["DCHAT_BOT_ID"],
                            'bot_type': cfg["DCHAT_BOT_TYPE"],
                            'text': text,
                            'username': user["username"]})


@bp.route('/msg_create', methods=['POST', 'GET'])
def msg_create():
    data = request.data
    if data:
        body = json.loads(data.decode('utf-8'))
        text = "host: %s alert at: 【 %s 】 !!!\r\n" % (body["target_ident"], convert_timestamp(body["trigger_time"])) + str(
            body["tags"]) + "\r\n current_value:%s" % body["trigger_value"]

        if not body["target_ident"]:
            return

        for user in body['notify_users_obj']:
            send_one_user(user, text)
    return 'ok'
