# -*- coding: utf-8 -*-
import datetime
import os
import socket
import time
from sys import argv

# 两次尝试时间间隔
time_interval = 1
# 尝试次数
try_time = 3
# 本地的ip地地址
default_address = '127.0.0.1'

# socket
connect_socket = None

# 获取的所有参数
all_argv = argv[1:]


class Manage:
    # socket
    connect_socket = None

    def __init__(self):
        self.socket = socket.socket()
        self.argv = argv[1:]
        self.address = []
        self.command = []
        self.analyze_argv()

    def analyze_argv(self):
        """
        分析参数
        """
        i = 0
        while i < len(self.argv):
            address = self.check_is_address_or_port(self.argv[i])
            if address:
                self.address.append(address)
                i += 1
            else:
                break
        if i == len(self.argv):
            raise Exception('没有可执行的指令')
        else:
            self.command = self.argv[i:]

    @staticmethod
    def check_is_port(item):
        """
        检查是否是端口
        """
        return item.isdecimal() and 1 <= int(item) <= 65535

    @staticmethod
    def create_address(address, port):
        """
        创建address
        """
        return str(address), int(port)

    def check_is_address_or_port(self, item):
        """
        检查是否是address:port, 或者是port
        因为docker-compose环境下，什么address都有，主要检查端口是否正确
        :param item: 待检测的 argv
        :return:
        """
        if ':' in item:
            address, port = item.split(':', 1)
            if self.check_is_port(port):
                return self.create_address(address, port)
            else:
                return False
        elif self.check_is_port(item):
            return self.create_address(default_address, item)
        return False

    def _test_connect(self, address):
        t = 0
        print('{}:尝试连接地址: <{}>'.format(str(datetime.datetime.now()), address))
        while t < try_time:
            status = self.socket.connect_ex(address)
            if status == 0:
                return True
            t += 1
            time.sleep(time_interval)
        raise Exception('连接地址: <{}> 失败，尝试次数：<{}>'.format(address, t))

    def check_connect(self):
        for a in self.address:
            self._test_connect(a)
        return True

    def exec(self):
        os.system(' '.join(self.command))

    def check_connect_and_exec(self):
        self.check_connect()
        self.exec()

def main():
    print(all_argv)
    m = Manage()
    m.check_connect_and_exec()


if __name__ == '__main__':
    main()
