#!/usr/bin/pythonCGI
# -*- coding: utf8
import logging
import logging.handlers


class Logger:
    """
    Loggerクラス。
    """

    LOG_FILENAME = "logger.log"
    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s - %(message)s"

    def __init__(self, logfilename):
        #rootロガーを取得
        logger = logging.getLogger()
        logger.setLevel(self.LOG_LEVEL)
        #出力のフォーマットを定義
        formatter = logging.Formatter(self.LOG_FORMAT)
        #ログファイルを時刻でローテーションするハンドラーを定義
        trh = logging.handlers.TimedRotatingFileHandler(
            filename=logfilename,
            when='D',
            backupCount=10
        )
        trh.setLevel(self.LOG_LEVEL)
        trh.setFormatter(formatter)
        #rootロガーにハンドラーを登録する
        logger.addHandler(trh)
        self.__logger = logger

    def __initBasic__(self, logfilename):
        logging.basicConfig(
            level=self.LOG_LEVEL,
            filename=logfilename,
            format=self.LOG_FORMAT)
        self.__logger = logging.getLogger()

    def debug(self, message):
        self.__logger.debug(message)
        print 'debug :' + message

    def info(self, message):
        self.__logger.info(message)
        print 'info :' + message

    def warning(self, message):
        self.__logger.warning(message)
        print 'warning :' + message

    def error(self, message):
        self.__logger.error(message)
        print 'error :' + message

    def fatal(self, message):
        self.__logger.fatal(message)
        print 'fatal :' + message


def main():
    logger = Logger('logger_test.log')
    logger.debug('Logger.main called.')
    print('end of Logger.main')

if __name__ == '__main__':
    main()
