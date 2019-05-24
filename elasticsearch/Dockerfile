FROM elasticsearch:7.1.0

# 换源
RUN wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
RUN yum makecache

# 升级
RUN yum update -y && yum install unzip

# ik分词器复制进去
COPY elasticsearch-analysis-ik-7.1.0.zip /root/elasticsearch-analysis-ik-7.1.0.zip

# 安装分析器
RUN cd /usr/share/elasticsearch/plugins && mkdir ik
RUN unzip /root/elasticsearch-analysis-ik-7.1.0.zip -d /usr/share/elasticsearch/plugins/ik
