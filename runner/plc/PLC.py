'''
Created on 04 apr 2016

@author: posiandr
'''
import snap7
from snap7.snap7types import areas
from snap7 import util

class PLC():
    
    def __init__(self, name, ip, rack, slot):
        self.ip = ip
        self.name = name
        self.rack = rack
        self.slot = slot
        self.array = [0] * 10
        self.index = 0
        self.avg = 0
        self.max = 0
        self.min = 0
    
        self.snap7 = snap7.client.Client()
        self.snap7.connect(ip, rack, slot)
    
    def readValue(self):
        read = self.snap7.read_area(areas['DB'], 105, 0, 16)
        return [util.get_int(read, 2), util.get_int(read, 4)]