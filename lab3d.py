#!/usr/bin/env python3
'''Lab 3 Part 2: free disk space checker'''
# Author ID: tloo1

import subprocess

def free_space():
    # Run the command to get available space on root directory
    command = "df -h | grep '/$' | awk '{print $4}'"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    return output[0].decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
