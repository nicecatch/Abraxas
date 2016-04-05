'''
Created on 04 apr 2016

@author: posiandr
'''
import numbers
import threading
import time
#from snap7 import util
#import snap7
#from snap7.snap7types import areas

#from runner.plc import PLC

READS_TO_LOG = 10

class PLCReader (threading.Thread):
    def __init__(self, plc, config):
        super(PLCReader, self).__init__()
        self.plc = plc
        self.config = config
        self.alive = True
        
        self.array = [0] * READS_TO_LOG
        self.index = 0
        self.avg = 0
        self.max = 0
        self.min = 0
        self.latestValue = 0
    
    def run(self):
        while self.alive is True:
            read = self.plc.readValue()
            
            readValue = -1
            
            if isinstance(read[0], numbers.Number):
                readValue = read[0]
            elif isinstance(read[1], numbers.Number):
                readValue = read[1]
            
            if readValue >= 0:    
                self.latestValue = readValue
                self.array[self.currentIndex()] = readValue
                self.incrementIndex()
                self.calcAvgMaxMin()
                
            print self.plc.name + ': Value: ' + str(self.latestValue) + '. Avg: ' + str(self.avg) + '. Min: ' + str(self.min) + '. Max: ' + str(self.max)
            time.sleep(1)
            
    def stop(self):
        self.alive = False
    
    def currentIndex(self):
        return self.index if self.index < READS_TO_LOG else self.index - READS_TO_LOG
    
    def calcCurrentValues(self):
        return self.index if self.index < READS_TO_LOG else READS_TO_LOG
    
    def incrementIndex(self):
        self.index = self.index + 1
        self.index = self.index if self.index < READS_TO_LOG * 2 else self.index - READS_TO_LOG

    
    def calcAvgMaxMin(self):
        total = 0
        currentMax = self.array[0]
        currentMin = self.array[0]
        
        for x in range(0, self.calcCurrentValues()):
            currentValue = self.array[x]
            if currentValue > currentMax:
                currentMax = currentValue
            if currentValue < currentMin:
                currentMin = currentValue
            total += currentValue
            
        self.max = currentMax
        self.min = currentMin
        self.avg = total / (self.calcCurrentValues())      
        