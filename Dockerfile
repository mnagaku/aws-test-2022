FROM python:buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
ENV LANGUAGE ja_JP.UTF-8
ENV LANG ja_JP.UTF-8

RUN pip install --upgrade pip==22.0.4
COPY requirements.txt .
RUN pip install -r requirements.txt

