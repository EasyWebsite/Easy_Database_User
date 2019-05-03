FROM ubuntu:18.04
MAINTAINER LeoPan <pzf0000@foxmail.com>

RUN rm /etc/apt/sources.list
COPY sources.list /etc/apt/sources.list

RUN mkdir /home/easy
WORKDIR /home/easy
RUN apt-get update; apt-get install python3-psycopg2 python3-pip curl build-essential netcat rlwrap ca-certificates telnet libpq-dev -y

ADD Easy_Database_User /home/easy/Easy_Database_User
ADD ServiceUtils /home/easy/ServiceUtils
ADD templates /home/easy/templates
ADD User /home/easy/User
ADD manage.py /home/easy/manage.py
ADD requirements.txt /home/easy/requirements.txt
COPY run.sh /home/easy/run.sh

RUN chmod +x /home/easy/run.sh
RUN rm /home/easy/User/migrations/0001_initial.py
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

EXPOSE 8000

CMD python3 manage.py makemigrations;python3 manage.py migrate;python3 manage.py runserver 0.0.0.0:8000
