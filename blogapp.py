#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
flask project entrance.
'''

# 导入flask扩展
from flask import Flask

# 创建Flask应用程序实例
# 需要传入__name__，作用是确定资源所在的路径
app = Flask(__name__)

# 定义路由及视图函数
# Flask中定义路由是由专门的路由装饰器实现的
@app.route("/")
def hello():
    return "Hello World!"

# 启动程序
if __name__ == '__main__':
    app.run()