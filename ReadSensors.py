import subprocess

def gps():
    cmd = ['termux-location']
    p = subprocess.Popen(cmd,
            stdout=subprocess.PIPE)
    text = p.stdout.read().decode("UTF-8")
    #retcode = p.wait()
    return f'{{"gps": {text} }}' #, retcode

#text, ret = gps()
print(eval(gps()))
#print(ret)
