# BLE Scanning software moduleing for processing 
 
import blescan
import sys
import bluetooth._bluetooth as bluez

def init():
    dev_id = 0
    try:
        sock = bluez.hci_open_dev(dev_id)
        print "ble thread started"

    except:
        print "error accessing bluetooth device..."
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)
    
    return sock

def scanbeacon():
    sock = init()
    while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------"
	for beacon in returnedList:
		print beacon
		
if __name__ == '__main__':
   scanbeacon()

