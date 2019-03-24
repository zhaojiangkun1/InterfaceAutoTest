import logging
# 默认日志等级是warning
# logging.basicConfig(level=10)
#
# # 调试信息，也是日志打印最详细的一个级别，用于帮助我们调试程序
# logging.debug("this is debug logging")
# # 日志详细信息，打印的频率会比debug稍微低一些，一般生产环境开启此日志级别
# logging.info("info logging")
# # 警告信息，当程序已经发生错误，但是并不影响程序的运行
# logging.warning("warning logging")
# # 错误信息，已经发生错误，影响了程序的运行
# logging.error("error logging")

#
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
# logging.basicConfig(filename="my-first.log",
#                     level=10,
#                     format=LOG_FORMAT,
#                     datefmt=DATE_FORMAT)
#
#
#
# # logging.debug("debug info")
# logging.debug("这是debug的日志")

import sys

file_path = "my-second.log"
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# 文件日志的配置
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh = logging.FileHandler(file_path, encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)


# 控制台的日志配置
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


logger.info("这是我的日志信息")















