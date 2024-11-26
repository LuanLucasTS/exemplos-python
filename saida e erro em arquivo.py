from datetime import datetime
import logging
import patoolib
import sys



path = 'log.log'
sys.stdout = open(path, 'w')
sys.stderr = open(path, 'w')


data = datetime.now().strftime('%d-%m-%Y_%H-%M')


sys.stdout.close()