#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: hive.py 
@time: 2018/1/4 10:07 
@describe:hive的远程操作模式，简单实现远程查询功能

在使用Python连接hive之前需要将hive中的文件拷贝到python的sys.path中
cp -r $HIVE_PATH/lib/py /usr/local/lib/python2.7/site-packages
调用：eg:from py.hive_service import ThriftHive 需要加 py
"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from py.hive_service import ThriftHive
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def hiveExe(sql):
    try:
        transport = TSocket.TSocket('192.168.8.10', 10000)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = ThriftHive.Client(protocol)
        transport.open()

        client.execute(sql)

        print "The return value is : "
        data = client.fetchAll()
        for i in data:
            print i
        print "............"
        transport.close()
    except Thrift.TException, tx:
        print '%s' % (tx.message)


if __name__ == '__main__':
    hiveExe("select tip from trip limit 5")  # hive会启动一个MapReduce作业去实现该过程，所以速度比较慢