FROM python:3.12-alpine3.20
LABEL maintainer="firdous.pro"

ENV PYTHONUNBUFFERED=1
ARG DEV=false



COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --no-cache-dir -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install --no-cache-dir -r /tmp/requirements.dev.txt; fi && \
    rm -rf /tmp && \
    adduser -D -H -s /sbin/nologin django-user

ENV PATH="/py/bin:$PATH"

USER django-user