# 1.myflaskblog简单说明
一个flask的blog
### 1.1所需数据库
mysql 和 redis
### 1.2首次运行
#### 1.2.1检查config.py文件中的设置是否符合运行环境的需求
特别是mysql和redis数据库配置，以及发邮件服务器的配置。发邮件服务器默认使用qq邮箱，帐号密码分别从环境变量的MAIL_USERNAME和MAIL_PASSWORD获取
#### 1.2.2本地环境在项目路径终端输入
~~~
#安装所需的python库
pip install -r requirements.txt

#数据库创建

python manage.py create_db

#运行服务器

python manage.py runserver
~~~
等待网站配置完成即可正常运行（约15秒）
### 1.3所使用的flask第三方库
#### 定时任务
Flask-APScheduler
#### 前端Bootstrap
Flask-Bootstrap
#### flask登陆验证
Flask-Login
#### 发送邮件
Flask-Mail
#### 数据库迁移
Flask-Migrate
#### flask的redis数据库库
Flask-Redis
#### flask的shell及相关配置
Flask-Script
#### flask的SQLAlchemy（用于数据库处理）
Flask-SQLAlchemy
#### flask的WTF表单
Flask-WTF
### 1.4管理员帐号
帐号：123456

密码：a123456

### 1.5权限说明
#### 普通用户
直接可以在主页注册成为普通用户，邮箱激活后就可以使用。可以进行文章浏览、评论管理和个人信息的设置
#### 管理员用户
默认只有一个管理员用户。管理员用户拥有普通用户的全部权限外，还可以进行用户管理，文章管理，网站管理，文章发表和全评论管理
### 1.6用户登陆管理
注册用户必须进行邮箱认证后才可以正常的使用。

网站强制单点登陆，登陆用户180秒（可在config.py中配置这个时间）无操作就可以被挤下线。
# 2.部分前端页面展示
![首页](https://note.youdao.com/yws/api/personal/file/2F014E1A10CB452B9ADD547389A4AA6E?method=download&shareKey=11db0f083a69dc50a16378abe2f31b4f)

![管理界面](https://note.youdao.com/yws/api/personal/file/184C11E1D4184507B6C67D686F7838A6?method=download&shareKey=034db1cb0d72e7bfd6866270a1dd9954)

![网站设置](https://note.youdao.com/yws/api/personal/file/FF1FBA93343D4B31AE12E30830D0DD09?method=download&shareKey=139a1ba070a26352ed63379551cc512b)

![个人设置](https://note.youdao.com/yws/api/personal/file/D554883ED9B244ED9FE8D4FEB47D202F?method=download&shareKey=a1b63e0a983a797bc7c8a9656dc07a60)

![新文章编辑](https://note.youdao.com/yws/api/personal/file/91F27475166446F689458980D5CC27AC?method=download&shareKey=628e5a49254b13c9edcd9cc32df083cd)

# 3.项目文件说明
## 3.1根目录
migrations：数据库迁移所需文件，系统自动生成的

myflaskblog：项目主体文件夹

tests：单元测试文件夹

config.py：项目配置文件

manage.py：项目入口文件

requirements.txt:项目需要第三方模块文档
## 3.2myflaskblog文件夹
main：控制器文件

static：静态文件

templates：模板文件

.py文件内均有注释说明详细用途用法

# 4.可以改进的地方
1.用户头像上传的时候要进行检测，防止所上传的图片违法法律，考虑使用第三方api进行

# 5.可能出现的问题及解决方案
###  5.1处理ImportError: No module named MySQLdb问题
1.easy_install mysql-python (mac os)

2.pip install mysql-python (mac os)

3.apt-get install python-mysqldb (Linux Ubuntu)

4.cd/usr/ports/databases/py-MySQLdb && make install clean (FreeBSD)

5.yum install MySQL-python (linux Fedora, CentOS)

6.pip install mysqlclient (Windows)

### 5.2处理mysql启动1366问题

mysql+driver://username:password@host:port/database?charset=utf8

driver为：python2, 为'mysqldb'；python3, 为'pymysql'。安装mysql官方库如'python-mysql',如无法解决问题可能由于不支持python版本或mysql驱动BUG，可尝试使用第三方库如 'PyMySQL3' 'MySQLdb'等


 