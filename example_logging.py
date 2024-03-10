import logging
import time

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                     datefmt='%Y-%m-%d %H:%M:%S')

a = 3 + 4
b = "aa"

#Throws assertion error if not true
assert a == 7

if a == 7:
    logging.info(f"This was 7")
    logging.debug(f"debug level as well")
    logging.warning('And this, too')
    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

print("end of the script")