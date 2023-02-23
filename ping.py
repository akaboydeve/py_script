import os
import wmi
import time
import sys

First3SetFfIp= input("enter first 3 set of your ip for example-8.8.8-")

v1= int(input("enter starting value-"))
if v1 < 1:
    print("not less than 1")
    exit("not less than 1")
elif v1>254:
    print("not more than 254")
    exit("not more than 254")
v2= int(input("enter second value-"))
if v2 < 1:
    print("not less than 1")
    exit("not less than 1")
elif v2 >254:
    print("not more than 254")
    exit("not more than 254")


# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

# First network adaptor
nic = nic_configs[0]

for i in range(v1,v2):

    # IP address, subnetmask and gateway values should be unicode objects
    ip = u''+First3SetFfIp+'.'+str(i)
    subnetmask = u'255.255.255.0'
    gateway = u''+First3SetFfIp+'.'+'1'

    # Set IP address, subnetmask and default gateway
    # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])

    time.sleep(5)
    response = os.system("ping -n 1 8.8.8.8")
    if response== 0:
        print("connected done "+ip)
        print(u'connected '+ip+"\n", file=open("output.txt", 'a',encoding='ascii'))
    else:
        print ("not connected  "+ip)
        print(u'not connected '+ip+"\n", file=open("output.txt", 'a',encoding='ascii'))



