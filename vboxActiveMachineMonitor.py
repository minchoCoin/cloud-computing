import os
import time

tmp_file = 'tmp.txt'

while(True):
    os.system("VBoxManage.exe list runningvms > " + tmp_file)
    time.sleep(1)
    with open(tmp_file) as f:
        cnt=0
        for line in f:
            cnt=cnt+1
            print(line)
        print("total runningVMS : " + str(cnt))
        print("----------------")
