FROM python:3.6-alpine
RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                --no-cache bash \
                  gcc \
                  libc-dev \
                   mariadb-dev \
        ;
ENV PYTHONUNBUFFERED 1
ENV WEBAPP_DIR=/edspace-server
WORKDIR $WEBAPP_DIR
ADD requirements.txt $WEBAPP_DIR/
RUN pip install -r requirements.txt
ADD . $WEBAPP_DIR/

