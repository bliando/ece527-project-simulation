# Simulation of benefits of 5G cloud network in an Industry 4.0 system
# Author - Bill Liando & Lydia Allen
# Subject - ECE547 Project Simulation Fall 2023
# Asumptions:  
# - each transaction is 1KB
# - data transfer speeds are at max setting
# - 99% machine sucess rate

import sys
from random import randint

transaction_count = 0

def verification(packets):
    #verify packets by packet
    if 0 in packets:
        return 0
    else:
        return 1

def send_ack():
    # success an ACK is sent back to machine
    if randint(1, 100) <= 99:
        ack = True
    else:
        ack = False
    return ack

def manufacturing_plant():
    #build 5 devices, after completion send data to controller 
    status = []
    for item in range(0,6):
        if randint(1, 100) <=99:
            val = 1 # 99% success rate
        else:
            val = 0
        status.append(val)
    return status

def system_admin(number_of_machines):
    transaction_count = 0
    #machine level, each machine responds to verification
    for machine in range(number_of_machines):
        machine_status =  manufacturing_plant()
        transaction_count = transaction_count + 1
    #send to gNodeB for verification
        gnodeb_status = verification(machine_status)
        transaction_count = transaction_count + 1
        if gnodeb_status == 0:
            #send alert to correct error
            send_ack
            transaction_count = transaction_count + 1
    #send ack back to device
        send_ack
        transaction_count = transaction_count + 1

    return transaction_count


if __name__ == "__main__":
    if str(sys.argv[2]) == '4GLTE':
        speed = 300 #300 Mbps
        speed_type = '4G LTE'
    elif str(sys.argv[2]) == '5G':
        speed = 30000 #30Gbps
        speed_type = '5G'
    elif str(sys.argv[2]) == 'Ethernet':
        speed = 10000 #10Gbps
        speed_type = 'Ethernet'
    results = system_admin(int(sys.argv[1]))
    print("Number of machines: "+str(sys.argv[1]))
    print("Number of transactions: "+str(results))
    print("Data Transfer Rate: "+str(speed_type)+", "+str(speed)+" Mbps")
    time_elapsed = (results/125)/speed
    print("Time elapsed : "+str(time_elapsed)+" ms")
    # run with python3 main.py #ofMachines TransferType
    # i.e. python3 main.py 10000 5G

    
