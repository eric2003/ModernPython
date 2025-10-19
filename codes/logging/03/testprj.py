import logging
import os
os.chdir("./") # 日志写入地址
logging.basicConfig(filename='example.log', level=logging.DEBUG) 
# 注意：上面level设置的是显示的最低严重级别，小于level设置的最低严重级别将不会打印出来
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')