# Python
import sys
import subprocess

def get_encrypt():
  try:
    retcode = subprocess.call("php AesDeTest.php" + " ", shell=True)
    if retcode < 0:
         print (sys.stderr, "Child was terminated by signal", retcode)
    else:
         print ("\n")
         #print (stdout..read())
  except OSError as e:
     print (sys.stderr, "Execution failed:", e)

##proc = subprocess.Popen("php php脚本路径/index.php",shell=True,stdout=subprocess.PIPE)
#subprocess.call('/usr/bin/php /root/addpass.php ' + ftp + ' ' + ftppass,shell=True)
#response = proc.stdout.read()
#print(response) #这里输出为空
get_encrypt()
