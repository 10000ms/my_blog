FROM elasticsearch:7.1.0

# 换源
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# 升级
RUN apt-get update && apt-get install zip 

# 创建目录
RUN mkdir -p /usr/share/elasticsearch/plugins/ik 

# 安装分析器
RUN /elasticsearch/bin/elasticsearch install elasticsearch-analysis-ik-5.1.1.zip
