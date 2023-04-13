FROM ghcr.io/mjanez/ckan-pycsw:main

# Set up environment variables
ENV APP_DIR=/app
ENV TZ=UTC
RUN echo ${TZ} > /etc/timezone
ENV PYCSW_CKAN_SCHEMA=iso19139_inspire
ENV PYCSW_CONFIG=${APP_DIR}/pycsw.conf
ENV CKAN_URL=http://localhost:5000/
ENV PYCSW_PORT=8000
ENV PYCSW_URL=http://localhost:${PYCSW_PORT}/
ENV DEV_MODE: False
ENV TIMEOUT=300
WORKDIR ${APP_DIR}

COPY pycsw/conf/pycsw.conf.template pycsw/entrypoint.sh .

EXPOSE 8080/TCP
ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
CMD ["pdm", "run", "python3", "-m", "gunicorn", "pycsw.wsgi:application", "-b", "0.0.0.0:${PYCSW_PORT}"]