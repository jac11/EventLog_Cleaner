# EventLog Cleaner

This is a python script that can be used to quickly and easily clear all EventLogs in Windows. It can be compiled to an executable using py2exe or pyinstaller.

## Setup

If you are compiling the script to an executable using py2exe, you will need to use the setup.py file.

## Warning

This script will clear all EventLogs, so please use it with caution. It must be run as an administrator.

## Usage

The script calls wevtutil.exe with the subprocess python module to get a list of all EventLogs, and then clears them one by one.

The GitHub repo contains an executable file that can be used for quick and easy usage.

## Readme

This readme file provides an overview of the EventLog Cleaner script. It explains the setup, warning, usage, and readme information.

* Please note that this code is provided as-is and no warranty is provided. Use at your own risk.
