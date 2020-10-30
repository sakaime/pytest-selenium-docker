FROM python:3

COPY ./requirements.txt /root

RUN pip install --upgrade pip && \
    pip install -r /root/requirements.txt

WORKDIR /root/src

ENV TZ "Asia/Tokyo"
