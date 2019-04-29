FROM python:3.6-alpine
RUN apk add --no-cache bash bash gcc libc-dev mariadb-dev --update-cache gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev

ENV PYTHONUNBUFFERED 1
ENV WEBAPP_DIR=/edspace-server
WORKDIR $WEBAPP_DIR
ADD requirements.txt $WEBAPP_DIR/
RUN pip install -r requirements.txt
ADD . $WEBAPP_DIR/

