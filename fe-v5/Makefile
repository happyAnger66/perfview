.PHONY: build

NOW = $(shell date -u '+%Y%m%d%I%M%S')


ROOT:=$(shell pwd -P)
GIT_COMMIT:=$(shell git --work-tree ${ROOT}  rev-parse 'HEAD^{commit}')
_GIT_VERSION:=$(shell git --work-tree ${ROOT} describe --tags --abbrev=14 "${GIT_COMMIT}^{commit}" 2>/dev/null)
TAG=$(shell echo "${_GIT_VERSION}" |  awk -F"-" '{print $$1}')
RELEASE_VERSION:="$(TAG)-$(GIT_COMMIT)"

# RELEASE_ROOT 	= release
# RELEASE_SERVER 	= release/${APP}
# GIT_COUNT 		= $(shell git rev-list --all --count)
# GIT_HASH        = $(shell git rev-parse --short HEAD)
# RELEASE_TAG     = $(RELEASE_VERSION).$(GIT_COUNT).$(GIT_HASH)

all: build

build:
	docker build -t harbor.intra.xiaojukeji.com/cargo/alpas:nightingale_webapi_$(NOW) .
	docker push harbor.intra.xiaojukeji.com/cargo/alpas:nightingale_webapi_$(NOW)
	echo harbor.intra.xiaojukeji.com/cargo/alpas:nightingale_webapi_$(NOW)