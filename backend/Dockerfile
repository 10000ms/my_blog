FROM ubuntu:18.04
# 输出不缓存
ENV PYTHONUNBUFFERED 1
# 安装时不报ssl错误
ENV PYTHONWARNINGS ignore:Unverified HTTPS request

# 使用阿里云的 apt 源
COPY sources.list /etc/apt/sources.list
RUN apt update
RUN apt -y install python3 python3-pip
# mysql依赖库
RUN apt-get -y install libmysqlclient-dev libmysqld-dev default-libmysqlclient-dev python-dev python-setuptools

# 使用阿里云的 pip 源
COPY pip.conf /root/.pip/pip.conf
COPY requirements.txt /backend/requirements.txt
RUN pip3 install -r /backend/requirements.txt

# 复制wait-for-it进镜像
COPY wait-for-it.sh /backend/wait-for-it.sh

# 将所有文件复制进/code/
COPY code/ /backend/code/

# 指定工作目录
WORKDIR /backend/code


# 启动django服务
#CMD ["python3", "manage.py", "runserver", "8000"]

# 暴露端口
EXPOSE 8000
