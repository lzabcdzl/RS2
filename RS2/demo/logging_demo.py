# print('hello', file=open('test.log', 'w', encoding='utf-8'))

import logging
import sys

# 创建日志对象
logger = logging.getLogger()
# 设置日志级别
# logging.basicConfig(level=logging.ERROR)
logger.setLevel(logging.ERROR)
# 设置日志输出格式
formatter = logging.Formatter('[%(asctime)s]:[%(levelname)s]:[%(filename)s]:[%(message)s]')

'''输出日志到控制台'''
# 创建控制台处理器
sh = logging.StreamHandler(sys.stdout)
# 应用日志格式
sh.setFormatter(formatter)
# 添加到日志对象中
logger.addHandler(sh)

'''输出日志到文件中'''
# 创建文件处理器
fh = logging.FileHandler('test.log', 'a', encoding='utf-8')
# 应用日志格式
fh.setFormatter(formatter)
# 添加到日志对象中
logger.addHandler(fh)

# 输出
logger.debug('调试')
logger.info('信息')
logger.warning('警告')
logger.error('错误')
logger.critical('严重')