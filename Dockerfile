FROM harbor.intra.xiaojukeji.com/cargo/alpas:nightingale_20230214

COPY requirements.txt requirements.txt
RUN apt-get update && apt install -y -qq python3-pip
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

RUN apt-get update && \
  apt install -y -qq vim \
  redis-server

RUN rm -rf /app/pub
ADD nightingale/n9e /app/n9e
ADD fe-v5/pub /app/pub
ADD etc /app/etc

COPY cargo_protos/dist-packages/ /usr/lib/python3/dist-packages/

ADD datas/admin_db.sqlite3 /tmp/
COPY out-adapter/app /app/app
COPY perfview /app/perfview
RUN cd /app/perfview && python3 setup.py install

COPY wait.sh /app
RUN chmod 777 /app/wait.sh
ENV FLASK_APP app

CMD ["sh", "-c", "/app/wait.sh"]
