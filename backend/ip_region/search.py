# -*- coding:utf-8 -*-
"""
" ip2region python searcher client module
"
" Author: koma<komazhang@foxmail.com>
" Date : 2015-11-06
"""
import struct
import io
import socket
import sys


class Ip2Region(object):
    __INDEX_BLOCK_LENGTH = 12
    __TOTAL_HEADER_LENGTH = 8192

    __f = None
    __header_sip = []
    __header_ptr = []
    __header_len = 0
    __index_s_ptr = 0
    __index_l_ptr = 0
    __index_count = 0
    __db_bin_str = ''

    def __init__(self, db_file):
        self.init_database(db_file)

    def search(self, ip):
        """
        memory search method
        只使用内存搜索，所以只保留这个方法
        :param ip: 要搜索的IP
        """
        if not ip.isdigit():
            ip = self.ip_to_long(ip)

        if self.__db_bin_str == '':
            self.__db_bin_str = self.__f.read()  # read all the contents in file
            self.__index_s_ptr = self.get_long(self.__db_bin_str, 0)
            self.__index_l_ptr = self.get_long(self.__db_bin_str, 4)
            self.__index_count = int((self.__index_l_ptr - self.__index_s_ptr) / self.__INDEX_BLOCK_LENGTH) + 1

        s, h, data_ptr = (0, self.__index_count, 0)
        while s <= h:
            m = int((s + h) >> 1)
            p = self.__index_s_ptr + m * self.__INDEX_BLOCK_LENGTH
            sip = self.get_long(self.__db_bin_str, p)

            if ip < sip:
                h = m - 1
            else:
                eip = self.get_long(self.__db_bin_str, p + 4)
                if ip > eip:
                    s = m + 1
                else:
                    data_ptr = self.get_long(self.__db_bin_str, p + 8)
                    break

        if data_ptr == 0:
            raise Exception('Data pointer not found')

        return self.return_data(data_ptr)

    def init_database(self, db_file):
        """
        initialize the database for search
        :param db_file: 数据库文件地址
        """
        try:
            self.__f = io.open(db_file, 'rb')
        except IOError as e:
            print('[Error]: %s' % e)
            sys.exit()

    def return_data(self, data_ptr):
        """
        get ip data from db file by data start ptr
        :param data_ptr:
        """
        data_len = (data_ptr >> 24) & 0xFF
        data_ptr = data_ptr & 0x00FFFFFF

        self.__f.seek(data_ptr)
        data = self.__f.read(data_len)

        return {
            'city_id': self.get_long(data, 0),
            'region': data[4:]
        }

    @staticmethod
    def ip_to_long(ip):
        _ip = socket.inet_aton(ip)
        return struct.unpack('!L', _ip)[0]

    @staticmethod
    def is_ip(ip):
        p = ip.split('.')

        if len(p) != 4:
            return False
        for pp in p:
            if not pp.isdigit():
                return False
            if len(pp) > 3:
                return False
            if int(pp) > 255:
                return False

        return True

    @staticmethod
    def get_long(b, offset):
        if len(b[offset:offset + 4]) == 4:
            return struct.unpack('I', b[offset:offset + 4])[0]
        return 0

    def close(self):
        if self.__f is not None:
            self.__f.close()
        self.__db_bin_str = None
        self.__header_ptr = None
        self.__header_sip = None
