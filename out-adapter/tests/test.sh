curl -XPOST https://api-kylin.intra.xiaojukeji.com/snitch_openapi_online_lb/v1/message.create \
-u '79b7469cf48d480cae0677aa7ebb654d:2f032f32728f4b4d92f3112abf609722' \
-H "Content-Type: application/json;charset=utf-8" \
-d '{
      "bot_id": "99357",
      "bot_type": "bot_user",
      "text": "Hello World",
      "vchannel_id": "1605286273952414208"
    }'