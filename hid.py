import requests
import subprocess
import os
import hashlib 

def GetUUID():
   cmd = 'wmic csproduct get uuid'
   uuid = str(subprocess.check_output(cmd))
   pos1 = uuid.find("\\n")+2
   uuid = uuid[pos1:-15]
   return uuid
# print(GetUUID())


  

md5 = hashlib.md5()
md5.update((GetUUID()).encode('utf-8'))
print(md5.hexdigest())

# print(hashlib.sha256(str('xxxx').encode('utf-8')).hexdigest())