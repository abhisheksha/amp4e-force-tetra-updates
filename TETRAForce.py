import os
import re
"""
#Stop the service //// 
def toggle_service(action, name):
    cmd = 'runas /noprofile /user:administrator "net {} \'{}\'"'.format(action, name)
    os.system(cmd)
"""

path = input("Enter the file path")

target = open(path)
read = target.read()

m = re.search('<lastsuccesstime>(.+?)</lastsuccesstime>', read)
if m:
    found = m.group(1)

print(m)
