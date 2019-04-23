#!/usr/bin/env python
# -*- coding: utf_8 -*-
import os,sys
import csv
import time
import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


print("Please input the port No.")
port_num=input()
PORT = "COM"+port_num

print("Please input the Number of sensors")
sensor_num=input()


master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
master.set_timeout(5.0)
master.set_verbose(True)




now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
fname=now+r".csv"
csvFile = open(fname,'w+')

csvFile.write("Time,")

for i in range (1,int(sensor_num)+1):
    csvFile.write(str(i))
    csvFile.write(" Current A,")
    csvFile.write(str(i))
    csvFile.write(" Current B,")
    csvFile.write(str(i))
    csvFile.write(" Current C,")
    csvFile.write(str(i))
    csvFile.write(" Current D,")
    csvFile.write(str(i))
    csvFile.write(" Voltage A,")
    csvFile.write(str(i))
    csvFile.write(" Voltage B,")
    csvFile.write(str(i))
    csvFile.write(" Voltage C,")
    csvFile.write(str(i))
    csvFile.write(" Voltage D,")

csvFile.write("\n")
'''fileHeader = ["Time", "1 Current A","1 Current B","1 Current C","1 Current D","1"]
writer = csv.writer(csvFile)
writer.writerow(fileHeader)'''
csvFile.close()

while(1):
    try:
        csvFile = open(fname,'a+')
        now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        now+=","
        csvFile.write(now)

        listbuff=[]
        for i in range (1,int(sensor_num)+1):
            '''csvFile.write(str(master.execute(1, cst.READ_HOLDING_REGISTERS, 40,8 )))'''
            csvFile.write(str(master.execute(i, cst.READ_HOLDING_REGISTERS, 40,8 )).replace('(','').replace(')',''))
            print(i)
            print(str(master.execute(i, cst.READ_HOLDING_REGISTERS, 40,8 )).replace('(','').replace(')',''))
        csvFile.write("\n")
        print("Continue")
        csvFile.close()
        time.sleep(1) # 休眠时间
    except:
        print("Error")
        csvFile = open(fname,'a+')
        now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        now+=","
        csvFile.write(now)
        csvFile.write("Error")
        csvFile.write("\n")
        continue
    
csvFile.close()
