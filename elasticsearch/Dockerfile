FROM elasticsearch:7.1.0

# 指定nameserver
RUN echo "nameserver 223.5.5.5" >> /etc/resolv.conf
RUN echo "nameserver 223.6.6.6" >> /etc/resolv.conf

# 换源(阿里的源不好用，用清华大学的源)
COPY CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo
RUN yum makecache

# 升级
RUN yum update -y && yum install -y unzip

# 使用东8时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN yum install -y tzdata

# ik分词器复制进去
COPY elasticsearch-analysis-ik-7.1.0.zip /root/elasticsearch-analysis-ik-7.1.0.zip

# 安装分析器
RUN cd /usr/share/elasticsearch/plugins && mkdir ik
RUN unzip /root/elasticsearch-analysis-ik-7.1.0.zip -d /usr/share/elasticsearch/plugins/ik
