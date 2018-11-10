#!/usr/bin/env python2

import RFM69
from RFM69registers import *
import datetime
import time
import struct

test = RFM69.RFM69(RF69_433MHZ, 1, 100, False)
print "class initialized"
print "reading all registers"
results = test.readAllRegs()
for result in results:
    print result
print "Performing rcCalibration"
test.rcCalibration()
print "setting high power"
test.setHighPower(True)
print "Checking temperature"
print test.readTemperature(0)
print "setting encryption"
test.encrypt("sampleEncryptKey")
print "sending blah to 99"
if test.sendWithRetry(99, "blah", 3, 20):
    print "ack recieved"
print "reading"
while True:
    test.receiveBegin()
    while not test.receiveDone():
        time.sleep(.1)
    print(len(test.DATA))
    data = test.DATA[:2]+[0x00, 0x00]+test.DATA[2:]
    id, uptime, temperature, humidity = struct.unpack("hLff", "".join([chr(x) for x in data]))
    
    print "id={} uptime={} temperature={} humidity={} from {} RSSI: {}".format(
        id, uptime, temperature, humidity, test.SENDERID, test.RSSI)
    if test.ACKRequested():
        test.sendACK()
print "shutting down"
test.shutdown()
