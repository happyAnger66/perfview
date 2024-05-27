FROM python

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

COPY app /app

ENV FLASK_APP app

WORKDIR /
