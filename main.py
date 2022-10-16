import time
import psutil
import os
import sys
import subprocess
from datetime import datetime

OS_W = psutil.WINDOWS

path = input('Catalog: ')
delay = int(input('Timeout: '))

if  OS_W  == True:
    os.startfile(path)

    process_name = path.split('\\')[-1]
    print(process_name)
    try:
        for i in psutil.process_iter():
            if i.name() == process_name:
                with open('log.txt', 'a') as f:
                    while True:
                        f.write(f'Datetime: {datetime.now()}\n')
                        print(f'Datetime: {datetime.now()}')
                        f.write(f'cpu: {i.cpu_percent()}\n')
                        print(f'cpu: {i.cpu_percent()}')
                        f.write(f'Working Set: {i.memory_full_info()[4]}\n')
                        print(f'Working Set: {i.memory_full_info()[4]}')
                        f.write(f'Private Bytes: {i.memory_full_info()[-2]}\n')
                        print(f'Private Bytes: {i.memory_full_info()[-2]}')
                        f.write(f'handle: {i.num_handles()}\n')
                        print(f'handle: {i.num_handles()}')
                        time.sleep(delay)
    except:
        pass


if psutil.LINUX == True:
    subprocess.Popen(path)
    process_name = path.split('/')[-1]
    try:
        for i in psutil.process_iter():
            if i.name() == process_name:
                with open('log.txt', 'a') as f:
                    while True:
                        f.write(f'Datetime: {datetime.now()}\n')
                        print(f'Datetime: {datetime.now()}')
                        f.write(f'cpu: {i.cpu_percent()}\n')
                        print(f'cpu: {i.cpu_percent()}')
                        f.write(f'Resident Set Size: {i.memory_full_info()[0]}\n')
                        print(f'Resident Set Size: {i.memory_full_info()[0]}')
                        f.write(f'Virtual Memory Size: {i.memory_full_info()[1]}\n')
                        print(f'Virtual Memory Size: {i.memory_full_info()[1]}')
                        f.write(f'Descriptors: {i.num_fds()}\n')
                        print(f'Descriptors: {i.num_fds()}')
                        time.sleep(delay)
    except:
        pass
