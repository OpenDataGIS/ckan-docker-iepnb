FROM nginx:stable-alpine

ENV CKAN_PORT=5000
ENV PYCSW_PORT=8000
ENV BDN_PORT=5001
ENV PYCSW_COMPOSE_SERVICE=pycsw
ENV CKAN_COMPOSE_SERVICE=ckan
ENV CKAN_DEV_COMPOSE_SERVICE=ckan-dev
#ENV BDN_COMPOSE_SERVICE=bdn
ENV PROXY_SERVER_NAME=localhost
ENV PROXY_CKAN_LOCATION=/catalog
ENV PROXY_PYCSW_LOCATION=/csw
ENV PROXY_BDN_LOCATION=/bdn
ENV PROXY_PYCSW_PROXY_PASS=http://${PYCSW_COMPOSE_SERVICE}:${PYCSW_PORT}
ENV PROXY_CKAN_PROXY_PASS=http://${CKAN_COMPOSE_SERVICE}:${CKAN_PORT}
#ENV PROXY_BDN_PROXY_PASS=http://${BDN_COMPOSE_SERVICE}:${BDN_PORT}

ENV NGINX_PORT=80
ENV NGINX_LOG_DIR=/var/log/nginx
ENV NGINX_DIR=/etc/nginx

RUN mkdir -p ${NGINX_LOG_DIR} && \
    mkdir -p ${NGINX_DIR}/certs

COPY setup/nginx.conf ${NGINX_DIR}/nginx.conf
COPY setup/index.html /usr/share/nginx/html/index.html
COPY setup/default.conf.template ${NGINX_DIR}/templates/default.conf.template
COPY setup/ckan-local.* ${NGINX_DIR}/certs/
COPY setup/robots.txt /usr/share/nginx/html/robots.txt

EXPOSE ${NGINX_PORT}