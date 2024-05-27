FROM harbor.intra.xiaojukeji.com/cargo/alpas:nightingale_20230214

RUN rm -rf /app/pub
ADD pub /app/pub
ADD etc /app/etc

CMD ["sh", "-c", "/app/n9e server -c /app/etc/server.conf"]