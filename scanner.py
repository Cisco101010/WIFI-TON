from scapy.all import ARP, Ether, srp
import manuf
import time
import os
from tabulate import tabulate  # Import the 'tabulate' function

def get_connected_ips(subnet):
    arp = ARP(pdst=subnet + "/24")
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    connected_devices = []
    for sent, received in result:
        connected_devices.append((received.psrc, received.hwsrc))

    return connected_devices

def get_device_info(mac_address):
    p = manuf.MacParser()
    manufacturer = p.get_manuf(mac_address)
    return manufacturer

def animate_typing(message: str, delay: float):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def print_connected_devices(subnet, prev_connected_devices):
    connected_devices = get_connected_ips(subnet)

    # Clear the terminal
    os.system("cls" if os.name == "nt" else "clear")

    # Print banner and table headers
    banner = """
 
 (                   )    ) (       )             )                       )  (        )     
 )\ )  (    (     ( /( ( /( )\ ) ( /( (        ( /(      *   ) (  (    ( /(  )\ )  ( /(     
(()/(  )\   )\    )\()))\()(()/( )\()))\ )     )\())(  ` )  /( )\))(   )\())(()/(  )\())    
 /(_)(((_((((_)( ((_)\((_)\ /(_)((_)\(()/(    ((_)\ )\  ( )(_)((_)()\ ((_)\  /(_)|((_)\     
(_)) )\___)\ _ )\ _((_)_((_(_))  _((_)/(_))_   _((_((_)(_(_())_(())\_)()((_)(_)) |_ ((_)    
/ __((/ __(_)_\(_| \| | \| |_ _|| \| (_)) __| | \| | __|_   _|\ \((_)/ / _ \| _ \| |/ /     
\__ \| (__ / _ \ | .` | .` || | | .` | | (_ | | .` | _|  | |   \ \/\/ | (_) |   /  ' < _ _  
|___/ \___/_/ \_\|_|\_|_|\_|___||_|\_|  \___| |_|\_|___| |_|    \_/\_/ \___/|_|_\ _|\_(_(_) 
                                                                                            

"""
    print(banner)

    # Create a table of connected devices
    table_data = []
    for ip, mac in connected_devices:
        manufacturer = get_device_info(mac)
        table_data.append([ip, mac, manufacturer])

    table_headers = ["Dirección IP", "Dirección MAC", "Fabricante"]
    table_formatted = tabulate(table_data, headers=table_headers, tablefmt="grid")

    # Print the table
    print(table_formatted)

    # Check if option 0 (Return to menu) was selected
    if input("\nPresiona 0 para regresar al menú principal o cualquier otra tecla para continuar: ") == "0":
        return []

    return connected_devices
