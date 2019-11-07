#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: DEADF1SH_CAT
@File: Port_Scanner.py
@Time: 2019/11/07 21:40
@About: 
'''

import socket
import concurrent.futures
import datetime

class PortScanner():
    def __init__(self, host, start_port, end_port, flag):
        self.host = socket.gethostbyname(host)
        self.Sport = int(start_port)
        self.Eport = int(end_port)
        if flag:
            self.threads = 50
        else:
            self.threads = 30

    def run(self):
        print("-"*25 + "Start PortScanner" + "-"*25)
        if self.thread():
            print("-"*27 + "End PortScanner" + "-"*25)

    def scan(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        try:
            if sock.connect_ex((self.host, port)) == 0:
                print("[+]Host:" + self.host + " is opening " + str(port))
            else:
                pass
        except:
            pass

    def thread(self) -> bool:
        threadpool = concurrent.futures.ThreadPoolExecutor(max_workers = self.threads)
        futures = (threadpool.submit(self.scan, port) for port in range(self.Sport, self.Eport + 1))
        for i in concurrent.futures.as_completed(futures):
            pass
        return True

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    portscanner = PortScanner("www.baidu.com",1,80,0)
    portscanner.run()
    spend_time = (datetime.datetime.now() - start_time).seconds
    print("Total time: " + str(spend_time) + " seconds")