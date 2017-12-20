import testblescan
import blescan
import sqlite3
from multiprocessing import Process, Queue
 
sentinel = -1
 
def enroll_beacon():
    con = sqlite3.connect("/var/www/html/database/smart_bus3.db")
    sqlite3.Connection

    enroll_list = []
    cursor = con.cursor()
    cursor.execute("SELECT * FROM enroll_beacon WHERE 1")
    enroll_rows = cursor.fetchall()

    for i in range(0,len(enroll_rows)):
        enroll_list.append(enroll_rows[i][1])
        
    return enroll_list
 
 
def enroll_judgment(q):
    while True:
        data = q.get()
        print(data)
 
        if data is sentinel:
            break

def scan_beacon(q):
    sock = testblescan.init()
    while True:
	returnedList = blescan.parse_events(q, sock, 10)
	print("============")
    
 
if __name__ == '__main__':
    
    q = Queue()
    data = [5, 10, 13, -1]
    enroll = enroll_beacon()
    print(enroll)
    
    #process1 = Process(target=creator, args=(data, q))
    process1 = Process(target=scan_beacon, args=(q,))
    process2 = Process(target=enroll_judgment, args=(q,))
    
    process1.start()
    process2.start()
 
    q.close()
    q.join_thread()
 
    process1.join()
    process2.join()
