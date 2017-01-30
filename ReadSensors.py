import subprocess
from ast import literal_eval as leval

def gps():
    cmd = ['termux-location']
    p = subprocess.Popen(cmd,
            stdout=subprocess.PIPE)
    text = p.stdout.read().decode("UTF-8")
    #retcode = p.wait()
    return leval(f'{{"gps": {text} }}') #, retcode

#text, ret = gps()
print(gps())
#print(ret)
