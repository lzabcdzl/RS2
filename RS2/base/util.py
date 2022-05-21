"""
工具类
"""
import openpyxl
import logging
import sys


class Utility:

    @staticmethod  # 静态方法，可以使用类名直接调用
    def get_excel_data(bookname, sheetname):
        """
        读取Excel数据文件
        :param bookname: 工作簿名称
        :param sheetname: 工作表名称
        :return: 列表
        """
        # 加载工作簿
        workbook = openpyxl.load_workbook(bookname)
        # 获取指定的工作表
        worksheet = workbook[sheetname]
        # 获取单元格
        return list(worksheet.values)[1:]

    @staticmethod
    def get_csv_data(filename, encoding='utf-8'):
        """
        读取csv数据文件
        :param filename: 文件名
        :param encoding: 编码方式，默认是utf-8
        :return: 列表
        """
        # 按行读取数据文件
        with open(filename, 'r', encoding=encoding) as file:
            lines = file.readlines()
        # 将数据封装为指定的格式，并去除多余的空白字符
        return [tuple(e.strip() for e in line.split(',')) for line in lines][1:]

    @staticmethod
    def get_logger(level=logging.DEBUG, logname=None):
        """
        获取日志对象
        :param level: 日志等级，默认是DEBUG级别
        :param logname: 日志文件路径
        :return: 日志对象
        """
        # 创建日志对象
        logger = logging.getLogger()
        # 设置日志级别
        logger.setLevel(level)
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
        fh = logging.FileHandler(logname, 'a', encoding='utf-8')
        # 应用日志格式
        fh.setFormatter(formatter)
        # 添加到日志对象中
        logger.addHandler(fh)

        return logger


if __name__ == '__main__':
    r = Utility.get_csv_data(r'E:\ringsmiley\RS2\data\login_success.csv')
    print(r)
