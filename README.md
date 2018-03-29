# myflaskblog
flask blog

# requirement
Jinja2 ==> 2.10

Werkzeug ==> 0.14.1

Flask ==> 0.12.2

Flask-WTF ==> 0.14.2

Flask-SQLAlchemy ==> 2.3.2

Flask-bootstarp ==> 3.3.7.1

Flask-login ==> 0.4.1

Flask-mail ==> 0.9.1

Pillow ==> 5.0.0

# 处理ImportError: No module named MySQLdb问题
1.easy_install mysql-python (mix os)

2.pip install mysql-python (mix os)

3.apt-get install python-mysqldb (Linux Ubuntu)

4.cd/usr/ports/databases/py-MySQLdb && make install clean (FreeBSD)

5.yum install MySQL-python (linux Fedora, CentOS)

6.pip install mysqlclient (Windows)

# 处理mysql启动1366问题

mysql+driver://username:password@host:port/database?charset=utf8

driver为：python2, 为'mysqldb'；python3, 为'pymysql'。安装mysql官方库如'python-mysql',如无法解决问题可能由于不支持python版本或mysql驱动BUG，可尝试使用第三方库如 'PyMySQL3' 'MySQLdb'等


 