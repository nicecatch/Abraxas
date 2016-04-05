'''
Created on 04 apr 2016

@author: posiandr
'''
import snap7
from snap7.snap7exceptions import Snap7Exception 
from snap7.snap7types import areas
from snap7 import util

#import sys

class PLC():
    
    def __init__(self, name, ip, rack, slot):
        self.ip = ip
        self.name = name
        self.rack = rack
        self.slot = slot
        self.connect()
    
    def read(self):
        read = self.snap7.read_area(areas['DB'], 105, 0, 16)
        return [util.get_int(read, 2), util.get_int(read, 4)]
    
    def readValue(self):
        try:
            return self.read()
        except Snap7Exception as error: #Errore, provo una volta a ricollegarmi e a rileggere
            try:
                self.connect()
                return self.read()
            
            except Snap7Exception as error:
                print "Unexpected error: ", error
                
            
    def connect(self):
        try:
            self.snap7 = snap7.client.Client()
            self.snap7.connect(self.ip, self.rack, self.slot)
        except Snap7Exception as error:
            print "Unexpected error: ", error