import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a,%d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a'
#                     )



# logging.debug('我很帅u')



logger = logging.getLogger()
fh = logging.FileHandler('test.log')
sh = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
logger.addHandler(fh)
# logger.addHandler(sh)
logger.warning('我很帅')