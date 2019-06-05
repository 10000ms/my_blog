# -*- coding: utf-8 -*-
import datetime
import os
import time
from sys import argv

# 两次尝试时间间隔
time_interval = 3
# 尝试次数
try_time = 60
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
        if i != len(self.argv):
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
        d = {
            'address': str(address),
            'port': int(port),
        }
        return d

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

    @staticmethod
    def _test_connect(address, port):
        """
        测试连接
        """
        t = 1
        while t <= try_time:
            print('{}:第{}尝试连接地址: <{}:{}>'.format(str(datetime.datetime.now()), t, address, port))
            status = os.system('(echo > /dev/tcp/{}/{}) >/dev/null 2>&1'.format(address, port))
            if status == 0:
                return True
            t += 1
            time.sleep(time_interval)
        raise Exception('连接地址: <{}> 失败，总共尝试次数：<{}>'.format(address, t))

    def check_connect(self):
        """
        检测所有要连接的是否都连接上了
        """
        for a in self.address:
            self._test_connect(a['address'], a['port'])
        return True

    def exec(self):
        """
        执行命令
        """
        if len(self.command) != 0:
            os.system(' '.join(self.command))

    def check_connect_and_exec(self):
        """
        检测所有连接成功后执行命令
        """
        self.check_connect()
        self.exec()


def main():
    m = Manage()
    m.check_connect_and_exec()


if __name__ == '__main__':
    main()
