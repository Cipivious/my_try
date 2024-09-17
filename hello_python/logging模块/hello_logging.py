import logging

"""
%(asctime)s: 输出日志的时间，默认格式是 YYYY-MM-DD HH:MM:SS,MS（例如 2024-08-25 12:34:56,789）。
%(levelname)s: 日志级别的名称（例如 DEBUG, INFO, WARNING, ERROR, CRITICAL）。
%(message)s: 日志消息内容（即 logger.debug() 等方法中传递的消息）。
%(name)s: Logger 的名称。
%(filename)s: 输出日志调用所在的源文件名。
%(pathname)s: 输出日志调用所在的完整文件路径名。
%(funcName)s: 输出日志调用所在的函数名。
%(lineno)d: 输出日志调用所在的行号。
%(module)s: 模块名，即去掉路径和文件扩展名后的文件名。
%(process)d: 进程 ID。
%(processName)s: 进程名。
%(thread)d: 线程 ID。
%(threadName)s: 线程名。
%(created)f: 输出日志时间的浮点表示，从 1970-01-01 00:00:00 开始的秒数。
%(relativeCreated)d: 输出日志的时间，从 Logger 创建以来的毫秒数。
%(msecs)d: 输出日志的毫秒部分。
%(levelno)s: 日志级别的数值（例如 10 表示 DEBUG，20 表示 INFO，等等）。
%(message)s: 实际的日志消息字符串，由用户提供的 message 参数计算得到。
"""
logging.basicConfig(
    filename="demo.log",
    level=logging.DEBUG,
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.debug("this is a debug log")
logging.info("this is an info log")
logging.warning("this ia a warning log")
logging.error("this is an error log")
logging.critical("this is a critical log")
