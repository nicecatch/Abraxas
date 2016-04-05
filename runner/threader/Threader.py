'''
Created on 04 apr 2016

@author: posiandr
'''

import threading
import time
#from snap7 import util
#import snap7
#from snap7.snap7types import areas

#from runner.plc import PLC


class PLCReader (threading.Thread):
    def __init__(self, plc, config):
        super(PLCReader, self).__init__()
        self.plc = plc
        self.config = config
        self.alive = True
    
    def run(self):
        while self.alive is True:
            read = self.plc.readValue()
            print self.plc.name
            print 'Values: 1) ' + str(read[0]) + '. 2) ' + str(read[1])
            time.sleep(1)
            
    def stop(self):
        self.alive = False
        