import os
import datetime
import logging

today = datetime.date.today()
year = today.year
month = today.month
day = today.day
formatted_date = f'{year}{month:02d}{day:02d}'
save_dir = os.getenv('LOG_DIR')
file_name = formatted_date + '.log'
log_file_path = os.path.join(save_dir, file_name)
logging.basicConfig(filename=log_file_path , level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logging.debug('TEST DEBUG')
logging.info('TEST INFO')
logging.error('TEST ERROR')
logging.warning('TEST WARNNING')