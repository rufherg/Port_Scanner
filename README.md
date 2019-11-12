# Port_Scanner
基于TCP连接的简易端口扫描器

## 原理
基于套接字的端口探测

通过socket与目标端口进行连接，连接成功即证明端口存在性

## 并发处理futures
使用futures模块，创建线程池，从而使扫描效率提高

默认线程数为50，max模式下线程数目为100

## 使用方法

```shell
$ python PortScanner.py
usage: PortScanner.py [-h] [-u URL] [-p PORT] [-m]
Port Scanner
optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     目标URL
  -p PORT, --port PORT  待扫描的端口范围（默认1-65535）
  -m, --max             最高线程模式(max=100)
```

eg:

```shell
$ python PortScanner.py -u http://www.baidu.com -p 1-1000 -m
```

注：

- 此处url可以填带协议的url，也可以为ip地址，也可以为域名
- 参数port，可以填单个端口，也可以为一个端口范围，默认为1-65535（全部端口）

## 待完善

- 目前扫描方式只有TCP connect，后续可加入TCP SYN，UDP等其他方式
- 扫描C段IP，同时扫描多个ip
- 支持文件导入与导出
- 未完待续