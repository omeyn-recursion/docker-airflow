# syntax=docker/dockerfile:1

FROM apache/airflow:2.7.3

USER airflow
RUN pip install aiopath

USER root

RUN apt-get update
RUN apt-get install -y iputils-ping
RUN apt-get install -y nfs-common
RUN mkdir -p /mnt/shared_storage
RUN chmod 777 /mnt/shared_storage
