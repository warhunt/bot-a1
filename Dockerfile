FROM python:3.9.7-alpine3.14

ARG BOT_TOKEN
ARG PHONE_NUMBER
ARG PASSWORD
ARG HEROKU_APP_NAME
ARG WEBAPP_PORT

ENV BOT_TOKEN $BOT_TOKEN
ENV PHONE_NUMBER $PHONE_NUMBER
ENV PASSWORD $PASSWORD
ENV HEROKU_APP_NAME $HEROKU_APP_NAME
ENV WEBAPP_PORT $WEBAPP_PORT

ENV APP_PATH "/usr/src/application"

WORKDIR ${APP_PATH}

RUN pip install --upgrade pip

COPY ./ .

#RUN apk add gcc musl-dev python3-dev libffi-dev chromium chromium-chromedriver
RUN apk add gcc musl-dev python3-dev
RUN pip install --no-cache-dir -r ./requirements/production.txt

CMD python -B -m bot