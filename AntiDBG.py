import time, os

def AntiDebugger():
    print('AntiDebugger has been started!')
    while True:
        startTime = time.time()
        time.sleep(0.1)
        if time.time()-startTime>0.2: 
            print('Debugger detected!')
            os._exit(0)

AntiDebugger()