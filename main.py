from scapy.all import ARP, Ether, srp
import manuf
import pywifi
from tabulate import tabulate
import time
import os
from pywifi import const
import socket
from wifi import connect_to_network
from scanner import print_connected_devices




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



def animate_connection_attempt(password):
    animation = "1010101"
    for char in animation:
        print(char, end="", flush=True)
        time.sleep(0.2)
    print(f"  Trying password: {password}", flush=True, end="\r")




def print_available_networks(networks):
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
$$\      $$\$$$$$$\$$$$$$$$\$$$$$$\  $$$$$$$$\ $$$$$$\ $$\   $$\ 
$$ | $\  $$ \_$$  _$$  _____\_$$  _| \__$$  __$$  __$$\$$$\  $$ |
$$ |$$$\ $$ | $$ | $$ |       $$ |      $$ |  $$ /  $$ $$$$\ $$ |
$$ $$ $$\$$ | $$ | $$$$$\     $$ $$$$$$\$$ |  $$ |  $$ $$ $$\$$ |
$$$$  _$$$$ | $$ | $$  __|    $$ \______$$ |  $$ |  $$ $$ \$$$$ |
$$$  / \$$$ | $$ | $$ |       $$ |      $$ |  $$ |  $$ $$ |\$$$ |
$$  /   \$$ $$$$$$\$$ |     $$$$$$\     $$ |   $$$$$$  $$ | \$$ |
\__/     \__\______\__|     \______|    \__|   \______/\__|  \__|
                                                                 
"""

    lorem_paragraph = "Hola te saluda Wi-Fi-BOM una herramienta de Wi-Fi hack compilada por Cisco101. " \
                    "Selecciona una de las siguientes opciones  HAPPY HACKING!"
    animate_typing(lorem_paragraph, delay=0.03)

    print(banner)

    author_info = "Author: Cisco101\nInstagram: cisco10101\nGitHub: https://github.com/Cisco101010"
    animate_typing(author_info, delay=0.03)

    prompt_message = "¿Deseas iniciar el escaneo? (s/n): "
    user_input = input(prompt_message)

    if user_input.lower() != "s" and user_input.lower() != "n":
        animate_typing("Selecciona una opción válida.", delay=0.3)
        user_input = input(prompt_message)

    if user_input.lower() == "n":
        animate_typing("Escaneo cancelado. Hasta luego.", delay=0.5)
        return

    permission_prompt = "¿Tienes permitido escanear esta red? (s/n): "
    permission_input = input(permission_prompt)

    if permission_input.lower() != "s" and permission_input.lower() != "n":
        animate_typing("Selecciona una opción válida.", delay=0.3)
        permission_input = input(permission_prompt)

    if permission_input.lower() == "n":
        animate_typing("No tienes permiso para escanear esta red. Terminando el programa.", delay=0.3)
        return

    while True:
        option_prompt = "¿Qué opción deseas ejecutar?\n1. Escaneo de red\n2. Detección de redes Wi-Fi\nSelecciona un método: "
        option_input = input(option_prompt)

        if option_input != "0" and option_input != "1" and option_input != "2":
            animate_typing("Selecciona una opción válida.", delay=0.3)
            continue

        if option_input == "0":
            continue

        elif option_input == "1":
            subnet = "192.168.1.1"
            prev_connected_devices = []

            animate_typing("Escaneo de red iniciado.", delay=0.5)

            while True:
                try:
                    prev_connected_devices = print_connected_devices(subnet, prev_connected_devices)
                    if not prev_connected_devices:
                        break
                    time.sleep(5)
                    animate_typing("Actualizando...", delay=0.3)
                except KeyboardInterrupt:
                    animate_typing("Escaneo interrumpido por el usuario.", delay=0.5)
                    break

        elif option_input == "2":
            animate_typing("Detección de redes Wi-Fi iniciada.", delay=0.3)
            # Get the list of available Wi-Fi networks
            networks = get_available_networks()
            print_available_networks(networks)  # Pass the list of networks to the function

            selected_network = input("Enter the number of the network you want to connect to (0 to cancel): ")
            if selected_network == "0":
                continue

            wordlist_file = input("Enter the path to the wordlist file: ")

            selected_network = int(selected_network) - 1
            if selected_network < 0 or selected_network >= len(networks):
                print("Invalid network selection.")
                continue

            network = networks[selected_network]
            connected = connect_to_network(network, wordlist_file)

            if connected:
                print("Password found!")
            else:
                print("Password not found!")

            choice = input("Press 1 to try again or 0 to return to the main menu: ")
            while choice not in ["0", "1"]:
                choice = input("Invalid choice. Press 1 to try again or 0 to return to the main menu: ")

            if choice == "0":
                continue

            os.system("cls")


if __name__ == "__main__":
    main()
