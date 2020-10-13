import logging

class FileLogger:
    def __init__(self,filename='app.log',filemode='a',format='%(asctime)s - %(message)s',level=logging.INFO):
        logging.basicConfig(filename=filename, filemode=filemode, format=format,level=level)
        logging.info('File Logger Initiated')
        print('File Logger Initiated')

    def log(self,message="Logging"):
        logging.info(message)



# Ref : https://docs.python.org/3/library/logging.html#levels
# https://realpython.com/python-logging/
# https://www.geeksforgeeks.org/logging-in-python/