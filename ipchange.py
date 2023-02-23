import os
import wmi
import time
import sys

First3SetFfIp= '10.13.6'

v1= int(input("enter starting value-"))


# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

# First network adaptor
nic = nic_configs[0]


# IP address, subnetmask and gateway values should be unicode objects
ip = u''+First3SetFfIp+'.'+str(v1)
subnetmask = u'255.255.255.0'
gateway = u''+First3SetFfIp+'.'+'1'

# Set IP address, subnetmask and default gateway
# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
nic.SetGateways(DefaultIPGateway=[gateway])