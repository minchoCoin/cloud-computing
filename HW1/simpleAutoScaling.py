#requirements : vm name must not include space(' ')

import os
import time

HOST_CORE = 8
VM_CORE=2

def getVmName():
    filename = 'vmlist.txt'
    os.system("VBoxManage.exe list vms > " + filename)
    time.sleep(1)
    names=[]
    with open(filename) as f:
        for line in f:
            tmp = line.split()[0]
            names.append(tmp[1:-1])
    return names

def getRunningVmName():
    runningListFile = 'runningList.txt'
    os.system("VBoxManage.exe list runningvms > " + runningListFile)
    time.sleep(1)
    names=[]
    with open(runningListFile) as f:
        for line in f:
            tmp = line.split()[0]
            names.append(tmp[1:-1])
    return names

def getCPULoad(vmName):
    filename = vmName + '.txt'
    os.system("VBoxManage.exe metrics query \"{}\" CPU/Load/User:avg > {}".format(vmName,filename))
    time.sleep(1)
        
    with open(filename) as f:
        f.readline()
        f.readline()

        #read line, get percentage, remove space, and remove percentage sign
        try:
            value = f.readline().split()[2].strip().replace("%","")
        except Exception as e:
            value = '0.0'
        value=float(value)

    return value

def getOverLoadVm(loads, threshold):
    names = []
    for (name,value) in loads:
        if value>threshold/(HOST_CORE/VM_CORE):
            print('warning : Overloading ' + name +  " : " + str(value * (HOST_CORE/VM_CORE)) + "%")
            names.append(name)
    return names

print('simpleAutoScaling.py start...')

def getNewVmName(vmname):
    equalCnt=0
    names = getVmName()
    originalVmName = vmname
    if vmname.find('clone') !=-1:
        originalVmName = vmname[:vmname.find('clone')]
    for name in names:
        if name.find(originalVmName) >=0:
            equalCnt=equalCnt+1
    
    return originalVmName + ' clone ' + str(equalCnt)
        
def clonevm(source,newname):
    os.system('VBoxManage controlvm \"{}\" poweroff'.format(source))
    time.sleep(5)
    os.system(' VBoxManage.exe clonevm \"{}\" --name=\"{}\" --register --options=keepallmacs --options=keepdisknames --options=keephwuuids'.format(source,newname))

    os.system('VBoxManage startvm \"{}\" '.format(source))
    os.system('VBoxManage.exe startvm \"{}\"'.format(newname))
#setting metrics period and sample
os.system('VBoxManage.exe metrics setup --period 1 --samples 5 * CPU/Load/User')

while(True):
    names = getRunningVmName()
    
    loads=[]
    for name in names:
        loads.append((name,getCPULoad(name)))

    overloadVmList = getOverLoadVm(loads,70.0)
    
    for overloadvm in overloadVmList:
        print('starting clone vm : ' + overloadvm)
        clonevm(overloadvm,getNewVmName(overloadvm))

        #https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevm
    
    time.sleep(0.5)
