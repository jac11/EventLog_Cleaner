import subprocess
from subprocess import PIPE
import time
import os
print ("start Clear EventLog\n"+"*"*30)
command = 'wevtutil.exe el'
command_run =  subprocess.run(command,shell=True,capture_output=True)
output  = command_run.stdout.decode()
with open (os.getenv('APPDATA')+'\\'+'task','w')as Task:
    Task.write(output.replace('\n',''))
with open (os.getenv('APPDATA')+'\\'+'task','r')as Task:
      ReadTask = Task.readlines()
      
for EventLog  in ReadTask :
    clean = "wevtutil.exe cl "+EventLog
    subprocess.call(clean,shell=True,stderr=subprocess.PIPE,stdout=PIPE)
    print(EventLog.replace('\n',''))
print("*"*30+'\n'+"ALL EVENT CLEARED")
try:
   os.remove((os.getenv('APPDATA')+'\\'+'task'))
except :
     pass
time.sleep(3)
