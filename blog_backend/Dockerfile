FROM python:3.7-alpine

ENV DEBIAN_FRONTEND noninteractive

COPY ./ci /opt/blog_backend/ci

RUN apk update &&\
    cat /opt/blog_backend/ci/apt-requirements.txt | xargs apk add
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r /opt/blog_backend/ci/py-requirements.txt

COPY . /opt/blog_backend/
WORKDIR /opt/blog_backend/
RUN chmod +x /opt/blog_backend/docker-entrypoint.sh

VOLUME /opt/blog_backend/static/
EXPOSE 8000
ENTRYPOINT ["/opt/blog_backend/docker-entrypoint.sh"]

