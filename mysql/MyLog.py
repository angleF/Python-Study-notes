# import logging
#
# logger = logging.getLogger()
#
# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter(fmt="%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s",
#                               datefmt="%Y-%m-%d %I:%M:%S %p")  # 创建一个格式化对象
#
# console = logging.StreamHandler()  # 配置日志输出到控制台
# console.setLevel(logging.DEBUG)  # 设置输出到控制台的最低日志级别
# console.setFormatter(formatter)  # 设置格式
# logger.addHandler(console)
#
# logger.debug("sss")


import coloredlogs, logging

# Create a logger object.


handler = logging.StreamHandler()
handler.addFilter(coloredlogs.HostNameFilter())
handler.setFormatter(logging.Formatter('%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s'))
logger = logging.getLogger(__name__)
logger.addHandler(handler)
# By default the install() function installs a handler on the root logger,
# this means that log messages from your code and log messages from the
# libraries that you use will all show up on the terminal.
# coloredlogs.install(level='DEBUG')


# If you don't want to see log messages from libraries, you can pass a
# specific logger object to the install() function. In this case only log
# messages originating from that logger will show up on the terminal.
coloredlogs.install(level='DEBUG', logger=logger)

# Some examples.
# logger.debug("this is a debugging message")
# logger.info("this is an informational message")
# logger.warning("this is a warning message")
# logger.error("this is an error message")
# logger.critical("this is a critical message")