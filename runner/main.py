from runner.plc.PLC import PLC
from runner.threader.Threader import PLCReader

plcs = [ ['QC01','10.50.3.94', 0, 2] ]

plcList = list()
threadList = list()

for elem in plcs:
    plcList.append(PLC(elem[0], elem[1], elem[2], elem[3]))
    
for plcElem in plcList:
    x = PLCReader(plcElem, None)
    threadList.append(x)
    x.start()
    