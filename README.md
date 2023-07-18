WIFI-TON
WIFI-TON es una herramienta de Wi-Fi hacking que permite escanear redes Wi-Fi, detectar dispositivos conectados a una red y realizar ataques de fuerza bruta para intentar acceder a redes Wi-Fi protegidas.

Instalación
Clona el repositorio de WIFI-TON en tu máquina local:
shell
Copy code
git clone https://github.com/tu_usuario/WIFI-TON.git
Navega al directorio del proyecto:
shell
Copy code
cd WIFI-TON
Instala las dependencias necesarias utilizando pip:
shell
Copy code
pip install -r requirements.txt
Ejecución
Asegúrate de estar en el directorio del proyecto WIFI-TON:
shell
Copy code
cd WIFI-TON
Ejecuta el script principal main.py:
shell
Copy code
python main.py
Uso
Al ejecutar el script main.py, se presentará un menú con diferentes opciones:

Escaneo de red: Esta opción permite escanear una red local para detectar los dispositivos conectados a ella. El script mostrará una tabla con la dirección IP, dirección MAC y fabricante de cada dispositivo detectado.

Detección de redes Wi-Fi: Esta opción realiza un escaneo de las redes Wi-Fi disponibles en el área. Se mostrará una tabla con el número de red, el SSID, la dirección BSSID y la fuerza de la señal de cada red encontrada.

Selecciona la opción deseada ingresando el número correspondiente. Para cancelar y salir del programa, ingresa 0 en cualquier momento.

Si seleccionas la opción de escaneo de red, se te pedirá ingresar la dirección IP del router de tu red local. Después de cada escaneo, tendrás la opción de regresar al menú principal o continuar con un nuevo escaneo.

Si seleccionas la opción de detección de redes Wi-Fi, se mostrará una lista de las redes encontradas. Podrás seleccionar una red específica ingresando su número y también deberás proporcionar una lista de contraseñas en un archivo de texto para realizar un ataque de fuerza bruta. El script intentará conectar a la red seleccionada utilizando las contraseñas de la lista. Al finalizar, se mostrará si se encontró la contraseña correcta o no.

Después de cada operación, se te dará la opción de intentar nuevamente o volver al menú principal.

Requisitos
Python 3.6 o superior
Bibliotecas y dependencias especificadas en el archivo requirements.txt
Notas adicionales
Ten en cuenta que el uso de esta herramienta para acceder a redes Wi-Fi protegidas sin autorización es ilegal y está sujeto a las leyes y regulaciones de tu país. Utiliza esta herramienta solo con fines educativos o en redes en las que tengas permiso explícito para realizar pruebas de seguridad.

El desarrollador de esta herramienta no se hace responsable de ningún uso indebido o ilegal de la misma.




