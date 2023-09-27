# EventLog Cleaner

This is a python script that can be used to quickly and easily clear all EventLogs in Windows. It can be compiled to an executable using py2exe or pyinstaller.

## Setup

If you are compiling the script to an executable using py2exe, you will need to use the setup.py file.
*  Compiling your code on Windows without encountering any errors.
  * 1-  Keep the setup.py and Clear.py in the same directory.
  * 2-  Open PowerShell or Command Prompt.
  * 3- Navigate to the directory where your scripts are located.
  * 4-  Run the following command: python setup.py py2exe
  ## To compiling the script to an executable using pyinstaller
  * 1- Open PowerShell or Command Prompt.
  * 2- Navigate to the directory where your scripts are located.
  * 3- Run the following command: pyinstaller -F Clear.py
## Warning

This script will clear all EventLogs, so please use it with caution. It must be run as an administrator.
## how code work
The script calls wevtutil.exe with the subprocess python module to get a list of all EventLogs,
```python
print ("start Clear EventLog\n"+"*"*30)
command = 'wevtutil.exe el'
command_run =  subprocess.run(command,shell=True,capture_output=True)
output  = command_run.stdout.decode()
```
, and then clears them one by one.
The GitHub repo contains an executable file that can be used for quick and easy usage.

## Readme

This readme file provides an overview of the EventLog Cleaner script. It explains the setup, warning, usage, and readme information.
* Please note that this code is provided as-is and no warranty is provided. Use at your own risk.
