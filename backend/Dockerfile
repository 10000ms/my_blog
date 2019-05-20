FROM ubuntu:18.04

# 使用阿里云的 apt 源
COPY sources.list /etc/apt/sources.list
RUN apt update
RUN apt -y install python3 python3-pip
# mysql依赖库
RUN apt-get -y install libmysqlclient-dev libmysqld-dev default-libmysqlclient-dev python-dev python-setuptools

# 使用阿里云的 pip 源
COPY pip.conf /root/.pip/pip.conf

# 将所有文件复制进/code/
COPY . /code/
RUN pip3 install -r /code/requirements.txt

# 指定工作目录
WORKDIR /code


# 启动django服务
CMD ["python3", "manage.py", "runserver", "8000"]
