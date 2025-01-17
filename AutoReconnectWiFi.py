import pywifi, time



def AutoReconnect():

    while True:

        time.sleep(5)

        wifi = pywifi.PyWiFi()
        ifaces = wifi.interfaces()

        for iface in ifaces:

            if iface.status() == pywifi.const.IFACE_CONNECTED: break

        else: # if not broken
            
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

AutoReconnect()