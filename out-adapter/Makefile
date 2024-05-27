NOW = $(shell date -u '+%Y%m%d%I%M%S')

all: build

build:
	docker build -t harbor.intra.xiaojukeji.com/cargo/alpas:prom_proxy_$(NOW) .
	docker push harbor.intra.xiaojukeji.com/cargo/alpas:prom_proxy_$(NOW)
	echo prom_proxy_$(NOW)