#sends data from file to arduino
import serial
import time


usbport = 'COM3'
ser = serial.Serial(usbport, 9600, timeout=1)

while True:

  f=open('new.txt','r')
  
  data=f.read()
  if data=='1':
    ser.write(data)
    print '< << <<<'
    time.sleep(0.5)
  elif data=='2':
    ser.write(data)
    print '>>> >> >'
    time.sleep(0.5)  

  f.close()
 


